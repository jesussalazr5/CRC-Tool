import json
from pathlib import Path

# ============================================================
# ORC — Administração Orçamentária (Unicesumar, Aulas 1 a 5)
# 60 questions in 6 provas of 10, built from the course slides:
#   Aula 1 planejamento | Aula 2 orçamento, implantação e controle
#   Aula 3 elaboração das peças | Aula 4 tipos de orçamento
#   Aula 5 fluxo de caixa e DRE projetados
# Includes the "asserção I / II" format used in the real test.
# ============================================================

TOPIC_LABELS = {
    "aula1_planejamento": "Aula 1 — Planejamento",
    "aula2_orcamento": "Aula 2 — O Orçamento (conceito, premissas, metas)",
    "aula2_implantacao_controle": "Aula 2 — Implantação e Controle Orçamentário",
    "aula3_elaboracao": "Aula 3 — Elaboração das Peças Orçamentárias",
    "aula3_5_numerico": "Aulas 3 e 5 — Vendas, Caixa e DRE Projetada",
    "aula4_tipos": "Aula 4 — Tipos de Orçamento",
}

ASSERT = {
    "A": "As asserções I e II são verdadeiras, e a II é uma justificativa correta da I.",
    "B": "As asserções I e II são verdadeiras, mas a II não é uma justificativa correta da I.",
    "C": "A asserção I é verdadeira e a II é falsa.",
    "D": "A asserção I é falsa e a II é verdadeira.",
    "E": "As asserções I e II são falsas.",
}

PROVAS = []


def new_prova(name, topic):
    p = {"name": name, "topic": topic, "questions": []}
    PROVAS.append(p)
    return p


def q(prova, question, options, correct, explanation, hint):
    prova["questions"].append(dict(question=question, options=options, correct=correct,
                                    explanation=explanation, hint=hint))


def qa(prova, assertion_I, assertion_II, correct, explanation, hint):
    text = (
        "Analise as asserções a seguir e a relação proposta entre elas.\n"
        f"I. {assertion_I}\n"
        "PORQUE\n"
        f"II. {assertion_II}\n"
        "A respeito dessas asserções, assinale a opção correta."
    )
    q(prova, text, dict(ASSERT), correct, explanation, hint)


def opts(a, b, c, d):
    return {"A": a, "B": b, "C": c, "D": d}


# ============================================================
# PROVA 1 — Aula 1: Planejamento
# ============================================================

p1 = new_prova("Prova 1 — Aula 1: Planejamento", "aula1_planejamento")

q(p1, "Em um plano de ação, a pergunta “Como saberei que atingi os objetivos?” está ligada principalmente a",
  opts("controle: evidências (financeiras, de tempo, de medição) de que os objetivos que geraram a necessidade foram atingidos.",
       "definição dos responsáveis por cada etapa.",
       "justificativa de por que o plano será executado.",
       "identificação dos recursos financeiros, de estrutura e de pessoas."),
  "A", "O plano de ação responde: o que, por que, quando, por quem, como, de que recursos e como saberei que atingi os objetivos. Esta última pergunta é a do controle, que exige evidências de que os objetivos foram alcançados.",
  "Das perguntas do plano de ação, qual delas fala em “evidências”?")

q(p1, "Segundo a aula, planejar é, basicamente,",
  opts("uma tomada de decisões sistematizada e contínua por parte dos gestores, com programação antecipada para alcançar os objetivos organizacionais.",
       "registrar os fatos passados da empresa para prestar contas.",
       "executar as tarefas operacionais do dia a dia.",
       "uma decisão isolada, tomada apenas uma vez ao ano pela alta administração."),
  "A", "A aula define planejar como tomada de decisões sistematizada e contínua, com programação antecipada de decisões para que os objetivos sejam alcançados da melhor forma possível.",
  "As duas palavras-chave são “sistematizada e contínua”.")

q(p1, "Qual das perguntas abaixo NÃO faz parte das que o planejamento deve responder, segundo a aula?",
  opts("Onde se pretende chegar?", "O que deve ser feito?",
       "Quanto o concorrente lucrou no último ano?", "Em que sequência deve ser feito?"),
  "C", "As perguntas do planejamento são: onde se pretende chegar, o que deve ser feito, quando, como e em que sequência. O lucro do concorrente não é uma delas.",
  "São cinco perguntas sobre a própria empresa: onde, o quê, quando, como e sequência.")

q(p1, "A primeira função do processo administrativo é",
  opts("planejar.", "controlar.", "dirigir.", "organizar."),
  "A", "A aula destaca que a primeira função do processo administrativo é planejar (coletar dados, diagnosticar a situação, definir objetivos, desdobrá-los em metas, alocar recursos, elaborar o plano de ação e desdobrar os planos em programas). Depois vêm organização, direção e controle.",
  "O ciclo começa pelo que vem antes de organizar, dirigir e controlar.")

q(p1, "Segundo a aula, o exercício sistemático do planejamento contribui principalmente para",
  opts("reduzir as incertezas do processo decisório e aumentar a probabilidade de alcançar os objetivos e metas da empresa.",
       "eliminar totalmente as incertezas sobre o futuro.",
       "dispensar o acompanhamento dos resultados.",
       "substituir a definição de missão e visão."),
  "A", "O planejamento reduz as incertezas (não as elimina, pois é um processo de pensamento sobre o futuro e, portanto, envolve incertezas) e aumenta a probabilidade de atingir objetivos, desafios e metas.",
  "Reduz incerteza, mas não a elimina.")

