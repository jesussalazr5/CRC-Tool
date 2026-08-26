import json
from pathlib import Path

# ============================================================
# S&OP / CAPEX — Planejamento Integrado e Estratégia de Capacidade
# 60 practical questions, organized as 6 provas of 10, for
# interview prep (Analista de Planejamento Integrado / S&OP).
# Original content covering CAPEX/OPEX trade-offs, VPL/TIR,
# S&OP cycle, OEE/capacity, inventory/seasonality, and
# scarce-resource product-mix allocation.
# ============================================================

TOPIC_LABELS = {
    "capex_opex_payback": "CAPEX vs OPEX: Payback e Custo Unitário",
    "vpl_tir_fluxo_caixa": "VPL, TIR e Fluxo de Caixa Incremental",
    "sop_ciclo_conceitos": "S&OP: Ciclo e Conceitos",
    "capacidade_oee_gargalos": "Capacidade, OEE e Gargalos",
    "estoques_giro_sazonalidade": "Estoques, Giro e Sazonalidade",
    "mix_producao_margem": "Mix de Produção e Margem de Contribuição",
}

PROVAS = []


def new_prova(name, topic):
    p = {"name": name, "topic": topic, "questions": []}
    PROVAS.append(p)
    return p


def q(prova, question, options, correct, explanation, hint):
    prova["questions"].append(dict(question=question, options=options, correct=correct,
                                    explanation=explanation, hint=hint))


# ============================================================
# CENÁRIO A — Alimentos Vale Verde S.A. (CAPEX vs OPEX)
# Usado na Prova 1.
# ============================================================

SCENARIO_A = (
    "A Alimentos Vale Verde S.A. avalia como atender ao crescimento de demanda de sua linha de Lasanhas Congeladas:\n"
    "• Capacidade atual: 850.000 un/mês\n"
    "• Alternativa OPEX (3º turno): capacidade adicional de 380.000 un/mês; custo variável do turno extra R$ 2,27/un "
    "(vs R$ 1,85/un nos turnos regulares); sem investimento inicial\n"
    "• Alternativa CAPEX (nova linha): investimento de R$ 18.000.000,00; capacidade adicional de 600.000 un/mês; "
    "custo variável de R$ 1,65/un; custos fixos adicionais de R$ 900.000,00/ano; produção adicional média de "
    "500.000 un/mês assim que entrar em operação\n"
    "• Preço de venda médio: R$ 4,20/un\n"
    "• Demanda projetada para o Ano 3: 1.150.000 un/mês"
)

p1 = new_prova("Prova 1 — CAPEX vs OPEX: Payback e Custo Unitário", "capex_opex_payback")

q(p1, SCENARIO_A + "\n\nQual a capacidade total da fábrica se optar pelo 3º turno (OPEX)?",
  {"A": "1.150.000 un/mês.", "B": "1.230.000 un/mês.", "C": "1.300.000 un/mês.", "D": "1.450.000 un/mês."},
  "B", "Capacidade total = 850.000 + 380.000 = 1.230.000 un/mês.",
  "Some a capacidade atual à capacidade adicional do 3º turno.")

q(p1, SCENARIO_A + "\n\nQual a capacidade total da fábrica se optar pela nova linha (CAPEX)?",
  {"A": "1.230.000 un/mês.", "B": "1.350.000 un/mês.", "C": "1.450.000 un/mês.", "D": "1.550.000 un/mês."},
  "C", "Capacidade total = 850.000 + 600.000 = 1.450.000 un/mês.",
  "Some a capacidade atual à capacidade adicional da nova linha.")

q(p1, SCENARIO_A + "\n\nQual a margem de contribuição unitária nos turnos regulares (atuais)?",
  {"A": "R$ 1,93.", "B": "R$ 2,15.", "C": "R$ 2,35.", "D": "R$ 2,55."},
  "C", "Margem = Preço − Custo Variável = 4,20 − 1,85 = R$ 2,35.",
  "Margem de contribuição = Preço de venda − Custo variável unitário.")

q(p1, SCENARIO_A + "\n\nQual a margem de contribuição unitária no 3º turno (OPEX)?",
  {"A": "R$ 1,73.", "B": "R$ 1,93.", "C": "R$ 2,15.", "D": "R$ 2,35."},
  "B", "Margem = 4,20 − 2,27 = R$ 1,93 — menor do que nos turnos regulares, por causa do custo variável mais alto.",
  "Use o custo variável específico do turno extra (R$ 2,27).")

q(p1, SCENARIO_A + "\n\nQual a margem de contribuição unitária na nova linha (CAPEX)?",
  {"A": "R$ 2,35.", "B": "R$ 2,45.", "C": "R$ 2,55.", "D": "R$ 2,65."},
  "C", "Margem = 4,20 − 1,65 = R$ 2,55 — a maior das três, pela maior eficiência da linha nova.",
  "Use o custo variável da nova linha (R$ 1,65).")

q(p1, SCENARIO_A + "\n\nConsiderando que a nova linha produzirá, em média, 500.000 unidades/mês adicionais assim que entrar em operação, qual a margem de contribuição ANUAL gerada por essa produção adicional (500.000 un/mês × 12 meses × R$ 2,55/un)?",
  {"A": "R$ 13.260.000,00.", "B": "R$ 14.500.000,00.", "C": "R$ 15.300.000,00.", "D": "R$ 16.200.000,00."},
  "C", "500.000 × 12 × 2,55 = R$ 15.300.000,00.",
  "Volume mensal × 12 meses × margem de contribuição unitária da nova linha.")

