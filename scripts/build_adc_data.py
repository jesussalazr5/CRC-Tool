import json
from pathlib import Path

# ============================================================
# ADC — Análise das Demonstrações Contábeis
# 60 practical questions, organized as 6 "provas" of 10
# questions each (mirroring the real exam's 60-question format).
# Each prova is built around ONE realistic case-study scenario
# (a Balanço Patrimonial or DRE with real account values) that
# the student must classify and/or use to compute indicators —
# following the professor's own formulário (formulas analise.docx).
# Replaces the earlier 100 standalone conceptual questions.
# ============================================================

TOPIC_LABELS = {
    "bp_classificacao_liquidez": "Balanço Patrimonial: Classificação e Liquidez",
    "bp_endividamento_estrutura": "Balanço Patrimonial: Endividamento e Estrutura de Capital",
    "dre_margens_pratico": "DRE: Classificação e Margens",
    "giro_prazos_ciclos_pratico": "Giro, Prazos Médios e Ciclos",
    "av_ah_pratico": "Análise Vertical e Horizontal",
    "rentabilidade_fleuriet_dupont_pratico": "Rentabilidade Avançada, DuPont e Modelo Fleuriet",
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
# CENÁRIO A — Comercial Nordeste Ltda. (Balanço Patrimonial)
# Usado nas Provas 1 e 2.
# ============================================================

SCENARIO_A = (
    "A empresa Comercial Nordeste Ltda. apresenta o seguinte Balanço Patrimonial, em 31/12/20X5:\n"
    "ATIVO\n"
    "Ativo Circulante\n"
    "• Caixa e Equivalentes de Caixa: R$ 40.000,00\n"
    "• Aplicações Financeiras: R$ 20.000,00\n"
    "• Clientes (Duplicatas a Receber): R$ 150.000,00\n"
    "• Estoques: R$ 90.000,00\n"
    "Ativo Não Circulante\n"
    "• Realizável a Longo Prazo: R$ 50.000,00\n"
    "• Investimentos: R$ 20.000,00\n"
    "• Imobilizado: R$ 280.000,00\n"
    "• Intangível: R$ 50.000,00\n"
    "PASSIVO\n"
    "Passivo Circulante\n"
    "• Fornecedores: R$ 80.000,00\n"
    "• Empréstimos e Financiamentos (curto prazo): R$ 40.000,00\n"
    "• Salários e Encargos a Pagar: R$ 30.000,00\n"
    "Passivo Não Circulante\n"
    "• Empréstimos e Financiamentos (longo prazo): R$ 150.000,00\n"
    "PATRIMÔNIO LÍQUIDO\n"
    "• Capital Social: R$ 300.000,00\n"
    "• Reservas de Lucros: R$ 100.000,00"
)

p1 = new_prova("Prova 1 — Balanço Patrimonial: Classificação e Liquidez", "bp_classificacao_liquidez")

q(p1, SCENARIO_A + "\n\nCom base nesse Balanço, assinale a alternativa que classifica corretamente a conta “Aplicações Financeiras”.",
  {"A": "Ativo Circulante.", "B": "Ativo Não Circulante.", "C": "Passivo Circulante.", "D": "Patrimônio Líquido."},
  "A",
  "Aplicações Financeiras de curto prazo (conversíveis em caixa rapidamente) integram o Ativo Circulante, junto com Caixa, Clientes e Estoques.",
  "Pense em quais das quatro contas se convertem em caixa dentro de 12 meses.")

q(p1, SCENARIO_A + "\n\nAssinale a alternativa que classifica corretamente a conta “Empréstimos e Financiamentos (longo prazo)”.",
  {"A": "Ativo Circulante.", "B": "Ativo Não Circulante.", "C": "Passivo Não Circulante.", "D": "Patrimônio Líquido."},
  "C",
  "Dívidas com instituições financeiras vencíveis após 12 meses da data do balanço são classificadas no Passivo Não Circulante.",
  "É uma dívida (não um bem/direito) com vencimento além de 12 meses.")

q(p1, SCENARIO_A + "\n\nAssinale a alternativa que classifica corretamente a conta “Investimentos”.",
  {"A": "Ativo Circulante.", "B": "Ativo Não Circulante.", "C": "Passivo Circulante.", "D": "Passivo Não Circulante."},
  "B",
  "Investimentos (participações societárias permanentes) integram o Ativo Não Circulante, junto com Realizável a Longo Prazo, Imobilizado e Intangível.",
  "É um bem de longa maturação — pense no grupo do Ativo que reúne os recursos de longo prazo.")

q(p1, SCENARIO_A + "\n\nQual o valor total do Ativo Circulante dessa empresa?",
  {"A": "R$ 260.000,00.", "B": "R$ 300.000,00.", "C": "R$ 350.000,00.", "D": "R$ 400.000,00."},
  "B",
  "AC = Caixa (40.000) + Aplicações Financeiras (20.000) + Clientes (150.000) + Estoques (90.000) = R$ 300.000,00.",
  "Some todas as contas listadas sob “Ativo Circulante”.")

q(p1, SCENARIO_A + "\n\nQual o valor total do Ativo Não Circulante dessa empresa?",
  {"A": "R$ 300.000,00.", "B": "R$ 350.000,00.", "C": "R$ 400.000,00.", "D": "R$ 450.000,00."},
  "C",
  "ANC = Realizável a Longo Prazo (50.000) + Investimentos (20.000) + Imobilizado (280.000) + Intangível (50.000) = R$ 400.000,00. (Ativo Total = 300.000 + 400.000 = R$ 700.000,00.)",
  "Some todas as contas listadas sob “Ativo Não Circulante”.")

q(p1, SCENARIO_A + "\n\nQual a Liquidez Corrente (LC) dessa empresa?",
  {"A": "1,5.", "B": "1,7.", "C": "2,0.", "D": "2,3."},
  "C",
  "PC = 80.000 + 40.000 + 30.000 = 150.000. LC = AC ÷ PC = 300.000 ÷ 150.000 = 2,0.",
  "LC = Ativo Circulante ÷ Passivo Circulante. Primeiro some o Passivo Circulante.")

q(p1, SCENARIO_A + "\n\nQual a Liquidez Seca (LS) dessa empresa?",
  {"A": "1,0.", "B": "1,2.", "C": "1,4.", "D": "1,6."},
  "C",
  "LS = (AC − Estoques) ÷ PC = (300.000 − 90.000) ÷ 150.000 = 210.000 ÷ 150.000 = 1,4.",
  "LS = (Ativo Circulante − Estoques) ÷ Passivo Circulante.")

q(p1, SCENARIO_A + "\n\nQual a Liquidez Geral (LG) dessa empresa?",
  {"A": "1,00.", "B": "1,10.", "C": "1,17.", "D": "1,25."},
  "C",
  "PNC = 150.000. LG = (AC + ARLP) ÷ (PC + PNC) = (300.000 + 50.000) ÷ (150.000 + 150.000) = 350.000 ÷ 300.000 ≈ 1,17.",
  "LG = (Ativo Circulante + Realizável a Longo Prazo) ÷ (Passivo Circulante + Passivo Não Circulante).")

q(p1, SCENARIO_A + "\n\nQual a Liquidez Imediata (LI) dessa empresa?",
  {"A": "0,27.", "B": "0,40.", "C": "0,53.", "D": "0,67."},
  "B",
  "Disponibilidades = Caixa (40.000) + Aplicações Financeiras (20.000) = 60.000. LI = Disponibilidades ÷ PC = 60.000 ÷ 150.000 = 0,40.",
  "LI = Disponibilidades (Caixa + Aplicações Financeiras) ÷ Passivo Circulante — só a parte mais líquida do Ativo Circulante.")

q(p1, SCENARIO_A + "\n\nConsiderando a Liquidez Corrente de 2,0 calculada anteriormente, é correto afirmar que",
  {"A": "para cada R$ 1,00 de dívida de curto prazo, a empresa possui R$ 2,00 em ativos de curto prazo.",
   "B": "a empresa tem prejuízo no exercício.", "C": "a empresa não possui nenhuma dívida de longo prazo.", "D": "o índice indica insolvência iminente."},
  "A",
  "A leitura direta da Liquidez Corrente é: para cada R$ 1,00 de Passivo Circulante, a empresa tem R$ 2,00 de Ativo Circulante disponível — uma folga financeira confortável no curto prazo.",
  "Leia o índice como “R$ X de ativo circulante para cada R$ 1,00 de dívida circulante”.")

p2 = new_prova("Prova 2 — Balanço Patrimonial: Endividamento e Estrutura de Capital", "bp_endividamento_estrutura")

q(p2, SCENARIO_A + "\n\nAssinale a alternativa que classifica corretamente a conta “Reservas de Lucros”.",
  {"A": "Ativo Não Circulante.", "B": "Passivo Circulante.", "C": "Passivo Não Circulante.", "D": "Patrimônio Líquido."},
  "D",
  "Reservas de Lucros são recursos próprios acumulados pela empresa a partir de lucros retidos — integram o Patrimônio Líquido, junto com o Capital Social.",
  "É capital PRÓPRIO acumulado, não uma dívida com terceiros.")

q(p2, SCENARIO_A + "\n\nAssinale a alternativa que classifica corretamente a conta “Salários e Encargos a Pagar”.",
  {"A": "Ativo Circulante.", "B": "Passivo Circulante.", "C": "Passivo Não Circulante.", "D": "Patrimônio Líquido."},
  "B",
  "Salários e encargos a pagar são obrigações trabalhistas de curto prazo (normalmente vencíveis dentro de 30 dias) — Passivo Circulante.",
  "É uma dívida da empresa, com vencimento certamente dentro de 12 meses.")

q(p2, SCENARIO_A + "\n\nQual o valor do Passivo Total (Circulante + Não Circulante) dessa empresa?",
  {"A": "R$ 250.000,00.", "B": "R$ 300.000,00.", "C": "R$ 350.000,00.", "D": "R$ 400.000,00."},
  "B",
  "PC = 150.000 (80.000 + 40.000 + 30.000). PNC = 150.000. Passivo Total = 150.000 + 150.000 = R$ 300.000,00.",
  "Some o Passivo Circulante e o Passivo Não Circulante.")

q(p2, SCENARIO_A + "\n\nQual o valor do Patrimônio Líquido dessa empresa?",
  {"A": "R$ 300.000,00.", "B": "R$ 350.000,00.", "C": "R$ 400.000,00.", "D": "R$ 450.000,00."},
  "C",
  "PL = Capital Social (300.000) + Reservas de Lucros (100.000) = R$ 400.000,00. (Confirma a equação: Ativo 700.000 = Passivo 300.000 + PL 400.000.)",
  "Some Capital Social e Reservas de Lucros.")

q(p2, SCENARIO_A + "\n\nQual o Endividamento Geral (EG) dessa empresa? (EG = (PC+PNC) ÷ AT × 100)",
  {"A": "30,00%.", "B": "35,71%.", "C": "42,86%.", "D": "50,00%."},
  "C",
  "EG = Passivo Total ÷ Ativo Total × 100 = 300.000 ÷ 700.000 × 100 ≈ 42,86%.",
  "EG = (PC + PNC) ÷ Ativo Total × 100.")

q(p2, SCENARIO_A + "\n\nQual a Composição do Endividamento (CE) dessa empresa? (CE = PC ÷ (PC+PNC) × 100)",
  {"A": "30%.", "B": "40%.", "C": "50%.", "D": "60%."},
  "C",
  "CE = PC ÷ Passivo Total × 100 = 150.000 ÷ 300.000 × 100 = 50%.",
  "CE = Passivo Circulante ÷ Passivo Total × 100 — mostra o perfil (curto x longo prazo) da dívida.")

q(p2, SCENARIO_A + "\n\nQual a Participação de Capitais de Terceiros (PCT) em relação ao Patrimônio Líquido dessa empresa? (PCT = (PC+PNC) ÷ PL × 100)",
  {"A": "50%.", "B": "60%.", "C": "75%.", "D": "85%."},
  "C",
  "PCT = Passivo Total ÷ PL × 100 = 300.000 ÷ 400.000 × 100 = 75%.",
  "PCT usa o PL como referência (não o Ativo Total) — essa é a diferença em relação ao EG.")

q(p2, SCENARIO_A + "\n\nQual a Imobilização do Patrimônio Líquido (IPL) dessa empresa? (IPL = (Invest+Imob+Intang) ÷ PL × 100)",
  {"A": "70,0%.", "B": "75,0%.", "C": "80,0%.", "D": "87,5%."},
  "D",
  "Recursos imobilizados = Investimentos (20.000) + Imobilizado (280.000) + Intangível (50.000) = 350.000. IPL = 350.000 ÷ 400.000 × 100 = 87,5%.",
  "IPL soma Investimentos + Imobilizado + Intangível (sem o Realizável a Longo Prazo) sobre o PL.")

q(p2, SCENARIO_A + "\n\nQual a Imobilização dos Recursos Não Correntes (IRNC) dessa empresa? (IRNC = (Invest+Imob+Intang) ÷ (PL+PNC) × 100)",
  {"A": "55,00%.", "B": "58,33%.", "C": "63,64%.", "D": "70,00%."},
  "C",
  "Recursos imobilizados = 350.000 (igual à questão anterior). PL + PNC = 400.000 + 150.000 = 550.000. IRNC = 350.000 ÷ 550.000 × 100 ≈ 63,64%.",
  "IRNC usa o mesmo numerador do IPL, mas divide por PL + Passivo Não Circulante (não só o PL).")

q(p2, SCENARIO_A + "\n\nQual a Alavancagem dos Recursos Próprios (ARP) dessa empresa? (ARP = AT ÷ PL)",
  {"A": "1,50.", "B": "1,75.", "C": "2,00.", "D": "2,33."},
  "B",
  "ARP = Ativo Total ÷ Patrimônio Líquido = 700.000 ÷ 400.000 = 1,75.",
  "ARP = Ativo Total ÷ Patrimônio Líquido — mostra quanto do Ativo é “multiplicado” pelo uso de capital de terceiros em relação ao capital próprio.")

# ============================================================
# CENÁRIO B — Indústria Sul S.A. (DRE)
# Usado na Prova 3.
# ============================================================

SCENARIO_B = (
    "A Indústria Sul S.A. apresenta a seguinte Demonstração do Resultado do Exercício (DRE):\n"
    "• Receita Bruta de Vendas: R$ 1.000.000,00\n"
    "• (−) Devoluções e Abatimentos: R$ 40.000,00\n"
    "• (−) Impostos sobre Vendas: R$ 160.000,00\n"
    "• (−) Custo dos Produtos Vendidos (CPV): R$ 480.000,00\n"
    "• (−) Despesas com Vendas: R$ 60.000,00\n"
    "• (−) Despesas Administrativas: R$ 100.000,00\n"
    "• (−) Despesas Financeiras: R$ 20.000,00\n"
    "• (+) Receitas Financeiras: R$ 8.000,00\n"
    "• (−) IR e CSLL: R$ 48.000,00\n"
    "• Depreciação e Amortização do período (já incluída nas despesas): R$ 40.000,00"
)

p3 = new_prova("Prova 3 — DRE: Classificação e Margens", "dre_margens_pratico")

q(p3, SCENARIO_B + "\n\nNa estrutura da DRE dessa empresa, logo após a apuração da Receita Líquida, qual conta é deduzida para se chegar ao Lucro Bruto?",
  {"A": "Despesas com Vendas.", "B": "Custo dos Produtos Vendidos (CPV).", "C": "Despesas Financeiras.", "D": "IR e CSLL."},
  "B",
  "A ordem da DRE é: Receita Líquida − CPV = Lucro Bruto. As demais despesas (vendas, administrativas, financeiras, tributos sobre o lucro) são deduzidas em etapas posteriores.",
  "Lembre a ordem da DRE: o custo do que foi vendido vem logo depois da Receita Líquida.")

q(p3, SCENARIO_B + "\n\nQual o valor da Receita Líquida dessa empresa?",
  {"A": "R$ 760.000,00.", "B": "R$ 800.000,00.", "C": "R$ 840.000,00.", "D": "R$ 960.000,00."},
  "B",
  "Receita Líquida = Receita Bruta − Devoluções/Abatimentos − Impostos sobre Vendas = 1.000.000 − 40.000 − 160.000 = R$ 800.000,00.",
  "Receita Líquida = Receita Bruta menos as deduções sobre vendas.")

q(p3, SCENARIO_B + "\n\nQual o valor do Lucro Bruto dessa empresa?",
  {"A": "R$ 280.000,00.", "B": "R$ 300.000,00.", "C": "R$ 320.000,00.", "D": "R$ 340.000,00."},
  "C",
  "Lucro Bruto = Receita Líquida − CPV = 800.000 − 480.000 = R$ 320.000,00.",
  "Lucro Bruto = Receita Líquida − CPV.")

q(p3, SCENARIO_B + "\n\nQual a Margem Bruta (MB) dessa empresa? (MB = Lucro Bruto ÷ Receita Líquida × 100)",
  {"A": "32,0%.", "B": "36,0%.", "C": "40,0%.", "D": "45,0%."},
  "C",
  "MB = 320.000 ÷ 800.000 × 100 = 40,0%.",
  "MB = Lucro Bruto ÷ Receita Líquida × 100.")

q(p3, SCENARIO_B + "\n\nQual o Mark-up Global (MG) dessa empresa? (MG = Lucro Bruto ÷ Custo das Vendas × 100)",
  {"A": "55,3%.", "B": "60,0%.", "C": "66,7%.", "D": "75,0%."},
  "C",
  "MG = 320.000 ÷ 480.000 × 100 ≈ 66,7%. Diferente da Margem Bruta, o Mark-up Global compara o Lucro Bruto ao Custo (não à Receita).",
  "MG usa o Custo das Vendas no denominador, não a Receita Líquida — não confunda com a Margem Bruta.")

q(p3, SCENARIO_B + "\n\nQual o valor do Lucro Operacional (antes do resultado financeiro) dessa empresa?",
  {"A": "R$ 140.000,00.", "B": "R$ 160.000,00.", "C": "R$ 180.000,00.", "D": "R$ 200.000,00."},
  "B",
  "Lucro Operacional = Lucro Bruto − Despesas com Vendas − Despesas Administrativas = 320.000 − 60.000 − 100.000 = R$ 160.000,00.",
  "Lucro Operacional = Lucro Bruto menos as despesas de vendas e administrativas (antes do resultado financeiro).")

q(p3, SCENARIO_B + "\n\nQual a Margem Operacional (MO) dessa empresa? (MO = Lucro Operacional ÷ Receita Líquida × 100)",
  {"A": "15%.", "B": "18%.", "C": "20%.", "D": "22%."},
  "C",
  "MO = 160.000 ÷ 800.000 × 100 = 20%.",
  "MO = Lucro Operacional ÷ Receita Líquida × 100.")

q(p3, SCENARIO_B + "\n\nConsiderando a Depreciação e Amortização de R$ 40.000,00 do período (já incluída nas despesas), qual o EBITDA dessa empresa? (EBITDA ≈ Lucro Operacional + Depreciação/Amortização)",
  {"A": "R$ 180.000,00.", "B": "R$ 190.000,00.", "C": "R$ 200.000,00.", "D": "R$ 210.000,00."},
  "C",
  "EBITDA = Lucro Operacional + Depreciação/Amortização = 160.000 + 40.000 = R$ 200.000,00 — “limpa” o lucro operacional do efeito não-caixa da depreciação/amortização.",
  "Some a Depreciação/Amortização de volta ao Lucro Operacional.")

q(p3, SCENARIO_B + "\n\nQual a Margem do EBITDA (ME) dessa empresa? (ME = EBITDA ÷ Receita Líquida × 100)",
  {"A": "20%.", "B": "22,5%.", "C": "25%.", "D": "27,5%."},
  "C",
  "ME = 200.000 ÷ 800.000 × 100 = 25%.",
  "ME = EBITDA ÷ Receita Líquida × 100.")

q(p3, SCENARIO_B + "\n\nConsiderando as Despesas Financeiras (20.000), Receitas Financeiras (8.000) e IR/CSLL (48.000), qual a Margem Líquida (ML) dessa empresa? (Lucro Líquido = Lucro Operacional + Receitas Financeiras − Despesas Financeiras − IR/CSLL)",
  {"A": "10,0%.", "B": "12,5%.", "C": "15,0%.", "D": "18,5%."},
  "B",
  "Lucro Líquido = 160.000 + 8.000 − 20.000 − 48.000 = 100.000. ML = 100.000 ÷ 800.000 × 100 = 12,5%.",
  "Primeiro calcule o Lucro Líquido (Lucro Operacional ± resultado financeiro − IR/CSLL), depois divida pela Receita Líquida.")

# ============================================================
# CENÁRIO C — Distribuidora Central Ltda. (Giro, Prazos, Ciclos)
# Usado na Prova 4.
# ============================================================

SCENARIO_C = (
    "A Distribuidora Central Ltda. apresenta os seguintes dados do último exercício (ano com 360 dias):\n"
    "• Estoque Inicial: R$ 90.000,00\n"
    "• Compras Brutas: R$ 720.000,00\n"
    "• Estoque Final: R$ 90.000,00\n"
    "• Saldo Médio de Estoques: R$ 90.000,00\n"
    "• Vendas Brutas: R$ 1.200.000,00\n"
    "• Receita Operacional Líquida: R$ 1.100.000,00\n"
    "• Saldo Médio de Clientes: R$ 100.000,00\n"
    "• Saldo Médio de Fornecedores: R$ 120.000,00\n"
    "• Saldo Médio do Ativo Total: R$ 550.000,00"
)

p4 = new_prova("Prova 4 — Giro, Prazos Médios e Ciclos", "giro_prazos_ciclos_pratico")

q(p4, SCENARIO_C + "\n\nQual o Custo da Mercadoria Vendida (CMV) do período? (CMV = Estoque Inicial + Compras − Estoque Final)",
  {"A": "R$ 700.000,00.", "B": "R$ 710.000,00.", "C": "R$ 720.000,00.", "D": "R$ 730.000,00."},
  "C",
  "CMV = 90.000 + 720.000 − 90.000 = R$ 720.000,00.",
  "CMV = EI + Compras − EF.")

q(p4, SCENARIO_C + "\n\nQual o Prazo Médio de Renovação de Estoques (PMRE)? (PMRE = Saldo Médio de Estoques ÷ CMV × 360; considere CMV = R$ 720.000,00)",
  {"A": "30 dias.", "B": "40 dias.", "C": "45 dias.", "D": "50 dias."},
  "C",
  "PMRE = (90.000 ÷ 720.000) × 360 = 0,125 × 360 = 45 dias.",
  "PMRE = (Saldo Médio de Estoques ÷ CMV) × 360.")

q(p4, SCENARIO_C + "\n\nQual o Prazo Médio de Recebimento de Clientes (PMRC), considerando as Vendas Brutas ajustadas? (PMRC = Saldo Médio de Clientes ÷ Vendas Brutas × 360)",
  {"A": "25 dias.", "B": "30 dias.", "C": "35 dias.", "D": "40 dias."},
  "B",
  "PMRC = (100.000 ÷ 1.200.000) × 360 = 0,0833 × 360 = 30 dias.",
  "PMRC = (Saldo Médio de Clientes ÷ Vendas Brutas) × 360.")

q(p4, SCENARIO_C + "\n\nQual o Prazo Médio de Pagamento a Fornecedores (PMPF), considerando as Compras Brutas ajustadas? (PMPF = Saldo Médio de Fornecedores ÷ Compras Brutas × 360)",
  {"A": "50 dias.", "B": "55 dias.", "C": "60 dias.", "D": "65 dias."},
  "C",
  "PMPF = (120.000 ÷ 720.000) × 360 = 0,1667 × 360 = 60 dias.",
  "PMPF = (Saldo Médio de Fornecedores ÷ Compras Brutas) × 360.")

q(p4, SCENARIO_C + "\n\nQual o Giro de Estoques Total (GET)? (GET = CMV ÷ Saldo Médio de Estoques; considere CMV = R$ 720.000,00)",
  {"A": "6 vezes.", "B": "7 vezes.", "C": "8 vezes.", "D": "9 vezes."},
  "C",
  "GET = 720.000 ÷ 90.000 = 8 vezes.",
  "GET = CMV ÷ Saldo Médio de Estoques.")

q(p4, SCENARIO_C + "\n\nQual o Giro do Ativo Total (GAT), considerando a Receita Operacional Líquida e o Saldo Médio do Ativo Total? (GAT = Receita Operacional Líquida ÷ Saldo Médio do Ativo Total)",
  {"A": "1,5 vezes.", "B": "2,0 vezes.", "C": "2,2 vezes.", "D": "2,5 vezes."},
  "B",
  "GAT = 1.100.000 ÷ 550.000 = 2,0 vezes.",
  "GAT = Receita Operacional Líquida ÷ Saldo Médio do Ativo Total.")

q(p4, SCENARIO_C + "\n\nConsiderando PMRE = 45 dias e PMRC = 30 dias, qual o Ciclo Operacional dessa empresa? (Ciclo Operacional = PMRE + PMRC)",
  {"A": "60 dias.", "B": "70 dias.", "C": "75 dias.", "D": "90 dias."},
  "C",
  "Ciclo Operacional = PMRE + PMRC = 45 + 30 = 75 dias.",
  "Ciclo Operacional = PMRE + PMRC.")

q(p4, SCENARIO_C + "\n\nConsiderando o Ciclo Operacional de 75 dias e o PMPF de 60 dias, qual o Ciclo Financeiro dessa empresa? (Ciclo Financeiro = PMRE + PMRC − PMPF)",
  {"A": "10 dias.", "B": "15 dias.", "C": "20 dias.", "D": "25 dias."},
  "B",
  "Ciclo Financeiro = Ciclo Operacional − PMPF = 75 − 60 = 15 dias.",
  "Ciclo Financeiro = Ciclo Operacional − PMPF.")

q(p4, SCENARIO_C + "\n\nSe o PMPF dessa empresa fosse de 80 dias (mantendo o PMRE e o PMRC constantes), o Ciclo Financeiro seria de",
  {"A": "−5 dias (negativo).", "B": "0 dias.", "C": "5 dias.", "D": "10 dias."},
  "A",
  "Ciclo Financeiro = 75 − 80 = −5 dias. Um Ciclo Financeiro negativo significa que os fornecedores financiam, na prática, toda a operação e ainda sobra prazo.",
  "Ciclo Financeiro = Ciclo Operacional (75) − novo PMPF (80).")

q(p4, SCENARIO_C + "\n\nUm Ciclo Financeiro positivo, como o de 15 dias calculado, indica que a empresa",
  {"A": "precisa financiar suas operações por 15 dias com recursos próprios ou de terceiros, além dos fornecedores.",
   "B": "recebe dos clientes antes de precisar pagar os fornecedores.", "C": "não possui nenhum estoque.", "D": "tem prejuízo líquido no período."},
  "A",
  "Um Ciclo Financeiro positivo mostra que o prazo concedido pelos fornecedores (PMPF) não é suficiente para cobrir todo o Ciclo Operacional — a empresa precisa bancar essa diferença (15 dias) com capital próprio ou outras fontes de financiamento.",
  "Ciclo Financeiro positivo = período que falta financiar além do que os fornecedores já cobrem.")

# ============================================================
# CENÁRIO D — Comércio Atlântico S.A. (Análise Vertical e Horizontal)
# Usado na Prova 5.
# ============================================================

SCENARIO_D = (
    "O Comércio Atlântico S.A. apresenta os seguintes dados resumidos de dois exercícios:\n"
    "20X1: Ativo Circulante R$ 400.000,00 (dos quais R$ 150.000,00 de Estoques); Ativo Não Circulante R$ 600.000,00; "
    "Ativo Total R$ 1.000.000,00; Receita Líquida R$ 900.000,00; Lucro Líquido R$ 54.000,00.\n"
    "20X2: Ativo Circulante R$ 500.000,00; Ativo Não Circulante R$ 700.000,00; Ativo Total R$ 1.200.000,00; "
    "Receita Líquida R$ 1.080.000,00; Lucro Líquido R$ 75.600,00."
)

p5 = new_prova("Prova 5 — Análise Vertical e Horizontal", "av_ah_pratico")

q(p5, SCENARIO_D + "\n\nQual a representatividade (Análise Vertical) do Ativo Circulante sobre o Ativo Total em 20X1?",
  {"A": "35%.", "B": "40%.", "C": "45%.", "D": "50%."},
  "B",
  "AV = 400.000 ÷ 1.000.000 × 100 = 40%.",
  "AV = valor da conta ÷ Ativo Total × 100.")

q(p5, SCENARIO_D + "\n\nQual a representatividade (Análise Vertical) do Ativo Circulante sobre o Ativo Total em 20X2?",
  {"A": "40,00%.", "B": "41,67%.", "C": "43,33%.", "D": "45,00%."},
  "B",
  "AV = 500.000 ÷ 1.200.000 × 100 ≈ 41,67%.",
  "AV = valor da conta ÷ Ativo Total × 100, usando os valores de 20X2.")

q(p5, SCENARIO_D + "\n\nQual a representatividade (Análise Vertical) dos Estoques sobre o Ativo Total em 20X1?",
  {"A": "10%.", "B": "15%.", "C": "18%.", "D": "20%."},
  "B",
  "AV = 150.000 ÷ 1.000.000 × 100 = 15%.",
  "AV = Estoques ÷ Ativo Total × 100.")

q(p5, SCENARIO_D + "\n\nQual a variação da Análise Horizontal do Ativo Total de 20X1 para 20X2?",
  {"A": "+15%.", "B": "+20%.", "C": "+25%.", "D": "+30%."},
  "B",
  "AH = (1.200.000 ÷ 1.000.000 − 1) × 100 = +20%.",
  "AH = (valor atual ÷ valor de referência − 1) × 100.")

q(p5, SCENARIO_D + "\n\nQual a variação da Análise Horizontal da Receita Líquida de 20X1 para 20X2?",
  {"A": "+10%.", "B": "+15%.", "C": "+20%.", "D": "+25%."},
  "C",
  "AH = (1.080.000 ÷ 900.000 − 1) × 100 = +20%.",
  "AH = (Receita Líquida 20X2 ÷ Receita Líquida 20X1 − 1) × 100.")

q(p5, SCENARIO_D + "\n\nQual a variação da Análise Horizontal do Lucro Líquido de 20X1 para 20X2?",
  {"A": "+20%.", "B": "+30%.", "C": "+40%.", "D": "+50%."},
  "C",
  "AH = (75.600 ÷ 54.000 − 1) × 100 = +40%.",
  "AH = (Lucro Líquido 20X2 ÷ Lucro Líquido 20X1 − 1) × 100.")

q(p5, SCENARIO_D + "\n\nQual a Margem Líquida (ML) dessa empresa em 20X1?",
  {"A": "5%.", "B": "6%.", "C": "7%.", "D": "8%."},
  "B",
  "ML = 54.000 ÷ 900.000 × 100 = 6%.",
  "ML = Lucro Líquido ÷ Receita Líquida × 100, usando os valores de 20X1.")

q(p5, SCENARIO_D + "\n\nQual a Margem Líquida (ML) dessa empresa em 20X2?",
  {"A": "6%.", "B": "7%.", "C": "8%.", "D": "9%."},
  "B",
  "ML = 75.600 ÷ 1.080.000 × 100 = 7%.",
  "ML = Lucro Líquido ÷ Receita Líquida × 100, usando os valores de 20X2.")

q(p5, SCENARIO_D + "\n\nComparando os dois anos, é correto afirmar que",
  {"A": "o Ativo Total e a Receita Líquida cresceram (Análise Horizontal) na mesma proporção, ambos +20%.",
   "B": "o Lucro Líquido cresceu proporcionalmente menos do que a Receita Líquida.",
   "C": "a Margem Líquida piorou de 20X1 para 20X2.", "D": "o Ativo Circulante perdeu representatividade (Análise Vertical) sobre o Ativo Total."},
  "A",
  "Ativo Total e Receita Líquida cresceram exatamente +20% cada. O Lucro Líquido cresceu MAIS (proporcionalmente), não menos (+40% > +20%), então B é falsa. A Margem Líquida melhorou de 6% para 7% (não piorou), então C é falsa. O Ativo Circulante foi de 40% para 41,67% do Ativo Total — ganhou representatividade, não perdeu, então D é falsa.",
  "Compare as três variações de AH calculadas (Ativo Total, Receita Líquida, Lucro Líquido) lado a lado.")

q(p5, SCENARIO_D + "\n\nO fato de o Lucro Líquido ter crescido (Análise Horizontal) em ritmo maior do que a Receita Líquida entre os dois anos indica que",
  {"A": "a empresa melhorou sua Margem Líquida (rentabilidade sobre vendas) no período.", "B": "a empresa piorou sua Margem Líquida no período.",
   "C": "a Receita Líquida diminuiu no período.", "D": "o Ativo Total permaneceu constante no período."},
  "A",
  "Se o lucro cresce mais rápido do que a receita, a proporção lucro/receita (a Margem Líquida) necessariamente aumenta — o que já foi confirmado nas duas questões anteriores (6% → 7%).",
  "Se o numerador (lucro) cresce mais que o denominador (receita) de uma razão, a razão só pode aumentar.")

# ============================================================
# CENÁRIO E — Metalúrgica Vitória S.A. (Rentabilidade avançada,
# DuPont e Modelo Fleuriet)
# Usado na Prova 6.
# ============================================================

SCENARIO_E = (
    "A Metalúrgica Vitória S.A. apresenta os seguintes dados do exercício:\n"
    "• Lucro Operacional (LAJIR — antes de juros e tributos sobre o lucro): R$ 250.000,00\n"
    "• Despesas Financeiras: R$ 50.000,00\n"
    "• Receita Líquida: R$ 2.000.000,00\n"
    "• Lucro Líquido: R$ 120.000,00\n"
    "• Ativo Total: R$ 1.500.000,00\n"
    "• Patrimônio Líquido: R$ 750.000,00\n"
    "Reclassificando o circulante por natureza (Modelo Fleuriet):\n"
    "• Ativo Circulante Operacional (ACO): R$ 300.000,00\n"
    "• Ativo Circulante Financeiro (ACF): R$ 100.000,00\n"
    "• Passivo Circulante Operacional (PCO): R$ 180.000,00\n"
    "• Passivo Circulante Financeiro (PCF): R$ 70.000,00"
)

p6 = new_prova("Prova 6 — Rentabilidade Avançada, DuPont e Modelo Fleuriet", "rentabilidade_fleuriet_dupont_pratico")

q(p6, SCENARIO_E + "\n\nQual a Cobertura de Juros (CJ) dessa empresa? (CJ = LAJIR ÷ Despesas Financeiras)",
  {"A": "3,0 vezes.", "B": "4,0 vezes.", "C": "5,0 vezes.", "D": "6,0 vezes."},
  "C",
  "CJ = 250.000 ÷ 50.000 = 5,0 vezes.",
  "CJ = LAJIR ÷ Despesas Financeiras.")

q(p6, "Um índice de Cobertura de Juros de 5,0 vezes, como o calculado para a Metalúrgica Vitória S.A., significa que",
  {"A": "o LAJIR é 5 vezes maior do que as despesas financeiras, indicando boa capacidade de honrar os encargos da dívida.",
   "B": "a empresa possui 5 dívidas distintas com bancos.", "C": "a empresa está em situação de insolvência.", "D": "as despesas financeiras superam o LAJIR em 5 vezes."},
  "A",
  "Quanto maior a Cobertura de Juros, mais folgada é a capacidade da empresa de pagar os encargos financeiros de suas dívidas com o resultado operacional gerado — 5,0 vezes é um indicador confortável.",
  "CJ alto = boa folga para pagar juros com o resultado operacional.")

q(p6, SCENARIO_E + "\n\nQual a Margem Líquida (ML) dessa empresa?",
  {"A": "5%.", "B": "6%.", "C": "7%.", "D": "8%."},
  "B",
  "ML = Lucro Líquido ÷ Receita Líquida × 100 = 120.000 ÷ 2.000.000 × 100 = 6%.",
  "ML = Lucro Líquido ÷ Receita Líquida × 100.")

q(p6, SCENARIO_E + "\n\nQual o Giro do Ativo Total (GAT) dessa empresa? (GAT = Receita Líquida ÷ Ativo Total)",
  {"A": "1,00.", "B": "1,20.", "C": "1,33.", "D": "1,50."},
  "C",
  "GAT = 2.000.000 ÷ 1.500.000 ≈ 1,33.",
  "GAT = Receita Líquida ÷ Ativo Total.")

q(p6, SCENARIO_E + "\n\nPela Fórmula DuPont original (ROA = ML × GAT), qual o ROA dessa empresa? (considere ML = 6% e GAT ≈ 1,33)",
  {"A": "6%.", "B": "7%.", "C": "8%.", "D": "9%."},
  "C",
  "ROA = ML × GAT = 6% × 1,33 ≈ 8% (confirmando diretamente: 120.000 ÷ 1.500.000 × 100 = 8%).",
  "ROA = Margem Líquida × Giro do Ativo (multiplique, não some) — ou calcule direto: Lucro Líquido ÷ Ativo Total.")

q(p6, SCENARIO_E + "\n\nQual a Alavancagem dos Recursos Próprios (ARP) dessa empresa? (ARP = AT ÷ PL)",
  {"A": "1,5.", "B": "2,0.", "C": "2,5.", "D": "3,0."},
  "B",
  "ARP = 1.500.000 ÷ 750.000 = 2,0.",
  "ARP = Ativo Total ÷ Patrimônio Líquido.")

q(p6, SCENARIO_E + "\n\nPela Fórmula DuPont modificada (ROE = ROA × ARP), qual o ROE dessa empresa? (considere ROA = 8% e ARP = 2,0)",
  {"A": "12%.", "B": "14%.", "C": "16%.", "D": "18%."},
  "C",
  "ROE = ROA × ARP = 8% × 2,0 = 16% (confirmando diretamente: 120.000 ÷ 750.000 × 100 = 16%).",
  "ROE = ROA × Alavancagem dos Recursos Próprios — ou calcule direto: Lucro Líquido ÷ Patrimônio Líquido.")

q(p6, SCENARIO_E + "\n\nQual o Capital Circulante Líquido (CCL) dessa empresa? (CCL = AC − PC, considerando AC = ACO+ACF e PC = PCO+PCF)",
  {"A": "R$ 100.000,00.", "B": "R$ 120.000,00.", "C": "R$ 150.000,00.", "D": "R$ 180.000,00."},
  "C",
  "AC = ACO + ACF = 300.000 + 100.000 = 400.000. PC = PCO + PCF = 180.000 + 70.000 = 250.000. CCL = 400.000 − 250.000 = R$ 150.000,00.",
  "Primeiro some AC total e PC total (operacional + financeiro de cada um), depois subtraia.")

q(p6, SCENARIO_E + "\n\nQual a Necessidade de Capital de Giro (IOG/NCG) dessa empresa? (IOG = ACO − PCO)",
  {"A": "R$ 100.000,00.", "B": "R$ 110.000,00.", "C": "R$ 120.000,00.", "D": "R$ 130.000,00."},
  "C",
  "IOG = ACO − PCO = 300.000 − 180.000 = R$ 120.000,00.",
  "IOG usa só a parte OPERACIONAL do circulante (ACO e PCO), não o circulante total.")

q(p6, SCENARIO_E + "\n\nQual o Saldo de Tesouraria (ST) dessa empresa? (ST = ACF − PCF)",
  {"A": "R$ 20.000,00.", "B": "R$ 30.000,00.", "C": "R$ 40.000,00.", "D": "R$ 50.000,00."},
  "B",
  "ST = ACF − PCF = 100.000 − 70.000 = R$ 30.000,00. (Confirma: CCL = IOG + ST → 150.000 = 120.000 + 30.000 ✓, mostrando que o IOG está bem coberto pelo ST positivo — situação financeira equilibrada.)",
  "ST usa só a parte FINANCEIRA/errática do circulante (ACF e PCF).")

assert len(PROVAS) == 6, len(PROVAS)
for p in PROVAS:
    assert len(p["questions"]) == 10, (p["name"], len(p["questions"]))

total_questions = sum(len(p["questions"]) for p in PROVAS)
assert total_questions == 60, total_questions

# ============================================================
# Assemble and write data/adc_questions.json
# ============================================================

out_provas = []
for pi, prova in enumerate(PROVAS, start=1):
    entries = []
    for qi, item in enumerate(prova["questions"], start=1):
        entries.append({
            "id": f"adc-p{pi}-q{qi:02d}",
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
out_path = Path(__file__).resolve().parent.parent / "data" / "adc_questions.json"
out_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Wrote {len(out_provas)} provas ({total_questions} questions total) to {out_path}")
for p in out_provas:
    print(f"  {p['name']}: {len(p['questions'])} questions")