q(p1, "O planejamento tático é caracterizado por ser",
  opts("de nível setorial, voltado ao médio prazo, definido por cada unidade ou departamento, com objetivos quantitativos mensuráveis.",
       "definido pela alta administração, envolvendo toda a empresa no longo prazo.",
       "voltado a cada tarefa isolada, no curto prazo, como plano detalhado das operações.",
       "restrito à declaração de missão e visão."),
  "A", "Tático: setorial, médio prazo, por unidade/departamento, com objetivos quantitativos mensuráveis. Estratégico: alta administração, toda a empresa, longo prazo. Operacional: cada tarefa, curto prazo, plano detalhado.",
  "Tático = departamentos + médio prazo + metas mensuráveis.")

q(p1, "Na figura “Integrando os tempos”, o horizonte do orçamento (e de outros planos) é de",
  opts("1 ano.", "5 a 10 anos.", "1 a 5 anos.", "mais de 10 anos."),
  "A", "Na figura, missão/visão e planejamento estratégico ficam em 5 a 10 anos; tático e operacional em 1 a 5 anos; plano contingencial e orçamento em 1 ano.",
  "O orçamento está no círculo mais interno da figura.")

q(p1, "Qual dos itens abaixo NÃO é um motivo para utilizar o planejamento, segundo a aula?",
  opts("Reduzir a incerteza.", "Trazer cooperação e coordenação.",
       "Evitar a mortalidade organizacional.", "Dispensar o controle e o acompanhamento dos resultados."),
  "D", "Os motivos citados são: reduz a incerteza, traz cooperação e coordenação, economia em operação, antecipa contingências imprevisíveis, alcance dos objetivos predeterminados e evitar a mortalidade organizacional.",
  "Planejamento e controle andam juntos; um não dispensa o outro.")

q(p1, "Qual dos itens abaixo é um aspecto limitante do planejamento, segundo a aula?",
  opts("Falta de informações precisas.", "Cooperação e coordenação entre as áreas.",
       "Antecipação de contingências imprevisíveis.", "Redução da incerteza."),
  "A", "Aspectos limitantes: falta de informações precisas, resistência à mudança, inflexibilidade, planejamento inadequado, fatores de tempo e custo e filosofia organizacional. As demais alternativas são benefícios do planejamento.",
  "Procure o item que atrapalha o planejamento, e não o que o justifica.")

q(p1, "A declaração “Atuar no setor de energia com rentabilidade, qualidade e responsabilidade social” (exemplo da CEMIG na aula) é um exemplo de",
  opts("missão, pois declara o propósito e delimita a atuação da organização.",
       "visão, pois descreve a perspectiva de futuro de longo prazo.",
       "plano de ação, pois define prazos e responsáveis.",
       "premissa orçamentária, pois fixa a inflação do período."),
  "A", "A missão é declaração ampla e duradoura de propósitos que individualiza a organização e delimita suas atividades. A visão, no exemplo, é “Consolidar-se, nesta década, como o maior grupo do setor elétrico nacional...”, com perspectiva de futuro.",
  "Missão = o que a empresa faz e como; visão = onde quer chegar.")

# ============================================================
# PROVA 2 — Aula 2: O Orçamento
# ============================================================

p2 = new_prova("Prova 2 — Aula 2: O Orçamento", "aula2_orcamento")

q(p2, "Segundo a aula, o orçamento pode ser definido como",
  opts("um plano administrativo que abrange todas as fases das operações para um período futuro definido, expresso de forma quantitativa.",
       "um registro dos fatos contábeis já ocorridos.",
       "uma lista de tarefas diárias das equipes.",
       "a declaração de missão e visão da empresa."),
  "A", "O orçamento é o plano administrativo que abrange todas as fases das operações para um período futuro definido e a expressão quantitativa do que se pretende atingir, baseada nos objetivos e metas organizacionais.",
  "Orçamento olha para o futuro e é quantitativo.")

q(p2, "Qual dos itens abaixo NÃO é um dos recursos que o orçamento mostra, segundo a aula?",
  opts("Pessoal.", "Equipamentos.", "Espaço de trabalho.", "Cotação do dólar."),
  "D", "O orçamento mostra os recursos necessários e sua forma de utilização: pessoal, técnicas específicas, equipamentos, espaço de trabalho e dinheiro.",
  "Cinco recursos: pessoal, técnicas, equipamentos, espaço e dinheiro.")

q(p2, "Qual das alternativas apresenta uma característica do orçamento segundo a aula?",
  opts("Não deve ser uma ferramenta inflexível.", "Deve ser imutável depois de aprovado.",
       "Dispensa a análise de viabilidade.", "Estimula a tomada de decisão no improviso."),
  "A", "Características: evita a tomada de decisão no improviso, não deve ser inflexível, minimiza riscos de ameaças, gera segurança e baseia-se na viabilidade.",
  "O orçamento evita o improviso e admite ajustes.")

q(p2, "Qual das alternativas apresenta um objetivo do orçamento?",
  opts("Tornar-se uma forma de avaliação de performance.", "Substituir o planejamento estratégico.",
       "Eliminar a necessidade de controle.", "Impor as metas sem participação dos gerentes."),
  "A", "Objetivos: direcionar os gerentes ao planejamento, fornecer informações para melhorar a tomada de decisão, servir de forma de avaliação de performance e melhorar a comunicação e a coordenação.",
  "Um dos objetivos é justamente medir o desempenho.")