q(p1, SCENARIO_A + "\n\nDescontando os custos fixos adicionais de R$ 900.000,00/ano, qual o fluxo de caixa incremental ANUAL líquido gerado pela nova linha (considerando a margem de contribuição anual de R$ 15.300.000,00)?",
  {"A": "R$ 13.400.000,00.", "B": "R$ 14.400.000,00.", "C": "R$ 14.900.000,00.", "D": "R$ 15.300.000,00."},
  "B", "15.300.000 − 900.000 = R$ 14.400.000,00.",
  "Fluxo de caixa incremental = Margem de contribuição anual − Custos fixos adicionais.")

q(p1, SCENARIO_A + "\n\nCom base no fluxo de caixa líquido ANUAL de R$ 14.400.000,00 e no investimento de R$ 18.000.000,00, qual o Payback Simples aproximado da nova linha?",
  {"A": "1,00 ano.", "B": "1,25 anos.", "C": "1,50 anos.", "D": "2,00 anos."},
  "B", "Payback Simples = Investimento ÷ Fluxo de Caixa Anual = 18.000.000 ÷ 14.400.000 = 1,25 anos.",
  "Payback Simples = Investimento inicial ÷ Fluxo de caixa anual líquido.")

q(p1, SCENARIO_A + "\n\nComparando o custo variável unitário das três opções (turno regular R$ 1,85; 3º turno R$ 2,27; nova linha R$ 1,65), é correto afirmar que",
  {"A": "o 3º turno tem o menor custo unitário.", "B": "a nova linha tem o menor custo unitário, sendo a opção mais eficiente por unidade produzida.",
   "C": "os três custos unitários são iguais.", "D": "o turno regular é a opção mais cara."},
  "B", "R$ 1,65 (nova linha) < R$ 1,85 (turno regular) < R$ 2,27 (3º turno) — a nova linha é a mais eficiente em custo unitário.",
  "Compare os três valores diretamente: menor custo unitário = mais eficiente.")

q(p1, SCENARIO_A + "\n\nConsiderando que a demanda no Ano 3 alcançará 1.150.000 un/mês, qual alternativa garante capacidade suficiente com MAIOR folga para crescimento futuro?",
  {"A": "Somente o 3º turno (1.230.000 un/mês de capacidade, folga de 80.000 un/mês).",
   "B": "Somente a nova linha (1.450.000 un/mês de capacidade, folga de 300.000 un/mês).",
   "C": "Nenhuma das duas alternativas atende à demanda do Ano 3.", "D": "As duas alternativas têm exatamente a mesma folga de capacidade."},
  "B", "3º turno: folga de 1.230.000 − 1.150.000 = 80.000 un/mês (apertada). Nova linha: folga de 1.450.000 − 1.150.000 = 300.000 un/mês (folga maior, mais espaço para crescer além do Ano 3).",
  "Subtraia a demanda do Ano 3 da capacidade total de cada alternativa e compare as folgas.")

# ============================================================
# CENÁRIO B — Indústria Campo Fértil Ltda. (VPL e TIR)
# Usado na Prova 2.
# ============================================================

SCENARIO_B = (
    "A Indústria Campo Fértil Ltda. avalia um investimento em uma nova linha de embalagem automatizada:\n"
    "• Investimento inicial: R$ 5.000.000,00\n"
    "• Fluxo de caixa incremental líquido: R$ 2.000.000,00/ano, constante por 4 anos\n"
    "• Taxa de desconto (WACC): 10% ao ano\n"
    "• Valor residual ao final do Ano 4: R$ 0,00 (desprezar)\n"
    "Fatores de desconto a 10% a.a.: Ano 1 = 0,9091; Ano 2 = 0,8264; Ano 3 = 0,7513; Ano 4 = 0,6830"
)

p2 = new_prova("Prova 2 — VPL, TIR e Fluxo de Caixa Incremental", "vpl_tir_fluxo_caixa")

q(p2, SCENARIO_B + "\n\nQual o Payback Simples desse investimento?",
  {"A": "2,0 anos.", "B": "2,5 anos.", "C": "3,0 anos.", "D": "3,5 anos."},
  "B", "Payback Simples = 5.000.000 ÷ 2.000.000 = 2,5 anos.",
  "Payback Simples = Investimento ÷ Fluxo de caixa anual.")

q(p2, SCENARIO_B + "\n\nQual o valor presente do fluxo de caixa do Ano 1 (R$ 2.000.000,00 × fator de desconto de 0,9091)?",
  {"A": "R$ 1.652.800,00.", "B": "R$ 1.818.200,00.", "C": "R$ 1.900.000,00.", "D": "R$ 2.000.000,00."},
  "B", "2.000.000 × 0,9091 = R$ 1.818.200,00.",
  "Multiplique o fluxo de caixa do ano pelo fator de desconto correspondente.")

q(p2, SCENARIO_B + "\n\nQual o valor presente do fluxo de caixa do Ano 2 (R$ 2.000.000,00 × fator de desconto de 0,8264)?",
  {"A": "R$ 1.502.600,00.", "B": "R$ 1.600.000,00.", "C": "R$ 1.652.800,00.", "D": "R$ 1.818.200,00."},
  "C", "2.000.000 × 0,8264 = R$ 1.652.800,00.",
  "Multiplique R$ 2.000.000,00 pelo fator de desconto do Ano 2.")

