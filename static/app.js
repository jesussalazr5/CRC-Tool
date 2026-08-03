(() => {
  const root = document.getElementById("app");

  const state = {
    data: null,
    guide: null,
    level: null, // "level1" | "level2"
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

  async function loadGuide() {
    if (state.guide) return state.guide;
    const res = await fetch("data/guide.json");
    state.guide = await res.json();
    return state.guide;
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

  async function renderStart() {
    root.innerHTML = "";
    const data = await loadData();

    const card = el("div", { class: "card" }, [
      el("h1", {}, "Vamos praticar? 💜"),
      el("p", { class: "subtitle" }, "Escolha um nível para começar seu simulado. As perguntas e as opções aparecem em uma ordem diferente a cada tentativa."),
      el("div", { class: "level-grid" }, [
        el(
          "button",
          {
            class: "level-btn",
            onclick: () => startLevel("level1", data.level1),
          },
          [
            el("div", { class: "level-name" }, "Nível 1 — Prova Real (Tipo 4)"),
            el("div", { class: "level-desc" }, `${data.level1.length} questões reais da prova CFC, embaralhadas.`),
          ]
        ),
        el(
          "button",
          {
            class: "level-btn",
            onclick: () => startLevel("level2", data.level2),
          },
          [
            el("div", { class: "level-name" }, "Nível 2 — Questões Extras"),
            el("div", { class: "level-desc" }, `${data.level2.length} questões inéditas, no mesmo estilo da prova, para praticar mais.`),
          ]
        ),
        el(
          "button",
          {
            class: "level-btn",
            onclick: renderGuide,
          },
          [
            el("div", { class: "level-name" }, "Módulo 3 — Guia de Estudos"),
            el("div", { class: "level-desc" }, "Os temas que caem na prova, organizados do básico ao avançado, para estudar antes (ou entre) os simulados."),
          ]
        ),
      ]),
    ]);

    root.appendChild(brand());
    root.appendChild(card);
  }

  function startLevel(level, rawQuestions) {
    state.level = level;
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
    const levelLabel = state.level === "level1" ? "Nível 1" : "Nível 2";

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

    const card = el("div", { class: "card" }, [
      el("a", { class: "exit-link", onclick: renderStart }, "← Voltar ao início"),
      el("div", { class: "progress-row" }, [
        el("span", {}, `${levelLabel} · Questão ${state.index + 1} de ${total}`),
        el("span", {}, `${progressPct}%`),
      ]),
      el("div", { class: "progress-bar" }, [el("div", { class: "progress-fill", style: `width:${progressPct}%` })]),
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
              el("a", { class: "hint-guide-link", onclick: renderGuide }, "Módulo 3 — Guia de Estudos"),
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
        el("div", { class: "feedback-note" }, "Explicação de apoio para os estudos — não é conteúdo oficial da FGV/CFC."),
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
    const levelLabel = state.level === "level1" ? "Nível 1 — Prova Real" : "Nível 2 — Questões Extras";

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
            onclick: () => startLevel(state.level, state.data[state.level]),
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

  async function renderGuide() {
    root.innerHTML = "";
    const guide = await loadGuide();

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
      el("h1", {}, "Guia de Estudos"),
      el("p", { class: "subtitle" }, "Toque em cada tema para abrir o resumo. Organizado do básico ao avançado — vale a pena estudar nessa ordem."),
      el("div", { class: "guide-sections" }, sections),
    ]);

    root.appendChild(brand());
    root.appendChild(card);
  }

  renderStart();
})();