q(p2, "Qual das alternativas descreve uma vantagem do orçamento apontada na aula?",
  opts("Reduz o envolvimento dos altos administradores com as operações diárias, por meio da delegação de poderes e de autoridade.",
       "Elimina qualquer estimativa e incerteza do processo.",
       "Dispensa a coordenação entre as áreas.",
       "Impede que se identifiquem pontos de deficiência das unidades."),
  "A", "Vantagens citadas: definir metas, pensar o futuro, alocar recursos de forma otimizada, descobrir gargalos, coordenar atividades, comunicar os planos, fixar objetivos e políticas, delegar poderes, identificar eficiência ou deficiência das unidades e melhorar a utilização dos recursos.",
  "Pense em delegação: a cúpula sai do operacional.")

q(p2, "Por que os orçamentos podem falhar em se concretizar, segundo a aula?",
  opts("Porque os dados contidos neles são estimativas, sujeitas a eventos internos e externos que podem inviabilizar a previsão.",
       "Porque o orçamento sempre é elaborado sem dados.",
       "Porque o orçamento só considera o passado.",
       "Porque o controle orçamentário é proibido."),
  "A", "Os dados do orçamento não passam de estimativas e estão sujeitos a eventos internos e externos que afetam a previsão.",
  "Orçamento = estimativa.")

q(p2, "Um sistema orçamentário, segundo a aula,",
  opts("contempla todas as atividades operacionais e acessórias, dispõe de controle eficiente para apurar desvios e prevê e controla fluxos de caixa, resultados e patrimônio.",
       "abrange apenas as vendas e ignora as demais atividades.",
       "não precisa apurar desvios, apenas registrar os valores.",
       "prevê somente o patrimônio, sem considerar caixa."),
  "A", "As características do sistema orçamentário incluem: projeção para o futuro, expressão monetária, flexibilidade, comprometimento, completude, oportunidade, uniformidade e controle.",
  "Completo e com controle de desvios.")

q(p2, "“Período de planejamento (anual, semestral, coincidente com o ano civil ou não)” é exemplo de qual tipo de premissa orçamentária?",
  opts("Estrutural.", "Operacional.", "Econômico-financeira.", "Tributária."),
  "A", "Premissas estruturais: moeda de decisão e período de planejamento. Operacionais: fatores de consumo de materiais e mão de obra, hierarquia de produtos, estrutura organizacional, centros de custos. Econômico-financeiras: inflação, juros, preços dos insumos e variação cambial.",
  "Moeda e período de planejamento formam o grupo das premissas estruturais.")

q(p2, "No cenário e premissas orçamentárias, a taxa de juros representa",
  opts("o custo de oportunidade de reter o recurso.", "o nível de atividade econômica do país.",
       "a perda do poder aquisitivo da moeda.", "a variação do preço dos insumos importados."),
  "A", "Na aula: PIB é o nível de atividade econômica do país; inflação é a perda do poder aquisitivo da moeda; taxa de juros é o custo de oportunidade de reter o recurso.",
  "Juros: custo de oportunidade.")

q(p2, "Qual das alternativas é um exemplo de meta de desempenho (e não de meta de lucro), segundo a aula?",
  opts("Redução do índice de inadimplência dos clientes.", "Definição da missão da empresa.",
       "Escolha da moeda de decisão.", "Estimativa do PIB do período."),
  "A", "Metas orçamentárias quantificam os objetivos do planejamento estratégico e se dividem em metas de lucro e de desempenho. Exemplos de desempenho: aumento do giro dos ativos, redução da devolução de vendas, da inadimplência, do custo de mão de obra, do endividamento e da imobilização do PL.",
  "Meta de desempenho é um indicador operacional a melhorar.")

# ============================================================
# PROVA 3 — Aula 2: Implantação e controle
# ============================================================

p3 = new_prova("Prova 3 — Aula 2: Implantação e Controle", "aula2_implantacao_controle")

qa(p3, "A participação dos gerentes na elaboração do orçamento aumenta a aceitação das metas e o empenho em cumpri-las.",
   "Nessa situação, as metas orçamentárias não foram impostas pela alta administração.",
   "A", "Ambas são verdadeiras e a II justifica a I: a aula afirma que a aceitação e o empenho são maiores justamente porque as metas não foram impostas pela alta administração.",
   "A segunda frase explica por que a primeira acontece?")

q(p3, "Na aula, “contabilidade aberta, informatizada e descentralizada” significa",
  opts("um processo autogerenciável, com o lançamento contábil feito na origem pelo próprio usuário.",
       "que apenas o contador pode lançar valores no sistema.",
       "que os dados contábeis ficam restritos à diretoria.",
       "que a contabilidade é feita manualmente ao final do ano."),
  "A", "Uma das condições para implantar o orçamento é a contabilidade aberta, informatizada e descentralizada: processo autogerenciável, com lançamento feito na origem pelo próprio usuário.",
  "Descentralizada: quem gera o fato faz o lançamento.")