q(p2, SCENARIO_B + "\n\nQual o valor presente do fluxo de caixa do Ano 3 (R$ 2.000.000,00 × fator de desconto de 0,7513)?",
  {"A": "R$ 1.366.000,00.", "B": "R$ 1.502.600,00.", "C": "R$ 1.652.800,00.", "D": "R$ 1.700.000,00."},
  "B", "2.000.000 × 0,7513 = R$ 1.502.600,00.",
  "Multiplique R$ 2.000.000,00 pelo fator de desconto do Ano 3.")

q(p2, SCENARIO_B + "\n\nSomando os valores presentes dos 4 anos (R$ 1.818.200 + R$ 1.652.800 + R$ 1.502.600 + R$ 1.366.000), qual o valor presente TOTAL dos fluxos de caixa?",
  {"A": "R$ 5.339.600,00.", "B": "R$ 6.000.000,00.", "C": "R$ 6.339.600,00.", "D": "R$ 7.339.600,00."},
  "C", "1.818.200 + 1.652.800 + 1.502.600 + 1.366.000 = R$ 6.339.600,00.",
  "Some os quatro valores presentes anuais já calculados.")

q(p2, SCENARIO_B + "\n\nQual o VPL (Valor Presente Líquido) desse investimento (Valor Presente Total dos fluxos − Investimento inicial)?",
  {"A": "R$ 1.000.000,00.", "B": "R$ 1.339.600,00.", "C": "R$ 1.500.000,00.", "D": "R$ 2.339.600,00."},
  "B", "VPL = 6.339.600 − 5.000.000 = R$ 1.339.600,00.",
  "VPL = Valor Presente Total dos fluxos de caixa − Investimento inicial.")

q(p2, SCENARIO_B + "\n\nComo o VPL calculado é positivo, é correto afirmar que",
  {"A": "o investimento deve ser rejeitado, pois destrói valor.", "B": "o investimento deve ser aceito, pois gera valor acima do custo de capital exigido (10% a.a.).",
   "C": "o Payback é automaticamente menor que 1 ano.", "D": "não é possível calcular a TIR desse projeto."},
  "B", "Um VPL positivo indica que o projeto remunera o capital investido acima da taxa mínima exigida (WACC) — ele deve ser aceito, do ponto de vista financeiro.",
  "VPL positivo = projeto gera retorno acima do custo de capital exigido.")

q(p2, "A Taxa Interna de Retorno (TIR) de um projeto é, por definição,",
  {"A": "a taxa de desconto que faz o VPL do projeto ser igual a zero.", "B": "sempre igual à taxa de desconto (WACC) utilizada no VPL.",
   "C": "o mesmo que o Payback Simples.", "D": "sempre menor que o WACC quando o VPL é positivo."},
  "A", "A TIR é, por definição, a taxa de desconto na qual o VPL do projeto se torna exatamente zero.",
  "Pense na TIR como “a taxa que zera o VPL”.")

q(p2, "Sabendo que o VPL do projeto da Indústria Campo Fértil é positivo à taxa de 10% a.a., é correto afirmar sobre a TIR desse projeto que",
  {"A": "a TIR é necessariamente maior do que 10% a.a.", "B": "a TIR é necessariamente menor do que 10% a.a.",
   "C": "a TIR é necessariamente igual a 10% a.a.", "D": "não há relação entre o VPL calculado e a TIR."},
  "A", "Como o VPL decresce à medida que a taxa de desconto aumenta, um VPL positivo a 10% a.a. implica que a taxa que zeraria o VPL (a TIR) é maior do que 10% a.a.",
  "O VPL cai conforme a taxa de desconto sobe — se está positivo a 10%, a TIR (que zera o VPL) fica acima de 10%.")

q(p2, "Comparando VPL e Payback Simples como critérios de decisão de investimento, é correto afirmar que",
  {"A": "o Payback Simples considera o valor do dinheiro no tempo, enquanto o VPL não.",
   "B": "o VPL considera o valor do dinheiro no tempo (fluxos descontados) e todo o horizonte do projeto, enquanto o Payback Simples ignora ambos.",
   "C": "os dois critérios sempre levam exatamente à mesma decisão.", "D": "o Payback Simples é sempre mais completo do que o VPL."},
  "B", "O Payback Simples é uma medida rápida e intuitiva, mas ignora o valor do dinheiro no tempo e os fluxos após o período de payback. O VPL corrige ambas as limitações.",
  "Pense nas limitações clássicas do Payback Simples versus o que o VPL corrige.")

# ============================================================
# PROVA 3 — S&OP: Ciclo e Conceitos (conceitual, sem cenário numérico)
# ============================================================

p3 = new_prova("Prova 3 — S&OP: Ciclo e Conceitos", "sop_ciclo_conceitos")

q(p3, "S&OP (Sales and Operations Planning) é, por definição, um processo que busca principalmente",
  {"A": "substituir o orçamento anual da empresa.", "B": "integrar, em um ciclo recorrente, as áreas comercial, operações/supply chain e financeiro em um plano único e factível.",
   "C": "ser responsabilidade exclusiva da área de vendas.", "D": "eliminar completamente a necessidade de previsão de demanda."},
  "B", "S&OP é, na essência, um processo de integração multifuncional que busca alinhar demanda, capacidade e resultado financeiro em um plano único e executável.",
  "A palavra-chave é “integração” entre áreas — não é um processo de uma área só.")

