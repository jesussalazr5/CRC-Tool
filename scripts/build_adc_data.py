import json
from pathlib import Path

# ============================================================
# ADC — Análise das Demonstrações Contábeis
# 100 practice questions across the 5 units of the course
# textbook (Unicesumar, "Análise das Demonstrações Contábeis",
# José Manoel da Costa). 14 of the 100 are adapted from the
# textbook's own end-of-unit "Atividades de Estudos" (verified
# against its own gabarito); the remaining 86 are original
# questions written to cover the same topics/formulas at a
# comparable difficulty, for broad practice coverage.
# ============================================================

TOPIC_LABELS = {
    "estrutura_bp": "Estrutura do Balanço Patrimonial e Demonstrações",
    "av_ah": "Análise Vertical e Horizontal",
    "giro_prazos_ciclos": "Giro dos Recursos, Prazos Médios e Ciclos",
    "liquidez": "Indicadores de Liquidez",
    "endividamento": "Indicadores de Endividamento",
    "rentabilidade": "Indicadores de Rentabilidade",
    "indices_padrao_dupont": "Índices-Padrão e Fórmula DuPont",
    "kanitz_fleuriet": "Termômetro de Kanitz e Modelo Fleuriet",
}

QUESTIONS = []


def add(topic, question, options, correct, explanation, hint, source="original"):
    QUESTIONS.append(dict(topic=topic, question=question, options=options, correct=correct,
                           explanation=explanation, hint=hint, source=source))


# ============================================================
# UNIDADE I — Estrutura do Balanço Patrimonial e Demonstrações
# ============================================================

add("estrutura_bp",
    "O Balanço Patrimonial é uma demonstração financeira obrigatória (Lei nº 6.404/76) que pode ser comparada, de forma figurativa, a uma “fotografia” da empresa em determinada data. Assinale a alternativa que descreve corretamente os grupos de contas do Passivo, segundo a Lei nº 6.404/76.",
    {"A": "Circulante, Não Circulante e Patrimônio Líquido.", "B": "Circulante, Realizável a Longo Prazo e Patrimônio Líquido.",
     "C": "Circulante, Não Circulante e Capital Social.", "D": "Circulante e Não Circulante."},
    "D",
    "Após a Lei nº 11.941/2009, o Passivo (exigível) passou a ser dividido em apenas dois grupos: Passivo Circulante e Passivo Não Circulante. O Patrimônio Líquido é um grupo à parte, que não integra o Passivo exigível.",
    "Lembre que, desde a reforma da lei societária, o PL deixou de ser considerado um “grupo do Passivo” — o Passivo exigível ficou só com Circulante e Não Circulante.",
    source="textbook")

add("estrutura_bp",
    "O Passivo representa origens de recursos de terceiros. Um grupo importante desses recursos é o obtido junto a instituições financeiras. Sobre esses recursos, analise:\nI. Aparecem no Balanço Patrimonial com o nome de fornecedores.\nII. São chamados no Balanço Patrimonial de empréstimos e financiamentos.\nIII. Podem aparecer no Passivo Circulante e no Passivo Não Circulante.\nIV. Estão no grupo Realizável a Longo Prazo, no lado esquerdo do Balanço.\nAssinale a alternativa correta:",
    {"A": "Apenas I e II estão corretas.", "B": "Apenas II e III estão corretas.",
     "C": "Apenas I está correta.", "D": "Apenas II, III e IV estão corretas."},
    "B",
    "Recursos obtidos de bancos aparecem como “empréstimos e financiamentos” (II) — não como “fornecedores”, que são dívidas com fornecedores de mercadorias/insumos (I é falsa). Podem estar no Passivo Circulante (vencimento em até 12 meses) ou no Passivo Não Circulante (vencimento posterior) — III é verdadeira. “Realizável a Longo Prazo” é conta de Ativo, não de Passivo — IV é falsa.",
    "Cuidado para não confundir “fornecedores” (dívida por mercadorias) com “empréstimos e financiamentos” (dívida com bancos) — e lembre que Realizável a Longo Prazo é Ativo, não Passivo.",
    source="textbook")

add("estrutura_bp",
    "O Balanço Patrimonial reflete a posição da estrutura patrimonial em determinada data. Sobre o conceito de Passivo, analise as afirmações a seguir e assinale Verdadeiro (V) ou Falso (F):\n(  ) É um recurso controlado pela entidade como resultado de eventos passados, do qual se espera que resultem benefícios econômicos futuros.\n(  ) É o interesse residual nos ativos da entidade depois de deduzidas todas as dívidas — a soma do investimento inicial com os resultados da atividade.\n(  ) É uma obrigação presente da entidade, derivada de eventos passados, cuja liquidação se espera que resulte na saída de recursos capazes de gerar benefícios econômicos.\nAssinale a alternativa correta:",
    {"A": "V, V, V.", "B": "V, V, F.", "C": "F, F, V.", "D": "V, F, V."},
    "C",
    "As três afirmações são, individualmente, definições corretas — mas apenas a terceira descreve de fato o Passivo. A primeira descreve o Ativo (recurso controlado com benefícios futuros esperados), e a segunda descreve o Patrimônio Líquido (interesse residual). Como o enunciado pede a análise “sobre o conceito de Passivo”, as duas primeiras são falsas nesse contexto, e apenas a terceira é verdadeira: F, F, V.",
    "As três frases são definições corretas de conceitos diferentes — o truque é notar que só a terceira é realmente sobre Passivo; as outras duas descrevem Ativo e Patrimônio Líquido.",
    source="textbook")

add("estrutura_bp",
    "Esta demonstração evidencia a riqueza criada pela empresa, medida pela diferença entre o valor das vendas e os insumos adquiridos de terceiros, e também mostra como essa riqueza foi distribuída (entre pessoal, governo, capital de terceiros e capital próprio). A qual demonstração o excerto se refere?",
    {"A": "DFC.", "B": "DRA.", "C": "DMPL.", "D": "DVA."},
    "D",
    "A descrição corresponde exatamente à Demonstração do Valor Adicionado (DVA), que evidencia a riqueza gerada pela empresa e a forma como ela foi distribuída entre pessoal, governo, capital de terceiros e capital próprio — diferente da DFC (fluxos de caixa), DRA (resultado abrangente) e DMPL (mutações do PL).",
    "A palavra-chave é “distribuição da riqueza gerada” — essa é a assinatura da DVA, diferente das demais demonstrações.",
    source="textbook")

add("estrutura_bp",
    "Assinale a opção que apresenta uma conta classificada corretamente como Ativo Não Circulante.",
    {"A": "Caixa e Equivalentes de Caixa.", "B": "Estoques.", "C": "Investimentos (participações societárias permanentes).", "D": "Clientes (duplicatas a receber de curto prazo)."},
    "C",
    "Investimentos (participações societárias permanentes) integram o Ativo Não Circulante, junto com Realizável a Longo Prazo, Imobilizado e Intangível. Caixa, Estoques e Clientes de curto prazo são Ativo Circulante.",
    "Pense em qual dessas quatro contas normalmente NÃO se converte em caixa dentro de 12 meses.")

add("estrutura_bp",
    "Uma empresa apresenta Ativo Total de R$ 850.000,00 e Passivo Total (Circulante + Não Circulante) de R$ 510.000,00. Qual o valor do Patrimônio Líquido?",
    {"A": "R$ 340.000,00.", "B": "R$ 360.000,00.", "C": "R$ 1.360.000,00.", "D": "R$ 255.000,00."},
    "A",
    "Pela equação fundamental (Ativo = Passivo + PL), o Patrimônio Líquido é a diferença: 850.000 − 510.000 = R$ 340.000,00.",
    "Ativo = Passivo + PL → isole o PL: PL = Ativo Total − Passivo Total.")

add("estrutura_bp",
    "Na Demonstração do Resultado do Exercício (DRE), logo após a apuração da Receita Líquida de Vendas, a próxima dedução para se chegar ao Lucro Bruto é o(a)",
    {"A": "Despesas administrativas.", "B": "Custo das Mercadorias/Produtos/Serviços Vendidos (CMV/CPV/CSP).",
     "C": "Despesas financeiras.", "D": "Provisão para Imposto de Renda."},
    "B",
    "A estrutura da DRE segue: Receita Líquida − CMV/CPV/CSP = Lucro Bruto. As despesas administrativas, financeiras e o IR são deduzidos em etapas posteriores, depois do Lucro Bruto.",
    "Lembre a ordem da DRE: Receita Líquida menos o custo do que foi vendido é que dá o Lucro Bruto — as despesas vêm depois.")

add("estrutura_bp",
    "Uma empresa realiza o pagamento de dividendos aos seus acionistas. Na Demonstração dos Fluxos de Caixa (DFC), esse pagamento deve ser classificado como fluxo de caixa de qual atividade?",
    {"A": "Operacional.", "B": "Investimento.", "C": "Financiamento.", "D": "Não circulante."},
    "C",
    "Pagamento de dividendos é uma remuneração ao capital próprio dos sócios/acionistas — por isso é classificado como fluxo de caixa de financiamento, junto com captações e amortizações de empréstimos e integralizações de capital.",
    "Dividendo é retorno de capital ao sócio — pense em qual das três atividades da DFC trata da relação da empresa com quem financia o negócio.")

add("estrutura_bp",
    "Qual a principal diferença conceitual entre a Demonstração do Resultado do Exercício (DRE) e a Demonstração do Valor Adicionado (DVA)?",
    {"A": "A DRE apura o lucro ou prejuízo do período; a DVA evidencia a riqueza gerada e sua distribuição entre governo, empregados, capital de terceiros e sócios.",
     "B": "A DRE é obrigatória apenas para companhias fechadas; a DVA, apenas para companhias abertas.",
     "C": "A DRE trata de fluxos de caixa; a DVA, de fluxos exclusivamente contábeis.", "D": "Não há diferença conceitual relevante entre as duas demonstrações."},
    "A",
    "A DRE tem como objetivo apurar o resultado (lucro ou prejuízo) do período. Já a DVA, embora parta de dados semelhantes, tem outro foco: mostrar quanto de riqueza a empresa gerou e como essa riqueza foi repartida entre os diversos “stakeholders” (empregados, governo, financiadores e sócios).",
    "Pense: uma demonstração termina no “lucro”; a outra vai além e mostra para quem esse valor gerado foi parar.")

