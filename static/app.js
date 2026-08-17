(() => {
  const root = document.getElementById("app");

  const GUIDES = {
    cfc: { url: "data/guide.json", title: "Guia de Estudos — CFC", subtitle: "Toque em cada tema para abrir o resumo. Organizado do básico ao avançado — vale a pena estudar nessa ordem." },
    adc: { url: "data/adc_guide.json", title: "Guia de Estudos — Análise das Demonstrações Contábeis", subtitle: "Toque em cada tema para abrir o resumo. Organizado do básico ao avançado — vale a pena estudar nessa ordem." },
  };

  const state = {
    data: null,
    adcData: null,
    guides: {}, // cache per GUIDES key
    levelKey: null,
    levelLabel: null,
    feedbackNote: null,
    guideKey: null,
    rawQuestions: [],
    questions: [], // shuffled, with shuffled option order baked in
    index: 0,
    answers: [], // { question, chosenLetter, isCorrect }
    answered: false,
    hintShown: false,
  };

  function shuffle(array) {
    const a = array.slice();
    for (let i = a.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [a[i], a[j]] = [a[j], a[i]];
    }
    return a;
  }

  function prepareQuestions(rawQuestions) {
    return shuffle(rawQuestions).map((q) => {
      const letters = shuffle(Object.keys(q.options));
      const displayOptions = letters.map((letter) => ({
        letter,
        text: q.options[letter],
      }));
      return { ...q, displayOptions };
    });
  }

  async function loadData() {
    if (state.data) return state.data;
    const res = await fetch("data/questions.json");
    state.data = await res.json();
    return state.data;
  }

  async function loadAdcData() {
    if (state.adcData) return state.adcData;
    const res = await fetch("data/adc_questions.json");
    state.adcData = await res.json();
    return state.adcData;
  }

  async function loadGuideByKey(key) {
    if (state.guides[key]) return state.guides[key];
    const res = await fetch(GUIDES[key].url);
    const guide = await res.json();
    state.guides[key] = guide;
    return guide;
  }

  function el(tag, attrs = {}, children = []) {
    const node = document.createElement(tag);
    for (const [k, v] of Object.entries(attrs)) {
      if (v == null) continue;
      if (k === "class") node.className = v;
      else if (k === "html") node.innerHTML = v;
      else if (k.startsWith("on") && typeof v === "function") node.addEventListener(k.slice(2), v);
      else node.setAttribute(k, v);
    }
    for (const child of [].concat(children)) {
      if (child == null) continue;
      node.appendChild(typeof child === "string" ? document.createTextNode(child) : child);
    }
    return node;
  }

  function brand() {
    return el("div", { class: "brand" }, [
      el("div", { class: "brand-dot" }),
      el("div", { class: "brand-title" }, "Simulado CFC — Exame de Suficiência"),
    ]);
  }

  // ---------------- Start screen ----------------

  const CFC_FEEDBACK_NOTE = "Explicação de apoio para os estudos — não é conteúdo oficial da FGV/CFC.";
  const ADC_FEEDBACK_NOTE = "Explicação de apoio para os estudos, baseada no livro-texto e em normas contábeis — não é o gabarito oficial da sua prova.";

  async function renderStart() {
    root.innerHTML = "";
    const data = await loadData();
    const adcData = await loadAdcData();

    const card = el("div", { class: "card" }, [
      el("h1", {}, "Vamos praticar? 💜"),
      el("p", { class: "subtitle" }, "Escolha um simulado ou guia para começar. As perguntas e as opções aparecem em uma ordem diferente a cada tentativa."),
      el("div", { class: "level-grid" }, [
        el(
          "button",
          {
            class: "level-btn",
            onclick: () => startLevel("level1", data.level1, "Nível 1 — Exame 2026.1", CFC_FEEDBACK_NOTE, "cfc"),
          },
          [
            el("div", { class: "level-name" }, "Nível 1 — Exame 2026.1 (Tipo 4)"),
            el("div", { class: "level-desc" }, `${data.level1.length} questões reais dessa prova oficial do CFC, embaralhadas.`),
          ]
        ),
        el(
          "button",
          {
            class: "level-btn",
            onclick: () => startLevel("level2", data.level2, "Nível 2 — Exame 2025.2", CFC_FEEDBACK_NOTE, "cfc"),
          },
          [
            el("div", { class: "level-name" }, "Nível 2 — Exame 2025.2 (Tipo 1)"),
            el("div", { class: "level-desc" }, `${data.level2.length} questões reais de outra prova oficial do CFC, embaralhadas.`),
          ]
        ),
        el(
          "button",
          {
            class: "level-btn",
            onclick: () => renderGuide("cfc"),
          },
          [
            el("div", { class: "level-name" }, "Módulo 3 — Guia de Estudos (CFC)"),
            el("div", { class: "level-desc" }, "Os temas que caem na prova, organizados do básico ao avançado, para estudar antes (ou entre) os simulados."),
          ]
        ),
        el(
          "button",
          {
            class: "level-btn",
            onclick: () => startLevel("adc", adcData.questions, "Simulado ADC", ADC_FEEDBACK_NOTE, "adc"),
          },
          [
            el("div", { class: "level-name" }, "Módulo 4 — Análise das Demonstrações Contábeis"),
            el("div", { class: "level-desc" }, `${adcData.questions.length} questões (livro-texto + complementares) sobre AV/AH, liquidez, endividamento, giro, prazos, ciclos, DuPont e Kanitz.`),
          ]
        ),
        el(
          "button",
          {
            class: "level-btn",
            onclick: () => renderGuide("adc"),
          },
          [
            el("div", { class: "level-name" }, "Módulo 4 — Guia de Estudos (ADC)"),
            el("div", { class: "level-desc" }, "Os temas da sua prova de Análise das Demonstrações Contábeis, organizados do básico ao avançado."),
          ]
        ),
      ]),
    ]);

    root.appendChild(brand());
    root.appendChild(card);
  }

  function startLevel(levelKey, rawQuestions, levelLabel, feedbackNote, guideKey) {
    state.levelKey = levelKey;
    state.levelLabel = levelLabel;
    state.feedbackNote = feedbackNote;
    state.guideKey = guideKey;
    state.rawQuestions = rawQuestions;
    state.questions = prepareQuestions(rawQuestions);
    state.index = 0;
    state.answers = [];
    state.answered = false;
    state.hintShown = false;
    renderQuiz();
  }

  function toggleHint() {
    state.hintShown = !state.hintShown;
    renderQuiz();
  }

  // ---------------- Quiz screen ----------------

  function renderQuiz() {
    root.innerHTML = "";
    const total = state.questions.length;
    const q = state.questions[state.index];
    const levelLabel = state.levelLabel;

    const progressPct = Math.round((state.index / total) * 100);

    const optionButtons = q.displayOptions.map((opt) => {
      const btn = el(
        "button",
        {
          class: "option-btn",
          disabled: state.answered ? "disabled" : null,
          onclick: () => selectAnswer(opt.letter),
        },
        [el("span", { class: "option-letter" }, opt.letter), el("span", {}, opt.text)]
      );
      return { letter: opt.letter, btn };
    });

    const correctSoFar = state.answers.filter((a) => a.isCorrect).length;
    const incorrectSoFar = state.answers.length - correctSoFar;

    const card = el("div", { class: "card" }, [
      el("a", { class: "exit-link", onclick: renderStart }, "← Voltar ao início"),
      el("div", { class: "progress-row" }, [
        el("span", {}, `${levelLabel} · Questão ${state.index + 1} de ${total}`),
        el("span", {}, `${progressPct}%`),
      ]),
      el("div", { class: "progress-bar" }, [el("div", { class: "progress-fill", style: `width:${progressPct}%` })]),
      el("div", { class: "tally-row" }, [
        el("span", { class: "tally tally-correct" }, `✓ Certas: ${correctSoFar}`),
        el("span", { class: "tally tally-incorrect" }, `✗ Erradas: ${incorrectSoFar}`),
      ]),
      el("p", { class: "question-text" }, q.question),
    ]);

    if (!state.answered) {
      card.appendChild(
        el(
          "button",
          { class: "hint-toggle", onclick: toggleHint },
          state.hintShown ? "💡 Ocultar dica" : "💡 Não sabe por onde começar? Peça uma dica"
        )
      );

      if (state.hintShown) {
        card.appendChild(
          el("div", { class: "hint-box" }, [
            el("div", { class: "hint-title" }, "💡 Dica"),
            el("div", { class: "hint-text" }, q.hint),
            el("div", { class: "hint-topic" }, [
              "📚 Tema para revisar: ",
              el("strong", {}, q.topicLabel),
              " — veja no ",
              el("a", { class: "hint-guide-link", onclick: () => renderGuide(state.guideKey) }, "Guia de Estudos"),
              ".",
            ]),
          ])
        );
      }
    }

    card.appendChild(el("div", { class: "options" }, optionButtons.map((o) => o.btn)));

    if (state.answered) {
      const last = state.answers[state.answers.length - 1];
      optionButtons.forEach((o) => {
        if (o.letter === q.correct) o.btn.classList.add("correct");
        else if (o.letter === last.chosenLetter) o.btn.classList.add("incorrect");
      });

      const feedback = el("div", { class: `feedback ${last.isCorrect ? "correct" : "incorrect"}` }, [
        el("div", { class: "feedback-title" }, last.isCorrect ? "Certo! 🎉" : `Não foi dessa vez — a resposta certa é ${q.correct}.`),
        el("div", {}, q.explanation),
        el("div", { class: "feedback-note" }, state.feedbackNote),
      ]);
      card.appendChild(feedback);

      const isLast = state.index === total - 1;
      card.appendChild(
        el("div", { class: "actions-row" }, [
          el(
            "button",
            { class: "btn", onclick: isLast ? renderScore : nextQuestion },
            isLast ? "Ver resultado" : "Próxima"
          ),
        ])
      );
    }

    root.appendChild(brand());
    root.appendChild(card);
  }

  function selectAnswer(letter) {
    if (state.answered) return;
    const q = state.questions[state.index];
    state.answers.push({
      question: q,
      chosenLetter: letter,
      isCorrect: letter === q.correct,
    });
    state.answered = true;
    renderQuiz();
  }

  function nextQuestion() {
    state.index += 1;
    state.answered = false;
    state.hintShown = false;
    renderQuiz();
  }

  // ---------------- Score screen ----------------

  function renderScore() {
    root.innerHTML = "";
    const total = state.answers.length;
    const correctCount = state.answers.filter((a) => a.isCorrect).length;
    const pct = Math.round((correctCount / total) * 100);
    const levelLabel = state.levelLabel;

    const reviewItems = state.answers.map((a) => {
      const q = a.question;
      return el("div", { class: "review-item" }, [
        el("span", { class: `review-tag ${a.isCorrect ? "correct" : "incorrect"}` }, a.isCorrect ? "Certa" : "Errada"),
        el("p", { class: "review-q" }, q.question),
        el(
          "div",
          { class: "review-answers" },
          a.isCorrect
            ? `Sua resposta: ${a.chosenLetter} (correta)`
            : `Sua resposta: ${a.chosenLetter} · Resposta certa: ${q.correct}`
        ),
        el("div", { class: "review-explanation" }, q.explanation),
      ]);
    });

    const card = el("div", { class: "card" }, [
      el("div", { class: "score-hero" }, [
        el("div", { class: "score-number" }, `${correctCount}/${total}`),
        el("div", { class: "score-label" }, `${levelLabel} · Você acertou ${pct}%`),
      ]),
      el("div", { class: "review-list" }, reviewItems),
      el("div", { class: "score-actions" }, [
        el("button", { class: "btn secondary", onclick: renderStart }, "Voltar ao início"),
        el(
          "button",
          {
            class: "btn",
            onclick: () => startLevel(state.levelKey, state.rawQuestions, state.levelLabel, state.feedbackNote, state.guideKey),
          },
          "Repetir nível"
        ),
      ]),
    ]);

    root.appendChild(brand());
    root.appendChild(card);
  }

  // ---------------- Study guide screen ----------------

  const GUIDE_LEVEL_SLUGS = { "Básico": "basico", "Intermediário": "intermediario", "Avançado": "avancado" };

  async function renderGuide(guideKey) {
    root.innerHTML = "";
    const meta = GUIDES[guideKey];
    const guide = await loadGuideByKey(guideKey);

    const sections = guide.sections.map((section) => {
      const topics = section.topics.map((topic) =>
        el("details", { class: "guide-topic" }, [
          el("summary", {}, topic.title),
          el("p", { class: "guide-summary" }, topic.summary),
        ])
      );
      const slug = GUIDE_LEVEL_SLUGS[section.level] || "";
      return el("div", { class: "guide-section" }, [
        el("div", { class: `level-tag level-tag-${slug}` }, section.level),
        el("p", { class: "guide-level-desc" }, section.levelDesc),
        el("div", { class: "guide-topics" }, topics),
      ]);
    });

    const card = el("div", { class: "card" }, [
      el("a", { class: "exit-link", onclick: renderStart }, "← Voltar ao início"),
      el("h1", {}, meta.title),
      el("p", { class: "subtitle" }, meta.subtitle),
      el("div", { class: "guide-sections" }, sections),
    ]);

    root.appendChild(brand());
    root.appendChild(card);
  }

  renderStart();
})();