q(p3, "As condições para a implantação do orçamento apontadas por Welsch são:",
  opts("um sistema de informação, com dados contábeis, históricos adequados e apropriados.",
       "apenas o apoio verbal da diretoria.",
       "a ausência de dados históricos, para não engessar a projeção.",
       "a imposição das metas pela alta administração."),
  "A", "Para Welsch, as condições são um sistema de informação com dados contábeis e históricos adequados e apropriados.",
  "Sistema de informação + dados contábeis + histórico.")

q(p3, "Qual das alternativas é um fator imprescindível para a implantação do orçamento, segundo a aula?",
  opts("Expectativas realistas.", "Implantação muito apressada.",
       "Expectativa prematura de resultados.", "Papelada e detalhes excessivos."),
  "A", "Fatores imprescindíveis: envolvimento da alta administração, adaptação organizacional, definição de objetivos, comunicação integral, expectativas realistas, oportunidade, reconhecimento de esforços individuais e em grupo e acompanhamento. As demais alternativas são falhas de implantação.",
  "Três das alternativas são erros de implantação.")

q(p3, "Qual das alternativas é uma falha na implantação do orçamento, segundo a aula?",
  opts("Implantação muito apressada.", "Comunicação integral.",
       "Envolvimento da alta administração.", "Reconhecimento de esforços individuais e em grupo."),
  "A", "Entre as falhas: estrutura organizacional inadequada, sistema ineficaz de registro contábil, falta de sistema de custos, falta de apoio da cúpula, expectativas exageradas ou prematuras, implantação apressada, supervisão deficiente, falta de cooperação, falta de dados históricos, papelada excessiva, período de projeção longo demais e falta de flexibilidade.",
  "Procure o que atrapalha, não o que ajuda.")

q(p3, "O controle orçamentário é a técnica que procura",
  opts("acompanhar, avaliar e analisar o planejamento financeiro, verificando as defasagens entre orçado e realizado para sugerir medidas saneadoras na próxima proposta orçamentária.",
       "elaborar o orçamento sem comparar com o realizado.",
       "substituir o planejamento estratégico.",
       "registrar apenas o que aconteceu no passado, sem sugerir medidas."),
  "A", "Definição da aula: acompanhar, avaliar e analisar o planejamento financeiro em suas várias etapas, verificando as defasagens entre valores orçados e realizados, para sugerir medidas saneadoras na próxima proposta orçamentária.",
  "Compara orçado x realizado e sugere medidas.")

qa(p3, "O controle orçamentário permite sugerir medidas preventivas, corretivas e saneadoras em tempo hábil.",
   "O controle orçamentário confronta os valores realizados com os orçados e analisa as defasagens positivas e negativas.",
   "A", "Ambas são verdadeiras e a II explica a I: é ao confrontar realizado x orçado e analisar as defasagens que se conseguem sugerir medidas em tempo hábil.",
   "Sem comparar orçado e realizado não há como sugerir medidas.")

q(p3, "A meta orçada de vendas de um mês era de R$ 500.000,00 e as vendas realizadas somaram R$ 460.000,00. Qual o desvio percentual em relação ao orçado e como ele se classifica?",
  opts("−8%, desfavorável.", "+8%, favorável.", "−8%, favorável.", "+8,7%, desfavorável."),
  "A", "Desvio = (460.000 − 500.000) ÷ 500.000 = −8%. Como as vendas ficaram abaixo do orçado, o desvio é desfavorável.",
  "Desvio % = (Realizado − Orçado) ÷ Orçado. Para receitas, abaixo do orçado é desfavorável.")

q(p3, "A despesa orçada de um departamento era de R$ 80.000,00 e a despesa realizada foi de R$ 92.000,00. O desvio é de",
  opts("R$ 12.000,00 (15%), desfavorável, pois o gasto superou o orçado.", "R$ 12.000,00 (15%), favorável.",
       "R$ 12.000,00 (13%), desfavorável.", "R$ 8.000,00 (10%), favorável."),
  "A", "Desvio = 92.000 − 80.000 = 12.000, ou 12.000 ÷ 80.000 = 15% (o percentual é sobre o orçado). Para despesas, gastar acima do orçado é desfavorável.",
  "O percentual do desvio sempre usa o valor ORÇADO como base.")

q(p3, "Segundo a aula, os indicadores de desempenho podem ser referenciados em qual conjunto de níveis?",
  opts("Nível mundial, nível nacional/estadual e nível interno.", "Apenas nível interno.",
       "Apenas nível mundial.", "Nível diário, semanal e mensal."),
  "A", "Na aula, os indicadores de desempenho são apresentados em nível mundial, nacional/estadual e interno, e podem ser acompanhados em painéis (vendas e marketing, cliente, financeiros, pessoas, operações, TI e gestão de projetos).",
  "Do mais amplo ao mais interno: mundial, nacional/estadual, interno.")

# ============================================================
# PROVA 4 — Aula 3: Elaboração das peças
# ============================================================

SCENARIO_P = (
    "A Móveis Serra Verde projeta, para o Mês 1: vendas de 1.000 unidades; estoque inicial de produtos acabados de "
    "200 un e estoque final desejado de 300 un. Cada unidade consome 4 kg de matéria-prima. O estoque inicial de "
    "matéria-prima é de 1.000 kg e o estoque final desejado é de 1.400 kg."
)

p4 = new_prova("Prova 4 — Aula 3: Elaboração das Peças", "aula3_elaboracao")