add("estrutura_bp",
    "Para fins de análise das demonstrações contábeis, é comum realizar ajustes (adequações) nas demonstrações publicadas. Um exemplo clássico desse tipo de ajuste é",
    {"A": "reclassificar duplicatas descontadas como redutora de Duplicatas a Receber, em vez de mantê-las isoladamente no Passivo Circulante.",
     "B": "somar o estoque inicial ao estoque final para simplificar o cálculo do CMV.",
     "C": "excluir integralmente o Patrimônio Líquido da análise.", "D": "desconsiderar a Demonstração do Resultado na análise da situação econômica."},
    "A",
    "Um ajuste clássico para fins de análise é reclassificar as duplicatas descontadas (que contabilmente aparecem no Passivo Circulante) como uma conta redutora de Duplicatas a Receber, já que economicamente representam uma antecipação de recebíveis, e não uma dívida operacional típica.",
    "Pense em contas que, embora contabilmente registradas de um jeito, representam economicamente outra coisa — duplicatas descontadas são o exemplo clássico dos livros de análise.")

add("estrutura_bp",
    "O Patrimônio Líquido de uma sociedade empresária é formado, entre outras, pelas contas de",
    {"A": "Fornecedores e Empréstimos a Pagar.", "B": "Capital Social e Reservas de Lucros.",
     "C": "Estoques e Imobilizado.", "D": "Duplicatas a Receber e Caixa."},
    "B",
    "O Patrimônio Líquido reúne os recursos próprios da empresa: Capital Social, Reservas (de Lucros e de Capital) e, quando houver, Prejuízos Acumulados. As demais opções trazem contas de Passivo (A) ou de Ativo (C, D).",
    "PL é capital PRÓPRIO dos sócios — pense em quais das opções listadas pertencem aos sócios, e não a terceiros ou a bens da empresa.")

add("estrutura_bp",
    "Segundo a Lei nº 6.404/76, uma obrigação da empresa com vencimento previsto para 8 meses após a data do Balanço Patrimonial deve ser classificada no",
    {"A": "Ativo Circulante.", "B": "Passivo Circulante.", "C": "Passivo Não Circulante.", "D": "Patrimônio Líquido."},
    "B",
    "O critério de classificação entre circulante e não circulante é o prazo de 12 meses após a data do balanço. Uma obrigação com vencimento em 8 meses (menos de 12 meses) é Passivo Circulante.",
    "O critério direto é: vence em até 12 meses da data do balanço? Então é circulante.")

# ============================================================
# UNIDADE II — Análise Vertical e Horizontal
# ============================================================

add("av_ah",
    "O analista precisa explicar ao gestor o que ocorreu com a conta Fornecedores: há 5 anos a empresa devia R$ 150.000,00 e, no ano passado, R$ 285.000,00. Considerando que o gestor quer um único percentual de evolução entre esses dois pontos, assinale a alternativa que representa a análise a ser feita.",
    {"A": "Análise Vertical.", "B": "Análise Horizontal Ano-Base.", "C": "Análise Vertical Ano a Ano.", "D": "Análise Horizontal Ano a Ano."},
    "B",
    "Como o gestor quer comparar dois pontos no tempo distantes entre si (usando o mais antigo como referência), a ferramenta adequada é a Análise Horizontal Ano-Base, que sempre compara cada período ao mesmo ano de referência.",
    "A pista é “um único percentual” comparando o ano mais antigo (referência) com o mais recente — isso é Análise Horizontal com ano-base fixo.",
    source="textbook")

add("av_ah",
    "Se uma empresa apresenta o saldo da conta Imobilizado de R$ 500.000,00 e o Ativo Total de R$ 1.250.000,00, qual a representatividade do Imobilizado no total dos recursos (Análise Vertical)?",
    {"A": "250%.", "B": "150%.", "C": "100%.", "D": "40%."},
    "D",
    "Análise Vertical = (valor da conta ÷ valor de referência) × 100. Aqui: (500.000 ÷ 1.250.000) × 100 = 40%.",
    "Divida o Imobilizado pelo Ativo Total e multiplique por 100.",
    source="textbook")

add("av_ah",
    "A empresa Boa Ltda. apresentou o saldo do Imobilizado de R$ 550.000,00 em 20X7, R$ 520.000,00 em 20X8 e R$ 500.000,00 em 20X9. Considerando 20X7 como ano-base, qual a evolução da Análise Horizontal do Imobilizado de 20X9 em relação a 20X7?",
    {"A": "Positiva de 9,09%.", "B": "Negativa de 9,09%.", "C": "Positiva de 10,00%.", "D": "Negativa de 10,00%."},
    "B",
    "AH ano-base = (valor do período ÷ valor do ano-base − 1) × 100. Em 20X9: (500.000 ÷ 550.000 − 1) × 100 = (0,9091 − 1) × 100 ≈ −9,09%.",
    "Compare sempre com o ano-base (20X7): (valor atual ÷ valor base − 1) × 100.",
    source="textbook")

add("av_ah",
    "Na Análise Vertical do Balanço Patrimonial, qual é o referencial (100%) utilizado para calcular a representatividade das contas do Ativo?",
    {"A": "Patrimônio Líquido.", "B": "Ativo Total.", "C": "Receita Líquida.", "D": "Passivo Circulante."},
    "B",
    "No Balanço Patrimonial, a base de cálculo (100%) para a Análise Vertical das contas do Ativo é o próprio Ativo Total (e, do lado do Passivo, o Passivo Total + PL, que é igual ao Ativo Total).",
    "Pense: contra qual valor cada conta do Ativo é comparada para saber sua “fatia” do total?")

add("av_ah",
    "Na Análise Vertical da Demonstração do Resultado do Exercício (DRE), qual é o referencial (100%) utilizado?",
    {"A": "Lucro Líquido.", "B": "Ativo Total.", "C": "Receita Líquida (ou Receita de Vendas).", "D": "Patrimônio Líquido."},
    "C",
    "Na DRE, a base de cálculo da Análise Vertical é a Receita Líquida (de vendas ou de serviços), contra a qual todas as demais linhas (custos, despesas, lucros) são comparadas percentualmente.",
    "É diferente do Balanço: na DRE, tudo é comparado à receita, não ao ativo.")

add("av_ah",
    "Uma empresa apresenta Estoques de R$ 180.000,00 e Ativo Total de R$ 900.000,00. Qual a representatividade (Análise Vertical) dos Estoques sobre o Ativo Total?",
    {"A": "5%.", "B": "10%.", "C": "20%.", "D": "50%."},
    "C",
    "(180.000 ÷ 900.000) × 100 = 20%.",
    "Divida Estoques pelo Ativo Total e multiplique por 100.")

add("av_ah",
    "Na Análise Horizontal Ano a Ano (encadeada), a variação percentual de cada período é calculada tomando-se como referência",
    {"A": "sempre o primeiro ano da série (ano-base).", "B": "sempre o ano imediatamente anterior.",
     "C": "sempre a média dos anos anteriores.", "D": "sempre o último ano da série."},
    "B",
    "Na Análise Horizontal Ano a Ano, cada período é comparado apenas ao período imediatamente anterior, ao contrário da AH Ano-Base, que sempre usa o mesmo ano de referência fixo.",
    "“Ano a ano” é literal: compara sempre com o ano logo antes, e não com um ano fixo de referência.")

add("av_ah",
    "Uma conta de Clientes apresentou os saldos de R$ 200.000,00 em 20X1 e R$ 250.000,00 em 20X2. Qual a variação da Análise Horizontal de 20X1 para 20X2?",
    {"A": "+20%.", "B": "+25%.", "C": "+80%.", "D": "−20%."},
    "B",
    "(250.000 ÷ 200.000 − 1) × 100 = (1,25 − 1) × 100 = +25%.",
    "Divida o valor mais recente pelo mais antigo, subtraia 1 e multiplique por 100.")

add("av_ah",
    "Uma conta de Estoques apresentou os saldos de R$ 300.000,00 em 20X0 (ano-base), R$ 330.000,00 em 20X1 e R$ 360.000,00 em 20X2. Qual a variação da Análise Horizontal Ano-Base de 20X2 em relação a 20X0?",
    {"A": "+10%.", "B": "+20%.", "C": "+9,09%.", "D": "+30%."},
    "B",
    "(360.000 ÷ 300.000 − 1) × 100 = (1,2 − 1) × 100 = +20%.",
    "Compare sempre com o ano-base fixo (20X0), não com o ano imediatamente anterior.")

add("av_ah",
    "A visão conjunta da Análise Vertical (AV) e da Análise Horizontal (AH) é importante porque",
    {"A": "a AV mostra a estrutura (composição) das contas em um momento, enquanto a AH mostra a evolução ao longo do tempo — juntas, dão uma visão mais completa.",
     "B": "a AV e a AH sempre chegam exatamente ao mesmo resultado numérico.",
     "C": "a AH substitui totalmente a necessidade da AV.", "D": "a AV só pode ser calculada depois que a AH tiver sido feita."},
    "A",
    "AV e AH respondem perguntas diferentes e complementares: a AV mostra “quanto essa conta representa do todo, hoje”, e a AH mostra “como essa conta evoluiu ao longo do tempo”. Usá-las juntas dá uma visão mais rica do que qualquer uma isoladamente.",
    "Pense no que cada uma responde: composição (AV) x evolução no tempo (AH) — são complementares, não substitutas.")

add("av_ah",
    "Se uma conta do Ativo cresce em termos absolutos (Análise Horizontal positiva), mas sua representatividade no Ativo Total diminui (Análise Vertical), isso indica que",
    {"A": "essa conta cresceu mais devagar do que o Ativo Total como um todo.", "B": "essa conta é a única que mudou de valor no período.",
     "C": "houve um erro de cálculo, pois isso é matematicamente impossível.", "D": "a empresa reduziu seu Ativo Total a zero."},
    "A",
    "É perfeitamente possível (e comum) que uma conta cresça em valores absolutos, mas perca participação relativa, se o Ativo Total como um todo cresceu em ritmo ainda mais acelerado.",
    "Pense num exemplo simples: se uma conta dobra, mas o total do Ativo triplica, a conta cresceu, mas ficou proporcionalmente menor dentro do total.")