q(p3, "O ciclo tradicional de S&OP costuma ser composto pelas seguintes etapas, em ordem:",
  {"A": "Executive S&OP → Demand Review → Supply Review → Reconciliation.", "B": "Demand Review → Supply Review → Reconciliation (Pre-S&OP) → Executive S&OP.",
   "C": "Supply Review → Executive S&OP → Demand Review → Reconciliation.", "D": "Reconciliation → Demand Review → Executive S&OP → Supply Review."},
  "B", "A sequência clássica é: primeiro se valida a demanda, depois se avalia a capacidade de atendê-la, depois se reconciliam os gaps, e só então a decisão sobe para o nível executivo.",
  "Pense na lógica: primeiro entender o que se quer vender, depois se dá para produzir, depois resolver os gaps, e só então decidir no topo.")

q(p3, "Na etapa de Demand Review do S&OP, o principal objetivo é",
  {"A": "definir o investimento em CAPEX do próximo ano.", "B": "consolidar e validar a previsão de vendas (forecast), incorporando inteligência comercial e de mercado.",
   "C": "aprovar o plano financeiro anual.", "D": "calcular o OEE das linhas de produção."},
  "B", "A Demand Review é o momento de consolidar e validar o forecast de vendas, incorporando visão comercial, de mercado e de novos lançamentos.",
  "Demand Review = sobre a DEMANDA, não sobre capacidade ou finanças.")

q(p3, "Na etapa de Supply Review, a área de Operações/Supply Chain avalia principalmente",
  {"A": "a viabilidade de atender ao plano de demanda com a capacidade, estoque e recursos disponíveis, identificando gaps e restrições.",
   "B": "o preço de venda dos produtos.", "C": "a estratégia de marketing da empresa.", "D": "apenas o fluxo de caixa da empresa."},
  "A", "A Supply Review confronta o plano de demanda validado com a capacidade real de produção, estoque e recursos, identificando onde há gaps ou restrições.",
  "Supply Review = a resposta operacional ao que foi validado na Demand Review.")

q(p3, "A etapa de Reconciliation (ou Pre-S&OP) tem como principal função",
  {"A": "aprovar o plano estratégico de 5 anos.", "B": "identificar e resolver os gaps entre o plano de demanda e o plano de suprimento, preparando cenários e recomendações para a decisão executiva.",
   "C": "substituir a reunião executiva.", "D": "definir apenas o orçamento de marketing."},
  "B", "A Reconciliation é onde os gaps entre demanda e capacidade são trabalhados, com cenários e recomendações preparados para a decisão final no Executive S&OP.",
  "É a etapa “ponte” — prepara as opções antes de subir para a decisão executiva.")

q(p3, "No Executive S&OP, a decisão final sobre trade-offs (como priorizar um cliente estratégico em caso de restrição de capacidade) deve ser tomada por",
  {"A": "apenas o time de Supply Chain, sem envolvimento de outras áreas.", "B": "a liderança executiva multifuncional (geralmente com participação de Vendas, Operações, Finanças e a Diretoria/CEO).",
   "C": "apenas o time comercial.", "D": "o fornecedor externo de matéria-prima."},
  "B", "Decisões de trade-off que afetam múltiplas áreas (receita, capacidade, custo) precisam ser tomadas no nível executivo, com visão multifuncional — não isoladamente por uma única área.",
  "Pense em quem tem visão e autoridade sobre TODAS as áreas afetadas pela decisão.")

q(p3, "Quando o plano de vendas (otimista) excede a capacidade fabril disponível, a forma mais estruturada de conciliar esse gap dentro do processo de S&OP é",
  {"A": "ignorar a restrição e aprovar o plano de vendas como está.", "B": "apresentar cenários alternativos (priorização de SKUs/clientes, turno extra, CAPEX, terceirização) com seus respectivos custos e trade-offs, para decisão na etapa executiva.",
   "C": "cortar a previsão de vendas pela metade, sem análise.", "D": "transferir toda a decisão para o time de TI."},
  "B", "A abordagem estruturada é traduzir o gap em cenários concretos e quantificados (custo, capacidade, risco), permitindo que a decisão executiva seja tomada com dados, não no escuro.",
  "A resposta certa sempre envolve trazer OPÇÕES QUANTIFICADAS, não decidir sozinho nem ignorar o problema.")

q(p3, "Um KPI comum para medir a aderência entre o que foi planejado no S&OP e o que efetivamente aconteceu é",
  {"A": "o Forecast Accuracy (acurácia da previsão de demanda).", "B": "o EBITDA da empresa.", "C": "o preço da ação no mercado.", "D": "a taxa de câmbio."},
  "A", "O Forecast Accuracy mede diretamente o quão próxima a previsão de demanda ficou do realizado — um dos KPIs centrais de maturidade do processo de S&OP.",
  "Pense em qual métrica mede diretamente “planejado x realizado” na ponta de demanda.")

q(p3, "Sobre a periodicidade do ciclo de S&OP, é correto afirmar que",
  {"A": "o ciclo é executado apenas uma vez, no início do ano.", "B": "o ciclo é tipicamente mensal, com um horizonte de planejamento rolante (ex.: 18 a 24 meses à frente).",
   "C": "o ciclo deve ser executado a cada 5 anos.", "D": "não existe periodicidade definida."},
  "B", "O S&OP é, por natureza, um processo recorrente mensal, com horizonte de planejamento rolante — não um evento único ou esporádico.",
  "S&OP é um CICLO recorrente, não um evento pontual.")