q(p4, "Na consolidação do orçamento empresarial, a peça que serve de ponto de partida e alimenta as demais (produção, despesas operacionais, investimentos, marketing e caixa) é o orçamento de",
  opts("vendas.", "caixa.", "investimentos.", "marketing."),
  "A", "A previsão de vendas é o ponto de partida do orçamento empresarial: dela derivam produção (matéria-prima, mão de obra e custos indiretos), despesas operacionais, investimentos, marketing e caixa.",
  "O que vender determina todo o resto.")

q(p4, "Na previsão de vendas, qual dos fatores abaixo é um fator EXTERNO (e não interno)?",
  opts("Concorrência e intensidade da competição.", "Capacidade produtiva.",
       "Custo e disponibilidade de capital.", "Estrutura administrativa."),
  "A", "Fatores internos: capacidade produtiva, vendas e marketing, engenharia e gestão e finanças. Fatores externos: mercado, competitividade, economia e governo, tecnologia e impactos ambientais.",
  "Três alternativas descrevem a empresa por dentro.")

q(p4, "Segundo a aula, na política de preços e volumes, se o preço permanece e o volume de itens vendidos aumenta, a tendência é que",
  opts("lucro e rentabilidade aumentem.", "lucro e rentabilidade diminuam.",
       "o preço tenha de cair obrigatoriamente.", "o orçamento de vendas deixe de ser o ponto de partida."),
  "A", "Nos esquemas da aula, tanto o aumento do preço mantido o volume quanto o aumento do volume mantido o preço levam a aumento de lucro e rentabilidade.",
  "Mais unidades vendidas ao mesmo preço.")

q(p4, "O método de estimação de vendas baseado no levantamento de intenções de compradores, opiniões de vendedores e opiniões de especialistas é classificado, na aula, como",
  opts("método baseado no que se diz.", "método baseado no crescimento histórico (médias aritméticas ou geométricas).",
       "método baseado no que se fez (modelos matemáticos e estatísticos).", "método baseado em determinantes de crescimento (ROE, alavancagem, margem e giro)."),
  "A", "A aula separa: crescimento histórico; crescimento esperado da empresa/setor/economia; previsão dos analistas; determinantes de crescimento; métodos baseados no que se diz (levantamentos) e método baseado no que se fez (instrumental matemático e estatístico).",
  "Perguntar a compradores, vendedores e especialistas = “o que se diz”.")

q(p4, "Na aula, qual dos itens abaixo é um aspecto inerente ao nível de estoque desejado no orçamento de produção?",
  opts("Sazonalidade das vendas.", "Cotação da moeda estrangeira.",
       "Localização da matriz da empresa.", "Escolha das cores da embalagem."),
  "A", "O nível de estoque desejado depende da sazonalidade das vendas, da capacidade financeira e de crédito e da disponibilidade de mão de obra capacitada.",
  "Vendas sazonais exigem estoques diferentes ao longo do ano.")

q(p4, SCENARIO_P + "\n\nQuantas unidades devem ser produzidas no Mês 1? (Produção = Vendas + Estoque Final desejado − Estoque Inicial)",
  opts("900 un.", "1.000 un.", "1.100 un.", "1.500 un."),
  "C", "Produção = 1.000 + 300 − 200 = 1.100 unidades.",
  "Produção = Vendas + Estoque Final desejado − Estoque Inicial.")

q(p4, SCENARIO_P + "\n\nConsiderando a produção de 1.100 unidades, quantos kg de matéria-prima devem ser comprados no Mês 1? (Compras = Consumo + Estoque Final − Estoque Inicial)",
  opts("4.000 kg.", "4.400 kg.", "4.800 kg.", "5.200 kg."),
  "C", "Consumo = 1.100 × 4 = 4.400 kg. Compras = 4.400 + 1.400 − 1.000 = 4.800 kg.",
  "Primeiro calcule o consumo (produção × 4 kg), depois ajuste pelos estoques de matéria-prima.")

q(p4, "No orçamento dos custos de produção, “máquinas e equipamentos compartilhados”, “mão de obra compartilhada” e “insumos compartilhados” compõem o orçamento dos",
  opts("custos gerais/indiretos de fabricação (CIF).", "custos com matérias-primas.",
       "custos de marketing.", "custos com despesas tributárias."),
  "A", "O orçamento de produção divide-se em matérias-primas (insumos, embalagens, rótulos, suprimentos), mão de obra e custos gerais/indiretos de fabricação, que envolvem recursos compartilhados entre produtos.",
  "Recursos compartilhados entre vários produtos são indiretos.")

q(p4, "“Perdas com devedores duvidosos” são classificadas, no orçamento de despesas operacionais, como despesas",
  opts("com vendas.", "administrativas.", "tributárias.", "financeiras."),
  "A", "Despesas com vendas: salários e encargos dos vendedores, impostos sobre a venda, aluguel do ponto de venda, telefonemas, fretes, perdas com devedores duvidosos e cobrança. Administrativas: controladoria, contabilidade, seguros, aluguel administrativo, etc. Tributárias: IPI, ICMS, ISS, PIS, COFINS, IRPJ, CSLL etc. Financeiras: juros e correção monetária (recebidos somam; pagos e tarifas subtraem).",
  "Pense em quem gera a perda: as vendas a prazo.")