add("av_ah",
    "Uma empresa apresenta Passivo Circulante de R$ 240.000,00 e Passivo Total (Circulante + Não Circulante) de R$ 800.000,00. Qual a representatividade do Passivo Circulante em relação ao Passivo Total (Análise Vertical)?",
    {"A": "20%.", "B": "30%.", "C": "40%.", "D": "60%."},
    "B",
    "(240.000 ÷ 800.000) × 100 = 30%.",
    "Divida o Passivo Circulante pelo Passivo Total e multiplique por 100.")

add("av_ah",
    "Ao comparar demonstrações de anos diferentes na Análise Horizontal, é fundamental que os valores estejam",
    {"A": "em moeda corrente, sem qualquer ajuste, mesmo em períodos de alta inflação.",
     "B": "atualizados/deflacionados para a mesma data-base, quando há efeitos inflacionários relevantes, sob pena de distorcer a análise.",
     "C": "sempre em dólares americanos.", "D": "sempre arredondados para o milhar mais próximo."},
    "B",
    "Em cenários de inflação relevante, comparar valores nominais de anos diferentes sem qualquer ajuste distorce a Análise Horizontal, fazendo parecer que houve crescimento real quando, na verdade, é apenas efeito inflacionário. Por isso, valores devem ser atualizados a uma mesma data-base quando esse efeito for relevante.",
    "Pense no que aconteceria se comparássemos R$ 1.000,00 de 10 anos atrás com R$ 1.000,00 de hoje sem qualquer ajuste — o poder de compra é bem diferente.")

add("av_ah",
    "Uma empresa apresenta Despesas Operacionais de R$ 150.000,00 e Receita Líquida de R$ 1.000.000,00. Qual a representatividade (Análise Vertical) das Despesas Operacionais sobre a Receita Líquida?",
    {"A": "5%.", "B": "10%.", "C": "15%.", "D": "25%."},
    "C",
    "(150.000 ÷ 1.000.000) × 100 = 15%.",
    "Na DRE, tudo se compara à Receita Líquida — divida a despesa por ela e multiplique por 100.")

add("av_ah",
    "Sobre a Análise Horizontal Ano-Base, é correto afirmar que",
    {"A": "o ano-base é sempre o último ano da série analisada.",
     "B": "todas as variações percentuais são calculadas sempre em relação ao mesmo ano de referência (o ano-base), permitindo comparar a evolução acumulada.",
     "C": "ela não pode ser aplicada a contas de resultado, apenas a contas patrimoniais.", "D": "ela e a Análise Horizontal Ano a Ano sempre produzem os mesmos percentuais."},
    "B",
    "A característica central da AH Ano-Base é usar sempre o mesmo período de referência (geralmente o primeiro da série) para todas as comparações, o que permite enxergar a evolução acumulada desde aquele ponto.",
    "Ano-base = referência FIXA para todas as comparações da série, ao contrário da AH ano a ano.")

# ============================================================
# UNIDADE III — Giro dos Recursos, Prazos Médios e Ciclos
# ============================================================

add("giro_prazos_ciclos",
    "Aprendemos a calcular os prazos médios de estoques, contas a receber e contas a pagar, utilizados também para calcular os indicadores dos ciclos de atividades. Sobre os saldos médios dos recursos, analise:\nI. Calculam-se os saldos médios para amenizar possíveis distorções, causadas principalmente pela sazonalidade.\nII. Os saldos médios são utilizados para calcular os giros e os prazos médios, refletindo diretamente nos ciclos de atividades.\nIII. Se não for possível calcular os saldos médios, é impossível calcular os giros e prazos médios, pois os índices seriam totalmente inúteis.\nIV. O saldo médio de um recurso é a soma dos valores encontrados em demonstrações mensais.\nEstão corretas somente as afirmativas:",
    {"A": "I e II.", "B": "II e III.", "C": "III e IV.", "D": "I e III."},
    "A",
    "I e II estão corretas: os saldos médios existem justamente para suavizar distorções sazonais, e alimentam diretamente os cálculos de giro, prazos médios e ciclos. III é falsa: mesmo sem saldo médio, é possível calcular esses índices usando o saldo final (embora com menos precisão). IV é falsa: saldo médio não é a “soma”, e sim uma média (tipicamente entre saldo inicial e final, ou média de saldos mensais).",
    "Pense no propósito do saldo médio: suavizar sazonalidade — isso já aponta para I e II como corretas.",
    source="textbook")

add("giro_prazos_ciclos",
    "Uma empresa apresenta, para dois anos consecutivos: Saldo médio dos estoques ano 1: R$ 32.466,00; ano 2: R$ 36.852,00. Custo das vendas ano 1: R$ 189.780,00; ano 2: R$ 226.820,00. Assinale a alternativa correta sobre o Giro de Estoques Total (GET).",
    {"A": "O GET do ano 2 é de 6,15 vezes e do ano 1 é de 5,85 vezes, portanto esse índice foi melhor no ano 2.",
     "B": "O GET do ano 2 é de 6,15 vezes e do ano 1 é de 5,85 vezes, portanto esse índice foi melhor no ano 1.",
     "C": "O GET do ano 2 é de 6,99 vezes e do ano 1 é de 5,15 vezes, portanto esse índice foi melhor no ano 2.",
     "D": "O GET do ano 2 é de 6,15 vezes e do ano 1 é de 6,99 vezes, portanto esse índice foi melhor no ano 1."},
    "A",
    "GET = Custo das Vendas ÷ Estoque Médio. Ano 1: 189.780 ÷ 32.466 ≈ 5,85 vezes. Ano 2: 226.820 ÷ 36.852 ≈ 6,15 vezes. Quanto maior o giro, mais eficiente é a gestão de estoques (mais vezes o estoque se renovou) — logo, o índice foi melhor no ano 2.",
    "Giro = Custo das Vendas ÷ Estoque Médio, para cada ano; giro MAIOR é melhor.",
    source="textbook")

add("giro_prazos_ciclos",
    "Os indicadores de prazos médios estão ligados ao giro dos recursos. Sobre os prazos médios, analise (V para verdadeiro, F para falso):\n(  ) O PMRE é o período médio que decorre da compra até a venda de um determinado estoque.\n(  ) O PMRC é o período médio compreendido entre a venda e o recebimento dos clientes.\n(  ) Para calcular o PMRE, devemos dividir o saldo médio dos estoques pelas compras brutas ajustadas e multiplicar pelo número de dias do período.\n(  ) Para calcular o PMRC, devemos dividir o saldo médio dos valores a receber pelas compras brutas ajustadas e multiplicar pelo número de dias do período.\n(  ) O PMRE indica a média do número de dias para venda dos estoques e recebimento das vendas.\n(  ) O PMPF é o período médio que decorre da compra e o efetivo pagamento aos fornecedores.\nAssinale a alternativa que representa a ordem correta:",
    {"A": "V, V, V, V, V, V.", "B": "F, V, F, V, F, V.", "C": "V, F, V, F, V, F.", "D": "V, V, F, F, F, V."},
    "D",
    "1ª (V): é a definição correta do PMRE. 2ª (V): é a definição correta do PMRC. 3ª (F): o PMRE usa o Custo das Vendas (ou compras, dependendo do método), não “compras brutas ajustadas” diretamente, no denominador padrão — a fórmula descrita não corresponde à do PMRE. 4ª (F): o PMRC deve usar a Receita/Vendas Brutas, não as compras, no denominador. 5ª (F): o PMRE mede só o tempo até a venda, não inclui o recebimento. 6ª (V): é a definição correta do PMPF.",
    "Vá afirmação por afirmação: as duas primeiras e a última são definições literais corretas; as do meio trocam as fórmulas/conceitos.",
    source="textbook")

add("giro_prazos_ciclos",
    "O Prazo Médio de Renovação de Estoques (PMRE) indica",
    {"A": "o tempo médio, em dias, que os estoques permanecem na empresa até serem vendidos.", "B": "o tempo médio para pagamento aos fornecedores.",
     "C": "o tempo médio para recebimento dos clientes.", "D": "o número de vezes que o estoque gira ao ano."},
    "A",
    "O PMRE mede, em dias, quanto tempo em média a mercadoria fica parada em estoque antes de ser vendida. É o \"espelho em dias\" do Giro de Estoques (que mede em número de vezes).",
    "PMRE é sempre medido em DIAS, e sempre sobre estoques — não confunda com PMRC (clientes) ou PMPF (fornecedores).")

add("giro_prazos_ciclos",
    "Uma empresa apresenta Estoque Médio de R$ 120.000,00 e Custo das Mercadorias Vendidas (CMV) de R$ 720.000,00 no ano (360 dias). Qual o Prazo Médio de Renovação de Estoques (PMRE)?",
    {"A": "30 dias.", "B": "60 dias.", "C": "90 dias.", "D": "120 dias."},
    "B",
    "PMRE = (Estoque Médio ÷ CMV) × 360 = (120.000 ÷ 720.000) × 360 = 0,1667 × 360 = 60 dias.",
    "PMRE = (Estoque Médio ÷ CMV) × número de dias do período.")

add("giro_prazos_ciclos",
    "Uma empresa apresenta saldo médio de Clientes de R$ 80.000,00 e Vendas Brutas de R$ 960.000,00 no ano (360 dias). Qual o Prazo Médio de Recebimento de Clientes (PMRC)?",
    {"A": "20 dias.", "B": "30 dias.", "C": "40 dias.", "D": "45 dias."},
    "B",
    "PMRC = (Saldo Médio de Clientes ÷ Vendas Brutas) × 360 = (80.000 ÷ 960.000) × 360 = 0,0833 × 360 = 30 dias.",
    "PMRC = (Saldo Médio de Clientes ÷ Vendas Brutas) × número de dias do período.")

