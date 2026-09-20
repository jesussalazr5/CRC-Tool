import json
from pathlib import Path

# ============================================================
# ORC — Administração / Análise Orçamentária
# 60 practical questions, 6 provas of 10. Original content
# covering: planning levels, budget implementation and control,
# budget types (OBZ, flexible, static, continuous), sales/tax/
# expense budgets, production & materials, cash budget, CIF and
# project management. Includes the "asserção I / II" format.
# ============================================================

TOPIC_LABELS = {
    "planejamento_niveis": "Planejamento Estratégico, Tático e Operacional",
    "implantacao_controle": "Implantação e Controle Orçamentário",
    "tipos_orcamento": "Tipos de Orçamento (Base Zero, Flexível, Estático, Contínuo)",
    "vendas_impostos_despesas": "Orçamento de Vendas, Impostos e Despesas",
    "producao_materiais": "Orçamento de Produção e Matérias-Primas",
    "caixa_cif_projetos": "Orçamento de Caixa, CIF e Projetos",
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


# ============================================================
# PROVA 1 — Planejamento Estratégico, Tático e Operacional
# ============================================================

p1 = new_prova("Prova 1 — Planejamento Estratégico, Tático e Operacional", "planejamento_niveis")

q(p1, "Na estrutura do planejamento estratégico, a Visão de uma organização representa",
  {"A": "a imagem de futuro desejada para a empresa no longo prazo, ou seja, onde ela pretende chegar.",
   "B": "a lista de tarefas diárias de cada colaborador.", "C": "o orçamento aprovado para o próximo mês.",
   "D": "o conjunto de regras operacionais de cada setor."},
  "A", "A Visão descreve o futuro desejado no longo prazo — o “onde queremos chegar”. As demais opções tratam de rotinas, orçamento mensal e regras internas, que pertencem a outros níveis.",
  "Visão = futuro desejado, longo prazo.")

q(p1, "A Missão de uma organização expressa principalmente",
  {"A": "sua razão de existir e o propósito que orienta suas ações no presente, servindo de caminho entre a situação atual e a visão de futuro.",
   "B": "a previsão de vendas do trimestre.", "C": "o resultado contábil do último exercício.", "D": "apenas o preço praticado nos seus produtos."},
  "A", "A Missão responde “para que a empresa existe e como atua hoje”, funcionando como ponte entre o presente e a Visão (o futuro desejado).",
  "Missão = razão de existir e forma de atuar no presente; Visão = onde se quer chegar.")

q(p1, "Uma indústria de alimentos definiu, em reunião da diretoria, ampliar sua participação de mercado nos próximos 5 anos. Em seguida, cada gerente traduziu essa diretriz em metas anuais para sua área, e os supervisores organizaram as tarefas diárias das equipes para cumpri-las. Sobre a relação entre os níveis de planejamento, é correto afirmar que",
  {"A": "o planejamento estratégico orienta as decisões de longo prazo e serve de base para os planejamentos tático e operacional.",
   "B": "o planejamento operacional define a visão de longo prazo da empresa.",
   "C": "os três níveis são independentes e não precisam estar alinhados.",
   "D": "o planejamento tático é responsabilidade exclusiva dos supervisores e se limita às tarefas diárias."},
  "A", "A diretriz de 5 anos é estratégica; as metas anuais por área são táticas; as tarefas diárias são operacionais. Cada nível se desdobra do anterior, e o estratégico é a base dos demais.",
  "Identifique o que é longo prazo (diretoria), médio prazo (gerentes) e curto prazo (supervisores).")

q(p1, "O planejamento tático caracteriza-se por",
  {"A": "traduzir as diretrizes estratégicas em metas e planos por departamento/área, normalmente no médio prazo, sob responsabilidade dos gerentes.",
   "B": "definir a missão e a visão da empresa.", "C": "executar as tarefas rotineiras de produção.",
   "D": "tratar exclusivamente do fluxo de caixa diário."},
  "A", "O nível tático faz a ponte: pega o que a alta direção decidiu e o desdobra em metas e planos por área, tipicamente em horizonte de médio prazo.",
  "Tático = “desdobrar” a estratégia por departamento.")

q(p1, "O planejamento operacional está relacionado principalmente a",
  {"A": "tarefas e rotinas do dia a dia, no curto prazo, executadas pelas equipes sob a coordenação de supervisores.",
   "B": "decisões de longo prazo sobre o posicionamento da empresa.", "C": "definição da visão de futuro.",
   "D": "escolha do mercado em que a empresa atuará daqui a 10 anos."},
  "A", "O operacional trata do “como executar hoje”: rotinas, escalas e tarefas, com foco no curto prazo.",
  "Operacional = execução, dia a dia, curto prazo.")

q(p1, "Analise as afirmativas sobre planejamento:\nI. O planejamento é orientado ao futuro: busca definir aonde se quer chegar e como.\nII. O planejamento é pré-requisito do controle, pois define os padrões que serão comparados ao realizado.\nIII. O planejamento consiste em analisar apenas o passado da empresa, sem se preocupar com o futuro.\nEstão corretas",
  {"A": "I e II, apenas.", "B": "I e III, apenas.", "C": "II e III, apenas.", "D": "I, II e III."},
  "A", "I e II descrevem corretamente o planejamento (voltado ao futuro e base do controle). III é falsa: o planejamento olha para o futuro; o passado serve apenas de referência.",
  "Planejamento olha para frente — isso já elimina a III.")

qa(p1, "O planejamento deve ser tratado como um processo contínuo, e não como um evento pontual.",
   "As condições internas e externas da empresa mudam e exigem revisões e ajustes periódicos.",
   "A", "Ambas são verdadeiras e a II explica a I: como o ambiente muda, o planejamento precisa ser revisto continuamente.",
   "Pergunte-se: a segunda frase explica por que a primeira é verdadeira?")

qa(p1, "Missão e visão são conceitos idênticos e podem ser usados como sinônimos.",
   "Ambas descrevem exclusivamente as tarefas operacionais do dia a dia.",
   "E", "As duas são falsas: missão (propósito atual) e visão (futuro desejado) são conceitos distintos, e nenhum deles trata de tarefas operacionais do dia a dia.",
   "Lembre a diferença: missão = presente/propósito; visão = futuro desejado.")

q(p1, "Qual alternativa associa corretamente cada nível de planejamento ao seu foco predominante?",
  {"A": "Estratégico: longo prazo e alta direção; Tático: médio prazo e departamentos; Operacional: curto prazo e tarefas diárias.",
   "B": "Estratégico: tarefas diárias; Tático: longo prazo; Operacional: definição da visão.",
   "C": "Estratégico: supervisores; Tático: alta direção; Operacional: gerentes.",
   "D": "Os três níveis têm o mesmo foco e horizonte de tempo."},
  "A", "Cada nível tem horizonte e responsáveis próprios: estratégico (longo prazo/alta direção), tático (médio prazo/gerentes) e operacional (curto prazo/supervisores).",
  "Ordene por horizonte de tempo: longo → médio → curto.")

q(p1, "A diretoria definiu como estratégia posicionar os produtos como premium, com margens elevadas, mas a meta atribuída ao gerente comercial é aumentar o volume de vendas por meio de descontos agressivos. O principal problema dessa situação é",
  {"A": "a falta de alinhamento entre o nível estratégico e o tático, gerando metas que contradizem a estratégia.",
   "B": "o excesso de planejamento operacional.", "C": "a ausência de estoques.", "D": "o fato de o orçamento ser flexível."},
  "A", "Se as metas de um nível contradizem a estratégia, os níveis não estão integrados. O planejamento tático deveria desdobrar a estratégia, e não conflitar com ela.",
  "Compare a meta do gerente com a estratégia da diretoria: elas caminham na mesma direção?")

# ============================================================
# PROVA 2 — Implantação e Controle Orçamentário
# ============================================================

p2 = new_prova("Prova 2 — Implantação e Controle Orçamentário", "implantacao_controle")

q(p2, "Uma empresa vai implantar o processo orçamentário. Para que a implantação tenha chance de sucesso, é fundamental",
  {"A": "garantir o apoio da administração, dispor de informações adequadas e assegurar a comunicação entre os envolvidos.",
   "B": "elaborar o orçamento apenas na contabilidade, sem envolver as demais áreas.",
   "C": "impor as metas sem explicá-las aos responsáveis pela execução.",
   "D": "utilizar apenas estimativas sem base em dados da empresa."},
  "A", "Os três pilares clássicos são: apoio da alta administração, informações confiáveis e comunicação clara entre os envolvidos. Sem eles, o orçamento vira apenas um documento formal.",
  "Pense nos três pilares: apoio, informação e comunicação.")

q(p2, "Sobre a participação na elaboração do orçamento, a prática mais adequada é",
  {"A": "envolver vários níveis hierárquicos, especialmente os gestores responsáveis por executar cada parte do orçamento.",
   "B": "restringir a elaboração à alta direção.", "C": "deixar que cada área elabore o seu orçamento de forma totalmente isolada.",
   "D": "entregar o orçamento pronto aos gestores, sem consulta."},
  "A", "O orçamento participativo gera comprometimento e usa o conhecimento de quem executa. Nem a elaboração exclusiva pela cúpula nem a totalmente isolada por área são adequadas.",
  "Quem executa conhece melhor os recursos de que precisa.")

qa(p2, "O orçamento deve envolver os vários níveis hierárquicos da empresa.",
   "Os gestores de cada área conhecem melhor os recursos de que suas áreas necessitam.",
   "A", "Ambas são verdadeiras e a II justifica a I: o conhecimento dos gestores de área é justamente o motivo de sua participação.",
   "A segunda afirmação explica o “porquê” da primeira?")

q(p2, "As fases do controle orçamentário, em sequência lógica, são:",
  {"A": "estabelecer padrões; observar o desempenho; tomar ações corretivas.",
   "B": "tomar ações corretivas; estabelecer padrões; observar o desempenho.",
   "C": "observar o desempenho; tomar ações corretivas; estabelecer padrões.",
   "D": "tomar ações corretivas; observar o desempenho; estabelecer padrões."},
  "A", "Primeiro se definem os padrões (o orçado), depois se observa o desempenho real e se compara, e só então se tomam as ações corretivas — que são a última fase.",
  "A ação corretiva só faz sentido depois de comparar o realizado com o padrão.")

q(p2, "Analise as afirmativas sobre o controle orçamentário:\nI. Estabelecer padrões é a primeira fase do controle.\nII. Observar o desempenho e compará-lo aos padrões é uma fase do controle.\nIII. A ação corretiva é uma fase intermediária, executada antes de observar o desempenho.\nEstão corretas",
  {"A": "I e II, apenas.", "B": "I e III, apenas.", "C": "II e III, apenas.", "D": "I, II e III."},
  "A", "I e II estão corretas. A III é falsa: a ação corretiva é a última fase, feita depois de observar o desempenho e identificar desvios.",
  "Qual fase vem por último na sequência do controle?")

q(p2, "A meta orçada de vendas de um mês era de R$ 500.000,00 e as vendas realizadas somaram R$ 460.000,00. Qual o desvio percentual em relação ao orçado e como ele se classifica?",
  {"A": "−8%, desfavorável.", "B": "+8%, favorável.", "C": "−8%, favorável.", "D": "+8,7%, desfavorável."},
  "A", "Desvio = (460.000 − 500.000) ÷ 500.000 = −8%. Como as vendas ficaram abaixo do orçado, o desvio é desfavorável.",
  "Desvio % = (Realizado − Orçado) ÷ Orçado. Para receitas, abaixo do orçado é desfavorável.")

q(p2, "A despesa orçada de um departamento era de R$ 80.000,00 e a despesa realizada foi de R$ 92.000,00. O desvio é de",
  {"A": "R$ 12.000,00 (15%), desfavorável, pois o gasto superou o orçado.", "B": "R$ 12.000,00 (15%), favorável.",
   "C": "R$ 12.000,00 (13%), desfavorável.", "D": "R$ 8.000,00 (10%), favorável."},
  "A", "Desvio = 92.000 − 80.000 = 12.000, ou 12.000 ÷ 80.000 = 15% (o percentual é sobre o orçado). Para despesas, gastar acima do orçado é desfavorável.",
  "O percentual do desvio sempre usa o valor ORÇADO como base.")

qa(p2, "A revisão periódica do orçamento permite identificar desvios e corrigir o rumo da empresa.",
   "O orçamento é sempre um instrumento rígido, que não admite qualquer revisão depois de aprovado.",
   "C", "A I é verdadeira. A II é falsa: o orçamento deve ter algum grau de flexibilidade e pode ser revisado quando o ambiente muda.",
   "A ideia de que o orçamento “não admite revisão” combina com a I?")

q(p2, "O principal objetivo da análise de desvios entre o orçado e o realizado é",
  {"A": "identificar as causas das diferenças e subsidiar ações corretivas.", "B": "punir os gestores cujas áreas ultrapassaram o orçamento.",
   "C": "substituir a etapa de planejamento.", "D": "eliminar a necessidade de novos orçamentos."},
  "A", "A análise de desvios serve para entender por que o realizado diferiu do orçado e decidir o que corrigir — não para punir nem para substituir o planejamento.",
  "Pense no papel do desvio dentro do ciclo: comparar → entender → corrigir.")

qa(p2, "Dados históricos podem ser usados como referência na elaboração do orçamento.",
   "O orçamento deve ser elaborado de forma isolada por cada área, sem integração com as demais.",
   "C", "A I é verdadeira: o histórico é uma referência útil. A II é falsa: o orçamento é um plano integrado, e as áreas dependem umas das outras (por exemplo, vendas alimentam produção).",
   "Um orçamento integrado pode ser feito “isoladamente” por cada área?")

# ============================================================
# PROVA 3 — Tipos de Orçamento
# ============================================================

SCENARIO_T = (
    "A Tecnologia Norte Ltda. elaborou seu orçamento estático para 10.000 unidades: custo variável de R$ 30,00 por unidade "
    "e custos fixos de R$ 50.000,00 no mês. O volume real do mês foi de 12.000 unidades e o custo total realizado foi "
    "de R$ 420.000,00."
)

p3 = new_prova("Prova 3 — Tipos de Orçamento", "tipos_orcamento")

q(p3, "O orçamento estático é aquele que",
  {"A": "é elaborado para um único nível de atividade e não se ajusta às variações do volume real.",
   "B": "se ajusta automaticamente a qualquer volume de vendas.", "C": "adiciona um novo período sempre que outro termina.",
   "D": "exige justificar todos os gastos a partir de zero."},
  "A", "O orçamento estático parte de um único nível de atividade planejado e permanece o mesmo, mesmo que o volume real seja diferente.",
  "Estático = “parado” em um único nível de atividade.")

q(p3, "O orçamento flexível se caracteriza por",
  {"A": "ajustar os custos variáveis ao volume real de atividade, mantendo os custos fixos, permitindo uma comparação mais justa com o realizado.",
   "B": "manter todos os valores idênticos ao orçado, independentemente do volume.", "C": "ser elaborado uma única vez na vida da empresa.",
   "D": "ignorar os custos variáveis."},
  "A", "O orçamento flexível recalcula o orçado para o volume efetivamente atingido: os custos variáveis acompanham o volume, e os fixos (na faixa relevante) permanecem.",
  "Flexível = recalcula o orçado para o volume que realmente aconteceu.")

q(p3, "No orçamento contínuo (ou rolling budget),",
  {"A": "novos períodos são adicionados à medida que os anteriores terminam, mantendo sempre um horizonte de planejamento à frente.",
   "B": "o orçamento é feito uma única vez e nunca revisado.", "C": "todo gasto precisa ser justificado do zero a cada ciclo.",
   "D": "considera apenas o volume do mês corrente."},
  "A", "No orçamento contínuo, a cada período encerrado acrescenta-se um novo período no fim do horizonte, mantendo o planejamento sempre “rolando” à frente.",
  "Pense em uma janela que vai avançando no tempo.")

q(p3, "O Orçamento Base Zero (OBZ) exige que",
  {"A": "cada despesa seja justificada desde o início a cada ciclo, sem presumir aprovação automática baseada no que foi gasto no passado.",
   "B": "todas as despesas do ano anterior sejam automaticamente aprovadas.", "C": "o orçamento parta sempre do valor do ano anterior mais um percentual.",
   "D": "as despesas fixas sejam eliminadas."},
  "A", "A lógica do OBZ é começar do zero: cada gasto precisa provar seu valor, evitando perpetuar ineficiências históricas.",
  "“Base zero” significa que o passado não garante aprovação.")

qa(p3, "O Orçamento Base Zero não aceita a aprovação automática de despesas com base no que foi gasto no passado.",
   "O OBZ exige a justificativa de cada despesa a cada ciclo orçamentário.",
   "A", "Ambas são verdadeiras e a II é a razão da I: por exigir justificativa a cada ciclo, o OBZ não permite aprovação automática baseada no histórico.",
   "Uma afirmação descreve o efeito; a outra, o mecanismo que o causa.")

q(p3, SCENARIO_T + "\n\nQual o custo total previsto no orçamento estático (10.000 unidades)?",
  {"A": "R$ 300.000,00.", "B": "R$ 350.000,00.", "C": "R$ 410.000,00.", "D": "R$ 420.000,00."},
  "B", "Custo estático = 10.000 × 30 + 50.000 = 300.000 + 50.000 = R$ 350.000,00.",
  "Custo total = custo variável total + custos fixos.")

q(p3, SCENARIO_T + "\n\nQual o custo total do orçamento flexível para o volume real de 12.000 unidades?",
  {"A": "R$ 350.000,00.", "B": "R$ 360.000,00.", "C": "R$ 410.000,00.", "D": "R$ 420.000,00."},
  "C", "Custo flexível = 12.000 × 30 + 50.000 = 360.000 + 50.000 = R$ 410.000,00 (variáveis ajustadas ao volume; fixos mantidos).",
  "Recalcule só o custo variável para 12.000 un; o custo fixo permanece o mesmo.")

q(p3, SCENARIO_T + "\n\nComparando o custo real com o orçamento flexível, o desvio é de",
  {"A": "R$ 10.000,00 desfavorável.", "B": "R$ 10.000,00 favorável.", "C": "R$ 70.000,00 desfavorável.", "D": "R$ 60.000,00 favorável."},
  "A", "Desvio = 420.000 (real) − 410.000 (flexível) = R$ 10.000,00. O custo real superou o que seria esperado para aquele volume, portanto é desfavorável.",
  "Compare o realizado com o orçamento ajustado ao volume real (flexível).")

q(p3, SCENARIO_T + "\n\nSe o custo real (R$ 420.000,00) fosse comparado diretamente com o orçamento estático (R$ 350.000,00), o desvio aparente seria de R$ 70.000,00, o que",
  {"A": "superestimaria o problema, pois grande parte da diferença decorre do maior volume produzido, e não de ineficiência.",
   "B": "seria a medida mais correta de desempenho.", "C": "mostraria que a empresa economizou custos.",
   "D": "não teria nenhuma relação com o volume."},
  "A", "Dos R$ 70.000, R$ 60.000 se explicam pelo volume extra (2.000 un × R$ 30). Só R$ 10.000 são desvio real de eficiência — por isso o flexível é a comparação justa.",
  "Quanto do desvio de R$ 70.000 é explicado apenas por produzir 2.000 unidades a mais?")

qa(p3, "O Orçamento Base Zero resolve automaticamente todos os problemas históricos da empresa.",
   "O OBZ aprova as despesas com base no que foi gasto no ano anterior.",
   "E", "As duas são falsas: o OBZ não é uma solução automática (depende de análise e justificativa) e, sobretudo, não aprova despesas com base no passado — ao contrário, exige justificá-las do zero.",
   "A afirmação II contradiz a própria definição de Base Zero.")

# ============================================================
# PROVA 4 — Orçamento de Vendas, Impostos e Despesas
# ============================================================

SCENARIO_V = (
    "A Distribuidora Atlântica Med projeta vender kits hospitalares a R$ 120,00 por unidade, com o seguinte volume: "
    "Mês 1 – 1.000 unidades; Mês 2 – 1.200 unidades; Mês 3 – 1.500 unidades. Sobre a receita incidem impostos de 5% "
    "e comissões de vendas de 4%."
)

p4 = new_prova("Prova 4 — Orçamento de Vendas, Impostos e Despesas", "vendas_impostos_despesas")

q(p4, SCENARIO_V + "\n\nQual a receita orçada do Mês 1 (preço × quantidade)?",
  {"A": "R$ 100.000,00.", "B": "R$ 120.000,00.", "C": "R$ 144.000,00.", "D": "R$ 180.000,00."},
  "B", "Receita = 1.000 un × R$ 120,00 = R$ 120.000,00.", "Receita = preço unitário × quantidade projetada.")

q(p4, SCENARIO_V + "\n\nQual a receita orçada do Mês 2?",
  {"A": "R$ 120.000,00.", "B": "R$ 132.000,00.", "C": "R$ 144.000,00.", "D": "R$ 150.000,00."},
  "C", "Receita = 1.200 × 120 = R$ 144.000,00.", "Multiplique o preço pela quantidade do Mês 2.")

q(p4, SCENARIO_V + "\n\nQual a receita orçada total do trimestre?",
  {"A": "R$ 420.000,00.", "B": "R$ 432.000,00.", "C": "R$ 444.000,00.", "D": "R$ 460.000,00."},
  "C", "Mês 1: 120.000; Mês 2: 144.000; Mês 3: 1.500 × 120 = 180.000. Total = 120.000 + 144.000 + 180.000 = R$ 444.000,00.",
  "Calcule o Mês 3 (1.500 × 120) e some os três meses.")

q(p4, SCENARIO_V + "\n\nQual o valor dos impostos (5%) do Mês 1?",
  {"A": "R$ 5.000,00.", "B": "R$ 6.000,00.", "C": "R$ 7.200,00.", "D": "R$ 9.000,00."},
  "B", "Imposto = 5% × 120.000 = R$ 6.000,00.", "Imposto = alíquota × receita do mês.")

q(p4, SCENARIO_V + "\n\nQual o valor dos impostos (5%) do Mês 3?",
  {"A": "R$ 7.200,00.", "B": "R$ 8.000,00.", "C": "R$ 9.000,00.", "D": "R$ 10.000,00."},
  "C", "Receita do Mês 3 = 180.000; imposto = 5% × 180.000 = R$ 9.000,00.", "Primeiro ache a receita do Mês 3, depois aplique 5%.")

q(p4, SCENARIO_V + "\n\nQual o total de impostos do trimestre?",
  {"A": "R$ 21.000,00.", "B": "R$ 22.200,00.", "C": "R$ 23.400,00.", "D": "R$ 24.000,00."},
  "B", "5% × 444.000 = R$ 22.200,00 (ou 6.000 + 7.200 + 9.000).", "Aplique 5% sobre a receita total do trimestre.")

q(p4, SCENARIO_V + "\n\nQual o valor das comissões de vendas (4%) do Mês 2?",
  {"A": "R$ 4.800,00.", "B": "R$ 5.760,00.", "C": "R$ 7.200,00.", "D": "R$ 7.680,00."},
  "B", "4% × 144.000 = R$ 5.760,00.", "Comissão = 4% × receita do Mês 2.")

q(p4, "Uma empresa vende, em média, R$ 5.000,00 por dia útil. Janeiro tem 22 dias úteis e fevereiro, 20. Qual a diferença entre os orçamentos de vendas dos dois meses?",
  {"A": "R$ 5.000,00.", "B": "R$ 10.000,00.", "C": "R$ 12.000,00.", "D": "R$ 22.000,00."},
  "B", "Janeiro: 22 × 5.000 = 110.000; fevereiro: 20 × 5.000 = 100.000. Diferença = R$ 10.000,00 — a quantidade de dias do mês influencia diretamente a receita orçada.",
  "Calcule cada mês multiplicando os dias úteis pela venda diária média.")

q(p4, "O orçamento de vendas costuma ser o ponto de partida do processo orçamentário porque",
  {"A": "seus dados alimentam os demais orçamentos (produção, matérias-primas, impostos, despesas com vendas etc.).",
   "B": "é o único que não depende de estimativas.", "C": "dispensa a elaboração dos demais orçamentos.",
   "D": "é elaborado apenas depois do orçamento de caixa."},
  "A", "As vendas previstas determinam quanto produzir, quanto comprar, quais impostos e comissões incidirão — daí o orçamento de vendas ser a peça inicial que abastece as demais.",
  "O que decide quanto será produzido, comprado e taxado?")

qa(p4, "Os impostos sobre vendas dependem do volume e dos valores projetados no orçamento de vendas.",
   "O cálculo dos impostos só pode ser feito depois que o orçamento de vendas estiver definido.",
   "A", "Ambas são verdadeiras e a II decorre da I: como a base de cálculo do imposto é a receita, é preciso definir o orçamento de vendas antes.",
   "A base de cálculo do imposto vem de qual orçamento?")

# ============================================================
# PROVA 5 — Orçamento de Produção e Matérias-Primas
# ============================================================

SCENARIO_P = (
    "A Móveis Serra Verde projeta, para o Mês 1: vendas de 1.000 unidades; estoque inicial de produtos acabados de "
    "200 un e estoque final desejado de 300 un. Cada unidade consome 4 kg de matéria-prima (R$ 5,00/kg) e 2 horas de "
    "mão de obra direta (R$ 15,00/hora). O estoque inicial de matéria-prima é de 1.000 kg e o estoque final desejado "
    "é de 1.400 kg."
)

p5 = new_prova("Prova 5 — Orçamento de Produção e Matérias-Primas", "producao_materiais")

q(p5, SCENARIO_P + "\n\nQuantas unidades devem ser produzidas no Mês 1 (Produção = Vendas + Estoque Final − Estoque Inicial)?",
  {"A": "900 un.", "B": "1.000 un.", "C": "1.100 un.", "D": "1.500 un."},
  "C", "Produção = 1.000 + 300 − 200 = 1.100 unidades.", "Produção = Vendas + Estoque Final desejado − Estoque Inicial.")

q(p5, SCENARIO_P + "\n\nQual o consumo de matéria-prima no Mês 1 (considerando a produção de 1.100 unidades)?",
  {"A": "4.000 kg.", "B": "4.400 kg.", "C": "4.800 kg.", "D": "5.500 kg."},
  "B", "Consumo = 1.100 × 4 kg = 4.400 kg.", "Consumo = unidades produzidas × kg por unidade.")

q(p5, SCENARIO_P + "\n\nQuantos kg de matéria-prima devem ser comprados no Mês 1 (Compras = Consumo + Estoque Final − Estoque Inicial)?",
  {"A": "4.000 kg.", "B": "4.400 kg.", "C": "4.800 kg.", "D": "5.200 kg."},
  "C", "Compras = 4.400 + 1.400 − 1.000 = 4.800 kg.", "Compras = Consumo + Estoque Final desejado − Estoque Inicial de matéria-prima.")

q(p5, SCENARIO_P + "\n\nQual o valor das compras de matéria-prima do Mês 1 (4.800 kg a R$ 5,00/kg)?",
  {"A": "R$ 22.000,00.", "B": "R$ 24.000,00.", "C": "R$ 26.000,00.", "D": "R$ 27.500,00."},
  "B", "4.800 × 5,00 = R$ 24.000,00.", "Multiplique os kg a comprar pelo preço por kg.")

q(p5, SCENARIO_P + "\n\nQuantas horas de mão de obra direta são necessárias no Mês 1 (produção de 1.100 unidades)?",
  {"A": "2.000 h.", "B": "2.200 h.", "C": "2.400 h.", "D": "4.400 h."},
  "B", "Horas = 1.100 × 2 = 2.200 horas.", "Horas = unidades produzidas × horas por unidade.")

q(p5, SCENARIO_P + "\n\nQual o custo da mão de obra direta do Mês 1 (2.200 horas a R$ 15,00/hora)?",
  {"A": "R$ 30.000,00.", "B": "R$ 33.000,00.", "C": "R$ 36.000,00.", "D": "R$ 66.000,00."},
  "B", "2.200 × 15 = R$ 33.000,00.", "Multiplique as horas pelo valor da hora.")

q(p5, "No Mês 2, as vendas previstas são de 1.200 unidades, o estoque inicial de produtos acabados é o estoque final do Mês 1 (300 un) e o estoque final desejado é de 250 un. Qual a produção do Mês 2?",
  {"A": "1.150 un.", "B": "1.200 un.", "C": "1.250 un.", "D": "1.750 un."},
  "A", "Produção = 1.200 + 250 − 300 = 1.150 unidades.", "O estoque inicial do Mês 2 é o final do Mês 1.")

q(p5, "Qual sequência reflete a dependência lógica entre as peças orçamentárias de uma indústria?",
  {"A": "Vendas → Produção → Matérias-primas e mão de obra.", "B": "Matérias-primas → Produção → Vendas.",
   "C": "Mão de obra → Vendas → Produção.", "D": "Produção → Vendas → Matérias-primas."},
  "A", "O que se espera vender define quanto produzir, e a produção define quanto de matéria-prima e mão de obra será necessário.",
  "Comece pelo que “puxa” todas as demais peças.")

qa(p5, "O orçamento de produção depende do orçamento de vendas e da política de estoques da empresa.",
   "A produção necessária é igual às vendas mais o estoque final desejado, menos o estoque inicial.",
   "A", "Ambas são verdadeiras e a II explica a I: a fórmula mostra exatamente como vendas e política de estoques determinam a produção.",
   "A fórmula da II mostra como vendas e estoques entram no cálculo?")

q(p5, SCENARIO_P + "\n\nSe a empresa decidir aumentar o estoque final desejado de produtos acabados de 300 para 400 unidades (mantendo os demais dados), a produção do Mês 1 passa a ser de",
  {"A": "1.000 un.", "B": "1.100 un.", "C": "1.200 un.", "D": "1.300 un."},
  "C", "Produção = 1.000 + 400 − 200 = 1.200 unidades. Aumentar o estoque final exige produzir mais.",
  "Refaça a fórmula com o novo estoque final desejado.")

# ============================================================
# PROVA 6 — Orçamento de Caixa, CIF e Projetos
# ============================================================

SCENARIO_C = (
    "A Comercial Bela Vista vende 60% à vista e 40% a prazo, recebendo a parcela a prazo no mês seguinte. Vendas: "
    "Mês 0: R$ 80.000,00; Mês 1: R$ 100.000,00; Mês 2: R$ 120.000,00. Pagamentos totais: Mês 1: R$ 85.000,00; "
    "Mês 2: R$ 130.000,00. Saldo inicial de caixa no Mês 1: R$ 5.000,00."
)

p6 = new_prova("Prova 6 — Orçamento de Caixa, CIF e Projetos", "caixa_cif_projetos")

q(p6, SCENARIO_C + "\n\nQual o total de recebimentos do Mês 1?",
  {"A": "R$ 60.000,00.", "B": "R$ 88.000,00.", "C": "R$ 92.000,00.", "D": "R$ 100.000,00."},
  "C", "À vista do Mês 1: 60% × 100.000 = 60.000. A prazo recebido do Mês 0: 40% × 80.000 = 32.000. Total = R$ 92.000,00.",
  "Recebimentos = parte à vista do mês + parte a prazo das vendas do mês anterior.")

q(p6, SCENARIO_C + "\n\nQual o saldo final de caixa do Mês 1?",
  {"A": "R$ 7.000,00.", "B": "R$ 12.000,00.", "C": "R$ 17.000,00.", "D": "R$ 92.000,00."},
  "B", "Saldo final = 5.000 + 92.000 − 85.000 = R$ 12.000,00.", "Saldo final = saldo inicial + recebimentos − pagamentos.")

q(p6, SCENARIO_C + "\n\nQual o total de recebimentos do Mês 2?",
  {"A": "R$ 72.000,00.", "B": "R$ 104.000,00.", "C": "R$ 112.000,00.", "D": "R$ 120.000,00."},
  "C", "À vista do Mês 2: 60% × 120.000 = 72.000. A prazo do Mês 1: 40% × 100.000 = 40.000. Total = R$ 112.000,00.",
  "Mesma lógica do Mês 1, usando as vendas do Mês 2 (à vista) e do Mês 1 (a prazo).")

q(p6, SCENARIO_C + "\n\nQual o saldo final de caixa do Mês 2 e o que ele indica?",
  {"A": "R$ 6.000,00 positivo — sobra de caixa.", "B": "−R$ 6.000,00 — falta de caixa, indicando necessidade de captação ou renegociação de prazos.",
   "C": "R$ 18.000,00 positivo — sobra de caixa.", "D": "R$ 0,00 — caixa equilibrado."},
  "B", "Saldo final = 12.000 + 112.000 − 130.000 = −R$ 6.000,00. O orçamento de caixa antecipa a falta de recursos, permitindo captar dinheiro ou renegociar prazos antes que o problema ocorra.",
  "Parta do saldo final do Mês 1, some os recebimentos do Mês 2 e subtraia os pagamentos.")

q(p6, "Para antecipar sobras e faltas de dinheiro em razão de vendas a prazo e pagamentos imediatos, a peça orçamentária mais adequada é o",
  {"A": "orçamento de caixa.", "B": "orçamento de vendas.", "C": "orçamento de produção.", "D": "orçamento de matérias-primas."},
  "A", "O orçamento de caixa projeta entradas e saídas reais de dinheiro, mostrando quando haverá sobra ou falta de recursos.",
  "Qual orçamento trata do dinheiro que de fato entra e sai?")

qa(p6, "Uma empresa pode ter lucro contábil e, ainda assim, enfrentar falta de liquidez.",
   "As vendas a prazo geram receita reconhecida antes do efetivo recebimento do dinheiro.",
   "A", "Ambas são verdadeiras e a II explica a I: a receita entra no resultado na venda, mas o caixa só é recebido depois — o que pode gerar falta de dinheiro mesmo com lucro.",
   "Receita reconhecida = dinheiro no caixa?")

q(p6, "Os Custos Indiretos de Fabricação (CIF) são caracterizados como",
  {"A": "gastos que beneficiam vários produtos ou setores e não podem ser atribuídos diretamente a uma única unidade, exigindo critérios de rateio.",
   "B": "gastos que podem ser medidos diretamente em cada unidade produzida.", "C": "despesas exclusivas do departamento comercial.",
   "D": "receitas indiretas da produção."},
  "A", "CIF são custos comuns a vários produtos (energia da fábrica, aluguel, supervisão) que precisam ser distribuídos por algum critério de rateio.",
  "Indireto = não dá para ligar diretamente a um único produto.")

q(p6, "Os CIF totais do mês somam R$ 60.000,00. O Produto A utilizou 3.000 horas-máquina e o Produto B, 1.000 horas-máquina. Rateando pelas horas-máquina, quanto de CIF é atribuído ao Produto A?",
  {"A": "R$ 30.000,00.", "B": "R$ 40.000,00.", "C": "R$ 45.000,00.", "D": "R$ 50.000,00."},
  "C", "Total de horas = 4.000. A responde por 3.000 ÷ 4.000 = 75%. CIF de A = 75% × 60.000 = R$ 45.000,00 (B recebe R$ 15.000,00).",
  "Calcule a proporção de horas do Produto A sobre o total e aplique ao CIF.")

qa(p6, "Os CIF não podem ser identificados diretamente em um único produto.",
   "Por isso, exigem a utilização de critérios de rateio para serem distribuídos entre os produtos.",
   "A", "Ambas são verdadeiras e a II decorre da I: como não há vínculo direto com um produto, é necessário um critério de rateio.",
   "Como distribuir algo que não dá para atribuir diretamente?")

q(p6, "A administração por projetos contribui para o desempenho financeiro da empresa principalmente ao",
  {"A": "alinhar os investimentos com a estratégia global e priorizar iniciativas que geram valor.", "B": "eliminar a necessidade de orçamento.",
   "C": "dispensar o controle de custos.", "D": "concentrar todas as decisões no nível operacional."},
  "A", "Gerir por projetos permite priorizar e acompanhar investimentos de acordo com a estratégia, evitando dispersão de recursos e melhorando o retorno.",
  "Pense na ligação entre projetos, estratégia e retorno financeiro.")

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
            "source": "original",
        })
    out_provas.append({"name": prova["name"], "topic": prova["topic"], "questions": entries})

out_path = Path(__file__).resolve().parent.parent / "data" / "orc_questions.json"
out_path.write_text(json.dumps({"provas": out_provas}, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Wrote {len(out_provas)} provas ({total_questions} questions) to {out_path}")