q(p3, "Ao defender, para a Diretoria e o time de Engenharia, o adiamento de um investimento (CAPEX) milionário, uma abordagem tecnicamente sólida é",
  {"A": "apenas afirmar que o CAPEX não é prioridade, sem dados de suporte.",
   "B": "apresentar alternativas de curto prazo (como otimização de OEE, regimes de turno, revisão de mix) que postergam a necessidade do investimento sem comprometer o atendimento à demanda, sustentadas por números de capacidade, custo e risco.",
   "C": "pedir para a área financeira decidir sozinha, sem envolvimento técnico.", "D": "recusar-se a discutir o tema até o próximo ano fiscal."},
  "B", "A defesa tecnicamente sólida sempre se apoia em dados quantificados (capacidade, custo, risco) mostrando alternativas viáveis de curto prazo — não em afirmações sem embasamento.",
  "Pense em como você mostraria, com números, que existe uma alternativa viável antes do CAPEX.")

# ============================================================
# CENÁRIO C — Metalcor Alimentos (Capacidade, OEE e Gargalos)
# Usado na Prova 4.
# ============================================================

SCENARIO_C = (
    "Uma linha de produção da Metalcor Alimentos apresenta os seguintes dados de um turno de 8 horas (480 minutos):\n"
    "• Tempo de parada (setup, manutenção, paradas não planejadas): 60 minutos\n"
    "• Velocidade padrão: 100 unidades/minuto\n"
    "• Produção real no turno: 33.600 unidades\n"
    "• Unidades com defeito (retrabalho/descarte): 600 unidades"
)

p4 = new_prova("Prova 4 — Capacidade, OEE e Gargalos", "capacidade_oee_gargalos")

q(p4, SCENARIO_C + "\n\nQual o Tempo Disponível de produção nesse turno (Tempo Total − Tempo de Parada)?",
  {"A": "360 min.", "B": "420 min.", "C": "440 min.", "D": "480 min."},
  "B", "Tempo Disponível = 480 − 60 = 420 minutos.",
  "Tempo Disponível = Tempo Total do turno − Tempo de Parada.")

q(p4, SCENARIO_C + "\n\nQual o Índice de Disponibilidade desse turno (Tempo Disponível ÷ Tempo Total)?",
  {"A": "75,0%.", "B": "80,0%.", "C": "87,5%.", "D": "90,0%."},
  "C", "Disponibilidade = 420 ÷ 480 = 87,5%.",
  "Disponibilidade = Tempo Disponível ÷ Tempo Total do turno.")

q(p4, SCENARIO_C + "\n\nQual a Produção Teórica Máxima no tempo disponível (Tempo Disponível × Velocidade Padrão)?",
  {"A": "36.000 un.", "B": "38.500 un.", "C": "40.000 un.", "D": "42.000 un."},
  "D", "Produção Teórica = 420 min × 100 un/min = 42.000 unidades.",
  "Produção Teórica = Tempo Disponível × Velocidade Padrão.")

q(p4, SCENARIO_C + "\n\nQual o Índice de Performance desse turno (Produção Real ÷ Produção Teórica Máxima)?",
  {"A": "72%.", "B": "78%.", "C": "80%.", "D": "84%."},
  "C", "Performance = 33.600 ÷ 42.000 = 80%.",
  "Performance = Produção Real ÷ Produção Teórica Máxima.")

q(p4, SCENARIO_C + "\n\nQuantas unidades boas (sem defeito) foram produzidas nesse turno?",
  {"A": "32.400.", "B": "33.000.", "C": "33.600.", "D": "34.200."},
  "B", "Unidades boas = 33.600 − 600 = 33.000.",
  "Unidades boas = Produção Real − Unidades com defeito.")

q(p4, SCENARIO_C + "\n\nQual o Índice de Qualidade desse turno (Unidades Boas ÷ Produção Real), aproximadamente?",
  {"A": "95,0%.", "B": "96,5%.", "C": "98,2%.", "D": "99,5%."},
  "C", "Qualidade = 33.000 ÷ 33.600 ≈ 98,2%.",
  "Qualidade = Unidades Boas ÷ Produção Real.")

q(p4, SCENARIO_C + "\n\nQual o OEE (Overall Equipment Effectiveness) dessa linha (Disponibilidade × Performance × Qualidade), aproximadamente?",
  {"A": "60,0%.", "B": "65,0%.", "C": "67,5%.", "D": "72,0%."},
  "C", "OEE = 87,5% × 80% × 98,2% ≈ 67,5%.",
  "OEE = Disponibilidade × Performance × Qualidade (multiplique os três índices já calculados).")

q(p4, "Um OEE de classe mundial costuma ser referenciado na literatura como próximo de",
  {"A": "50%.", "B": "65%.", "C": "85%.", "D": "100%."},
  "C", "A referência mais citada na literatura de manufatura para “classe mundial” é um OEE em torno de 85%.",
  "É um número frequentemente citado como benchmark de excelência operacional.")

q(p4, SCENARIO_C + "\n\nDiante de um OEE de aproximadamente 67,5% calculado nessa linha, uma ação prioritária e de baixo investimento para elevar a capacidade efetiva, ANTES de considerar CAPEX, seria",
  {"A": "atacar as perdas de Disponibilidade e Performance (reduzir paradas, otimizar setup, eliminar microparadas), que juntas têm mais impacto do que a Qualidade nesse caso.",
   "B": "investir imediatamente em uma nova linha, sem investigar as causas de perda.", "C": "reduzir a velocidade padrão da linha.", "D": "aumentar o número de unidades com defeito."},
  "A", "Disponibilidade (87,5%) e Performance (80%) têm mais espaço de melhoria do que Qualidade (98,2%, já bem próxima do ideal) — atacar essas duas frentes normalmente gera ganho de capacidade sem CAPEX.",
  "Compare os três índices: qual tem mais “gordura” para queimar antes de precisar de investimento?")