q(p4, "O orçamento de investimentos, segundo a aula, contempla",
  opts("acréscimos, melhoramentos, substituições de ativos e patentes, alinhados à estratégia global, pois determinam o crescimento futuro da empresa.",
       "apenas as despesas de marketing do período.",
       "apenas os salários dos vendedores.",
       "o controle diário do caixa."),
  "A", "O orçamento de investimentos trata de acréscimos, melhoramentos, substituição de ativos, patentes e fundos reservados a esses fins, com uso de métodos de avaliação e alinhamento à estratégia global.",
  "Ativos de longo prazo e crescimento futuro.")

# ============================================================
# PROVA 5 — Aulas 3 e 5: Vendas, caixa e DRE projetada
# ============================================================

SCENARIO_V = (
    "A Distribuidora Atlântica Med projeta vender kits hospitalares a R$ 120,00 por unidade: "
    "Mês 1 – 1.000 un; Mês 2 – 1.200 un; Mês 3 – 1.500 un. Sobre a receita incidem impostos de 5% e comissões de "
    "vendas de 4%. O custo variável é de R$ 50,00 por unidade e as despesas administrativas somam R$ 60.000,00 no trimestre."
)

SCENARIO_C = (
    "A Comercial Bela Vista vende 60% à vista e 40% a prazo, recebendo a parcela a prazo no mês seguinte. Vendas: "
    "Mês 0: R$ 80.000,00; Mês 1: R$ 100.000,00; Mês 2: R$ 120.000,00. Pagamentos totais: Mês 1: R$ 85.000,00; "
    "Mês 2: R$ 130.000,00. Saldo inicial de caixa no Mês 1: R$ 5.000,00."
)

p5 = new_prova("Prova 5 — Aulas 3 e 5: Vendas, Caixa e DRE Projetada", "aula3_5_numerico")

q(p5, SCENARIO_V + "\n\nQual a receita orçada total do trimestre (preço × quantidade)?",
  opts("R$ 420.000,00.", "R$ 432.000,00.", "R$ 444.000,00.", "R$ 460.000,00."),
  "C", "Mês 1: 1.000 × 120 = 120.000; Mês 2: 1.200 × 120 = 144.000; Mês 3: 1.500 × 120 = 180.000. Total = R$ 444.000,00.",
  "Receita = preço × quantidade de cada mês; depois some os três meses.")

q(p5, SCENARIO_V + "\n\nQual o total de impostos (5%) do trimestre?",
  opts("R$ 21.000,00.", "R$ 22.200,00.", "R$ 23.400,00.", "R$ 24.000,00."),
  "B", "5% × 444.000 = R$ 22.200,00. Os impostos dependem do volume e dos valores projetados no orçamento de vendas.",
  "Aplique 5% sobre a receita do trimestre.")

q(p5, SCENARIO_V + "\n\nQual o total de comissões de vendas (4%) do trimestre?",
  opts("R$ 16.000,00.", "R$ 17.760,00.", "R$ 18.500,00.", "R$ 22.200,00."),
  "B", "4% × 444.000 = R$ 17.760,00.",
  "Comissão = 4% × receita do trimestre.")

q(p5, SCENARIO_V + "\n\nNa Demonstração de Resultado Projetada, qual a receita líquida do trimestre (receita − impostos sobre vendas)?",
  opts("R$ 399.600,00.", "R$ 421.800,00.", "R$ 426.240,00.", "R$ 444.000,00."),
  "B", "Receita líquida = 444.000 − 22.200 = R$ 421.800,00.",
  "Receita líquida = receita bruta menos os impostos sobre vendas.")

q(p5, SCENARIO_V + "\n\nQual o lucro bruto projetado do trimestre (receita líquida − custo variável dos produtos vendidos)?",
  opts("R$ 186.800,00.", "R$ 236.800,00.", "R$ 259.000,00.", "R$ 271.800,00."),
  "B", "Volume = 1.000 + 1.200 + 1.500 = 3.700 un. Custo = 3.700 × 50 = 185.000. Lucro bruto = 421.800 − 185.000 = R$ 236.800,00.",
  "Some as unidades dos três meses e multiplique por R$ 50,00.")

q(p5, SCENARIO_V + "\n\nQual o resultado projetado do trimestre, após deduzir também as comissões (R$ 17.760,00) e as despesas administrativas?",
  opts("R$ 119.040,00.", "R$ 159.040,00.", "R$ 176.800,00.", "R$ 219.040,00."),
  "B", "Resultado = 236.800 − 17.760 − 60.000 = R$ 159.040,00. A DRE projetada permite analisar a formação do resultado, confrontando a previsão de vendas com deduções, impostos, custos e despesas.",
  "Do lucro bruto, subtraia as comissões e as despesas administrativas.")

q(p5, SCENARIO_C + "\n\nQual o total de recebimentos do Mês 1?",
  opts("R$ 60.000,00.", "R$ 88.000,00.", "R$ 92.000,00.", "R$ 100.000,00."),
  "C", "À vista do Mês 1: 60% × 100.000 = 60.000. A prazo, das vendas do Mês 0: 40% × 80.000 = 32.000. Total = R$ 92.000,00.",
  "Recebimentos = parte à vista do mês + parte a prazo das vendas do mês anterior.")

q(p5, SCENARIO_C + "\n\nQual o saldo final de caixa do Mês 1?",
  opts("R$ 7.000,00.", "R$ 12.000,00.", "R$ 17.000,00.", "R$ 92.000,00."),
  "B", "Saldo final = 5.000 + 92.000 − 85.000 = R$ 12.000,00.",
  "Saldo final = saldo inicial + recebimentos − pagamentos.")