add("giro_prazos_ciclos",
    "Uma empresa apresenta saldo médio de Fornecedores de R$ 90.000,00 e Compras Brutas de R$ 540.000,00 no ano (360 dias). Qual o Prazo Médio de Pagamento a Fornecedores (PMPF)?",
    {"A": "30 dias.", "B": "45 dias.", "C": "60 dias.", "D": "90 dias."},
    "C",
    "PMPF = (Saldo Médio de Fornecedores ÷ Compras Brutas) × 360 = (90.000 ÷ 540.000) × 360 = 0,1667 × 360 = 60 dias.",
    "PMPF = (Saldo Médio de Fornecedores ÷ Compras Brutas) × número de dias do período.")

add("giro_prazos_ciclos",
    "O Ciclo Operacional de uma empresa é formado pela soma de",
    {"A": "PMRE + PMPF.", "B": "PMRE + PMRC.", "C": "PMRC + PMPF.", "D": "PMRE + PMRC + PMPF."},
    "B",
    "O Ciclo Operacional cobre o período desde a compra da mercadoria (ou matéria-prima) até o recebimento da venda — soma-se, portanto, o Prazo Médio de Renovação de Estoques (PMRE) ao Prazo Médio de Recebimento de Clientes (PMRC).",
    "Ciclo Operacional cobre da compra até o RECEBIMENTO — não envolve o pagamento a fornecedores.")

add("giro_prazos_ciclos",
    "Uma empresa apresenta PMRE de 45 dias e PMRC de 35 dias. Qual o Ciclo Operacional dessa empresa?",
    {"A": "10 dias.", "B": "45 dias.", "C": "70 dias.", "D": "80 dias."},
    "D",
    "Ciclo Operacional = PMRE + PMRC = 45 + 35 = 80 dias.",
    "Some PMRE + PMRC.")

add("giro_prazos_ciclos",
    "O Ciclo Financeiro (ou Ciclo de Caixa) é calculado por",
    {"A": "Ciclo Operacional + PMPF.", "B": "Ciclo Operacional − PMPF.", "C": "PMRE − PMRC.", "D": "PMRE + PMRC + PMPF."},
    "B",
    "O Ciclo Financeiro representa o período que a empresa precisa financiar com recursos próprios (ou de terceiros, além de fornecedores): é o Ciclo Operacional menos o prazo que os fornecedores concedem de \"financiamento espontâneo\" (PMPF).",
    "Ciclo Financeiro = Ciclo Operacional − PMPF (o prazo que os fornecedores “financiam” a operação).")

add("giro_prazos_ciclos",
    "Uma empresa apresenta Ciclo Operacional de 80 dias e Prazo Médio de Pagamento a Fornecedores (PMPF) de 30 dias. Qual o Ciclo Financeiro dessa empresa?",
    {"A": "30 dias.", "B": "50 dias.", "C": "80 dias.", "D": "110 dias."},
    "B",
    "Ciclo Financeiro = Ciclo Operacional − PMPF = 80 − 30 = 50 dias.",
    "Ciclo Financeiro = Ciclo Operacional − PMPF.")

add("giro_prazos_ciclos",
    "Quando o Ciclo Financeiro de uma empresa é negativo, isso significa que",
    {"A": "o PMPF é maior que o Ciclo Operacional, ou seja, a empresa recebe dos clientes antes de precisar pagar os fornecedores — situação financeiramente favorável.",
     "B": "a empresa está com problemas graves de caixa.", "C": "o cálculo está necessariamente errado, pois ciclo financeiro nunca pode ser negativo.", "D": "a empresa não tem fornecedores."},
    "A",
    "Um Ciclo Financeiro negativo ocorre quando o prazo concedido pelos fornecedores (PMPF) é maior do que o próprio Ciclo Operacional — nesse caso, a empresa recebe dos clientes antes mesmo de precisar pagar os fornecedores, o que é uma situação financeiramente favorável (menor necessidade de capital de giro próprio).",
    "Ciclo Financeiro negativo é bom sinal: significa que os fornecedores estão, na prática, financiando a operação.")

add("giro_prazos_ciclos",
    "O Giro de Estoques indica",
    {"A": "quantas vezes, em média, o estoque se renovou (foi vendido e reposto) em um determinado período.", "B": "o valor em reais do estoque médio.",
     "C": "o prazo médio de pagamento aos fornecedores.", "D": "a margem de lucro sobre as vendas."},
    "A",
    "O Giro de Estoques mede, em número de vezes, quantas vezes o estoque se renovou no período — é o \"espelho em vezes\" do PMRE (que mede o mesmo fenômeno em dias).",
    "Giro é medido em VEZES por período; PMRE é o mesmo conceito medido em DIAS.")

add("giro_prazos_ciclos",
    "Uma empresa tem Giro de Estoques de 8 vezes ao ano. Considerando um ano de 360 dias, qual o Prazo Médio de Renovação de Estoques (PMRE) correspondente?",
    {"A": "30 dias.", "B": "45 dias.", "C": "60 dias.", "D": "90 dias."},
    "B",
    "PMRE = número de dias do período ÷ Giro = 360 ÷ 8 = 45 dias.",
    "PMRE = 360 (ou dias do período) ÷ Giro.")

add("giro_prazos_ciclos",
    "Os saldos médios (de estoques, clientes ou fornecedores) costumam ser utilizados nos cálculos de giro e prazos médios, em vez do saldo final isolado, principalmente para",
    {"A": "simplificar os cálculos, embora sempre produzam exatamente o mesmo resultado do saldo final.", "B": "amenizar possíveis distorções causadas pela sazonalidade das operações.",
     "C": "atender a uma exigência exclusiva da Lei das Sociedades por Ações.", "D": "eliminar a necessidade de conhecer o CMV."},
    "B",
    "Um saldo final isolado pode estar distorcido por um pico ou vale sazonal (ex.: estoque muito alto às vésperas de uma data comemorativa). O saldo médio (geralmente inicial + final ÷ 2, ou média de saldos mensais) suaviza esse efeito.",
    "Pense num exemplo sazonal: uma loja de brinquedos terá estoque muito maior em novembro do que em fevereiro — o saldo médio evita que esse pico distorça o índice.")

add("giro_prazos_ciclos",
    "Uma indústria apresenta Ciclo Operacional de 100 dias e Prazo Médio de Pagamento a Fornecedores (PMPF) de 40 dias. Por quantos dias a empresa precisa financiar suas operações com recursos próprios ou de terceiros que não fornecedores (Ciclo Financeiro)?",
    {"A": "40 dias.", "B": "60 dias.", "C": "100 dias.", "D": "140 dias."},
    "B",
    "Ciclo Financeiro = Ciclo Operacional − PMPF = 100 − 40 = 60 dias.",
    "Ciclo Financeiro = Ciclo Operacional − PMPF.")

add("giro_prazos_ciclos",
    "O Ciclo Econômico de uma empresa comercial, diferentemente do Ciclo Operacional, considera o período",
    {"A": "entre a compra da mercadoria e sua venda, sem considerar o prazo de recebimento dos clientes.", "B": "entre o recebimento dos clientes e o pagamento dos fornecedores.",
     "C": "exclusivamente entre o pagamento aos fornecedores e o recebimento das vendas.", "D": "apenas o prazo de pagamento aos fornecedores."},
    "A",
    "O Ciclo Econômico vai da compra até a venda da mercadoria (equivalente ao PMRE), sem incluir o tempo adicional até o efetivo recebimento do cliente — diferente do Ciclo Operacional, que já soma o prazo de recebimento (PMRC).",
    "Ciclo Econômico é mais curto que o Operacional: ele para na VENDA, não vai até o recebimento.")

add("giro_prazos_ciclos",
    "Uma empresa aumentou seu Prazo Médio de Recebimento de Clientes (PMRC) de 30 para 50 dias, mantendo os demais prazos constantes. O efeito mais provável sobre o Ciclo Financeiro dessa empresa é",
    {"A": "reduzir o Ciclo Financeiro.", "B": "manter o Ciclo Financeiro inalterado.", "C": "aumentar o Ciclo Financeiro, pressionando a necessidade de capital de giro.", "D": "eliminar totalmente o Ciclo Financeiro."},
    "C",
    "Como o Ciclo Operacional inclui o PMRC (Ciclo Operacional = PMRE + PMRC), um aumento no PMRC eleva o Ciclo Operacional e, consequentemente, o Ciclo Financeiro (Ciclo Operacional − PMPF), aumentando a necessidade de capital de giro da empresa.",
    "PMRC maior → Ciclo Operacional maior → Ciclo Financeiro maior (mantendo o PMPF constante).")

# ============================================================
# UNIDADE IV — Liquidez, Endividamento e Rentabilidade
# ============================================================

add("liquidez",
    "Uma empresa apresenta: Ativo Total R$ 1.000.000,00; Ativo Realizável a Longo Prazo R$ 60.000,00; Patrimônio Líquido R$ 400.000,00; Ativo Circulante R$ 600.000,00; Passivo Não Circulante R$ 200.000,00. Escolha a alternativa que indica corretamente a Liquidez Corrente (LC), a Liquidez Geral (LG) e a Imobilização do Patrimônio Líquido (IPL).",
    {"A": "LC 1,0; LG 1,1; IPL 85%.", "B": "LC 1,0; LG 1,7; IPL 85%.", "C": "LC 1,5; LG 1,6; IPL 100%.", "D": "LC 1,5; LG 1,1; IPL 85%."},
    "D",
    "Passivo Total = Ativo − PL = 1.000.000 − 400.000 = 600.000; Passivo Circulante = 600.000 − 200.000 (PNC) = 400.000. LC = AC ÷ PC = 600.000 ÷ 400.000 = 1,5. LG = (AC + ARLP) ÷ (PC + PNC) = (600.000 + 60.000) ÷ (400.000 + 200.000) = 660.000 ÷ 600.000 = 1,1. Recursos imobilizados = ANC − ARLP = (1.000.000 − 600.000) − 60.000 = 340.000; IPL = 340.000 ÷ 400.000 = 85%.",
    "Primeiro derive o Passivo Circulante (Passivo Total − PNC) e o Ativo Não Circulante (Ativo Total − AC); depois aplique as três fórmulas.",
    source="textbook")