q(p4, "Um “gargalo” (bottleneck), em uma linha de produção com múltiplas etapas, é definido como",
  {"A": "qualquer etapa do processo, independentemente de sua capacidade.", "B": "a etapa (ou recurso) com a MENOR capacidade, que limita a capacidade de todo o sistema, independentemente da capacidade das demais etapas.",
   "C": "sempre a última etapa do processo.", "D": "a etapa com o menor custo variável."},
  "B", "O gargalo é a etapa com menor capacidade dentro do fluxo — ela dita o ritmo máximo de todo o sistema, mesmo que as demais etapas tenham capacidade sobrando.",
  "O gargalo é sempre o “elo mais fraco da corrente” em termos de capacidade.")

# ============================================================
# CENÁRIO D — Congelados Serra Azul Ltda. (Estoques, Giro e Sazonalidade)
# Usado na Prova 5.
# ============================================================

SCENARIO_D = (
    "A Congelados Serra Azul Ltda. apresenta os seguintes dados de um SKU de sobremesas congeladas:\n"
    "• Custo das Vendas (CMV) do último ano: R$ 7.200.000,00\n"
    "• Estoque médio do período: R$ 600.000,00\n"
    "• Ano com 360 dias\n"
    "• Validade (shelf-life) do produto: 90 dias"
)

p5 = new_prova("Prova 5 — Estoques, Giro e Sazonalidade", "estoques_giro_sazonalidade")

q(p5, SCENARIO_D + "\n\nQual o Giro de Estoque desse SKU (CMV ÷ Estoque Médio)?",
  {"A": "8 vezes/ano.", "B": "10 vezes/ano.", "C": "12 vezes/ano.", "D": "15 vezes/ano."},
  "C", "Giro = 7.200.000 ÷ 600.000 = 12 vezes/ano.",
  "Giro = CMV ÷ Estoque Médio.")

q(p5, SCENARIO_D + "\n\nQual a Cobertura de Estoque em dias (Days of Supply), considerando o giro de 12 vezes/ano e um ano de 360 dias?",
  {"A": "24 dias.", "B": "30 dias.", "C": "36 dias.", "D": "45 dias."},
  "B", "Cobertura = 360 ÷ 12 = 30 dias.",
  "Cobertura em dias = número de dias do período ÷ Giro.")

q(p5, "Em produtos perecíveis/congelados, uma cobertura de estoque excessivamente ALTA representa principalmente o risco de",
  {"A": "falta de produto para atender o cliente.", "B": "perdas por vencimento/validade (shelf-life) e maior custo de armazenagem em câmara fria.",
   "C": "aumento da margem de contribuição.", "D": "redução do custo variável de produção."},
  "B", "Estoque excessivo em produtos perecíveis aumenta o risco de perda por vencimento e eleva o custo de armazenagem (câmara fria), sem necessariamente gerar benefício.",
  "Pense no que acontece quando um produto com validade curta fica parado em estoque por muito tempo.")

q(p5, "Já uma cobertura de estoque excessivamente BAIXA, em um produto sazonal, representa principalmente o risco de",
  {"A": "ruptura de estoque (stockout) durante picos de demanda, perdendo vendas ou market share.", "B": "excesso de capital de giro imobilizado.",
   "C": "maior risco de perdas por validade.", "D": "redução do custo de armazenagem."},
  "A", "Cobertura baixa demais deixa a empresa vulnerável a rupturas quando a demanda sobe (picos sazonais), com risco de perda de vendas e até de espaço de gôndola/mercado.",
  "Pense no oposto do excesso de estoque: o risco de faltar produto num pico de venda.")

q(p5, "“Nivelamento de produção” (level loading/level scheduling), como estratégia para lidar com sazonalidade de demanda, consiste em",
  {"A": "produzir exatamente a demanda de cada mês, variando fortemente o volume produzido mês a mês.",
   "B": "manter um ritmo de produção mais constante ao longo do ano, formando estoque nos períodos de baixa demanda para atender aos picos, dentro dos limites de capacidade de armazenagem.",
   "C": "parar totalmente a produção nos meses de baixa demanda.", "D": "só é aplicável a produtos não perecíveis."},
  "B", "O nivelamento busca produzir em ritmo mais constante, formando estoque na entressafra para atender aos picos sazonais, respeitando as restrições de armazenagem e validade.",
  "A ideia central é “suavizar” a produção ao longo do ano, e não seguir a demanda mês a mês.")

q(p5, SCENARIO_D + "\n\nPara esse produto, com validade de 90 dias, uma política de nivelamento de produção que gerasse uma cobertura de estoque de 75 dias representaria",
  {"A": "um risco relevante de perda por vencimento, já que resta pouca margem de segurança dentro do prazo de validade.",
   "B": "uma situação totalmente segura, sem nenhum risco.", "C": "uma cobertura baixa demais para o produto.", "D": "uma situação irrelevante para a decisão de nivelamento."},
  "A", "75 dias de cobertura sobre uma validade de 90 dias deixa apenas 15 dias de margem — um risco relevante de perda por vencimento, especialmente considerando o tempo de distribuição até o ponto de venda.",
  "Compare a cobertura (75 dias) com o prazo de validade total (90 dias) — quanto sobra de margem?")