q(p5, SCENARIO_C + "\n\nO Mês 2 tem recebimentos de R$ 112.000,00 (à vista 72.000 + a prazo 40.000). Qual o saldo final do Mês 2 e o que o fluxo de caixa projetado indica?",
  opts("−R$ 6.000,00: insuficiência de disponibilidades, indicando necessidade de empréstimos ou renegociação de prazos.",
       "R$ 6.000,00: excesso de disponibilidades, sugerindo investimento temporário.",
       "R$ 18.000,00: excesso de disponibilidades.", "R$ 0,00: caixa perfeitamente equilibrado."),
  "A", "Saldo final = 12.000 + 112.000 − 130.000 = −R$ 6.000,00. O fluxo de caixa projetado indica excesso ou insuficiência de disponibilidades e a necessidade de empréstimos ou a disponibilidade de fundos para investimento temporário.",
  "Parta do saldo final do Mês 1 (R$ 12.000,00).")

qa(p5, "Uma empresa pode ter lucro contábil e, ainda assim, enfrentar falta de liquidez.",
   "As vendas a prazo geram receita reconhecida antes do efetivo recebimento do dinheiro.",
   "A", "Ambas são verdadeiras e a II explica a I: a receita entra no resultado na venda, mas o caixa só é recebido depois, o que pode gerar falta de dinheiro mesmo com lucro. Por isso existe o orçamento de caixa.",
   "Receita reconhecida = dinheiro no caixa?")

# ============================================================
# PROVA 6 — Aula 4: Tipos de orçamento
# ============================================================

p6 = new_prova("Prova 6 — Aula 4: Tipos de Orçamento", "aula4_tipos")

q(p6, "Sobre o orçamento estático, segundo a aula, é correto afirmar que",
  opts("é o próprio orçamento empresarial tradicional, elaborado a partir de determinados níveis de produção ou vendas, em que a gestão não tolera alterações nas peças orçamentárias.",
       "é refeito continuamente, a cada mês, com novos períodos.",
       "exige justificar todos os gastos a partir de zero.",
       "ajusta automaticamente todos os custos ao volume real."),
  "A", "O orçamento estático é o orçamento tradicional, montado sobre níveis definidos de produção ou vendas, sem tolerância a alterações; se os volumes não puderem ser atingidos por fatores incontroláveis, ele perde a utilidade.",
  "Estático = parado em um único nível de atividade.")

q(p6, "No orçamento contínuo, conforme o esquema da aula (20x1 e 20x2),",
  opts("à medida que um mês sai (encerra), um novo mês entra no fim do horizonte, mantendo o planejamento sempre à frente.",
       "o orçamento é feito uma única vez para o ano e não muda mais.",
       "todo gasto é justificado do zero a cada ano.",
       "o período de planejamento é sempre o ano civil fixo."),
  "A", "No orçamento contínuo, o mês 1 sai e o mês 1 de 20x2 entra, e assim sucessivamente: quebra-se o paradigma do período anual, com análises constantes e mensais.",
  "Uma janela de 12 meses que vai “rolando”.")

qa(p6, "No orçamento contínuo, é possível replanejar e refazer projeções continuamente.",
   "O orçamento contínuo incorpora condições variáveis em momentos oportunos e mantém os envolvidos no processo orçamentário.",
   "A", "Ambas são verdadeiras e a II explica a I: por incorporar condições variáveis em momentos oportunos e manter os envolvidos continuamente no processo, é possível replanejar diante de circunstâncias não esperadas.",
   "A segunda frase descreve o mecanismo que permite a primeira.")

q(p6, "Sobre o Orçamento Base Zero (OBZ), segundo a aula, é correto afirmar que",
  opts("o histórico não é o ponto de partida: todas as atividades são analisadas e os recursos são submetidos à aprovação, em vez de apenas incrementar percentuais sobre o período passado.",
       "o ponto de partida é sempre o ano anterior, acrescido de um percentual.",
       "as despesas do passado são aprovadas automaticamente.",
       "é elaborado de cima para baixo, sem envolver as chefias."),
  "A", "No OBZ, o histórico NÃO é ponto de partida; todos os recursos e atividades são analisados e submetidos a aprovação; é elaborado de baixo para cima, exige envolvimento de todos os níveis de chefia e busca eliminar a perpetuação de ineficiências históricas.",
  "“Base zero” quer dizer sem herdar o passado automaticamente.")

q(p6, "No exemplo da aula, os insumos custam R$ 1,00 por unidade e a meta do mês é de R$ 10.000,00 (ou 10.000 unidades). A pergunta “se a empresa vender 12.000 unidades, não poderei fabricar neste mês?” ilustra qual aspecto negativo do OBZ?",
  opts("A possível inflexibilidade diante de variações de volume, pois o gasto aprovado limita a produção acima do previsto.",
       "A perpetuação de ineficiências históricas.",
       "A aprovação automática de despesas do ano anterior.",
       "A ausência de qualquer análise de custo-benefício."),
  "A", "O exemplo mostra o risco de o OBZ engessar a gestão: com o orçamento aprovado para 10.000 unidades, uma venda maior (12.000) não teria o insumo correspondente aprovado. É o tipo de situação que o orçamento flexível procura resolver.",
  "Meta rígida de 10.000 unidades x demanda de 12.000.")