add("liquidez",
    "O Índice de Liquidez Corrente (LC) é calculado por",
    {"A": "Ativo Circulante ÷ Passivo Circulante.", "B": "(Ativo Circulante − Estoques) ÷ Passivo Circulante.",
     "C": "(Ativo Circulante + Realizável a Longo Prazo) ÷ (Passivo Circulante + Passivo Não Circulante).", "D": "Ativo Total ÷ Passivo Total."},
    "A",
    "A Liquidez Corrente compara todo o Ativo Circulante com todo o Passivo Circulante — é o índice de liquidez mais simples e mais usado.",
    "É a fórmula mais básica de liquidez: tudo que é de curto prazo no Ativo, sobre tudo que é de curto prazo no Passivo.")

add("liquidez",
    "O Índice de Liquidez Seca (LS) exclui do Ativo Circulante, no numerador, o valor",
    {"A": "das Duplicatas a Receber.", "B": "do Caixa e Equivalentes de Caixa.", "C": "dos Estoques.", "D": "das Aplicações Financeiras de curto prazo."},
    "C",
    "A Liquidez Seca exclui os Estoques do numerador, pois eles costumam ser o item de conversão em caixa mais lenta e incerta dentro do Ativo Circulante.",
    "Pense em qual item do Ativo Circulante é o mais “demorado” para virar dinheiro.")

add("liquidez",
    "O Índice de Liquidez Geral (LG) é calculado por",
    {"A": "Ativo Circulante ÷ Passivo Circulante.", "B": "(Ativo Circulante + Realizável a Longo Prazo) ÷ (Passivo Circulante + Passivo Não Circulante).",
     "C": "(Ativo Circulante − Estoques) ÷ Passivo Circulante.", "D": "Patrimônio Líquido ÷ Ativo Total."},
    "B",
    "A Liquidez Geral amplia a análise para o longo prazo, somando o Realizável a Longo Prazo ao Ativo Circulante e o Passivo Não Circulante ao Passivo Circulante.",
    "LG é a “versão longo prazo” da LC: soma ARLP em cima, soma PNC embaixo.")

add("liquidez",
    "Uma empresa apresenta Ativo Circulante de R$ 400.000,00 e Passivo Circulante de R$ 250.000,00. Qual a Liquidez Corrente dessa empresa?",
    {"A": "0,625.", "B": "1,0.", "C": "1,6.", "D": "2,5."},
    "C",
    "LC = 400.000 ÷ 250.000 = 1,6.",
    "LC = Ativo Circulante ÷ Passivo Circulante.")

add("liquidez",
    "Uma empresa apresenta Ativo Circulante de R$ 500.000,00 (dos quais R$ 200.000,00 são Estoques) e Passivo Circulante de R$ 300.000,00. Qual a Liquidez Seca dessa empresa?",
    {"A": "0,67.", "B": "1,0.", "C": "1,67.", "D": "2,5."},
    "B",
    "LS = (500.000 − 200.000) ÷ 300.000 = 300.000 ÷ 300.000 = 1,0.",
    "LS = (Ativo Circulante − Estoques) ÷ Passivo Circulante.")

add("liquidez",
    "Uma empresa apresenta Ativo Circulante de R$ 300.000,00, Realizável a Longo Prazo de R$ 100.000,00, Passivo Circulante de R$ 200.000,00 e Passivo Não Circulante de R$ 200.000,00. Qual a Liquidez Geral dessa empresa?",
    {"A": "0,5.", "B": "1,0.", "C": "1,5.", "D": "2,0."},
    "B",
    "LG = (300.000 + 100.000) ÷ (200.000 + 200.000) = 400.000 ÷ 400.000 = 1,0.",
    "LG = (AC + ARLP) ÷ (PC + PNC).")

add("liquidez",
    "Um índice de Liquidez Corrente igual a 1,3 significa que, para cada R$ 1,00 de dívida de curto prazo, a empresa possui",
    {"A": "R$ 0,77 em recursos de curto prazo para pagar.", "B": "R$ 1,30 em recursos de curto prazo para pagar.", "C": "R$ 1,30 de lucro.", "D": "130% de endividamento."},
    "B",
    "A leitura direta da Liquidez Corrente é: para cada R$ 1,00 de dívida de curto prazo (Passivo Circulante), a empresa tem R$ 1,30 em ativos de curto prazo (Ativo Circulante) disponíveis.",
    "A liquidez é lida diretamente como “R$ X para cada R$ 1,00 de dívida de curto prazo”.")

add("liquidez",
    "Um índice de Liquidez Corrente menor do que 1,0 indica que",
    {"A": "o Ativo Circulante é maior que o Passivo Circulante — situação confortável.", "B": "o Ativo Circulante é menor que o Passivo Circulante — a empresa pode ter dificuldade para honrar seus compromissos de curto prazo apenas com recursos circulantes.",
     "C": "a empresa não tem nenhuma dívida.", "D": "a empresa é necessariamente insolvente."},
    "B",
    "Um LC menor que 1,0 significa que o Ativo Circulante não é suficiente para cobrir o Passivo Circulante — um sinal de alerta, embora não signifique automaticamente insolvência (depende de outros fatores, como a capacidade de gerar caixa).",
    "LC < 1,0 significa que o Ativo Circulante não cobre totalmente o Passivo Circulante.")

add("liquidez",
    "A Liquidez Seca é considerada, por muitos analistas, uma medida mais conservadora do que a Liquidez Corrente porque",
    {"A": "ela soma o Realizável a Longo Prazo ao Ativo Circulante.", "B": "ela exclui os estoques, que costumam ser o item de conversão em caixa mais lenta e incerta dentro do Ativo Circulante.",
     "C": "ela ignora totalmente o Passivo Circulante.", "D": "ela é sempre maior do que a Liquidez Corrente."},
    "B",
    "Ao remover os estoques (item menos líquido do Ativo Circulante) do numerador, a Liquidez Seca oferece uma visão mais conservadora e rigorosa da capacidade de pagamento imediato da empresa.",
    "Pense: sem estoques, a liquidez enxerga só os ativos mais rapidamente conversíveis em caixa.")

add("liquidez",
    "A Liquidez Geral (LG) diferencia-se da Liquidez Corrente (LC) principalmente por",
    {"A": "considerar apenas os itens de curtíssimo prazo.", "B": "incluir, tanto no numerador quanto no denominador, itens de longo prazo (Realizável a Longo Prazo e Passivo Não Circulante), além dos de curto prazo.",
     "C": "excluir totalmente o Ativo Circulante do cálculo.", "D": "usar o Patrimônio Líquido como base de cálculo."},
    "B",
    "A LG amplia o horizonte de análise da LC, somando itens de longo prazo (ARLP no numerador e PNC no denominador) aos itens de curto prazo já usados na LC.",
    "LG = LC “ampliada” com os itens de longo prazo somados em cima e embaixo.")

add("liquidez",
    "Uma empresa apresenta Liquidez Corrente de 0,9 em determinado exercício. Isso significa, na prática, que",
    {"A": "a empresa tem excesso de recursos de curto prazo.", "B": "para cada R$ 1,00 de obrigação de curto prazo, a empresa possui apenas R$ 0,90 em ativos de curto prazo.",
     "C": "a empresa é totalmente insolvente.", "D": "a Liquidez Seca dessa empresa será necessariamente maior que 0,9."},
    "B",
    "A leitura direta é: R$ 0,90 de Ativo Circulante para cada R$ 1,00 de Passivo Circulante — um sinal de atenção, sem necessariamente significar insolvência.",
    "Leia o índice como “R$ X de ativo circulante para cada R$ 1,00 de dívida circulante”.")

add("liquidez",
    "Sobre os índices de liquidez, é correto afirmar que",
    {"A": "um índice de liquidez alto é sempre sinônimo de boa gestão financeira, sem exceções.", "B": "eles devem ser interpretados em conjunto com outros indicadores e comparados com padrões do setor, pois um índice isolado não conta toda a história da empresa.",
     "C": "eles substituem totalmente a necessidade de analisar o endividamento.", "D": "eles são calculados exclusivamente a partir da Demonstração do Resultado."},
    "B",
    "Nenhum índice deve ser interpretado isoladamente — a análise financeira ganha robustez quando os índices são comparados entre si, ao longo do tempo, e com padrões do setor (índices-padrão).",
    "Lembre da lógica dos índices-padrão: um número sozinho não diz muita coisa sem comparação.")

add("liquidez",
    "Uma empresa apresenta Ativo Circulante de R$ 250.000,00 (sendo R$ 90.000,00 de Estoques) e Passivo Circulante de R$ 200.000,00. Calcule a Liquidez Corrente e a Liquidez Seca, respectivamente.",
    {"A": "1,25 e 0,80.", "B": "1,25 e 1,25.", "C": "0,80 e 1,25.", "D": "1,25 e 0,45."},
    "A",
    "LC = 250.000 ÷ 200.000 = 1,25. LS = (250.000 − 90.000) ÷ 200.000 = 160.000 ÷ 200.000 = 0,80.",
    "Calcule a LC normalmente e depois refaça excluindo os Estoques do numerador para a LS.")

add("endividamento",
    "O Índice de Endividamento Geral (EG) é calculado por",
    {"A": "Passivo Circulante ÷ Ativo Circulante.", "B": "(Passivo Circulante + Passivo Não Circulante) ÷ Ativo Total.",
     "C": "Patrimônio Líquido ÷ Ativo Total.", "D": "Ativo Total ÷ Patrimônio Líquido."},
    "B",
    "O Endividamento Geral mostra qual percentual do Ativo Total é financiado por capital de terceiros (Passivo Total, somando Circulante e Não Circulante).",
    "EG = todo o Passivo exigível dividido pelo Ativo Total.")

add("endividamento",
    "Uma empresa apresenta Passivo Circulante de R$ 200.000,00, Passivo Não Circulante de R$ 300.000,00 e Ativo Total de R$ 1.000.000,00. Qual o Endividamento Geral dessa empresa?",
    {"A": "20%.", "B": "30%.", "C": "50%.", "D": "60%."},
    "C",
    "EG = (200.000 + 300.000) ÷ 1.000.000 = 500.000 ÷ 1.000.000 = 50%.",
    "Some Passivo Circulante e Não Circulante, e divida pelo Ativo Total.")