q(p5, "O trade-off central do nivelamento de produção para itens sazonais e perecíveis é equilibrar",
  {"A": "o custo de produzir fora do pico (turnos extras, ineficiências) contra o custo/risco de formar estoque (armazenagem, capital de giro, shelf-life).",
   "B": "apenas o preço de venda do produto.", "C": "apenas o câmbio da moeda.", "D": "o número de fornecedores de matéria-prima."},
  "A", "O nivelamento sempre pesa dois lados: o custo de atender picos com capacidade extra versus o custo/risco de antecipar produção e carregar estoque.",
  "Pense nos dois lados da balança: custo de produzir no pico x custo/risco de estocar antes.")

q(p5, "Se a demanda de um produto congelado triplica no verão em relação ao inverno, e a capacidade fabril é fixa, uma alternativa operacional (sem CAPEX) para atender ao pico é",
  {"A": "antecipar parte da produção no inverno/entressafra e formar estoque, respeitando o shelf-life e a capacidade de câmara fria.",
   "B": "simplesmente recusar pedidos no verão.", "C": "reduzir o preço de venda no verão.", "D": "eliminar o produto do portfólio."},
  "A", "Antecipar produção na entressafra (nivelamento) é a alternativa operacional clássica para atender picos sazonais sem investir em capacidade adicional — desde que a validade e a câmara fria suportem.",
  "Pense na estratégia de nivelamento aplicada diretamente a esse caso.")

q(p5, "O Estoque de Segurança (safety stock) tem como principal objetivo",
  {"A": "maximizar o lucro contábil do período.", "B": "proteger o nível de serviço contra variabilidade de demanda e/ou de suprimento, reduzindo o risco de ruptura.",
   "C": "eliminar totalmente a necessidade de previsão de demanda.", "D": "reduzir o custo variável de produção."},
  "B", "O estoque de segurança existe para absorver a variabilidade (de demanda ou de suprimento) e proteger o nível de serviço ao cliente, reduzindo o risco de faltar produto.",
  "Pense no propósito de uma “margem de segurança” de estoque.")

q(p5, "Ao decidir o quanto antecipar de produção para um pico sazonal, o Analista de S&OP deve considerar, além da capacidade de câmara fria, principalmente",
  {"A": "apenas o preço da ação da empresa.", "B": "o shelf-life do produto, o custo financeiro de carregar estoque (capital de giro) e o risco de obsolescência/perda.",
   "C": "apenas a opinião pessoal do gestor de vendas.", "D": "nenhum fator adicional além da capacidade fabril."},
  "B", "A decisão de antecipação envolve equilibrar validade do produto, custo financeiro de carregar estoque e risco de perda — não apenas a capacidade de armazenagem física.",
  "Pense em todos os custos e riscos de \"guardar\" produto perecível antes da hora.")

# ============================================================
# CENÁRIO E — Multigrãos Alimentos (Mix de Produção e Margem)
# Usado na Prova 6.
# ============================================================

SCENARIO_E = (
    "A fábrica Multigrãos Alimentos possui um recurso escasso: 4.000 horas-máquina disponíveis no mês na linha de "
    "extrusão, compartilhada entre três produtos:\n"
    "• Produto X: margem de contribuição unitária R$ 3,00; consome 0,5 hora-máquina/unidade; demanda máxima de "
    "mercado: 5.000 unidades/mês\n"
    "• Produto Y: margem de contribuição unitária R$ 5,00; consome 1,0 hora-máquina/unidade; demanda máxima de "
    "mercado: 3.000 unidades/mês\n"
    "• Produto Z: margem de contribuição unitária R$ 8,00; consome 2,0 horas-máquina/unidade; demanda máxima de "
    "mercado: 1.500 unidades/mês"
)

p6 = new_prova("Prova 6 — Mix de Produção e Margem de Contribuição", "mix_producao_margem")

q(p6, SCENARIO_E + "\n\nQual a margem de contribuição por hora-máquina do Produto X?",
  {"A": "R$ 3,00/h.", "B": "R$ 5,00/h.", "C": "R$ 6,00/h.", "D": "R$ 8,00/h."},
  "C", "3,00 ÷ 0,5 = R$ 6,00/hora.",
  "Margem por hora = Margem de contribuição unitária ÷ Horas-máquina consumidas por unidade.")

q(p6, SCENARIO_E + "\n\nQual a margem de contribuição por hora-máquina do Produto Y?",
  {"A": "R$ 4,00/h.", "B": "R$ 5,00/h.", "C": "R$ 6,00/h.", "D": "R$ 8,00/h."},
  "B", "5,00 ÷ 1,0 = R$ 5,00/hora.",
  "Margem por hora = Margem de contribuição unitária ÷ Horas-máquina consumidas por unidade.")

q(p6, SCENARIO_E + "\n\nQual a margem de contribuição por hora-máquina do Produto Z?",
  {"A": "R$ 3,00/h.", "B": "R$ 4,00/h.", "C": "R$ 5,00/h.", "D": "R$ 8,00/h."},
  "B", "8,00 ÷ 2,0 = R$ 4,00/hora.",
  "Margem por hora = Margem de contribuição unitária ÷ Horas-máquina consumidas por unidade.")