q(p6, "O orçamento flexível, segundo a aula,",
  opts("é ajustado conforme as mudanças no nível de atividade real, comparando os custos incorridos com os necessários para aquele nível, e depura os insumos em custos fixos e variáveis.",
       "mantém um único nível de atividade durante todo o período.",
       "ignora a separação entre custos fixos e variáveis.",
       "parte sempre de zero para cada atividade."),
  "A", "O orçamento flexível mostra quanto serão os custos em vários níveis de atividade, exige conhecimento do comportamento dos custos e separa custos fixos e variáveis.",
  "Flexível = recalcula para o volume que realmente aconteceu.")

q(p6, "No exemplo de orçamento flexível da aula: Mês 1 com 10.000 unidades (gasto fixo R$ 100.000,00 e variável R$ 40.000,00) e Mês 2 com 12.000 unidades (gasto fixo R$ 100.000,00 e variável R$ 48.000,00). Qual o gasto total por unidade no Mês 2?",
  opts("R$ 12,33.", "R$ 14,00.", "R$ 10,00.", "R$ 15,60."),
  "A", "Mês 2: 100.000 + 48.000 = 148.000; ÷ 12.000 = R$ 12,33 por unidade. No Mês 1 era 140.000 ÷ 10.000 = R$ 14,00. O custo por unidade cai porque o gasto fixo é diluído em mais unidades (o variável é R$ 4,00 por unidade nos dois meses).",
  "Gasto total ÷ unidades do Mês 2.")

q(p6, "Com preço de venda de R$ 20,00 por unidade e gasto total exato de R$ 148.000,00 no Mês 2 (12.000 unidades), qual o lucro do mês?",
  opts("R$ 92.000,00.", "R$ 60.000,00.", "R$ 240.000,00.", "R$ 148.000,00."),
  "A", "Receita = 12.000 × 20 = 240.000. Lucro = 240.000 − 148.000 = R$ 92.000,00. (No slide aparece R$ 92.040,00 porque usa o gasto unitário arredondado de R$ 12,33 × 12.000 = 147.960; o valor exato é R$ 92.000,00. No Mês 1 o lucro é 200.000 − 140.000 = R$ 60.000,00.)",
  "Receita (12.000 × R$ 20,00) menos o gasto total.")

q(p6, "O orçamento por atividades, segundo a aula, permite",
  opts("associar os custos à produção, identificar melhor os recursos necessários, eliminar atividades supérfluas e identificar folgas orçamentárias.",
       "elaborar orçamentos menos realistas, mas mais rápidos.",
       "ignorar a responsabilidade do quadro funcional.",
       "manter todas as atividades independentemente do benefício."),
  "A", "O orçamento por atividades baseia-se na precificação das atividades e seus benefícios: orçamentos mais realistas, melhor identificação dos recursos, associação dos custos à produção, vinculação dos custos às responsabilidades, identificação de folgas e eliminação de atividades supérfluas.",
  "Cada atividade é precificada e avaliada pelo benefício.")

q(p6, "Sobre o Beyond Budgeting (“além do orçamento”), segundo a aula, é correto afirmar que",
  opts("é um conjunto de métodos adaptativos, com prazos de análise mais curtos, metas por indicadores-chave, desempenho comparado ao mercado e gestores com elevada autonomia para reagir a mudanças.",
       "reforça a centralização do poder e o orçamento anual rígido.",
       "avalia o desempenho apenas com base em resultados anteriores internos.",
       "surgiu em siderúrgicas e nunca migrou para outros setores."),
  "A", "Beyond Budgeting tem origem em empresas de software, com métodos ágeis migrando para outros setores, prazos trimestrais ou semestrais, metas por indicadores-chave, desempenho com base no mercado e gestores autônomos. Critica o orçamento tradicional por ser demorado, caro, pouco focado na estratégia e centralizador.",
  "Pense em agilidade e autonomia, o oposto do orçamento rígido e centralizado.")

# ============================================================
# Validation and output
# ============================================================

assert len(PROVAS) == 6, len(PROVAS)
for p in PROVAS:
    assert len(p["questions"]) == 10, (p["name"], len(p["questions"]))
    for item in p["questions"]:
        keys = set(item["options"].keys())
        assert keys in ({"A", "B", "C", "D"}, {"A", "B", "C", "D", "E"}), (p["name"], keys)
        assert item["correct"] in item["options"], (p["name"], item["question"][:50])

total_questions = sum(len(p["questions"]) for p in PROVAS)
assert total_questions == 60, total_questions

out_provas = []
for pi, prova in enumerate(PROVAS, start=1):
    entries = []
    for qi, item in enumerate(prova["questions"], start=1):
        entries.append({
            "id": f"orc-p{pi}-q{qi:02d}",
            "topic": prova["topic"],
            "topicLabel": TOPIC_LABELS[prova["topic"]],
            "question": item["question"],
            "options": item["options"],
            "correct": item["correct"],
            "explanation": item["explanation"],
            "hint": item["hint"],
            "source": "slides Aulas 1-5",
        })
    out_provas.append({"name": prova["name"], "topic": prova["topic"], "questions": entries})

out_path = Path(__file__).resolve().parent.parent / "data" / "orc_questions.json"
out_path.write_text(json.dumps({"provas": out_provas}, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Wrote {len(out_provas)} provas ({total_questions} questions) to {out_path}")