add("endividamento",
    "O índice de Composição do Endividamento indica",
    {"A": "o percentual do Ativo financiado por capital próprio.", "B": "qual a parcela das dívidas totais que vence no curto prazo (Passivo Circulante em relação ao Passivo Total).",
     "C": "a rentabilidade sobre o capital próprio.", "D": "o prazo médio de renovação dos estoques."},
    "B",
    "A Composição do Endividamento mostra o \"perfil\" da dívida: qual fração dela precisa ser paga logo (curto prazo) versus o que ainda tem prazo mais longo para ser quitado.",
    "Esse índice é sobre o PERFIL da dívida (curto x longo prazo), não sobre o total dela.")

add("endividamento",
    "Uma empresa apresenta Passivo Circulante de R$ 180.000,00 e Passivo Total (Circulante + Não Circulante) de R$ 600.000,00. Qual a Composição do Endividamento dessa empresa?",
    {"A": "20%.", "B": "30%.", "C": "40%.", "D": "70%."},
    "B",
    "Composição do Endividamento = Passivo Circulante ÷ Passivo Total = 180.000 ÷ 600.000 = 30%.",
    "Divida o Passivo Circulante pelo Passivo Total (não pelo Ativo Total).")

add("endividamento",
    "O índice de Imobilização do Patrimônio Líquido (IPL) indica",
    {"A": "quanto do Patrimônio Líquido está aplicado em recursos de longa maturação (imobilizado, intangível, investimentos), em vez de estar disponível para o giro dos negócios.",
     "B": "o percentual de dívidas de curto prazo.", "C": "a margem de lucro líquido sobre as vendas.", "D": "o giro dos estoques."},
    "A",
    "O IPL mostra quanto do capital próprio (PL) está \"preso\" em ativos de longa maturação, e não disponível para financiar o capital de giro do dia a dia.",
    "IPL relaciona recursos “fixos” de longo prazo com o Patrimônio Líquido — pense em quanto do capital dos sócios está imobilizado.")

add("endividamento",
    "Uma empresa apresenta Patrimônio Líquido de R$ 500.000,00 e Ativo Imobilizado de R$ 350.000,00 (sem outros recursos de longa maturação). Qual a Imobilização do Patrimônio Líquido (IPL)?",
    {"A": "50%.", "B": "60%.", "C": "70%.", "D": "143%."},
    "C",
    "IPL = 350.000 ÷ 500.000 = 70%.",
    "IPL = recursos imobilizados/longa maturação ÷ Patrimônio Líquido.")

add("endividamento",
    "Quando a Imobilização do Patrimônio Líquido (IPL) é superior a 100%, isso indica que",
    {"A": "o Patrimônio Líquido é insuficiente para financiar todo o imobilizado, sendo necessário usar recursos de terceiros (Passivo) para financiar parte dele.",
     "B": "a empresa não tem nenhum imobilizado.", "C": "a empresa está totalmente livre de dívidas.", "D": "a Liquidez Corrente é necessariamente maior que 1."},
    "A",
    "Um IPL acima de 100% significa que o valor imobilizado excede o próprio Patrimônio Líquido, o que obriga a empresa a recorrer a capital de terceiros para cobrir essa diferença — reduzindo os recursos próprios disponíveis para o giro do negócio.",
    "Se IPL > 100%, o PL sozinho não é suficiente para bancar tudo que está imobilizado.")

add("endividamento",
    "Um Endividamento Geral de 70% significa que",
    {"A": "70% do Ativo Total da empresa é financiado por capital de terceiros (dívidas), e 30% por capital próprio.", "B": "a empresa tem lucro de 70%.",
     "C": "70% do Patrimônio Líquido é imobilizado.", "D": "a empresa está isenta de impostos."},
    "A",
    "O Endividamento Geral de 70% indica que 70% dos recursos totais aplicados no Ativo vieram de terceiros (Passivo), restando apenas 30% de capital próprio (PL) financiando o Ativo.",
    "EG é sempre lido em relação ao Ativo Total: quanto dele vem de dívida, versus quanto vem do PL.")

add("endividamento",
    "Sobre o endividamento, uma empresa muito alavancada (com Endividamento Geral elevado) apresenta, entre outros riscos,",
    {"A": "maior dependência de capital de terceiros e maior exposição a variações de juros e a exigências de pagamento das dívidas.",
     "B": "automaticamente maior lucratividade, sem qualquer risco adicional.", "C": "Liquidez Corrente necessariamente igual a zero.", "D": "impossibilidade de calcular qualquer outro índice financeiro."},
    "A",
    "Quanto mais alavancada (endividada) a empresa, maior sua dependência de terceiros e maior sua exposição a riscos como aumento de juros e exigência de pagamento das dívidas — mesmo que a alavancagem também possa, em certos cenários, amplificar o retorno sobre o capital próprio.",
    "Alto endividamento não é automaticamente bom nem ruim — mas sempre traz maior exposição a risco financeiro.")

add("endividamento",
    "Uma empresa apresenta Ativo Total de R$ 2.000.000,00 e Patrimônio Líquido de R$ 800.000,00. Qual o Endividamento Geral dessa empresa (considerando Passivo Total = Ativo Total − PL)?",
    {"A": "40%.", "B": "60%.", "C": "80%.", "D": "120%."},
    "B",
    "Passivo Total = 2.000.000 − 800.000 = 1.200.000. EG = 1.200.000 ÷ 2.000.000 = 60%.",
    "Primeiro derive o Passivo Total (Ativo − PL), depois divida pelo Ativo Total.")

add("endividamento",
    "A Participação de Capitais de Terceiros (PCT), também chamada de Grau de Endividamento em relação ao PL, relaciona",
    {"A": "Passivo Total (Circulante + Não Circulante) com o Patrimônio Líquido, em vez de com o Ativo Total.", "B": "Ativo Circulante com Passivo Circulante.",
     "C": "Estoques com Ativo Total.", "D": "Receita Líquida com Ativo Total."},
    "A",
    "Diferente do Endividamento Geral (que compara o Passivo com o Ativo Total), a Participação de Capitais de Terceiros compara o Passivo Total diretamente com o Patrimônio Líquido, mostrando quanto de capital de terceiros existe para cada unidade de capital próprio.",
    "PCT usa o PL como referência, não o Ativo Total (essa é a diferença em relação ao EG).")

add("endividamento",
    "Uma empresa apresenta Passivo Total de R$ 480.000,00 e Patrimônio Líquido de R$ 400.000,00. Qual a Participação de Capitais de Terceiros em relação ao Patrimônio Líquido (Passivo Total ÷ PL)?",
    {"A": "83,3%.", "B": "100%.", "C": "120%.", "D": "12%."},
    "C",
    "PCT = 480.000 ÷ 400.000 = 1,2 = 120%.",
    "PCT = Passivo Total ÷ Patrimônio Líquido.")

add("endividamento",
    "Duas empresas do mesmo setor apresentam Endividamento Geral de 40% (Empresa X) e 75% (Empresa Y). Considerando apenas esse indicador, é correto afirmar que",
    {"A": "a Empresa Y depende proporcionalmente mais de capital de terceiros para financiar seus ativos do que a Empresa X.", "B": "as duas empresas têm exatamente a mesma estrutura de capital.",
     "C": "a Empresa X tem, necessariamente, menor lucro do que a Empresa Y.", "D": "o Endividamento Geral não tem relação com a estrutura de capital da empresa."},
    "A",
    "Quanto maior o Endividamento Geral, maior a dependência proporcional de capital de terceiros. Com EG de 75%, a Empresa Y depende muito mais de dívidas do que a Empresa X (40%) para financiar seus ativos.",
    "Compare os dois percentuais diretamente: quem tem EG maior depende proporcionalmente mais de terceiros.")

add("endividamento",
    "Uma empresa apresenta Ativo Total de R$ 1.500.000,00, Passivo Não Circulante de R$ 300.000,00 e Endividamento Geral de 40%. Qual o valor do Passivo Circulante dessa empresa?",
    {"A": "R$ 300.000,00.", "B": "R$ 600.000,00.", "C": "R$ 900.000,00.", "D": "R$ 1.200.000,00."},
    "A",
    "Passivo Total = 40% × 1.500.000 = 600.000. Passivo Circulante = Passivo Total − PNC = 600.000 − 300.000 = R$ 300.000,00.",
    "Primeiro ache o Passivo Total (EG × Ativo Total), depois subtraia o PNC para achar o PC.")

add("rentabilidade",
    "Uma empresa apresenta os seguintes saldos: Lucro Líquido R$ 10.000,00; Ativo Total R$ 1.000.000,00; Patrimônio Líquido R$ 400.000,00; Receitas Brutas R$ 2.400.000,00; Deduções da Receita Bruta R$ 400.000,00. Escolha a alternativa que indica corretamente a Margem Líquida (ML) e o ROE.",
    {"A": "ML 0,5% e ROE 1%.", "B": "ML 0,5% e ROE 2,5%.", "C": "ML 1,0% e ROE 2,5%.", "D": "ML 0,4% e ROE 2,5%."},
    "B",
    "Receita Líquida = 2.400.000 − 400.000 = 2.000.000. ML = Lucro Líquido ÷ Receita Líquida = 10.000 ÷ 2.000.000 = 0,5%. ROE = Lucro Líquido ÷ PL = 10.000 ÷ 400.000 = 2,5%.",
    "Primeiro ache a Receita Líquida (Receita Bruta − Deduções); ML usa a Receita Líquida, ROE usa o PL.",
    source="textbook")

add("rentabilidade",
    "A Margem Bruta (MB) é calculada por",
    {"A": "Lucro Bruto ÷ Receita Líquida.", "B": "Lucro Líquido ÷ Ativo Total.", "C": "Lucro Líquido ÷ Patrimônio Líquido.", "D": "Receita Líquida ÷ Ativo Total."},
    "A",
    "A Margem Bruta relaciona o Lucro Bruto (Receita Líquida − CMV) com a própria Receita Líquida, mostrando quanto sobra, em percentual, depois de cobrir apenas o custo direto do que foi vendido.",
    "Margem Bruta = primeiro lucro que aparece na DRE, sobre a Receita Líquida.")