q(p6, "Com um recurso escasso (horas-máquina), qual deve ser o critério para priorizar a alocação de produção entre os produtos?",
  {"A": "Priorizar o produto com a MAIOR margem de contribuição unitária, independentemente do consumo do recurso escasso.",
   "B": "Priorizar o produto com a MAIOR margem de contribuição POR UNIDADE DO RECURSO ESCASSO (aqui, por hora-máquina).",
   "C": "Priorizar o produto com a MAIOR demanda de mercado.", "D": "Priorizar o produto com o MENOR preço de venda."},
  "B", "Quando existe um recurso limitante compartilhado, a decisão correta é priorizar pela margem gerada POR UNIDADE do recurso escasso, não pela margem unitária do produto isoladamente.",
  "O critério certo sempre envolve o recurso escasso no denominador — não a margem do produto isolada.")

q(p6, SCENARIO_E + "\n\nConsiderando as margens por hora-máquina (X: R$ 6,00/h; Y: R$ 5,00/h; Z: R$ 4,00/h), qual a ordem de prioridade de produção correta?",
  {"A": "Z, depois Y, depois X.", "B": "Y, depois X, depois Z.", "C": "X, depois Y, depois Z.", "D": "A ordem é indiferente."},
  "C", "Prioriza-se sempre do maior para o menor valor de margem por hora-máquina: X (6,00) > Y (5,00) > Z (4,00).",
  "Ordene do maior para o menor valor de margem por hora-máquina calculado nas questões anteriores.")

q(p6, SCENARIO_E + "\n\nQuantas horas-máquina são necessárias para atender 100% da demanda de mercado do Produto X (5.000 unidades)?",
  {"A": "2.000h.", "B": "2.500h.", "C": "3.000h.", "D": "5.000h."},
  "B", "5.000 un × 0,5h/un = 2.500 horas.",
  "Multiplique a demanda total de X pelo consumo de horas-máquina por unidade.")

q(p6, SCENARIO_E + "\n\nApós alocar as horas necessárias para atender 100% da demanda do Produto X, quantas horas-máquina restam disponíveis (de um total de 4.000h)?",
  {"A": "1.000h.", "B": "1.500h.", "C": "2.000h.", "D": "2.500h."},
  "B", "4.000 − 2.500 = 1.500 horas restantes.",
  "Subtraia as horas já usadas por X do total disponível (4.000h).")

q(p6, SCENARIO_E + "\n\nCom as horas-máquina restantes (1.500h), quantas unidades do Produto Y é possível produzir (cada unidade consome 1,0h)?",
  {"A": "1.000 un.", "B": "1.500 un.", "C": "2.000 un.", "D": "3.000 un (100% da demanda)."},
  "B", "1.500h ÷ 1,0h/un = 1.500 unidades — as horas se esgotam antes de atender a demanda total de 3.000 unidades de Y.",
  "Divida as horas restantes pelo consumo de horas por unidade de Y — repare que não dá para atender toda a demanda de Y.")

q(p6, SCENARIO_E + "\n\nNessa alocação ótima, quantas unidades do Produto Z serão produzidas?",
  {"A": "0 unidades, pois as horas-máquina se esgotaram antes de alocar para Z.", "B": "750 unidades.", "C": "1.500 unidades (100% da demanda).", "D": "1.000 unidades."},
  "A", "Depois de alocar 2.500h para X e 1.500h para Y, as 4.000h disponíveis já se esgotaram (2.500+1.500=4.000) — não sobra nenhuma hora para produzir Z, mesmo sendo o produto de maior margem unitária absoluta.",
  "Some as horas já usadas por X e Y — sobrou alguma coisa das 4.000h disponíveis?")

q(p6, SCENARIO_E + "\n\nQual a margem de contribuição TOTAL mensal gerada por essa alocação ótima (5.000 un de X + 1.500 un de Y + 0 un de Z)?",
  {"A": "R$ 19.500,00.", "B": "R$ 21.000,00.", "C": "R$ 22.500,00.", "D": "R$ 24.000,00."},
  "C", "(5.000 × 3,00) + (1.500 × 5,00) + (0 × 8,00) = 15.000 + 7.500 + 0 = R$ 22.500,00.",
  "Multiplique a quantidade de cada produto pela sua margem de contribuição unitária e some tudo.")

assert len(PROVAS) == 6, len(PROVAS)
for p in PROVAS:
    assert len(p["questions"]) == 10, (p["name"], len(p["questions"]))

total_questions = sum(len(p["questions"]) for p in PROVAS)
assert total_questions == 60, total_questions

# ============================================================
# Assemble and write data/sop_questions.json
# ============================================================

out_provas = []
for pi, prova in enumerate(PROVAS, start=1):
    entries = []
    for qi, item in enumerate(prova["questions"], start=1):
        entries.append({
            "id": f"sop-p{pi}-q{qi:02d}",
            "topic": prova["topic"],
            "topicLabel": TOPIC_LABELS[prova["topic"]],
            "question": item["question"],
            "options": item["options"],
            "correct": item["correct"],
            "explanation": item["explanation"],
            "hint": item["hint"],
            "source": "original",
        })
    out_provas.append({"name": prova["name"], "topic": prova["topic"], "questions": entries})

data = {"provas": out_provas}
out_path = Path(__file__).resolve().parent.parent / "data" / "sop_questions.json"
out_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Wrote {len(out_provas)} provas ({total_questions} questions total) to {out_path}")
for p in out_provas:
    print(f"  {p['name']}: {len(p['questions'])} questions")