add("rentabilidade",
    "A Margem Líquida (ML) é calculada por",
    {"A": "Lucro Bruto ÷ Receita Líquida.", "B": "Lucro Líquido ÷ Receita Líquida.", "C": "Lucro Líquido ÷ Ativo Total.", "D": "Lucro Líquido ÷ Patrimônio Líquido."},
    "B",
    "A Margem Líquida relaciona o Lucro Líquido (resultado final, após todas as despesas e tributos) com a Receita Líquida do período.",
    "Margem Líquida = último lucro da DRE, sobre a Receita Líquida.")

add("rentabilidade",
    "Uma empresa apresenta Receita Líquida de R$ 500.000,00 e Lucro Bruto de R$ 200.000,00. Qual a Margem Bruta dessa empresa?",
    {"A": "20%.", "B": "25%.", "C": "40%.", "D": "60%."},
    "C",
    "MB = 200.000 ÷ 500.000 = 40%.",
    "MB = Lucro Bruto ÷ Receita Líquida.")

add("rentabilidade",
    "O Retorno sobre o Ativo (ROA) é calculado, em sua forma mais simples, por",
    {"A": "Lucro Líquido ÷ Ativo Total.", "B": "Lucro Líquido ÷ Patrimônio Líquido.", "C": "Receita Líquida ÷ Ativo Total.", "D": "Lucro Bruto ÷ Ativo Total."},
    "A",
    "O ROA mede quanto de lucro a empresa gerou para cada unidade de ativo total que possui — é um indicador da eficiência de uso de TODOS os recursos, próprios e de terceiros.",
    "ROA usa o ATIVO TOTAL como base (todos os recursos empregados, próprios e de terceiros).")

add("rentabilidade",
    "O Retorno sobre o Patrimônio Líquido (ROE) é calculado por",
    {"A": "Lucro Líquido ÷ Ativo Total.", "B": "Lucro Líquido ÷ Patrimônio Líquido.", "C": "Receita Líquida ÷ Patrimônio Líquido.", "D": "Patrimônio Líquido ÷ Ativo Total."},
    "B",
    "O ROE mede o retorno gerado especificamente para os sócios/acionistas, relacionando o Lucro Líquido apenas ao capital próprio (Patrimônio Líquido) investido por eles.",
    "ROE usa só o PATRIMÔNIO LÍQUIDO como base (o que pertence só aos sócios).")

add("rentabilidade",
    "Uma empresa apresenta Lucro Líquido de R$ 60.000,00 e Ativo Total de R$ 1.200.000,00. Qual o ROA dessa empresa?",
    {"A": "2%.", "B": "5%.", "C": "10%.", "D": "20%."},
    "B",
    "ROA = 60.000 ÷ 1.200.000 = 5%.",
    "ROA = Lucro Líquido ÷ Ativo Total.")

add("rentabilidade",
    "Uma empresa apresenta Lucro Líquido de R$ 80.000,00 e Patrimônio Líquido de R$ 400.000,00. Qual o ROE dessa empresa?",
    {"A": "5%.", "B": "10%.", "C": "20%.", "D": "40%."},
    "C",
    "ROE = 80.000 ÷ 400.000 = 20%.",
    "ROE = Lucro Líquido ÷ Patrimônio Líquido.")

add("rentabilidade",
    "O EBITDA (Lucro antes de Juros, Impostos, Depreciação e Amortização) é um indicador utilizado principalmente para",
    {"A": "medir a geração de caixa operacional da empresa, isolando efeitos financeiros, tributários e de itens não-caixa como a depreciação.",
     "B": "substituir totalmente o Lucro Líquido em qualquer análise.", "C": "calcular exclusivamente a Liquidez Corrente.", "D": "medir o endividamento de curto prazo."},
    "A",
    "O EBITDA (ou LAJIDA, em português) parte do lucro operacional e remove itens financeiros, tributários e não-caixa (depreciação/amortização), dando uma visão mais próxima da geração de caixa das operações do negócio.",
    "EBITDA \"limpa\" o lucro operacional de juros, impostos e depreciação/amortização, para focar na geração operacional de caixa.")

add("rentabilidade",
    "Duas empresas do mesmo setor apresentam lucro líquido absoluto de R$ 5.000.000,00 (Empresa A) e R$ 100.000,00 (Empresa B). Para saber qual delas teve melhor desempenho relativo (retorno sobre os recursos aplicados), o analista deve",
    {"A": "comparar apenas os valores absolutos de lucro, já que a maior empresa sempre performa melhor.", "B": "calcular e comparar índices de rentabilidade relativos, como ROA ou ROE, que relativizam o lucro ao tamanho dos recursos empregados.",
     "C": "somar os lucros das duas empresas.", "D": "ignorar o lucro líquido e olhar apenas para a Liquidez Corrente."},
    "B",
    "Comparar lucros em valores absolutos não diz nada sobre eficiência: uma empresa gigante pode ter lucro absoluto maior e, ainda assim, um retorno percentual pior do que uma empresa pequena e mais eficiente. Índices como ROA/ROE relativizam o lucro ao tamanho dos recursos empregados, permitindo comparação justa.",
    "Lucro absoluto não diz nada sobre eficiência — relativize sempre pelo tamanho dos recursos usados (ROA/ROE).")

add("rentabilidade",
    "A Margem Operacional relaciona o Lucro Operacional (antes das receitas/despesas financeiras e do resultado não operacional) com",
    {"A": "o Ativo Total.", "B": "o Patrimônio Líquido.", "C": "a Receita Líquida.", "D": "o Passivo Circulante."},
    "C",
    "Assim como as demais margens (bruta e líquida), a Margem Operacional também usa a Receita Líquida como base de comparação — apenas o numerador (o tipo de lucro considerado) muda.",
    "Todas as margens (bruta, operacional, líquida) têm a Receita Líquida como base — só muda qual “nível” de lucro é usado no numerador.")

add("rentabilidade",
    "Uma empresa aumentou seu Lucro Líquido de R$ 50.000,00 para R$ 70.000,00 entre dois exercícios, mas seu Ativo Total cresceu de R$ 500.000,00 para R$ 1.000.000,00 no mesmo período. Sobre o ROA dessa empresa, é correto afirmar que",
    {"A": "o ROA aumentou, pois o lucro aumentou.", "B": "o ROA diminuiu, pois o Ativo cresceu proporcionalmente mais do que o lucro (de 10% para 7%).",
     "C": "o ROA permaneceu exatamente igual.", "D": "não é possível calcular o ROA com esses dados."},
    "B",
    "ROA ano 1 = 50.000 ÷ 500.000 = 10%. ROA ano 2 = 70.000 ÷ 1.000.000 = 7%. Mesmo com o lucro em valores absolutos tendo aumentado, o ROA caiu, porque o Ativo Total cresceu proporcionalmente mais rápido do que o lucro.",
    "Calcule o ROA dos dois anos separadamente — não olhe só para o lucro absoluto, o Ativo também mudou.")

add("rentabilidade",
    "Quando a Margem Líquida (ML) de uma empresa é alta, mas seu Giro do Ativo (Receita Líquida ÷ Ativo Total) é baixo, e ainda assim o ROA é competitivo, isso é característico de",
    {"A": "empresas de giro rápido e margem baixa, como supermercados.", "B": "empresas de margem alta e giro lento, como bens de luxo ou indústrias de capital intensivo.",
     "C": "uma situação matematicamente impossível.", "D": "empresas sem nenhum ativo."},
    "B",
    "Existem, essencialmente, dois \"caminhos\" para um bom ROA: margem alta com giro baixo (típico de bens de luxo, indústrias de capital intensivo) ou margem baixa com giro alto (típico de supermercados e varejo de baixo ticket).",
    "Pense na Fórmula DuPont (ROA = Margem × Giro): dá para chegar num bom ROA por caminhos diferentes — margem alta ou giro alto.")

add("rentabilidade",
    "Uma empresa apresenta Receita Líquida de R$ 800.000,00, Lucro Líquido de R$ 40.000,00 e Ativo Total de R$ 400.000,00. Qual a Margem Líquida e o Giro do Ativo (Receita Líquida ÷ Ativo Total), respectivamente?",
    {"A": "5% e 1,0 vez.", "B": "5% e 2,0 vezes.", "C": "10% e 1,0 vez.", "D": "10% e 2,0 vezes."},
    "B",
    "ML = 40.000 ÷ 800.000 = 5%. Giro do Ativo = 800.000 ÷ 400.000 = 2,0 vezes.",
    "ML usa Lucro Líquido ÷ Receita Líquida; Giro do Ativo usa Receita Líquida ÷ Ativo Total.")

# ============================================================
# UNIDADE V — Índices-Padrão, DuPont, Kanitz e Fleuriet
# ============================================================

add("indices_padrao_dupont",
    "Os decis dividem a série de dados em dez partes iguais, com o mesmo número de elementos, de tal forma que cada intervalo do decil contenha 10% dos elementos coletados. Sobre os índices-padrão, analise:\nI. Os decis são utilizados para calcular a mediana da série.\nII. Os decis são utilizados para calcular as notas e os conceitos.\nIII. Para calcular os decis não é necessário organizar a série em ordem crescente.\nIV. Quando o índice é do tipo “quanto menor, melhor”, as empresas classificadas no decil 1 são melhores conceituadas.\nEstão corretas somente as afirmativas:",
    {"A": "I e II.", "B": "II e III.", "C": "I e IV.", "D": "II e IV."},
    "D",
    "II é correta: os decis são a base para atribuir notas/conceitos comparativos às empresas dentro da amostra. IV é correta: para índices \"quanto menor, melhor\" (como o Endividamento Geral), estar no decil 1 (os menores valores) é a melhor posição. I é falsa: a mediana é calculada de outra forma (o valor central da série ordenada), não diretamente pelos decis. III é falsa: para calcular decis, a série PRECISA estar organizada em ordem crescente.",
    "Pense: decis servem para conceituar empresas (II) e, em índices “quanto menor melhor”, o decil 1 (menores valores) é o melhor (IV) — mas exigem série ordenada, ao contrário do que diz III.",
    source="textbook")

add("indices_padrao_dupont",
    "O método Dupont é uma técnica que reúne em uma única avaliação todas as áreas responsáveis pela performance financeira da empresa. Escolha a alternativa que mostra os índices finais do método Dupont original e modificado.",
    {"A": "PMRE e PMC.", "B": "LG e LS.", "C": "EG e IRP.", "D": "ROA e ROE."},
    "D",
    "O método DuPont original chega ao ROA (Retorno sobre o Ativo), decompondo-o em Margem Líquida × Giro do Ativo. A versão modificada estende a análise até o ROE (Retorno sobre o Patrimônio Líquido), incorporando também o efeito da alavancagem financeira.",
    "DuPont original termina no ROA; a versão modificada vai além, até o ROE.",
    source="textbook")

add("indices_padrao_dupont",
    "Os índices-padrão são utilizados para",
    {"A": "comparar um índice da própria empresa com um valor de referência do setor (mediana ou média), permitindo avaliar se o desempenho está acima ou abaixo do mercado.",
     "B": "substituir totalmente a necessidade de calcular índices individuais da empresa.", "C": "eliminar a necessidade de Análise Vertical e Horizontal.", "D": "medir exclusivamente o Ciclo Financeiro."},
    "A",
    "Um índice isolado (por exemplo, Liquidez Corrente de 1,2) não diz muito por si só. Comparado a um índice-padrão do setor (por exemplo, a mediana das empresas do mesmo ramo), o analista consegue avaliar se aquele desempenho está bom ou ruim em relação ao mercado.",
    "Índices-padrão respondem: “esse número da empresa é bom ou ruim comparado ao setor?”")

add("indices_padrao_dupont",
    "Se a Liquidez Geral de uma empresa é de 0,85 e a mediana do setor é de 1,05, é correto afirmar que",
    {"A": "a empresa está em situação melhor que o padrão do setor quanto à liquidez geral.", "B": "a empresa está em situação inferior ao padrão do setor quanto à liquidez geral.",
     "C": "o índice da empresa não pode ser comparado ao do setor.", "D": "a empresa não tem nenhuma dívida de longo prazo."},
    "B",
    "Como a Liquidez Geral da empresa (0,85) é menor do que a mediana do setor (1,05), e liquidez é um índice \"quanto maior, melhor\", a empresa está em situação inferior ao padrão do mercado nesse quesito.",
    "Liquidez é “quanto maior, melhor” — compare os dois números diretamente.")

add("indices_padrao_dupont",
    "Uma empresa apresenta Margem Líquida de 8% e Giro do Ativo de 1,5 vezes. Pela Fórmula DuPont original, qual o ROA dessa empresa?",
    {"A": "6,5%.", "B": "9,5%.", "C": "12%.", "D": "16%."},
    "C",
    "ROA (DuPont original) = Margem Líquida × Giro do Ativo = 8% × 1,5 = 12%.",
    "ROA = Margem Líquida × Giro do Ativo (multiplique, não some).")

add("indices_padrao_dupont",
    "A Fórmula DuPont, em sua versão original, decompõe o ROA (Retorno sobre o Ativo) no produto de",
    {"A": "Margem Líquida × Giro do Ativo.", "B": "Liquidez Corrente × Endividamento Geral.", "C": "PMRE × PMRC.", "D": "Margem Bruta × Liquidez Seca."},
    "A",
    "A grande contribuição da Fórmula DuPont é mostrar que o ROA resulta de dois caminhos combinados: a lucratividade sobre as vendas (Margem Líquida) e a eficiência no uso dos ativos para gerar vendas (Giro do Ativo). ROA = ML × Giro do Ativo.",
    "Decore essa multiplicação: ROA = Margem Líquida × Giro do Ativo.")

add("indices_padrao_dupont",
    "A versão modificada da Fórmula DuPont tem como foco final o indicador",
    {"A": "ROA.", "B": "ROE.", "C": "EBITDA.", "D": "Liquidez Geral."},
    "B",
    "Enquanto a versão original do DuPont termina no ROA, a versão modificada avança um passo além, incorporando o efeito da alavancagem financeira (Ativo Total ÷ PL) para chegar ao ROE — o retorno específico sobre o capital próprio dos sócios.",
    "Original → ROA. Modificada → vai além, chega no ROE (acrescentando o efeito da alavancagem).")

add("kanitz_fleuriet",
    "O Termômetro de Solvabilidade de Kanitz tem como objetivo principal",
    {"A": "calcular o lucro líquido da empresa.", "B": "prever a probabilidade de insolvência (falência) de uma empresa, classificando-a em faixas de solvência, penumbra ou insolvência.",
     "C": "medir exclusivamente o giro dos estoques.", "D": "substituir a Demonstração do Resultado do Exercício."},
    "B",
    "Kanitz desenvolveu, a partir de uma amostra de empresas saudáveis e empresas com problemas de continuidade, uma fórmula (o Fator de Solvabilidade) que classifica a empresa em faixas de solvência, penumbra ou insolvência, servindo como um alerta de risco de falência.",
    "Kanitz = previsão de falência, com faixas: solvência, penumbra, insolvência.")

add("kanitz_fleuriet",
    "No Termômetro de Kanitz, uma empresa cujo Fator de Solvabilidade está na faixa de",
    {"A": "solvência apresenta maior risco de falência no curto prazo.", "B": "insolvência apresenta maior risco de falência no curto prazo, exigindo atenção imediata.",
     "C": "penumbra está livre de qualquer risco.", "D": "insolvência é sinônimo de excelente saúde financeira."},
    "B",
    "A faixa de insolvência é a mais crítica no Termômetro de Kanitz, indicando maior risco de falência e exigindo atenção imediata da gestão. A faixa de penumbra é intermediária (zona de alerta), e a de solvência é a mais saudável.",
    "As três faixas, da pior para a melhor, são: insolvência → penumbra → solvência.")

add("kanitz_fleuriet",
    "A Análise Financeira Dinâmica (Modelo Fleuriet) propõe reclassificar o Ativo e o Passivo Circulante em contas",
    {"A": "operacionais (ou cíclicas) e financeiras (ou erráticas), em vez da classificação tradicional de curto e longo prazo.",
     "B": "exclusivamente em moeda estrangeira.", "C": "apenas por ordem alfabética.", "D": "exclusivamente vinculadas ao Imposto de Renda."},
    "A",
    "O diferencial do Modelo Fleuriet é reclassificar as contas circulantes conforme sua natureza — operacional/cíclica (ligada diretamente à atividade-fim, como estoques, clientes, fornecedores) ou financeira/errática (não ligada à operação, como aplicações financeiras e empréstimos de curto prazo) — em vez de usar apenas o critério tradicional de prazo.",
    "Fleuriet reclassifica por NATUREZA (operacional x financeira), não pela classificação contábil tradicional de prazo.")

add("kanitz_fleuriet",
    "No Modelo Fleuriet, a Necessidade de Capital de Giro (também chamada de IOG ou NCG) é calculada por",
    {"A": "Ativo Circulante Financeiro − Passivo Circulante Financeiro.", "B": "Ativo Circulante Operacional − Passivo Circulante Operacional.",
     "C": "Ativo Total − Passivo Total.", "D": "Patrimônio Líquido − Ativo Permanente."},
    "B",
    "A NCG (ou IOG) considera apenas os itens circulantes classificados como operacionais/cíclicos (ligados diretamente à atividade-fim da empresa, como estoques, clientes e fornecedores), diferente do Capital Circulante Líquido tradicional, que usa todo o Ativo e Passivo Circulante.",
    "NCG/IOG usa só os itens OPERACIONAIS do circulante, não os financeiros nem o circulante como um todo.")

add("kanitz_fleuriet",
    "A principal diferença entre o Capital Circulante Líquido (CCL) tradicional e a Necessidade de Capital de Giro (IOG/NCG) do Modelo Fleuriet é que o IOG",
    {"A": "considera apenas os itens circulantes classificados como operacionais/cíclicos, enquanto o CCL considera todo o Ativo e o Passivo Circulante, sem distinção.",
     "B": "é sempre numericamente igual ao CCL.", "C": "não usa nenhum dado do Balanço Patrimonial.", "D": "só pode ser calculado para empresas do setor público."},
    "A",
    "O CCL tradicional (Ativo Circulante − Passivo Circulante) não distingue a natureza das contas circulantes. Já o IOG/NCG do Modelo Fleuriet foca apenas na parcela operacional do circulante, oferecendo uma visão mais específica da necessidade de capital de giro gerada pelas atividades-fim da empresa.",
    "CCL usa TODO o circulante; IOG/NCG usa só a parte OPERACIONAL do circulante.")

add("kanitz_fleuriet",
    "No Modelo Fleuriet, o Saldo de Tesouraria (ST) é calculado, de forma simplificada, por",
    {"A": "Ativo Circulante Financeiro − Passivo Circulante Financeiro.", "B": "Ativo Circulante Operacional − Passivo Circulante Operacional.",
     "C": "Receita Líquida − Custo das Vendas.", "D": "Patrimônio Líquido ÷ Ativo Total."},
    "A",
    "O Saldo de Tesouraria usa a parte financeira/errática do circulante (não a operacional), mostrando a folga (ou aperto) de caixa não ligada diretamente à operação do negócio. Um ST negativo, junto com um IOG/NCG positivo elevado, é um sinal de alerta financeiro no Modelo Fleuriet.",
    "ST é o “espelho financeiro” do IOG/NCG: usa a parte FINANCEIRA/errática do circulante, não a operacional.")

assert len(QUESTIONS) == 100, len(QUESTIONS)

# ============================================================
# Assemble and write data/adc_questions.json
# ============================================================

entries = []
for i, q in enumerate(QUESTIONS, start=1):
    entries.append({
        "id": f"adc-q{i:03d}",
        "topic": q["topic"],
        "topicLabel": TOPIC_LABELS[q["topic"]],
        "question": q["question"],
        "options": q["options"],
        "correct": q["correct"],
        "explanation": q["explanation"],
        "hint": q["hint"],
        "source": q["source"],
    })

data = {"questions": entries}
out_path = Path(__file__).resolve().parent.parent / "data" / "adc_questions.json"
out_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Wrote {len(entries)} ADC questions to {out_path}")

by_topic = {}
for q in entries:
    by_topic[q["topic"]] = by_topic.get(q["topic"], 0) + 1
for topic, count in by_topic.items():
    print(f"  {topic}: {count}")
