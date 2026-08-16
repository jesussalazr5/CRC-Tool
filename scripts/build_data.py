import json
from pathlib import Path

# ============================================================
# LEVEL 1 — real Type 4 exam questions (48 of the 50; 12 and 42
# are excluded because they were officially annulled/"anuladas").
# Correct letters verified against the official gabarito:
# 1:B 2:B 3:A 4:C 5:D 6:C 7:B 8:D 9:D 10:C 11:C 13:C 14:B 15:C
# 16:B 17:C 18:B 19:A 20:D 21:D 22:A 23:C 24:A 25:A 26:D 27:A
# 28:D 29:A 30:D 31:C 32:C 33:D 34:B 35:D 36:B 37:B 38:B 39:C
# 40:A 41:A 43:D 44:C 45:C 46:D 47:D 48:D 49:D 50:D
# ============================================================

LEVEL1 = [
    dict(number=1, topic="lingua_portuguesa",
        question="Nem sempre os números indicam uma quantidade precisa. Assinale a frase em que há precisão.",
        options={
            "A": "Os especialistas em contagem de público dizem que havia mais de um milhão de pessoas na passeata.",
            "B": "O mesmo motorista envolvido no acidente de ontem já havia passado por três outras ocorrências semelhantes.",
            "C": "Perto de mil veículos passaram pelo pedágio, no mesmo dia, em função do feriado.",
            "D": "O vídeo mostrava cerca de 50 automóveis que estavam parados por causa do desmoronamento.",
        }, correct="B",
        explanation="“Mais de um milhão”, “perto de mil” e “cerca de 50” são expressões aproximativas. Só “três outras ocorrências” apresenta uma quantidade exata e precisa."),

    dict(number=2, topic="lingua_portuguesa",
        question="Observe o texto de Bertrand Russell: “A matemática, vista corretamente, possui não apenas verdade, mas também suprema beleza – uma beleza fria e austera, como a da escultura.” Assinale a opção que mostra uma afirmação correta sobre o texto.",
        options={
            "A": "A frase mostra simultaneamente aspectos positivos e negativos da matemática.",
            "B": "O emprego da expressão “não apenas verdade” abre a possibilidade de dizer-se “mas suprema beleza”.",
            "C": "A expressão “uma beleza fria e austera” nega a afirmação anterior de que a matemática possui suprema beleza.",
            "D": "Ao afirmar que a beleza da matemática é como a da escultura, a frase desvaloriza a escultura.",
        }, correct="B",
        explanation="A estrutura correlativa “não apenas X, mas também Y” prepara e justifica a continuação “mas também suprema beleza” — não há contradição nem desvalorização em nenhum dos dois termos comparados."),

    dict(number=3, topic="estatistica_probabilidade",
        question="O faturamento diário de uma rede varejista segue distribuição normal com média R$ 40.000,00. A probabilidade de que, em um dia aleatório, o faturamento esteja entre R$ 38.000,00 e R$ 42.000,00 é de 52%. Qual a probabilidade de o faturamento diário ser inferior a R$ 38.000,00?",
        options={"A": "24%.", "B": "26%.", "C": "48%.", "D": "76%."}, correct="A",
        explanation="R$ 38.000 e R$ 42.000 são simétricos em torno da média (± R$ 2.000). Os 48% restantes da curva se dividem igualmente nas duas caudas: 48% ÷ 2 = 24% abaixo de R$ 38.000."),

    dict(number=4, topic="matematica_financeira",
        question="Uma empresa financiou R$ 240.000,00 para pagar em 30 parcelas mensais pela Tabela SAC, com juros de 4% ao mês. Qual o valor do quinto pagamento?",
        options={"A": "R$ 8.320,00.", "B": "R$ 16.000,00.", "C": "R$ 16.320,00.", "D": "R$ 17.600,00."}, correct="C",
        explanation="Amortização constante = 240.000/30 = R$ 8.000. Antes do 5º pagamento já foram amortizadas 4 parcelas, saldo = 240.000 − 4×8.000 = R$ 208.000. Juros = 208.000×4% = R$ 8.320. Pagamento = 8.000+8.320 = R$ 16.320."),

    dict(number=5, topic="licitacoes_concessoes",
        question="Um órgão público federal deseja aderir a atas de registro de preços gerenciadas por um Município e por um Estado, sem ter participado da licitação original. Segundo a Lei nº 14.133/2021, esse órgão federal",
        options={
            "A": "não poderá aderir, salvo se houver concordância expressa dos entes federativos.",
            "B": "poderá aderir somente à ata do Estado, não à do Município.",
            "C": "poderá aderir somente à ata do Município, não à do Estado.",
            "D": "não poderá aderir às atas geridas pelo Município e pelo Estado.",
        }, correct="D",
        explanation="A Lei nº 14.133/2021 restringiu a adesão (“carona”) a atas de registro de preços entre entes de esferas federativas distintas — órgão federal não pode aderir a ata gerida por Município ou Estado."),

    dict(number=6, topic="licitacoes_concessoes",
        question="Durante a execução de um contrato administrativo, a Administração Pública identifica necessidade de melhor adequá-lo às finalidades de interesse público. Segundo a Lei nº 14.133/2021, a Administração",
        options={
            "A": "não poderá modificar o contrato, que é lei entre as partes.",
            "B": "poderá modificar o contrato apenas com concordância expressa ou tácita do contratado.",
            "C": "poderá modificar unilateralmente o contrato, respeitados os direitos do contratado.",
            "D": "não poderá modificar o contrato, salvo autorização judicial.",
        }, correct="C",
        explanation="As cláusulas exorbitantes autorizam a Administração a modificar unilateralmente os contratos administrativos por razões de interesse público, preservado o equilíbrio econômico-financeiro e os demais direitos do contratado."),

    dict(number=7, topic="licitacoes_concessoes",
        question="Uma sociedade empresária, concessionária de serviços públicos no Município Beta, deparou-se com a necessidade, em um sábado, de proceder à interrupção do serviço prestado à coletividade residente e domiciliada no bairro Gama, sem aviso prévio, em razão de situação de emergência constatada na localidade. Nesse cenário, considerando as disposições da Lei nº 8.987/1995, é correto afirmar que",
        options={
            "A": "não se está diante de hipótese de descontinuidade do serviço, pois a interrupção, em caso de emergência ou motivada por razões de ordem técnica, independe de aviso prévio.",
            "B": "não se está diante de hipótese de descontinuidade do serviço, pois a interrupção ocorreu em situação de emergência, dispensando aviso prévio.",
            "C": "se está diante de hipótese de descontinuidade do serviço, pois a interrupção, ainda que em situação de emergência, não pode se iniciar no final de semana.",
            "D": "se está diante de hipótese de descontinuidade do serviço, pois a interrupção, ainda que em situação de emergência, pressupõe aviso prévio.",
        }, correct="B",
        explanation="O art. 6º, §3º, da Lei nº 8.987/1995 dispensa o aviso prévio quando a interrupção decorre de emergência. A opção B é a mais precisa porque aplica essa regra diretamente ao caso concreto descrito (interrupção que de fato ocorreu em situação de emergência), e não apenas enuncia a regra geral de forma abstrata como a opção A."),

    dict(number=8, topic="etica_profissional",
        question="Uma firma de auditoria, após emitir relatório de asseguração sobre informações financeiras de uma entidade, aceita, no mesmo exercício, assumir decisões administrativas relacionadas à elaboração dessas mesmas informações. Conforme a NBC PG 01 e a NBC PG 100 (R1), essa conduta",
        options={
            "A": "é aceitável se houver confiança mútua entre auditor e administração.",
            "B": "é aceitável quando não houver impacto financeiro relevante.",
            "C": "é aceitável desde que a firma revise tecnicamente seu próprio trabalho depois.",
            "D": "não é aceitável, pois gera ameaça de autorrevisão e compromete a independência.",
        }, correct="D",
        explanation="Assumir responsabilidade de gestão da entidade auditada compromete a independência do auditor (ameaça de autorrevisão/familiaridade), ferindo o interesse público que fundamenta a profissão contábil."),

    dict(number=9, topic="etica_profissional",
        question="O contador de uma empresa é pressionado pela administração a postergar o reconhecimento de uma despesa relevante para melhorar artificialmente o resultado do período. Conforme a NBC PG 01, a conduta profissional adequada é",
        options={
            "A": "atender à solicitação, desde que sem impacto tributário relevante.",
            "B": "ajustar temporariamente o resultado, se a administração assumir a responsabilidade por escrito.",
            "C": "negociar a postergação da despesa para o exercício seguinte.",
            "D": "manter a escrituração conforme as normas contábeis, mesmo sob pressão.",
        }, correct="D",
        explanation="O Código de Ética exige integridade e objetividade do contador, que deve resistir a pressões da administração e manter a escrituração de acordo com as normas contábeis vigentes, independentemente de conveniências gerenciais."),

    dict(number=10, topic="estrutura_conceitual",
        question="Uma empresa sabia que a inadimplência real estava próxima de 5%, mas manteve a estimativa anterior de 2% porque os administradores são avaliados pelo resultado operacional. Essa informação contábil pode ser considerada representação fidedigna?",
        options={
            "A": "Pode ser, pois é comparável.", "B": "Pode ser, pois é tempestiva.",
            "C": "Não pode ser, pois não é neutra.", "D": "Não pode ser, pois não é verificável.",
        }, correct="C",
        explanation="Manter deliberadamente uma estimativa que se sabe desatualizada, para beneficiar o resultado apresentado, introduz viés — fere a neutralidade, um dos componentes da representação fidedigna na Estrutura Conceitual."),

    dict(number=11, topic="normas_contabeis",
        question="Uma máquina foi comprada em janeiro/2026 (contrato), paga em fevereiro, recebida e instalada em março (disponível para uso), mas só começou a ser efetivamente usada em abril. A partir de quando a máquina deve ser reconhecida no Balanço Patrimonial?",
        options={"A": "Janeiro.", "B": "Fevereiro.", "C": "Março.", "D": "Abril."}, correct="C",
        explanation="O reconhecimento do ativo ocorre quando a entidade obtém o controle do bem e ele está disponível para uso nas condições pretendidas pela administração — isso se dá em março, independentemente de o uso efetivo só começar em abril."),

    dict(number=13, topic="estrutura_conceitual",
        question="De acordo com a NBC TG Estrutura Conceitual (R2), ativo é um recurso econômico presente controlado pela entidade em decorrência de eventos passados. Um recurso econômico representa",
        options={
            "A": "um bem ou direito que pertence à entidade.",
            "B": "uma obrigação de transferir benefícios econômicos.",
            "C": "um direito que tem o potencial de produzir benefícios econômicos.",
            "D": "uma obrigação que resulta em aumento no patrimônio líquido.",
        }, correct="C",
        explanation="A Estrutura Conceitual (R2) define recurso econômico como um direito que tem o potencial de produzir benefícios econômicos — o foco está no potencial de gerar benefícios, não na propriedade jurídica do bem em si."),

    dict(number=14, topic="normas_contabeis",
        question="Sobre a contabilização de um contrato de arrendamento mercantil de uma máquina entre a arrendatária ABC e a arrendadora XYZ, conforme a NBC TG 06 (R3), é correto afirmar que",
        options={
            "A": "o ativo de direito de uso é mensurado inicialmente pelo valor justo da máquina e depois pelo valor contábil de máquinas similares da ABC.",
            "B": "se a ABC não pretende ficar com a máquina ao final do contrato, a vida útil para depreciação é a menor entre o prazo do arrendamento e a vida útil da máquina.",
            "C": "o reconhecimento do direito de uso pela ABC obriga a baixa do imobilizado pela XYZ.",
            "D": "a depreciação do direito de uso na ABC tem como contrapartida o passivo de arrendamento reconhecido pela XYZ.",
        }, correct="B",
        explanation="Quando não há expectativa de transferência de propriedade ao final do contrato, a arrendatária deve depreciar o ativo de direito de uso pelo menor prazo entre a duração do arrendamento e a vida útil do bem."),

    dict(number=15, topic="normas_contabeis",
        question="Uma empresa possui os segmentos “Cervejas” (12% da receita combinada) e “Refrigerantes” (9% da receita, mas 11% dos ativos combinados). Ambos são revisados regularmente pelo CODM. Conforme a NBC TG 22 (R2), sobre a divulgação por segmento é correto afirmar que",
        options={
            "A": "apenas Cervejas deve ser divulgado, pois só ele ultrapassa 10% da receita.",
            "B": "apenas Refrigerantes deve ser divulgado, pois o critério de ativos já é suficiente.",
            "C": "ambos devem ser divulgados, pois cada um atende a pelo menos um critério quantitativo de 10%.",
            "D": "nenhum deve ser divulgado, pois é preciso atender simultaneamente aos critérios de receita, resultado e ativos.",
        }, correct="C",
        explanation="Basta que um segmento ultrapasse UM dos limiares de 10% (receita, resultado OU ativos) para ser reportável. Cervejas atinge o limiar de receita e Refrigerantes o de ativos — ambos devem ser divulgados separadamente."),

    dict(number=16, topic="normas_contabeis",
        question="Uma empresa reconheceu ativos fiscais diferidos relevantes decorrentes de prejuízos fiscais, sustentados por projeções de lucros tributáveis futuros elaboradas pela administração. Conforme a NBC TG 32 (R4), o reconhecimento desses ativos é adequado somente quando",
        options={
            "A": "houver qualquer projeção de lucro futuro, independentemente de sua probabilidade.",
            "B": "for provável a existência de lucro tributável futuro suficiente para a compensação.",
            "C": "existirem prejuízos fiscais acumulados, o que por si só já garante o reconhecimento.",
            "D": "o auditor não fizer ressalva alguma sobre o tema em seu relatório.",
        }, correct="B",
        explanation="A NBC TG 32 exige que o reconhecimento do ativo fiscal diferido esteja condicionado à probabilidade de geração de lucro tributável futuro suficiente para absorver os prejuízos fiscais — mera projeção não sustentada por essa probabilidade não basta."),

    dict(number=17, topic="normas_contabeis",
        question="Um cliente compra um livro on-line, paga via PIX e recebe a nota fiscal na hora. A mercadoria é despachada pela própria transportadora da loja e, antes da entrega, o caminhão sofre acidente e destrói a carga. Conforme a NBC TG 47, a receita dessa venda deve ser reconhecida",
        options={
            "A": "no momento do pagamento via PIX.",
            "B": "no momento do despacho da mercadoria pelo centro de distribuição.",
            "C": "quando o livro for efetivamente entregue ao cliente; a perda antes disso é da própria companhia.",
            "D": "no momento da emissão da nota fiscal eletrônica.",
        }, correct="C",
        explanation="A receita só é reconhecida quando o controle do bem é transferido ao cliente — na entrega. Como o acidente ocorreu antes da entrega, o controle ainda era da companhia, que deve arcar com a perda."),

    dict(number=18, topic="normas_contabeis",
        question="Uma empresa gastou R$ 10.000,00 na obtenção de novo conhecimento, R$ 15.000,00 na formulação e seleção final de alternativas de materiais e processos, e R$ 20.000,00 no projeto, construção e teste de protótipos — todos os requisitos da fase de desenvolvimento da NBC TG 04 (R4) estavam presentes. Vida útil do ativo intangível: 10 anos, valor residual zero, amortização pela linha reta. Qual a despesa de amortização anual?",
        options={"A": "R$ 0,00.", "B": "R$ 2.000,00.", "C": "R$ 3.500,00.", "D": "R$ 4.500,00."}, correct="B",
        explanation="A NBC TG 04 classifica “obtenção de novo conhecimento” e “formulação, avaliação e seleção final de alternativas” como fase de PESQUISA (sempre despesa do período). Só “projeto, construção e teste de protótipos” (R$ 20.000) é fase de desenvolvimento, capitalizável. Amortização anual = 20.000/10 = R$ 2.000."),

    dict(number=19, topic="normas_contabeis",
        question="Um prédio (custo R$ 500.000,00, vida útil 20 anos, valor residual R$ 100.000,00) foi classificado como mantido para venda após 5 anos de uso (05/01/2025). Um ano depois (05/01/2026), a empresa desistiu da venda e reclassificou o prédio como imobilizado. Em 05/01/2026: valor justo R$ 450.000,00, despesas de venda R$ 45.000,00, valor em uso R$ 420.000,00. Pela NBC TG 31 (R4), por qual valor o prédio deve ser reclassificado no imobilizado?",
        options={"A": "R$ 380.000,00.", "B": "R$ 405.000,00.", "C": "R$ 420.000,00.", "D": "R$ 450.000,00."}, correct="A",
        explanation="Reclassifica-se pelo MENOR valor entre: (i) o valor contábil que o ativo teria se nunca tivesse sido classificado como mantido para venda (500.000 − 100.000 depreciação acumulada de 5 anos = 400.000; menos mais 1 ano de depreciação de 20.000 = 380.000); e (ii) o valor recuperável em 05/01/2026 (maior entre 450.000−45.000=405.000 e 420.000, ou seja 420.000). O menor entre 380.000 e 420.000 é R$ 380.000,00."),

    dict(number=20, topic="normas_contabeis",
        question="Uma enchente inutilizou 25% dos estoques de uma metalúrgica. Qual o tratamento contábil correto dessa perda?",
        options={
            "A": "Custo da Mercadoria Vendida (CMV), pois reduz o volume disponível para venda.",
            "B": "Despesa operacional, sem baixa do saldo de estoques.",
            "C": "Custo normal das operações, diluído entre as unidades produzidas.",
            "D": "Despesa (perda por sinistro), com a correspondente baixa no saldo de estoques.",
        }, correct="D",
        explanation="Perdas anormais/involuntárias de estoque (sinistros) não são custo do produto — devem ser reconhecidas diretamente como despesa do período, com a baixa correspondente no saldo de estoques, já que não há expectativa de recuperação econômica."),

    dict(number=21, topic="normas_contabeis",
        question="Uma concessionária emitiu faturas a prazo de R$ 100.000,00, vencíveis em 12 meses, com ajuste a valor presente de R$ 5.000,00 (NBC TG 12 – R1). Qual o lançamento correto no reconhecimento da receita?",
        options={
            "A": "Débito Clientes 100.000; Crédito Receita de Serviços 100.000.",
            "B": "Débito Clientes 95.000; Crédito Receita Financeira a Apropriar 5.000; Crédito Receita de Serviços 100.000.",
            "C": "Débito Clientes 95.000; Débito Juros a Apropriar 5.000; Crédito Receita de Serviços 100.000.",
            "D": "Débito Clientes 100.000; Crédito Receita de Serviços 95.000; Crédito Juros a Apropriar 5.000.",
        }, correct="D",
        explanation="Clientes é debitado pelo valor nominal (100.000); a receita é reconhecida pelo valor presente (95.000); a diferença (5.000) vai para uma conta retificadora do ativo (“Juros/Receita Financeira a Apropriar”), a crédito, para ser apropriada como receita financeira ao longo do prazo."),

    dict(number=22, topic="lancamentos_contabeis",
        question="Uma empresa apresenta os saldos:\n• Adiantamento a fornecedor: R$ 12.000,00\n• Adiantamento de clientes: R$ 8.000,00\n• Encargos financeiros a transcorrer (sobre empréstimos): R$ 3.500,00\n• Ações próprias em tesouraria: R$ 5.000,00\n• Juros sobre capital próprio a pagar: R$ 4.500,00\n• Perdas estimadas com créditos de liquidação duvidosa: R$ 2.000,00\nQual o somatório, em valores absolutos, das contas de natureza devedora?",
        options={"A": "R$ 20.500,00.", "B": "R$ 15.500,00.", "C": "R$ 12.000,00.", "D": "R$ 20.000,00."}, correct="A",
        explanation="Natureza devedora: Adiantamento a fornecedor (12.000, ativo) + Encargos financeiros a transcorrer (3.500, retificadora de passivo) + Ações em tesouraria (5.000, retificadora do PL) = 20.500. Adiantamento de clientes e Juros sobre capital próprio a pagar são passivos (credoras); a PECLD é retificadora do ativo, portanto credora."),

    dict(number=23, topic="lancamentos_contabeis",
        question="A empresa Alfa possui 70% de participação em Beta, avaliada por equivalência patrimonial. Beta apurou lucro líquido de R$ 1.000.000,00, sendo R$ 800.000,00 destinados a reservas e R$ 200.000,00 a dividendos. Qual o ganho de equivalência patrimonial a ser reconhecido por Alfa?",
        options={"A": "R$ 140.000,00.", "B": "R$ 560.000,00.", "C": "R$ 700.000,00.", "D": "R$ 3.500.000,00."}, correct="C",
        explanation="A equivalência patrimonial incide sobre o lucro líquido total do período, independentemente da destinação (reservas ou dividendos): 70% × 1.000.000 = R$ 700.000,00."),

    dict(number=24, topic="normas_contabeis",
        question="Na Demonstração do Valor Adicionado (NBC TG 09 – R1), uma empresa apresenta:\n• Despesas financeiras: R$ 35.000,00\n• Assistência médica a empregados: R$ 80.000,00\n• Aluguel: R$ 120.000,00\n• Remuneração direta de empregados: R$ 240.000,00\nQual o saldo de “Remuneração de Capitais de Terceiros”?",
        options={"A": "R$ 155.000,00.", "B": "R$ 235.000,00.", "C": "R$ 320.000,00.", "D": "R$ 475.000,00."}, correct="A",
        explanation="“Remuneração de Capitais de Terceiros” reúne despesas financeiras e aluguéis: 35.000 + 120.000 = R$ 155.000,00. Assistência médica e remuneração direta pertencem ao grupo “Pessoal”, não a capitais de terceiros."),

    dict(number=25, topic="lancamentos_contabeis",
        question="Uma empresa vendeu mercadorias por R$ 250.000,00, com controle transferido de imediato: 50% recebido em Caixa, 25% em Banco, 25% a prazo (30 dias). Qual o lançamento correto?",
        options={
            "A": "Débito Caixa 125.000; Débito Banco 62.500; Débito Duplicatas a Receber 62.500; Crédito Receita de Vendas 250.000.",
            "B": "Débito Caixa 125.000; Débito Duplicatas a Receber 125.000; Crédito Receita de Vendas 250.000.",
            "C": "Débito Caixa 250.000; Crédito Receita de Vendas 250.000.",
            "D": "Débito Caixa 125.000; Débito Banco 125.000; Crédito Receita de Vendas 250.000.",
        }, correct="A",
        explanation="50% de 250.000 = 125.000 em Caixa; 25% = 62.500 em Banco; 25% = 62.500 em Duplicatas a Receber (a prazo); tudo creditado em Receita de Vendas, totalizando 250.000."),

    dict(number=26, topic="lancamentos_contabeis",
        question="Uma empresa de serviços apresenta: Receita bruta R$ 1.500.000,00; Impostos sobre serviços R$ 40.000,00; Descontos incondicionais R$ 30.000,00; Custo dos serviços prestados R$ 400.000,00; Despesas operacionais R$ 20.000,00; Despesas com tributos sobre o lucro R$ 510.000,00. Qual o resultado apurado?",
        options={
            "A": "Um lucro bruto de R$ 1.050.000,00.", "B": "Uma receita líquida de R$ 1.030.000,00.",
            "C": "Um lucro bruto de R$ 1.010.000,00.", "D": "Um lucro líquido de R$ 500.000,00.",
        }, correct="D",
        explanation="Receita líquida = 1.500.000−40.000−30.000 = 1.430.000. Lucro bruto = 1.430.000−400.000 = 1.030.000. Resultado antes dos tributos = 1.030.000−20.000 = 1.010.000. Lucro líquido = 1.010.000−510.000 = R$ 500.000,00."),

    dict(number=27, topic="lancamentos_contabeis",
        question="Compra de mercadoria à vista: valor unitário R$ 200,00, 1.000 unidades; imposto de importação R$ 10,00/unidade (por fora, não recuperável); seguro R$ 6.000,00; transporte R$ 4.000,00; ICMS R$ 20,00/unidade (embutido, não recuperável); desconto comercial R$ 15,00/unidade. Qual o custo total do estoque adquirido?",
        options={"A": "R$ 205.000,00.", "B": "R$ 210.000,00.", "C": "R$ 220.000,00.", "D": "R$ 235.000,00."}, correct="A",
        explanation="200.000 (1.000×200, ICMS já embutido e não recuperável, permanece no custo) − 15.000 (desconto comercial) + 10.000 (imposto de importação, não recuperável) + 6.000 (seguro) + 4.000 (transporte) = R$ 205.000,00."),

    dict(number=28, topic="normas_contabeis",
        question="Uma construtora foi processada e os advogados avaliaram a chance de perda da causa como “possível” (não provável), com pedido de indenização de R$ 200.000,00. Conforme a NBC TG 25 (R2), qual o impacto no Balanço Patrimonial em 31/12/2025?",
        options={
            "A": "Provisão para contingências de R$ 200.000,00.", "B": "Provisão para contingências de R$ 500.000,00.",
            "C": "Provisão para contingências de R$ 700.000,00.", "D": "Não houve impacto nos elementos patrimoniais.",
        }, correct="D",
        explanation="Provisões só são reconhecidas quando a perda é PROVÁVEL. Sendo a chance apenas “possível”, cabe apenas divulgação em nota explicativa (passivo contingente) — sem registro de provisão nas contas patrimoniais."),

    dict(number=29, topic="normas_contabeis",
        question="Uma empresa passou a apresentar a Demonstração dos Fluxos de Caixa pelo método indireto (antes usava o direto) e republicou o ano anterior para fins comparativos. Ao comparar o saldo de caixa gerado pelas três atividades (operacional, investimento e financiamento) nos dois métodos, verifica-se que",
        options={
            "A": "o saldo de caixa gerado pelas três atividades permanece igual.",
            "B": "o saldo de caixa das três atividades apresenta mudança.",
            "C": "apenas o saldo da atividade operacional apresenta mudança.",
            "D": "apenas o saldo da atividade de financiamento apresenta mudança.",
        }, correct="A",
        explanation="Os métodos direto e indireto diferem apenas na FORMA de apresentar o fluxo das atividades operacionais; o valor total (saldo) gerado por cada uma das três atividades é sempre o mesmo, qualquer que seja o método escolhido."),

    dict(number=30, topic="normas_contabeis",
        question="Sobre influência significativa (NBC TG 18 – R4), analise as afirmativas:\nI. Presume-se influência significativa com 20% ou mais do poder de voto, salvo prova em contrário.\nII. Com menos de 20%, jamais se pode supor influência significativa.\nIII. Representação no Conselho de Administração da investida pode evidenciar influência significativa.\nEstá correto o que se afirma em",
        options={"A": "I, apenas.", "B": "II e III, apenas.", "C": "I, II e III.", "D": "I e III, apenas."}, correct="D",
        explanation="I e III são corretas pela NBC TG 18. II é falsa: mesmo com participação abaixo de 20%, influência significativa pode existir por outras evidências (como representação no conselho), não sendo uma impossibilidade absoluta."),

    dict(number=31, topic="normas_contabeis",
        question="Um ativo tem custo de aquisição R$ 105.000,00, depreciação acumulada R$ 20.000,00 e perda por redução ao valor recuperável já reconhecida em período anterior de R$ 10.000,00. No teste de recuperabilidade atual: valor justo líquido de despesas de venda R$ 80.000,00; valor em uso R$ 90.000,00. É correto afirmar que",
        options={
            "A": "o valor contábil líquido do ativo, antes do ajuste, é R$ 85.000,00.",
            "B": "o valor recuperável do ativo é R$ 80.000,00.",
            "C": "o valor recuperável do ativo é R$ 90.000,00.",
            "D": "a perda estimada para esse ativo é de R$ 25.000,00.",
        }, correct="C",
        explanation="Valor contábil líquido atual = 105.000−20.000−10.000 = 75.000 (não 85.000). Valor recuperável = maior entre valor justo líquido de venda (80.000) e valor em uso (90.000) = R$ 90.000,00, que é maior que o valor contábil — logo não há nova perda."),

    dict(number=32, topic="normas_contabeis",
        question="Uma loja usa Custo Médio Ponderado móvel diário. Sem estoque inicial: 02/07 compra 20un a R$ 3.000; 10/07 vende 10un; 15/07 compra 15un a R$ 3.200; 20/07 vende 8un; 27/07 vende 5un. Qual o valor do estoque final em 31/07?",
        options={"A": "R$ 36.988,00.", "B": "R$ 37.200,00.", "C": "R$ 37.440,00.", "D": "R$ 61.200,00."}, correct="C",
        explanation="02/07: 20un a 3.000 (total 60.000). 10/07: vende 10, restam 10un a 3.000 (30.000). 15/07: compra 15 a 3.200 (48.000); total 25un = 78.000, média 3.120/un. 20/07: vende 8, restam 17un = 53.040. 27/07: vende 5, restam 12un × 3.120 = R$ 37.440,00."),

    dict(number=33, topic="normas_contabeis",
        question="Cia X (Disponibilidades R$ 80.000,00, PL R$ 80.000,00) adquire 90% da Cia Y (Disponibilidades R$ 40.000,00, PL R$ 40.000,00) por R$ 42.000,00 à vista, com os valores contábeis correspondendo aos valores justos. Qual o saldo do Ativo Circulante (Disponibilidades) no Balanço Consolidado após a compra?",
        options={"A": "R$ 38.000,00.", "B": "R$ 74.000,00.", "C": "R$ 75.800,00.", "D": "R$ 78.000,00."}, correct="D",
        explanation="Disponibilidades de X após o pagamento: 80.000−42.000 = 38.000. Na consolidação, soma-se 100% das disponibilidades de Y (mesmo com 90% de participação, a subsidiária é consolidada integralmente): 38.000+40.000 = R$ 78.000,00."),

    dict(number=34, topic="normas_contabeis",
        question="Uma empresa pagou R$ 20.000,00 de juros sobre empréstimo bancário. Conforme a NBC TG 03 (R3), os juros pagos podem ser classificados, na Demonstração dos Fluxos de Caixa, como fluxos de caixa",
        options={
            "A": "operacionais ou de investimento.", "B": "operacionais ou de financiamento.",
            "C": "de investimento ou de financiamento.", "D": "de financiamento ou de equivalentes de caixa.",
        }, correct="B",
        explanation="A NBC TG 03 permite classificar os juros pagos como atividade operacional (por afetarem o resultado) ou como atividade de financiamento (por serem o custo de obtenção de recursos financeiros)."),

    dict(number=35, topic="custos",
        question="Uma fábrica de violinos vende cada unidade por R$ 2.000,00. Produziu 1.200 e vendeu 900 unidades. Custo variável: R$ 600,00/violino. Custos fixos mensais de fábrica: supervisores R$ 150.000,00, depreciação de máquinas R$ 39.800,00, aluguel da fábrica R$ 15.000,00, custos diversos de manufatura R$ 10.000,00. (Administrativo e propaganda não entram no custo fabril.) Pelo custeio por absorção, qual o Lucro Bruto?",
        options={"A": "R$ 1.061.397,00.", "B": "R$ 1.465.200,00.", "C": "R$ 1.045.200,00.", "D": "R$ 1.098.900,00."}, correct="D",
        explanation="Custos fixos de fábrica = 150.000+39.800+15.000+10.000 = 214.800. Custo variável total (produção) = 600×1.200 = 720.000. Custo total de produção = 934.800 ÷ 1.200 = R$ 779,00/un. CMV (900un) = 701.100. Receita = 900×2.000 = 1.800.000. Lucro Bruto = 1.800.000−701.100 = R$ 1.098.900,00."),

    dict(number=36, topic="custos",
        question="Uma indústria tem os setores Montagem (30 m²) e Acabamento (50 m²). O custo de energia elétrica da produção foi R$ 25.000,00, rateado por área ocupada. Qual o valor alocado ao setor de Montagem?",
        options={"A": "R$ 15.625,00.", "B": "R$ 9.375,00.", "C": "R$ 12.500,00.", "D": "R$ 10.000,00."}, correct="B",
        explanation="Área total = 30+50 = 80 m². Montagem = 30/80 × 25.000 = R$ 9.375,00."),

    dict(number=37, topic="custos",
        question="Uma indústria registrou:\n• Consumo de matéria-prima X: R$ 17.900,00\n• Depreciação do prédio do escritório: R$ 6.600,00\n• Compra de matéria-prima X: R$ 100.000,00\n• Depreciação de máquinas do parque fabril: R$ 8.500,00\n• Salários do setor de Faturamento: R$ 23.000,00\n• Aquisição de máquina para o parque fabril: R$ 149.000,00\nQuais os valores corretos de Custos, Despesas e Investimentos?",
        options={
            "A": "Custos: R$ 126.400,00; Despesas: R$ 29.600,00; Investimentos: R$ 149.000,00.",
            "B": "Custos: R$ 26.400,00; Despesas: R$ 29.600,00; Investimentos: R$ 249.000,00.",
            "C": "Custos: R$ 26.400,00; Despesas: R$ 52.600,00; Investimentos: R$ 149.000,00.",
            "D": "Custos: R$ 35.100,00; Despesas: R$ 29.600,00; Investimentos: R$ 228.000,00.",
        }, correct="B",
        explanation="Custos (ligados à produção): consumo de matéria-prima (17.900) + depreciação de máquinas fabris (8.500) = 26.400. Despesas (administrativas/comerciais): depreciação do escritório (6.600) + salários do Faturamento (23.000) = 29.600. Investimentos (gastos ativados): compra de matéria-prima ainda em estoque (100.000) + aquisição da máquina (149.000) = 249.000."),

    dict(number=38, topic="custos",
        question="Uma indústria apurou o Custo Padrão e o Custo Real (totais) de seus insumos:\n• Tensoativos: padrão R$ 135,00 / real R$ 247,50\n• Óleo de Argan: padrão R$ 39,30 / real R$ 49,30\n• Estabilizantes de espuma: padrão R$ 38,25 / real R$ 14,03\n• Espessantes: padrão R$ 5,60 / real R$ 14,00\nEm relação às variações de custo, é correto afirmar que",
        options={
            "A": "o Óleo de Argan apresentou variações favoráveis.",
            "B": "os Estabilizantes de espuma apresentam variações favoráveis.",
            "C": "as variações de Estabilizantes de espuma e Espessantes são desfavoráveis.",
            "D": "as variações de Tensoativos e Óleo de Argan são favoráveis.",
        }, correct="B",
        explanation="Variação favorável ocorre quando o custo real é MENOR que o padrão. Só os Estabilizantes de espuma tiveram custo real (14,03) menor que o padrão (38,25) — uma variação favorável. Os demais itens tiveram custo real maior que o padrão (desfavoráveis)."),

    dict(number=39, topic="custos",
        question="Uma empresa compra matéria-prima a prazo (pagamento em 20 dias), leva 70 dias para fabricar/armazenar/vender, e vende a prazo, recebendo em média em 80 dias. Qual o ciclo operacional dessa empresa?",
        options={"A": "70 dias.", "B": "90 dias.", "C": "150 dias.", "D": "160 dias."}, correct="C",
        explanation="Ciclo operacional = tempo de produção/armazenagem/venda + prazo médio de recebimento = 70+80 = 150 dias. O prazo de pagamento a fornecedores (20 dias) não integra o ciclo operacional — ele compõe o ciclo financeiro."),

    dict(number=40, topic="custos",
        question="Uma joalheria vende relógios a R$ 300,00 (custo variável R$ 170,00), com ponto de equilíbrio de 500 unidades. O preço sobe para R$ 330,00, mantidos os custos fixos e variáveis. Qual o novo ponto de equilíbrio?",
        options={"A": "407 unidades.", "B": "455 unidades.", "C": "475 unidades.", "D": "550 unidades."}, correct="A",
        explanation="Margem de contribuição original = 300−170 = 130/un. Custo fixo = 500×130 = 65.000. Nova margem = 330−170 = 160/un. Novo ponto de equilíbrio = 65.000/160 = 406,25 ≈ 407 unidades."),

    dict(number=41, topic="indicadores_financeiros",
        question="Uma empresa projeta, para o exercício seguinte:\n• Receitas com vendas a prazo: R$ 250.000,00 (prazo médio de recebimento: 38 dias)\n• Custo dos produtos vendidos: R$ 110.000,00 (prazo médio de estoque: 32 dias)\n• Aquisição de matéria-prima a prazo: R$ 90.000,00 (prazo médio de pagamento: 34 dias)\n• Demais despesas operacionais: R$ 30.000,00 (prazo médio de pagamento: 22 dias)\nConsiderando um ano de 365 dias, qual a Necessidade de Capital de Giro (NCG) dessa empresa?",
        options={"A": "R$ 25.479,00.", "B": "R$ 26.027,00.", "C": "R$ 27.287,00.", "D": "R$ 35.671,00."}, correct="A",
        explanation="Contas a receber = (250.000/365)×38 ≈ 26.027. Estoques = (110.000/365)×32 ≈ 9.644. Ativo Circulante Operacional ≈ 35.671. Contas a pagar = (90.000/365)×34 ≈ 8.384. Demais despesas a pagar = (30.000/365)×22 ≈ 1.808. Passivo Circulante Operacional ≈ 10.192. NCG = 35.671−10.192 ≈ R$ 25.479,00."),

    dict(number=43, topic="setor_publico",
        question="À luz do MCASP, sobre o reconhecimento e a mensuração de ativos da concessão de serviços públicos, avalie as afirmativas:\nI. A mensuração inicial dos ativos da concessão deve ser realizada pelo menor valor entre o custo histórico e o valor recuperável.\nII. Quando o concedente não controla nem regula os serviços objeto da concessão, o ativo da concessão não deve ser por ele reconhecido.\nIII. Os ativos da concessão devem ser classificados como intangível, sem necessidade de segregação em classes.\nIV. Os ativos da concessão estão sujeitos a depreciação, reavaliação e redução a valor recuperável, como os demais itens do imobilizado.\nEstão corretas apenas as afirmativas",
        options={"A": "I e IV.", "B": "III e IV.", "C": "II e III.", "D": "II e IV."}, correct="D",
        explanation="I é falsa (a mensuração inicial é pelo valor justo, não pelo menor entre custo histórico e valor recuperável). III é falsa (há necessidade de segregação em classes, como nos demais itens do imobilizado). II e IV estão corretas."),

    dict(number=44, topic="setor_publico",
        question="Um governo estadual incluiu na LOA receitas de um novo tributo cuja criação ainda dependia de aprovação legislativa e regulamentação. Essa prática viola, principalmente, o princípio orçamentário da",
        options={"A": "universalidade.", "B": "exclusividade.", "C": "legalidade.", "D": "anualidade."}, correct="C",
        explanation="Só se pode orçar receita cuja base legal já exista (tributo efetivamente instituído e regulamentado). Prever receita de tributo ainda não aprovado fere o princípio da legalidade."),

    dict(number=45, topic="setor_publico",
        question="Um empenho formalizado foi anulado parcialmente. Qual o motivo mais provável para essa anulação parcial?",
        options={
            "A": "O objeto do contrato não foi cumprido.", "B": "A nota de empenho foi emitida de modo incorreto.",
            "C": "O valor do empenho excedia o montante da despesa realizada.", "D": "O valor empenhado era insuficiente para a despesa realizada.",
        }, correct="C",
        explanation="A anulação parcial de empenho ocorre tipicamente quando o valor reservado é maior do que o efetivamente necessário para a despesa realizada — o excedente é anulado e liberado."),

    dict(number=46, topic="etica_profissional",
        question="Em uma organização contábil, o contador definiu diretrizes gerais de longo prazo; os gestores desdobraram essas diretrizes em metas por setor; e a equipe executou as rotinas diárias.\nAssocie os tipos de planejamento às suas descrições:\n1. Planejamento estratégico\n2. Planejamento tático\n3. Planejamento operacional\nI. Execução das rotinas diárias\nII. Definição de diretrizes gerais de longo prazo\nIII. Desdobramento das diretrizes em metas setoriais\nA correspondência correta é",
        options={"A": "1–III; 2–II; 3–I.", "B": "1–I; 2–III; 3–II.", "C": "1–II; 2–I; 3–III.", "D": "1–II; 2–III; 3–I."}, correct="D",
        explanation="Estratégico = diretrizes gerais de longo prazo (II); Tático = desdobramento em metas setoriais (III); Operacional = execução das rotinas diárias (I). Logo: 1–II; 2–III; 3–I."),

    dict(number=47, topic="auditoria",
        question="Mesmo após a execução adequada dos procedimentos de auditoria, pode haver emissão de opinião inadequada sobre as demonstrações contábeis. Esse cenário representa o conceito de",
        options={
            "A": "julgamento técnico do auditor, sujeito a interpretações.",
            "B": "erro natural do processo contábil, sem intenção da administração.",
            "C": "probabilidade de falha nos procedimentos ou controles.",
            "D": "possibilidade de o auditor emitir opinião inadequada quando há distorções relevantes não detectadas.",
        }, correct="D",
        explanation="Risco de auditoria é, por definição, a possibilidade de o auditor expressar uma opinião de auditoria inadequada quando as demonstrações contábeis contêm distorções relevantes que não foram detectadas pelo trabalho de auditoria."),

    dict(number=48, topic="auditoria",
        question="Durante uma auditoria, o auditor identifica vendas fictícias registradas por um funcionário para inflar as receitas — configurando fraude intencional. Diante da gravidade, o auditor deve, imediatamente,",
        options={
            "A": "procurar a ajuda de especialistas.", "B": "renunciar ao trabalho.",
            "C": "fazer denúncia anônima à Polícia Federal.", "D": "relatar ao Conselho de Administração (aos responsáveis pela governança).",
        }, correct="D",
        explanation="Ao identificar fraude, especialmente envolvendo pessoal da entidade, a norma de auditoria exige comunicação tempestiva aos responsáveis pela governança (como o Conselho de Administração), e não medidas unilaterais como denúncia anônima ou renúncia imediata."),

    dict(number=49, topic="direito_pericia",
        question="Um perito contábil recebeu prazo de 30 dias úteis para entregar o laudo, mas, por dificuldades técnicas, solicitou prorrogação ao juiz. De acordo com o CPC/2015, o juiz",
        options={
            "A": "poderá conceder, por uma vez, prorrogação de mais 30 dias úteis, se justificado.",
            "B": "deverá conceder, por uma vez, prorrogação de mais 15 dias úteis, se justificado.",
            "C": "deverá conceder, por uma vez, prorrogação de mais 30 dias úteis, se justificado.",
            "D": "poderá conceder, por uma vez, prorrogação de mais 15 dias úteis, se justificado.",
        }, correct="D",
        explanation="O art. 476 do CPC/2015 prevê que o prazo do perito pode ser prorrogado, por uma vez, por metade do prazo originalmente fixado (30÷2=15 dias úteis), mediante motivo justificado — é uma faculdade do juiz (“poderá”), não uma obrigação."),

    dict(number=50, topic="direito_pericia",
        question="Um empregado trabalhou de 01/03/2021 a 31/03/2023 (salário R$ 3.600,00/mês). Gozou 15 dias de férias; o restante ficou acumulado como férias proporcionais, com adicional de 1/3 (meses de 30 dias). Qual o valor total a pagar pelo saldo de férias proporcionais com o adicional de 1/3?",
        options={"A": "R$ 4.800,00.", "B": "R$ 5.200,00.", "C": "R$ 6.780,00.", "D": "R$ 7.600,00."}, correct="D",
        explanation="Em 25 meses trabalhados: 2 períodos completos (60 dias de férias) + 1 mês do 3º período (2,5 dias, a 2,5 dias/mês) = 62,5 dias de direito. Menos os 15 dias já gozados = 47,5 dias devidos. Salário-dia = 3.600/30 = 120. Com 1/3: 120×4/3 = 160/dia. 47,5×160 = R$ 7.600,00."),
]

assert len(LEVEL1) == 48, len(LEVEL1)

# ============================================================
# LEVEL 2 — real CFC exam questions, from a DIFFERENT exam than
# Level 1: Exame de Suficiência nº 2/2025 (Edital 02/2025), Tipo 1,
# applied 14/09/2025. 48 of the 50 questions; 49 and 50 are
# excluded because they were officially annulled/"anuladas" for
# Tipo 1. Correct letters verified against the official gabarito
# (Contador - 1 - Turno Manhã):
# 1:A 2:B 3:B 4:C 5:C 6:D 7:B 8:D 9:B 10:B 11:D 12:D 13:D 14:B
# 15:C 16:D 17:D 18:D 19:C 20:A 21:A 22:A 23:D 24:A 25:D 26:B
# 27:C 28:B 29:B 30:C 31:A 32:D 33:C 34:A 35:A 36:C 37:D 38:D
# 39:A 40:C 41:B 42:C 43:D 44:C 45:A 46:D 47:C 48:B
# ============================================================

LEVEL2 = [
    dict(number=1, topic="lingua_portuguesa",
        question="Os dicionários registram os diversos significados de um vocábulo; os dois textos abaixo definem o termo “contabilidade”, segundo, respectivamente, os dicionários de Antônio Houaiss (AH) e de Aurélio Buarque de Hollanda (ABH).\n(AH) Contabilidade: ciência teórica e prática que estuda os métodos de cálculo e registro da movimentação financeira de uma firma ou empresa.\n(ABH) Contabilidade: ciência que estuda e interpreta os registros dos fenômenos que afetam o patrimônio de uma entidade (empresa, instituição pública, pessoa física, instituição não lucrativa etc.).\nSobre esses textos, assinale a afirmativa correta.",
        options={
            "A": "As definições começam sempre por uma palavra de conteúdo geral que, nesses casos, é representada pela palavra “ciência”.",
            "B": "Os termos “teórica e prática” e “cálculo e registro” são construídos com palavras antônimas, ou seja, de significados opostos.",
            "C": "Os termos entre parênteses da segunda definição mostram todos os tipos de entidades referidas na definição.",
            "D": "As duas definições mostram o mesmo objetivo da ciência “contabilidade”.",
        }, correct="A",
        explanation="As duas definições começam com a palavra “ciência” — um termo de conteúdo geral (hiperônimo) que classifica a contabilidade antes de especificar suas características. As demais opções contêm erros: “teórica e prática” e “cálculo e registro” são palavras complementares, não antônimas; o “etc.” mostra que a lista não é exaustiva; e as definições enfatizam objetos diferentes (métodos x interpretação dos fenômenos)."),

    dict(number=2, topic="lingua_portuguesa",
        question="As frases listadas nas opções a seguir foram reescritas de forma a eliminar-se o “que”, com substituição do verbo por um substantivo semanticamente correlato.\nAssinale a frase em que a substituição foi feita de forma adequada.",
        options={
            "A": "Cabral, que descobriu o Brasil, merece homenagens. / Cabral, o criador do Brasil, merece homenagens.",
            "B": "Caminha, que escreveu a carta, registrou o fato. / Caminha, o redator da carta, registrou o fato.",
            "C": "As caravelas, que atravessaram o oceano, resistiram a tempestades. / As caravelas, navegadoras do oceano, resistiram a tempestades.",
            "D": "A descoberta do Brasil, que ocorreu em 1500, ficou na história. / A descoberta do Brasil, ocorrente em 1500, ficou na história.",
        }, correct="B",
        explanation="“Escreveu” → “redator” preserva exatamente o sentido original (quem escreve a carta é o redator). Já “descobriu” → “criador” muda o sentido (Cabral não criou o Brasil, descobriu-o); “atravessaram” → “navegadoras” é um substantivo que não corresponde precisamente ao verbo; e “ocorrente” não é uma substituição natural/correlata de “ocorreu”."),

    dict(number=3, topic="matematica_financeira",
        question="A empresa Gama S.A. avalia um projeto com investimento inicial de R$ 300.000,00, a ser realizado na data zero. Estimam-se entradas de caixa ao final de cada ano, conforme segue:\n• 1º ano: R$ 121.000,00\n• 2º ano: R$ 121.000,00\n• 3º ano em diante: R$ 146.410,00 por ano\nChama-se payback descontado ao tempo necessário para que a soma dos fluxos de caixa descontados iguale o investimento inicial.\nConsiderando-se uma taxa de desconto de 10% ao ano, o payback do projeto está entre",
        options={"A": "1 ano e 2 anos.", "B": "2 anos e 3 anos.", "C": "3 anos e 4 anos.", "D": "4 anos e 5 anos."}, correct="B",
        explanation="Trazendo a valor presente (÷1,10^n): ano 1 = 121.000/1,1 = 110.000; ano 2 = 121.000/1,21 = 100.000 (acumulado: 210.000); ano 3 = 146.410/1,331 = 110.000 (acumulado: 320.000). Como o acumulado ultrapassa 300.000 entre o ano 2 (210.000) e o ano 3 (320.000), o payback está entre 2 e 3 anos."),

    dict(number=4, topic="matematica_financeira",
        question="A empresa VGF S.A. tomou um empréstimo bancário de R$ 14.560,00 para financiar a compra de equipamentos. O contrato de empréstimo estabelece que o valor tomado deve ser liquidado por meio de uma série postecipada de 3 pagamentos mensais, iguais e sucessivos. O regime de capitalização adotado é o de juros compostos, à taxa de 20% ao mês.\nConsiderando essas informações, é correto afirmar que o valor das prestações mensais será de",
        options={"A": "R$ 4.853,33.", "B": "R$ 6.400,00.", "C": "R$ 6.912,00.", "D": "R$ 7.280,00."}, correct="C",
        explanation="Sistema Price: PMT = PV × [i(1+i)ⁿ] ÷ [(1+i)ⁿ − 1]. Com PV=14.560, i=20% e n=3: (1,2)³=1,728; PMT = 14.560 × (0,2×1,728)/(0,728) = 14.560 × 0,474725 ≈ R$ 6.912,00."),

    dict(number=5, topic="licitacoes_concessoes",
        question="Para o contador que atua no setor público ou na fiscalização de contratos administrativos, o conhecimento da Lei nº 14.133, de 1º de abril de 2021 (Lei de Licitações e Contratos), é fundamental para a avaliação da legalidade e conformidade dos gastos públicos.\nO Art. 5º dessa Lei elenca diversos princípios que devem guiar a atuação das Administrações Públicas diretas, autárquicas e fundacionais da União, dos Estados, do Distrito Federal e dos Municípios.\nCom base no texto legal, avalie os seguintes princípios:\nI. Impessoalidade\nII. Transparência\nIII. Racionalidade econômica\nIV. Probidade administrativa\nEstão expressamente listados no Art. 5º da Lei os princípios",
        options={"A": "I e IV, apenas.", "B": "II e III, apenas.", "C": "I, II e IV, apenas.", "D": "I, II, III e IV."}, correct="C",
        explanation="O Art. 5º da Lei 14.133/2021 lista expressamente impessoalidade, transparência e probidade administrativa, entre outros princípios (legalidade, moralidade, publicidade, eficiência etc.). “Racionalidade econômica” não é um termo expressamente listado nesse artigo — por isso apenas I, II e IV estão corretos."),

    dict(number=6, topic="direito_tributario",
        question="Um estudante de contabilidade, ao iniciar seus estudos em Direito Tributário, depara-se com o conceito fundamental de tributo. Para uma compreensão precisa, ele busca a definição legal contida no Código Tributário Nacional (Lei nº 5.172/1966).\nDe acordo com esse diploma legal, assinale a opção que define corretamente o tributo.",
        options={
            "A": "Tributo é toda prestação pecuniária voluntária, em moeda ou cujo valor nela se possa exprimir, que não constitua sanção de ato ilícito, instituída por meio de medida provisória e cobrada mediante atividade administrativa com alguma discricionariedade.",
            "B": "Tributo é toda sanção de ato ilícito, cobrada compulsoriamente em bens ou serviços, instituída em lei e aplicada com base em decisões discricionárias da administração pública.",
            "C": "Tributo é toda prestação pecuniária compulsória, em bens ou cujo valor nela se possa exprimir, que não constitua sanção de ato ilícito, instituída por qualquer ato normativo e cobrada mediante atividade administrativa parcialmente vinculada.",
            "D": "Tributo é toda prestação pecuniária compulsória, em moeda ou cujo valor nela se possa exprimir, que não constitua sanção de ato ilícito, instituída em lei e cobrada mediante atividade administrativa plenamente vinculada.",
        }, correct="D",
        explanation="É a definição literal do art. 3º do CTN: prestação pecuniária COMPULSÓRIA (não voluntária), em MOEDA (não bens), que NÃO constitui sanção de ato ilícito, instituída em LEI (não medida provisória ou ato normativo genérico) e cobrada mediante atividade administrativa PLENAMENTE vinculada (sem discricionariedade)."),

    dict(number=7, topic="direito_tributario",
        question="De acordo com a Lei Complementar nº 123, de 14 de dezembro de 2006, que institui o Estatuto Nacional da Microempresa e da Empresa de Pequeno Porte, os limites de receita bruta anual para fins de enquadramento são informações essenciais para a atuação do contador.\nConsiderando o que a lei estabelece sobre a definição de Microempresa (ME) e Empresa de Pequeno Porte (EPP), assinale a afirmativa correta.",
        options={
            "A": "Uma Microempresa (ME) aufere, em cada ano-calendário, receita bruta igual ou inferior a R$ 120.000,00, e uma Empresa de Pequeno Porte (EPP) aufere receita bruta superior a R$ 120.000,00 e igual ou inferior a R$ 1.200.000,00.",
            "B": "Uma Microempresa (ME) aufere, em cada ano-calendário, receita bruta igual ou inferior a R$ 360.000,00, e uma Empresa de Pequeno Porte (EPP) aufere receita bruta superior a R$ 360.000,00 e igual ou inferior a R$ 4.800.000,00.",
            "C": "Uma Microempresa (ME) aufere, em cada ano-calendário, receita bruta igual ou inferior a R$ 81.000,00, e uma Empresa de Pequeno Porte (EPP) aufere receita bruta superior a R$ 81.000,00 e igual ou inferior a R$ 4.800.000,00.",
            "D": "Os limites de receita bruta para ME e EPP são fixados anualmente por decreto do Comitê Gestor do Simples Nacional.",
        }, correct="B",
        explanation="Pela LC 123/2006: ME = receita bruta anual até R$ 360.000,00; EPP = receita bruta anual acima de R$ 360.000,00 até R$ 4.800.000,00. Esses limites são fixados em lei complementar, não por decreto do Comitê Gestor."),

    dict(number=8, topic="etica_profissional",
        question="Um escritório contábil quer expandir sua clientela com campanha de marketing, mas tem dúvidas sobre publicidade e preços conforme o Código de Ética.\nCom base na NBC PG 01 – CÓDIGO DE ÉTICA PROFISSIONAL DO CONTADOR, uma prática de divulgação e precificação eticamente correta é",
        options={
            "A": "prometer redução garantida de tributos sem embasamento técnico.",
            "B": "comparar preços e criticar concorrentes.",
            "C": "divulgar clientes e faturamento sem autorização.",
            "D": "expor conhecimento técnico com artigos e estudos de caso.",
        }, correct="D",
        explanation="Divulgar conhecimento técnico por meio de artigos e estudos de caso é uma forma legítima e ética de marketing profissional. Prometer resultados garantidos, criticar concorrentes e expor informações confidenciais de clientes sem autorização violam princípios do Código de Ética."),

    dict(number=9, topic="etica_profissional",
        question="Durante uma reunião com a diretoria de uma empresa cliente, o contador responsável apresentou os impactos financeiros de um novo contrato. Embora os dados estivessem tecnicamente corretos, os gestores demonstraram dúvidas e certa dificuldade em compreender a apresentação.\nNesse cenário, a habilidade profissional que contribuiria para que o contador fosse mais eficaz, de acordo com a NBC PG 100 (R1) - CUMPRIMENTO DO CÓDIGO, DOS PRINCÍPIOS FUNDAMENTAIS E DA ESTRUTURA CONCEITUAL, seria",
        options={
            "A": "realizar escuta ativa.", "B": "demonstrar clareza na exposição de dados.",
            "C": "revisar a legislação aplicável.", "D": "ignorar as dúvidas do cliente.",
        }, correct="B",
        explanation="Os dados já estavam tecnicamente corretos — o problema foi a COMUNICAÇÃO, não a técnica nem a legislação. A habilidade que faltou foi a clareza na exposição da informação, para que os gestores conseguissem compreendê-la."),

    dict(number=10, topic="estrutura_conceitual",
        question="De acordo com a NBC TG ESTRUTURA CONCEITUAL - ESTRUTURA CONCEITUAL PARA RELATÓRIO FINANCEIRO, as características qualitativas fundamentais são relevância e representação fidedigna, sendo que, para ser representação fidedigna, a representação deve ser completa, neutra e isenta de erros.\nUma informação neutra pode",
        options={"A": "ser parcial.", "B": "ser prudente.", "C": "possuir inclinações.", "D": "ser tendenciosa na seleção de informações financeiras."}, correct="B",
        explanation="Prudência (cautela ao lidar com incerteza) não é incompatível com neutralidade — pelo contrário, a Estrutura Conceitual afirma que o exercício de prudência apoia a neutralidade. Já ser parcial, possuir inclinações ou ser tendenciosa são exatamente o oposto de neutralidade."),

    dict(number=11, topic="estrutura_conceitual",
        question="De acordo com a NBC TG ESTRUTURA CONCEITUAL - ESTRUTURA CONCEITUAL PARA RELATÓRIO FINANCEIRO, para ajudar os usuários das demonstrações contábeis a identificar e avaliar mudanças e tendências, as demonstrações contábeis",
        options={
            "A": "são elaboradas com base na forma jurídica, em detrimento da essência das transações.",
            "B": "restringem a utilização de estimativas a casos em que poderá haver perdas financeiras do usuário.",
            "C": "incluem, apenas, informações que podem ser compreendidas, também, por usuários com pouco conhecimento das atividades comerciais e econômicas, sem auxílio de consultores.",
            "D": "fornecem informações comparativas de, pelo menos, um período de relatório anterior.",
        }, correct="D",
        explanation="Fornecer informação comparativa de pelo menos um período anterior é exatamente o que permite ao usuário identificar e avaliar mudanças e tendências ao longo do tempo. As demais opções contradizem a Estrutura Conceitual (que prioriza essência sobre forma e não limita a compreensibilidade a usuários leigos sem apoio de consultores)."),

    dict(number=12, topic="lancamentos_contabeis",
        question="Uma sociedade empresária presta serviços de perícia a terceiros.\nEm junho de 2024, aconteceram os seguintes fatos:\n• Compra de material de escritório para pagamento em 60 dias: R$ 5.000,00\n• Recebimento antecipado pelos serviços que serão prestados no segundo semestre: R$ 10.000,00\n• Reconhecimento do salário de seus empregados, para pagamento em 5 de julho: R$ 12.000,00\nEm junho de 2024, o passivo da sociedade empresária aumentou em",
        options={"A": "R$ 15.000,00.", "B": "R$ 17.000,00.", "C": "R$ 22.000,00.", "D": "R$ 27.000,00."}, correct="D",
        explanation="Os três fatos aumentam o passivo: fornecedores a pagar (5.000) + adiantamento de clientes/receita diferida (10.000) + salários a pagar (12.000) = R$ 27.000,00."),

    dict(number=13, topic="estrutura_conceitual",
        question="De acordo com a NBC TG ESTRUTURA CONCEITUAL - ESTRUTURA CONCEITUAL PARA RELATÓRIO FINANCEIRO, com relação às implicações das características qualitativas para a escolha da base de mensuração, avalie as afirmativas a seguir e assinale (V) para a verdadeira e (F) para a falsa.\n(  ) Utilizar consistentemente as mesmas bases de mensuração para os mesmos itens, seja de período a período, na entidade que reporta ou em um único período para diferentes entidades, prejudica a comparabilidade das demonstrações.\n(  ) A mudança na base de mensuração pode tornar as demonstrações contábeis menos compreensíveis. Contudo, a mudança pode ser justificada se outros fatores compensarem a redução na compreensibilidade, por exemplo, se a mudança resulta em informações mais relevantes.\n(  ) A verificação é melhorada utilizando-se bases de mensuração que resultam em avaliações que podem ser independentemente corroboradas diretamente, por exemplo, observando os preços, ou indiretamente, por exemplo, verificando dados de entrada de modelo.\nAs afirmativas são, respectivamente,",
        options={"A": "V – V – V.", "B": "V – V – F.", "C": "V – F – V.", "D": "F – V – V."}, correct="D",
        explanation="A 1ª afirmativa é FALSA: usar bases de mensuração consistentes MELHORA a comparabilidade, não a prejudica. A 2ª é VERDADEIRA: mudança pode ser justificada se resultar em informação mais relevante, mesmo perdendo um pouco de compreensibilidade. A 3ª é VERDADEIRA: verificação direta (preços observáveis) ou indireta (checar dados de um modelo) melhora a verificabilidade. Logo: F – V – V."),

    dict(number=14, topic="normas_contabeis",
        question="A NBC TG 28 (R4) - PROPRIEDADES PARA INVESTIMENTO trata de definição, classificação e mensuração de propriedades para investimento.\nSobre esse item, analise as seguintes afirmativas:\nI. Propriedade para Investimento é classificada dentro do subgrupo investimento no ativo circulante.\nII. Propriedade para investimento é um terreno, edifício ou veículo mantido pela entidade para auferir aluguel ou valorização do capital.\nIII. Propriedade para investimento no momento da aquisição deve ser mensurada pelo seu custo.\nEstá correto o que se afirma em",
        options={"A": "II e III, apenas.", "B": "III, apenas.", "C": "I, II e III.", "D": "II, apenas."}, correct="B",
        explanation="I é falsa: propriedade para investimento é ativo NÃO circulante, não um subgrupo do circulante. II é falsa: a definição inclui apenas terreno ou edifício (ou parte de edifício) — veículo não se enquadra na NBC TG 28. III é verdadeira: a mensuração inicial é sempre pelo custo. Logo, apenas III está correta."),

    dict(number=15, topic="normas_contabeis",
        question="Um ativo individual ou um grupo de ativos mantido para venda são ativos a ser alienados, por venda ou de outra forma, em conjunto como um grupo de ativos em uma só transação, e passivos diretamente associados a esses ativos que serão transferidos na transação.\nDe acordo com a NBC TG 31 (R4) - ATIVO NÃO CIRCULANTE MANTIDO PARA VENDA E OPERAÇÃO DESCONTINUADA, a depreciação do ativo ou grupo de ativos mantidos para venda deve",
        options={
            "A": "ser parcial, pois o ativo ou grupo de ativos ainda está operando.",
            "B": "ser mantida até a venda ser concretizada.",
            "C": "ser interrompida quando o ativo ou grupo de ativos for reclassificado como mantido para venda.",
            "D": "continuar como estava antes da reclassificação.",
        }, correct="C",
        explanation="A partir do momento em que um ativo é classificado como mantido para venda, ele deixa de ser depreciado — a depreciação é interrompida na data da reclassificação, já que o valor contábil será recuperado principalmente por venda, e não pelo uso contínuo."),

    dict(number=16, topic="normas_contabeis",
        question="De acordo com a NBC TG 01 (R4) - REDUÇÃO AO VALOR RECUPERÁVEL DE ATIVOS, o valor em uso é o valor presente de fluxos de caixa futuros esperados que devem advir de um ativo ou de unidade geradora de caixa.\nAvalie se os seguintes elementos devem ser refletidos no cálculo do valor em uso do ativo:\nI. O valor pago na aquisição do ativo.\nII. As expectativas acerca de possíveis variações no montante ou no período de ocorrência desses fluxos de caixa futuros.\nIII. As estimativas dos fluxos de caixa futuros que a entidade espera obter com esse ativo.\nIV. O valor do dinheiro no tempo, representado pela atual taxa de juros livre de risco.\nEstão corretos os elementos",
        options={"A": "I, II e III, apenas.", "B": "I e II, apenas.", "C": "III e IV, apenas.", "D": "II, III e IV, apenas."}, correct="D",
        explanation="O valor em uso é sobre fluxos de caixa FUTUROS: estimativas de fluxos futuros (III), expectativas de variação desses fluxos (II) e o valor do dinheiro no tempo (IV) entram no cálculo. O valor pago na aquisição (I) é custo histórico — não influencia a projeção de fluxos futuros. Logo: II, III e IV, apenas."),

    dict(number=17, topic="normas_contabeis",
        question="O ágio por expectativa de rentabilidade futura (goodwill) reconhecido em uma combinação de negócios é um ativo que representa benefícios econômicos futuros advindos de outros ativos adquiridos na combinação de negócios que não são identificados individualmente e não são reconhecidos separadamente.\nDe acordo com a NBC TG 04 (R4) - ATIVO INTANGÍVEL e com a NBC TG 15 (R4) - COMBINAÇÃO DE NEGÓCIOS, a empresa adquirente deve reconhecer, na data da aquisição, separadamente do ágio derivado da expectativa de rentabilidade futura (goodwill) apurado em uma combinação de negócios, um ativo intangível da adquirida, independentemente de o ativo ter sido reconhecido pela adquirida antes da aquisição da empresa.\nA perda por desvalorização reconhecida para o ágio por expectativa de rentabilidade futura (goodwill) não deve ser revertida em período subsequente, pois",
        options={
            "A": "não pode ser amortizada.", "B": "no plano de contas não há rubrica apropriada.",
            "C": "gera fluxos de caixa, independentemente de outros ativos ou grupos de ativos.", "D": "é equivalente ao goodwill gerado internamente.",
        }, correct="D",
        explanation="Um eventual aumento no valor recuperável do goodwill após uma perda reconhecida tende a ser, na prática, goodwill gerado internamente pela própria entidade — e esse tipo de goodwill nunca pode ser reconhecido contabilmente. Por isso, a reversão da perda é proibida: ela equivaleria a reconhecer goodwill gerado internamente."),

    dict(number=18, topic="normas_contabeis",
        question="A Demonstração do Valor Adicionado (DVA) busca evidenciar o valor e a distribuição da riqueza econômica gerada pelas atividades da sociedade empresária, incluindo também o valor adicionado recebido em transferência. A riqueza gerada é evidenciada na distribuição entre o capital (Remuneração de capital próprio e de terceiros), trabalho (Pessoal) e governo (Impostos, taxas e contribuições).\nRelacione cada item a seguir ao respectivo componente da distribuição da riqueza, conforme disposto na NBC TG 09 (R1) - DEMONSTRAÇÃO DO VALOR ADICIONADO.\n(  ) Fundo de Garantia por Tempo de Serviços (FGTS)\n(  ) Aluguéis pagos\n(  ) Dividendos distribuídos\n(  ) Contribuição Social sobre o Lucro Líquido (CSLL)\n1. Pessoal\n2. Impostos, taxas e contribuições\n3. Remuneração de capital de terceiros\n4. Remuneração de capital próprio\nA relação correta, na ordem apresentada, é",
        options={"A": "1 – 2 – 3 – 4.", "B": "2 – 3 – 4 – 1.", "C": "2 – 4 – 3 – 1.", "D": "1 – 3 – 4 – 2."}, correct="D",
        explanation="FGTS é encargo sobre a folha → Pessoal (1). Aluguéis pagos → Remuneração de capital de terceiros (3). Dividendos distribuídos → Remuneração de capital próprio (4). CSLL → Impostos, taxas e contribuições (2). Ordem: 1 – 3 – 4 – 2."),

    dict(number=19, topic="normas_contabeis",
        question="A empresa Delta S.A. adquiriu uma máquina por R$ 350.000,00 em 01/01/2020. No momento da aquisição, a administração de Delta S.A. estimou a vida útil desse ativo em 10 anos e um valor residual de R$ 50.000,00. A máquina estava disponível para uso em 01/01/2020 e a empresa adotou o método de depreciação linear.\nEm 31/12/2023, a empresa procedeu a uma revisão das suas estimativas, conforme previsto no NBC TG 27 (R4) - ATIVO IMOBILIZADO, e constatou as seguintes informações:\n• Vida útil remanescente: 9 anos\n• Valor Residual: R$ 50.000,00\nCom base exclusivamente nas informações apresentadas, o valor da depreciação anual dessa máquina a partir de 01/01/2024 será de",
        options={"A": "R$ 35.000,00.", "B": "R$ 30.000,00.", "C": "R$ 20.000,00.", "D": "R$ 15.000,00."}, correct="C",
        explanation="Depreciação original: (350.000−50.000)/10 = 30.000/ano. Após 4 anos (2020 a 2023): depreciação acumulada = 120.000. Valor contábil em 31/12/2023 = 350.000−120.000 = 230.000. Nova depreciação = (230.000−50.000)/9 = 180.000/9 = R$ 20.000,00/ano."),

    dict(number=20, topic="estrutura_conceitual",
        question="A NBC TG ESTRUTURA CONCEITUAL estabelece os conceitos dos elementos das demonstrações contábeis.\nCom base nessa norma, avalie as afirmativas a seguir e assinale (V) para a verdadeira e (F) para a falsa.\n(  ) Ativo é um recurso econômico presente de propriedade da entidade como resultado de eventos passados.\n(  ) Passivo é uma obrigação futura da entidade de transferir um recurso econômico como resultado de eventos passados.\n(  ) Receitas são aumentos nos ativos, ou reduções nos passivos, que resultam em aumento no patrimônio líquido, exceto aqueles referentes a contribuições de detentores de direitos sobre o patrimônio.\n(  ) Despesas são reduções nos ativos, ou aumentos nos passivos, que resultam em reduções no patrimônio líquido, exceto aqueles referentes a distribuições aos detentores de direitos sobre o patrimônio.\nAs afirmativas são, respectivamente,",
        options={"A": "F – F – V – V.", "B": "F – V – F – V.", "C": "V – F – V – F.", "D": "V – V – F – F."}, correct="A",
        explanation="A 1ª é FALSA: ativo é recurso CONTROLADO pela entidade, não necessariamente de sua PROPRIEDADE. A 2ª é FALSA: passivo é obrigação PRESENTE, não futura. A 3ª é VERDADEIRA: é a definição exata de receita. A 4ª é VERDADEIRA: é a definição exata de despesa. Logo: F – F – V – V."),

    dict(number=21, topic="normas_contabeis",
        question="A empresa Alfa S.A. adquiriu, por R$ 1.300.000,00, no dia 01/01/2025, 80% do capital da empresa Beta S.A., adquirindo nessa data o seu controle.\nNa data da aquisição:\n1. o valor contábil do patrimônio líquido da empresa Beta S.A. era de R$ 1.000.000,00\n2. o valor líquido dos ativos identificáveis e dos passivos da empresa Beta S.A. correspondentes a 100% de seu capital social, mensurados a valor justo, era de R$ 1.500.000,00\nCom base exclusivamente nos dados apresentados e na NBC TG 15 (R4) – COMBINAÇÃO DE NEGÓCIOS, avalie as afirmativas abaixo, com relação à contabilização ocorrida na empresa Alfa S.A.:\nI. Foi registrado um goodwill no valor de R$ 100.000,00.\nII. Foi registrada uma compra vantajosa no valor de R$ 200.000,00.\nIII. Foi registrado um ágio ou mais-valia dos ativos no valor de R$ 400.000,00.\nIV. Foi registrado um ágio ou mais-valia dos ativos no valor de R$ 500.000,00.\nEstão corretas as afirmativas",
        options={"A": "I e III, apenas.", "B": "I e IV, apenas.", "C": "II e III, apenas.", "D": "II e IV, apenas."}, correct="A",
        explanation="Mais-valia dos ativos líquidos (proporcional aos 80% adquiridos) = 80% × (1.500.000−1.000.000) = 80% × 500.000 = R$ 400.000,00 (afirmativa III). Valor justo da parcela adquirida = 80%×1.500.000 = 1.200.000. Goodwill = valor pago − valor justo da parcela adquirida = 1.300.000−1.200.000 = R$ 100.000,00, positivo (afirmativa I) — não há compra vantajosa. Logo: I e III, apenas."),

    dict(number=22, topic="normas_contabeis",
        question="Influência significativa é o poder de participar das decisões sobre políticas financeiras e operacionais de uma investida, mas sem que haja o controle individual ou o conjunto dessas políticas.\nA NBC TG 18 (R4) - INVESTIMENTO EM COLIGADA determina que a existência de influência significativa por investidor geralmente é evidenciada por uma ou mais das seguintes formas, à exceção de uma. Assinale-a.",
        options={
            "A": "Indicação de funcionários para a investida.", "B": "Operações materiais entre o investidor e a investida.",
            "C": "Intercâmbio de diretores ou gerentes.", "D": "Fornecimento de informação técnica essencial.",
        }, correct="A",
        explanation="A NBC TG 18 lista como evidências de influência significativa: representação no conselho, participação em decisões de políticas (inclusive dividendos), operações materiais entre as partes, intercâmbio de diretores/gerentes e fornecimento de informação técnica essencial. “Indicação de funcionários para a investida” não está entre essas formas listadas."),

    dict(number=23, topic="lancamentos_contabeis",
        question="A empresa ABCDE possui os seguintes registros referentes às movimentações em determinado período:\n• Compras: R$ 5.000,00\n• Estoque inicial: R$ 3.000,00\n• Estoque final: R$ 2.000,00\n• Vendas: R$ 30.000,00\n• Despesas gerais: R$ 1.000,00\n• Devolução de compras: R$ 500,00\nCom base nesses registros, é possível afirmar que a empresa obteve o Custo das Mercadorias Vendidas (CMV) de",
        options={"A": "R$ 6.000,00.", "B": "R$ 7.500,00.", "C": "R$ 8.000,00.", "D": "R$ 5.500,00."}, correct="D",
        explanation="CMV = Estoque Inicial + Compras − Devolução de Compras − Estoque Final = 3.000+5.000−500−2.000 = R$ 5.500,00."),

    dict(number=24, topic="normas_contabeis",
        question="A empresa S.A. possuía, em 31/12/2024, obrigações presentes como resultados de eventos passados cuja saída de recursos envolvendo benefícios futuros na liquidação esteve sujeita à análise, com a classificação disposta na tabela a seguir:\n• Garantia de venda — valor estimado: R$ 5.000,00 — probabilidade: Provável\n• Terreno contaminado e obrigação não formalizada — valor estimado: R$ 15.000,00 — probabilidade: Provável\n• Processo Trabalhista I — valor estimado: R$ 10.000,00 — probabilidade: Remota\n• Processo Trabalhista II — valor estimado: R$ 20.000,00 — probabilidade: Possível\n• Processo Fiscal — impossível estimar confiavelmente no momento — probabilidade: Possível\nCom base nos dados, seguindo a NBC TG 25 (R2) - PROVISÕES, PASSIVOS CONTINGENTES E ATIVOS CONTINGENTES, o montante a ser reconhecido como provisões no Balanço Patrimonial da empresa deve ser de",
        options={"A": "R$ 20.000,00.", "B": "R$ 40.000,00.", "C": "R$ 30.000,00.", "D": "R$ 50.000,00."}, correct="A",
        explanation="Só viram provisão os itens PROVÁVEIS com valor estimável: garantia de venda (5.000) e terreno contaminado (15.000) = 20.000. O Processo Trabalhista I é remoto (nem provisiona, nem divulga); o Processo Trabalhista II é possível (só divulga, não provisiona); o Processo Fiscal é possível e sem estimativa confiável (não provisiona). Total: R$ 20.000,00."),

    dict(number=25, topic="lancamentos_contabeis",
        question="A empresa Serviços S.A. encerrou seu exercício em 31/12/2024, deixando de efetuar o lançamento referente à receita de serviços prestados a um cliente em dezembro e ainda não recebidos, deixando de obedecer, assim, ao regime de competência.\nComo consequência do erro cometido pela ausência desse registro,",
        options={
            "A": "o saldo da conta clientes ficou superavaliado.", "B": "o saldo do disponível ficou subavaliado.",
            "C": "a receita do exercício ficou superavaliada.", "D": "o lucro do exercício ficou subavaliado.",
        }, correct="D",
        explanation="Ao deixar de registrar uma receita já ganha (regime de competência), tanto a receita quanto o lucro do exercício ficam SUBavaliados (para menos) — nunca superavaliados. O disponível (caixa) não é afetado, pois o valor ainda não havia sido recebido; a conta clientes também ficou subavaliada (não superavaliada), já que o direito a receber não foi registrado."),

    dict(number=26, topic="normas_contabeis",
        question="A Cia. Gold vende pulseiras.\nEm 31/12/2024, não havia estoque inicial de pulseiras.\nNo primeiro trimestre de 2025 aconteceram os seguintes fatos:\n• 05/01: compra de 20 pulseiras por R$ 10.000,00\n• 25/01: venda de 10 pulseiras por R$ 1.200,00 cada\n• 05/02: compra de 12 pulseiras por R$ 7.200,00\n• 20/02: venda de 11 pulseiras por R$ 1.200,00 cada\n• 10/03: compra de 8 pulseiras por R$ 5.200,00\n• 27/03: venda de 5 pulseiras por R$ 1.400,00 cada\nAssinale a opção que indica o valor aproximado do estoque final de pulseiras da Cia. Gold em 31/03/2025, considerando que a empresa utiliza o método do Custo Médio Ponderado Móvel em base diária.",
        options={"A": "R$ 7.840,00.", "B": "R$ 8.326,00.", "C": "R$ 9.100,00.", "D": "R$ 10.905,00."}, correct="B",
        explanation="05/01: 20un a 10.000 (custo médio 500/un). 25/01: vende 10, restam 10un=5.000. 05/02: compra 12 por 7.200 (600/un); total 22un=12.200, média≈554,55/un. 20/02: vende 11, restam 11un≈6.100. 10/03: compra 8 por 5.200 (650/un); total 19un=11.300, média≈594,74/un. 27/03: vende 5, restam 14un×594,74 ≈ R$ 8.326,00."),

    dict(number=27, topic="normas_contabeis",
        question="Uma loja de cosméticos começou a funcionar em 01/07/2024. No segundo semestre de 2024, aconteceram os seguintes fatos:\n• Integralização de capital social em dinheiro: R$ 300.000,00\n• Compra à vista de móveis e utensílios para a loja: R$ 40.000,00\n• Compra à vista de estoque para revenda: R$ 80.000,00\n• Pagamento do aluguel do semestre: R$ 30.000,00\n• Pagamento antecipado do aluguel do primeiro trimestre de 2025: R$ 18.000,00\n• Venda de todo o estoque por R$ 400.000,00, sendo que metade do valor já foi recebido e o restante deverá ser recebido no primeiro semestre de 2025. A loja estima inadimplência de 5%.\n• Reconhecimento e pagamento de despesas diversas: R$ 12.000,00\n• Reconhecimento da despesa de depreciação: R$ 4.000,00\nO fluxo de caixa gerado pela atividade operacional em 2024, de acordo com as diretrizes da NBC TG 03 (R3) – DEMONSTRAÇÃO DOS FLUXOS DE CAIXA foi de",
        options={"A": "R$ 20.000,00.", "B": "R$ 50.000,00.", "C": "R$ 60.000,00.", "D": "R$ 360.000,00."}, correct="C",
        explanation="Só entram no fluxo operacional os itens de caixa efetivamente movimentados pela operação: +200.000 (metade das vendas já recebida) −80.000 (compra de estoque) −30.000 (aluguel do semestre) −18.000 (aluguel antecipado) −12.000 (despesas diversas) = R$ 60.000,00. A integralização de capital é financiamento; a compra de móveis é investimento; a depreciação não movimenta caixa; a inadimplência estimada e o valor a receber ainda não são caixa."),

    dict(number=28, topic="normas_contabeis",
        question="Em 01/12/2024, uma sociedade empresária apresentava, em seu Balanço Patrimonial, como ativo imobilizado, um terreno, cujo valor contábil era de R$ 80.000,00.\nEm 31/12/2024, a sociedade empresária realizou um teste de recuperabilidade em seus ativos imobilizados.\nFoi constatado que o valor em uso do terreno era de R$ 75.000,00.\nPara que não haja reconhecimento de perda de recuperabilidade do terreno, o valor justo líquido de despesa de venda deve ser",
        options={"A": "menor do que R$ 75.000,00.", "B": "maior do que R$ 79.999,99.", "C": "entre R$ 72.000,00 e R$ 74.999,99.", "D": "entre R$ 75.000,00 e R$ 79.999,99."}, correct="B",
        explanation="Não há perda se o valor recuperável (o MAIOR entre valor justo líquido de venda e valor em uso) for igual ou superior ao valor contábil (80.000). Como o valor em uso (75.000) já é menor que 80.000, só não há perda se o valor justo líquido de venda for igual ou maior que 80.000 — ou seja, maior do que R$ 79.999,99."),

    dict(number=29, topic="normas_contabeis",
        question="Em junho de 2025, uma companhia aérea reconheceu as seguintes receitas:\n• com a marcação de assentos: R$ 150.000,00\n• com equivalência patrimonial: R$ 200.000,00\n• com a venda de passagens: R$ 900.000,00\nNesse mês, a companhia aérea reconheceu como Receita, na primeira linha da Demonstração do Resultado do Exercício, o seguinte montante:",
        options={"A": "R$ 900.000,00.", "B": "R$ 1.050.000,00.", "C": "R$ 1.100.000,00.", "D": "R$ 1.250.000,00."}, correct="B",
        explanation="A primeira linha da DRE (“Receita”) inclui apenas as receitas das atividades operacionais da companhia: marcação de assentos (150.000) + venda de passagens (900.000) = R$ 1.050.000,00. O resultado de equivalência patrimonial não é receita operacional bruta — aparece em linha própria, mais abaixo na demonstração."),

    dict(number=30, topic="normas_contabeis",
        question="Em 01/01/2025, uma livraria tinha em estoque 20 livros “Estatística Simples”. Cada livro tinha sido adquirido por R$ 80,00 e era vendido por R$ 140,00.\nNo primeiro trimestre desse ano, a movimentação do livro foi a seguinte:\n• 28/01: venda de 10 livros por R$ 140,00\n• 05/02: compra de 15 livros por R$ 90,00\n• 25/02: venda de 18 livros por R$ 150,00\n• 05/03: compra de 20 livros por R$ 95,00\n• 28/03: venda de 25 livros por R$ 150,00\nO custo das mercadorias vendidas no primeiro trimestre de 2025, considerando que a livraria utiliza o método PEPS para avaliação de estoque, foi de",
        options={"A": "R$ 3.860,00.", "B": "R$ 4.220,00.", "C": "R$ 4.660,00.", "D": "R$ 5.035,00."}, correct="C",
        explanation="PEPS (sai o mais antigo primeiro). Estoque inicial: 20@80. 28/01: vende 10@80=800; restam 10@80. 05/02: compra 15@90; estoque: 10@80+15@90. 25/02: vende 18 → 10@80(800)+8@90(720)=1.520; restam 7@90. 05/03: compra 20@95; estoque: 7@90+20@95. 28/03: vende 25 → 7@90(630)+18@95(1.710)=2.340. CMV total = 800+1.520+2.340 = R$ 4.660,00."),

    dict(number=31, topic="normas_contabeis",
        question="A compreensão dos conceitos e métodos relacionados à Demonstração do Resultado do Exercício (DRE) e à Demonstração do Resultado Abrangente (DRA) é fundamental para a adequada análise das variações do patrimônio líquido e para a tomada de decisões baseadas nos resultados operacionais.\nA respeito do tema, analise as seguintes afirmativas:\nI. A recompra de ações de emissão da própria entidade para manutenção em tesouraria afeta o resultado abrangente por representar uma redução no patrimônio líquido.\nII. O resultado abrangente compreende todos os componentes da demonstração do resultado e dos outros resultados abrangentes.\nIII. Pelo método da natureza da despesa, as despesas são classificadas conforme sua função, como administrativas, comerciais e de produção, facilitando a análise do custo dos produtos vendidos.\nIV. A informação sobre a natureza das despesas é útil para prever os fluxos de caixa futuros e requer divulgação adicional quando a classificação adotada na DRE for baseada no método da função das despesas.\nV. A entidade deve apresentar rubricas ou itens de receitas ou despesas como itens extraordinários, quer na demonstração do resultado abrangente, quer na demonstração do resultado do período, quer nas notas explicativas.\nDe acordo com a NBC TG 26 (R5) - APRESENTAÇÃO DAS DEMONSTRAÇÕES CONTÁBEIS, estão corretas as afirmativas",
        options={"A": "II e IV, apenas.", "B": "I, III e V, apenas.", "C": "II, III e IV, apenas.", "D": "I, II, IV e V, apenas."}, correct="A",
        explanation="I é falsa: recompra de ações em tesouraria é lançada diretamente no patrimônio líquido, sem passar pelo resultado nem pelo resultado abrangente. II é verdadeira: é a própria definição de resultado abrangente. III é falsa: a descrição corresponde ao método da FUNÇÃO da despesa, não ao da natureza (a questão trocou os conceitos). IV é verdadeira: é exatamente o que a norma exige quando se usa o método da função. V é falsa: a NBC TG 26 proíbe apresentar qualquer item como “extraordinário”, em qualquer lugar das demonstrações. Logo: II e IV, apenas."),

    dict(number=32, topic="normas_contabeis",
        question="A empresa S.A. é especializada na construção de galpões industriais sob encomenda de acordo com especificações exclusivas de cada cliente. Os contratos firmados pela empresa preveem que a construção ocorra no terreno do cliente, com pagamentos mensais vinculados ao andamento da obra, que pode durar de 6 a 10 meses.\nConsiderando as informações apresentadas e os preceitos da NBC TG 47 – RECEITA DE CONTRATO COM CLIENTE, o reconhecimento da receita deve ocorrer",
        options={
            "A": "somente após a emissão do certificado de aceitação técnica da obra pelo cliente.",
            "B": "no momento da conclusão da obra, quando todos os riscos e benefícios são transferidos.",
            "C": "no início do contrato, pois o pagamento mensal caracteriza o reconhecimento da receita.",
            "D": "ao longo do tempo, pois o desempenho da entidade cria ou melhora ativo que o cliente controla à medida que é construído.",
        }, correct="D",
        explanation="Como a construção ocorre no terreno do próprio cliente, o cliente já controla o ativo (o galpão em construção) à medida que ele é erguido — esse é um dos critérios da NBC TG 47 para reconhecimento de receita AO LONGO DO TEMPO, não em um único momento."),

    dict(number=33, topic="normas_contabeis",
        question="Uma empresa S.A. celebrou um contrato no valor de R$ 30.000,00 para utilizar um equipamento por um período de 10 meses, cujo ativo subjacente do contrato foi considerado de baixo valor pela empresa.\nA administração da empresa S.A. decidiu aplicar a isenção de reconhecimento autorizada pelo item 5 da NBC TG 06 (R3).\nConsiderando-se as informações apresentadas e os preceitos da NBC TG 06 (R3) – ARRENDAMENTOS, o tratamento contábil para esse contrato é",
        options={
            "A": "registrar o valor total do contrato antecipadamente como despesa no início do contrato.",
            "B": "capitalizar o valor do contrato como ativo imobilizado, amortizando ao longo do contrato.",
            "C": "reconhecer os pagamentos do arrendamento como despesa no resultado, de forma linear ou sistemática, ao longo do prazo do contrato.",
            "D": "reconhecer um ativo de direito de uso e um passivo de arrendamento, ambos, ao valor presente estipulado no contrato.",
        }, correct="C",
        explanation="A isenção para ativos de baixo valor (item 5 da NBC TG 06) dispensa o reconhecimento de ativo de direito de uso e passivo de arrendamento. Em vez disso, os pagamentos são reconhecidos diretamente como despesa no resultado, de forma linear (ou outra base sistemática), ao longo do prazo do contrato."),

    dict(number=34, topic="normas_contabeis",
        question="Uma empresa que atua na produção de medicamentos há 10 anos decidiu trocar dois de seus equipamentos (classificados como ativo imobilizado) mais relevantes por outros com tecnologia mais atualizada com o objetivo de redução nos seus custos de produção.\nAs informações sobre os equipamentos retirados de operação são relatadas a seguir:\n• Equipamento 1 — Valor Contábil Líquido: R$ 500.000,00 — Valor Justo Líquido: R$ 750.000,00\n• Equipamento 2 — Valor Contábil Líquido: R$ 1.500.000,00 — Valor Justo Líquido: R$ 1.250.000,00\nSabendo que os novos equipamentos adquiridos já estão em uso, um plano de venda desses ativos (Equipamentos 1 e 2) foi submetido e aprovado pelo Conselho de Administração, que considerou a venda altamente provável de ser concluída nos próximos 12 meses.\nLogo, segundo a NBC TG 31 (R3) – ATIVO NÃO CIRCULANTE MANTIDO PARA VENDA E OPERAÇÃO DESCONTINUADA, a mensuração subsequente dos equipamentos a ser adotada pela empresa a partir da decisão do Conselho de Administração é:",
        options={
            "A": "Equipamento 1 por R$ 500.000,00 e Equipamento 2 por R$ 1.250.000,00.",
            "B": "Equipamento 1 por R$ 500.000,00 e Equipamento 2 por R$ 1.500.000,00.",
            "C": "Equipamento 1 por R$ 750.000,00 e Equipamento 2 por R$ 1.500.000,00.",
            "D": "Equipamento 1 por R$ 750.000,00 e Equipamento 2 por R$ 1.250.000,00.",
        }, correct="A",
        explanation="Ativos mantidos para venda são mensurados pelo MENOR valor entre o valor contábil e o valor justo líquido de despesas de venda. Equipamento 1: menor entre 500.000 e 750.000 = 500.000. Equipamento 2: menor entre 1.500.000 e 1.250.000 = 1.250.000."),

    dict(number=35, topic="custos",
        question="A Contabilidade de Custos possui uma linguagem própria que permite ao profissional da contabilidade constituir o processo de análise, apuração e divulgação das informações relacionadas a custos, à medida que se mostrarem pertinentes de acordo com a necessidade informacional dos inúmeros stakeholders.\nTomando por base esse processo de terminologias na contabilidade de custos, assinale a afirmativa correta.",
        options={
            "A": "Os gastos representam a compra de um produto ou serviço que tem por capacidade gerar o dispêndio de recursos financeiros por parte da empresa, a exemplo da aquisição de um imobilizado.",
            "B": "Os custos representam um sacrifício monetário referente ao pagamento dos gastos, a exemplo do consumo de matéria-prima.",
            "C": "As despesas podem ser entendidas como os recursos utilizados na constituição de bens ou serviços em uma indústria, como exemplo tem-se as despesas com vendas e comissões.",
            "D": "As perdas são gastos anormais e involuntários do processo produtivo e já estão incluídas no custo do produto.",
        }, correct="A",
        explanation="“Gasto” é o termo mais amplo: qualquer sacrifício financeiro para adquirir um bem ou serviço, incluindo a compra de um imobilizado (que depois se torna investimento). As demais opções trocam os conceitos: custo é ligado à produção (não é só “pagamento dos gastos”), despesa é ligada a vendas/administração (não à produção de bens), e perdas NÃO entram no custo do produto — vão direto para o resultado."),

    dict(number=36, topic="lancamentos_contabeis",
        question="Uma empresa realizou a contagem de seus estoques, acabando por superavaliar o estoque inicial, mantendo o controle de compras e estoque final nos valores corretos.\nEm consequência da superavaliação do estoque inicial é correto afirmar que",
        options={
            "A": "a receita de vendas do período corrente foi subavaliada.", "B": "o lucro acumulado do período corrente foi superavaliado.",
            "C": "o custo dos produtos vendidos do período corrente foi superavaliado.", "D": "o estoque final foi subavaliado.",
        }, correct="C",
        explanation="CMV = Estoque Inicial + Compras − Estoque Final. Como o Estoque Inicial está superavaliado (e os demais itens corretos), o CMV também fica superavaliado. Isso, por sua vez, faz o LUCRO ficar subavaliado (não superavaliado) — a receita de vendas e o estoque final não são afetados pelo erro no estoque inicial."),

    dict(number=37, topic="custos",
        question="A Fazenda Laticínios Campo Verde Ltda. produz e comercializa queijos artesanais tipo minas frescal. No mês de julho de 2025, quando a empresa não possuía estoque inicial, foram produzidas 12.000 unidades de queijo. Nesse mesmo mês, vendeu 9.000 unidades a um preço unitário de R$ 25,00. Os custos variáveis totais somaram R$ 135.000,00 e os custos fixos totalizaram R$ 42.000,00. As despesas fixas totalizaram R$ 25.000,00, e as despesas variáveis com comissão aos vendedores corresponderam a 5% do valor de cada unidade vendida.\nConsiderando os dados fornecidos e desconsiderando efeitos tributários, os lucros líquidos com as vendas em julho de 2025, utilizando, respectivamente, os métodos de custeio por absorção e custeio variável, foram de",
        options={"A": "R$ 45.470,00 e R$ 11.750,00.", "B": "R$ 56.000,00 e R$ 56.000,00.", "C": "R$ 45.470,00 e R$ 112.500,00.", "D": "R$ 56.000,00 e R$ 45.500,00."}, correct="D",
        explanation="Receita = 9.000×25 = 225.000. Despesa variável (comissão) = 5%×225.000 = 11.250.\nAbsorção: custo unitário de produção = (135.000+42.000)/12.000 = 14,75. CPV(9.000)=132.750. Lucro = 225.000−132.750−25.000(desp. fixas)−11.250(comissão) = R$ 56.000,00.\nVariável: custo variável unitário = 135.000/12.000 = 11,25. Margem de contribuição = 225.000−(9.000×11,25)−11.250 = 225.000−101.250−11.250 = 112.500. Lucro = 112.500−42.000(custos fixos)−25.000(despesas fixas) = R$ 45.500,00."),

    dict(number=38, topic="custos",
        question="A Indústria Paranaguá Ltda. utiliza o sistema de custeio baseado em atividades (ABC). No mês de junho de 2025, foram apuradas as seguintes informações para os produtos X, Y e Z:\n• Produto X — Material Direto: R$ 35.000,00 — Mão de Obra Direta: R$ 18.000,00 — Pedidos de Mudança: 28 — kWh: 12.000\n• Produto Y — Material Direto: R$ 40.000,00 — Mão de Obra Direta: R$ 12.000,00 — Pedidos de Mudança: 20 — kWh: 14.000\n• Produto Z — Material Direto: R$ 25.000,00 — Mão de Obra Direta: R$ 10.000,00 — Pedidos de Mudança: 32 — kWh: 14.000\n• Total — Pedidos de Mudança: 80 — kWh: 40.000\nOs custos indiretos de manufatura totalizaram R$ 200.000,00, distribuídos entre as seguintes atividades:\n• Gerenciamento de mudanças de projeto (baseado em pedidos): R$ 140.000,00\n• Geração e uso de energia operacional (baseado em kWh): R$ 60.000,00\nNo período, foram produzidas 1.200 unidades do produto X, 1.500 unidades do produto Y e 2.000 unidades do produto Z.\nCom base nesses dados, os custos unitários dos produtos X, Y e Z, respectivamente, são",
        options={"A": "R$ 98,50; R$ 70,00; R$ 60,00.", "B": "R$ 90,00; R$ 80,00; R$ 65,00.", "C": "R$ 105,00; R$ 74,00; R$ 52,00.", "D": "R$ 100,00; R$ 72,00; R$ 56,00."}, correct="D",
        explanation="Taxa por pedido = 140.000/80 = 1.750/pedido. Taxa por kWh = 60.000/40.000 = 1,50/kWh.\nX: 35.000+18.000+(28×1.750=49.000)+(12.000×1,5=18.000) = 120.000 ÷ 1.200un = R$ 100,00.\nY: 40.000+12.000+(20×1.750=35.000)+(14.000×1,5=21.000) = 108.000 ÷ 1.500un = R$ 72,00.\nZ: 25.000+10.000+(32×1.750=56.000)+(14.000×1,5=21.000) = 112.000 ÷ 2.000un = R$ 56,00."),

    dict(number=39, topic="indicadores_financeiros",
        question="Em 31/12/2023, uma sociedade empresária apresentava os seguintes saldos em seus ativos e passivos:\n• Ativo Circulante: R$ 50.000,00\n• Ativo Realizável a Longo Prazo: R$ 30.000,00\n• Ativo Imobilizado: R$ 120.000,00\n• Passivo Circulante: R$ 40.000,00\n• Passivo não Circulante: R$ 100.000,00\nA proporção de capital próprio que financia o ativo da sociedade empresária foi igual a",
        options={"A": "30%.", "B": "40%.", "C": "60%.", "D": "70%."}, correct="A",
        explanation="Ativo total = 50.000+30.000+120.000 = 200.000. Passivo total = 40.000+100.000 = 140.000. Patrimônio Líquido (capital próprio) = 200.000−140.000 = 60.000. Proporção = 60.000/200.000 = 30%."),

    dict(number=40, topic="custos",
        question="Uma fábrica produz e vende apenas malas de mão. O custo fixo mensal da fábrica é de R$ 10.000,00. As malas são produzidas em dois modelos: com duas rodinhas e com quatro rodinhas.\nAs malas com duas rodinhas são vendidas por R$ 200,00 cada, enquanto as malas com quatro rodinhas são vendidas por R$ 370,00 cada. Além disso, o custo variável da mala com duas rodinhas é de R$ 80,00, e o custo variável da de quatro rodinhas é de R$ 140,00.\nNo primeiro trimestre de 2025, a fábrica tinha em estoque 500 unidades de rodinhas e não era possível adquirir mais. No período, as demandas pela produção de malas com duas e quatro rodinhas eram, respectivamente, de 80 e de 100.\nConsiderando que a fábrica tinha como objetivo maximizar o seu lucro, assinale a opção que indica a produção de malas de duas e quatro rodinhas, respectivamente, no período.",
        options={"A": "50 e 85.", "B": "50 e 100.", "C": "80 e 85.", "D": "80 e 100."}, correct="C",
        explanation="Com recurso escasso (rodinhas), prioriza-se quem dá mais margem de contribuição POR RODINHA usada. Mala 2 rodinhas: margem=200−80=120, usa 2 rodinhas → 60/rodinha. Mala 4 rodinhas: margem=370−140=230, usa 4 rodinhas → 57,50/rodinha. Como 60>57,50, produz-se toda a demanda de 2 rodinhas primeiro: 80un×2=160 rodinhas. Sobram 500−160=340 rodinhas, que dão 340÷4=85 malas de 4 rodinhas (menos que a demanda de 100, pois o recurso acabou). Resposta: 80 e 85."),

    dict(number=41, topic="custos",
        question="A empresa Gigulefere S.A. adota o custo padrão e verificou, em abril de 2025, alguns dados para analisar a variação ocorrida (realizado x orçado).\nAbaixo estão apresentados os dados apurados pelo contador:\n• a mão de obra direta efetivamente consumida foi 50 horas superior ao padrão estabelecido de 1.500 horas.\n• o custo incorrido com a mão de obra direta, por unidade de tempo, ficou R$ 7,00 abaixo do valor previsto de R$ 150,00 por hora.\nCom base exclusivamente nos dados apresentados pelo contador, as variações de taxa e eficiência, respectivamente, ocorridas no mês de abril de 2025, foram",
        options={"A": "350 desfavorável e 225.000 favorável.", "B": "10.500 favorável e 7.500 desfavorável.", "C": "75.000 desfavorável e 225.000 favorável.", "D": "1.050 favorável e 75.000 desfavorável."}, correct="B",
        explanation="Horas padrão (HP)=1.500, Taxa padrão (TP)=R$150,00/h, Horas reais (HR)=1.550, Taxa real (TR)=R$143,00/h.\nVariação de taxa = (TR−TP)×HP = (143−150)×1.500 = R$ 10.500,00 favorável.\nVariação de eficiência = (HR−HP)×TP = (1.550−1.500)×150 = R$ 7.500,00 desfavorável."),

    dict(number=42, topic="normas_contabeis",
        question="Em janeiro de 2024, um município adquiriu computadores para o edifício-sede da Prefeitura por R$ 50.000,00, classificando-os como ativo imobilizado. O transporte do estabelecimento do fornecedor para o edifício foi de R$ 5.000,00, pagos pelo município. Além disso, os custos de preparação dos locais para a instalação dos computadores foram de R$ 10.000,00.\nApós estarem devidamente instalados, o município gastou R$ 8.000,00 para treinar os funcionários que utilizarão esses computadores.\nO valor a ser reconhecido a título desse ativo, inicialmente, é",
        options={"A": "R$ 55.000,00.", "B": "R$ 63.000,00.", "C": "R$ 65.000,00.", "D": "R$ 73.000,00."}, correct="C",
        explanation="Entram no custo do ativo todos os gastos necessários para colocá-lo em condições de uso: compra (50.000) + transporte (5.000) + preparação do local (10.000) = R$ 65.000,00. O treinamento dos funcionários (8.000) NÃO é capitalizável — é sempre despesa, pois não é necessário para colocar o ativo em condições de funcionamento."),

    dict(number=43, topic="setor_publico",
        question="Uma escola do setor público serve, diariamente, café da manhã e almoço a seus alunos. Para as refeições, a escola adquire, semanalmente, frutas e verduras, e trimestralmente, alimentos não perecíveis. Todas as compras são pagas à vista.\nEm julho, a escola gastou R$ 4.000,00 com frutas e verduras e R$ 20.000,00 com os produtos não perecíveis, para serem estocados e utilizados até setembro.\nOs caixas consumidos, respectivamente, pela Atividade Operacional e pela Atividade de Investimento, na Demonstração dos Fluxos de Caixa da escola, foram",
        options={"A": "zero e R$ 24.000,00.", "B": "R$ 4.000,00 e R$ 20.000,00.", "C": "R$ 20.000,00 e R$ 4.000,00.", "D": "R$ 24.000,00 e zero."}, correct="D",
        explanation="Tanto as frutas/verduras quanto os produtos não perecíveis são suprimentos consumíveis para a atividade-fim da escola (alimentação) — ambos são despesas/estoques operacionais, não investimentos de longo prazo. Todo o gasto (4.000+20.000=24.000) é Atividade Operacional; zero vai para Atividade de Investimento."),

    dict(number=44, topic="setor_publico",
        question="De acordo com a NBC TSP - RECEITA DE TRANSAÇÃO SEM CONTRAPRESTAÇÃO, quando uma entidade do setor público adquire um ativo por meio de uma transação sem contraprestação, esse ativo deve ser mensurado inicialmente",
        options={
            "A": "pelo valor de ativo similar adquirido nos último três anos pela entidade pública.", "B": "pelo valor simbólico de R$ 1,00.",
            "C": "pelo valor justo do ativo na data de aquisição.", "D": "por valor nenhum, considerando que não houve pagamento na transação.",
        }, correct="C",
        explanation="Mesmo em transações sem contraprestação (doações, transferências), o ativo recebido deve ser mensurado inicialmente pelo seu VALOR JUSTO na data da aquisição — nunca por valor simbólico ou valor zero."),

    dict(number=45, topic="indicadores_financeiros",
        question="No planejamento orçamentário, a projeção da receita líquida de vendas é fundamental para estimar os resultados financeiros do período. Para isso, devem ser consideradas as quantidades a serem vendidas, o preço unitário e eventuais descontos concedidos.\nUma empresa projeta vender 4.000 unidades de seu produto no próximo trimestre. O preço de venda unitário é de R$ 120,00, e a empresa oferece um desconto comercial de 5% sobre o valor total.\nConsiderando essas premissas, o valor estimado da receita líquida de vendas no orçamento trimestral será de",
        options={"A": "R$ 456.000,00.", "B": "R$ 480.000,00.", "C": "R$ 484.000,00.", "D": "R$ 504.000,00."}, correct="A",
        explanation="Receita bruta = 4.000×120 = 480.000. Desconto comercial de 5% = 480.000×0,05 = 24.000. Receita líquida = 480.000−24.000 = R$ 456.000,00."),

    dict(number=46, topic="etica_profissional",
        question="Durante a reestruturação de uma empresa, o contador passou a atuar estrategicamente na controladoria e no compliance, contribuindo para o aprimoramento da gestão, monitorando indicadores e apoiando decisões. Ele também assegurou a conformidade com normas legais e regulatórias. Com isso, fortaleceu seu papel na governança e na transparência organizacional.\nConsiderando essa atuação conjunta, uma atribuição que caracteriza adequadamente essa integração funcional é",
        options={
            "A": "a mitigação de riscos.", "B": "o acompanhamento de metas.",
            "C": "o monitoramento da integridade dos controles internos.", "D": "o apoio à gestão com foco em desempenho e conformidade.",
        }, correct="D",
        explanation="A questão descreve DUAS frentes atuando juntas: controladoria (desempenho/indicadores/decisões) e compliance (conformidade com normas). Só a opção D combina explicitamente os dois focos — desempenho E conformidade — capturando a integração funcional descrita."),

    dict(number=47, topic="auditoria",
        question="Um Auditor foi contratado por uma determinada empresa S.A. para realizar auditoria independente e, na ocasião, deparou com a seguinte situação: nos demonstrativos auxiliares, verificou-se que a empresa adota o método linear de depreciação das máquinas e registra o lançamento mensalmente na contabilidade.\nConforme a NBC TA 500 (R1) - EVIDÊNCIA DE AUDITORIA, o procedimento que deverá ser adotado para a confirmação da exatidão dos valores lançados é",
        options={"A": "a confirmação externa.", "B": "a inspeção.", "C": "o recálculo.", "D": "a indagação."}, correct="C",
        explanation="Para verificar a EXATIDÃO MATEMÁTICA de um valor já calculado pela entidade (como uma depreciação linear recorrente), o procedimento de auditoria apropriado é o RECÁLCULO — refazer a conta de forma independente para conferir se bate com o valor lançado."),

    dict(number=48, topic="auditoria",
        question="De acordo com a NBC TA 300 (R1) – PLANEJAMENTO DA AUDITORIA DE DEMONSTRAÇÕES CONTÁBEIS, o envolvimento do sócio do trabalho e de outros membros-chave da equipe de trabalho no planejamento da auditoria",
        options={
            "A": "garante o controle e o cumprimento das etapas necessárias, fornecendo agilidade ao processo de planejamento.",
            "B": "incorpora a sua experiência e seus pontos de vista, otimizando a eficácia e a eficiência do processo de planejamento.",
            "C": "aumenta a admiração e o respeito transferidos pela equipe, proporcionando sinergia para o processo de planejamento.",
            "D": "melhora a proximidade e o relacionamento com a equipe, contribuindo para a qualidade do processo de planejamento.",
        }, correct="B",
        explanation="A NBC TA 300 destaca que envolver o sócio e membros-chave desde o planejamento traz a experiência e os pontos de vista deles para o processo, tornando-o mais eficaz e eficiente — não é sobre agilidade burocrática, relacionamento interpessoal ou hierarquia."),
]

assert len(LEVEL2) == 48, len(LEVEL2)


# ============================================================
# Topic labels — human-readable Portuguese names for each topic
# slug, used to tell the student which area of the Módulo 3
# study guide to review when they need a tip.
# ============================================================

TOPIC_LABELS = {
    "lingua_portuguesa": "Língua Portuguesa",
    "estatistica_probabilidade": "Estatística e Probabilidade",
    "matematica_financeira": "Matemática Financeira",
    "licitacoes_concessoes": "Licitações e Concessões (Lei 14.133 / Lei 8.987)",
    "direito_tributario": "Direito Tributário e Simples Nacional",
    "etica_profissional": "Ética Profissional (NBC PG)",
    "estrutura_conceitual": "Estrutura Conceitual",
    "normas_contabeis": "Normas Contábeis (NBC TG)",
    "lancamentos_contabeis": "Lançamentos Contábeis",
    "custos": "Contabilidade de Custos",
    "indicadores_financeiros": "Análise das Demonstrações / Indicadores",
    "setor_publico": "Contabilidade Pública (MCASP / Orçamento)",
    "auditoria": "Auditoria",
    "direito_pericia": "Perícia Contábil e Direito Processual",
}

# ============================================================
# Hints — short nudges (formula/approach) shown on request,
# before the student answers. They point toward the reasoning
# without revealing the correct letter.
# ============================================================

HINTS_L1 = {
    1: "Releia cada opção e pergunte-se: esse número é um valor exato ou uma estimativa (“mais de”, “cerca de”, “perto de”)?",
    2: "Preste atenção à estrutura “não apenas X, mas também Y” — ela soma um segundo elemento, não contradiz o primeiro.",
    3: "Numa distribuição normal simétrica, a probabilidade que sobra fora de um intervalo centrado na média se divide igualmente nas duas caudas.",
    4: "Tabela SAC: a amortização é sempre igual (valor financiado ÷ nº de parcelas); o juro de cada parcela incide sobre o saldo devedor, que vai diminuindo.",
    5: "Lei 14.133/2021: pense se os entes envolvidos pertencem à mesma esfera federativa (municipal, estadual, federal) ou a esferas diferentes.",
    6: "Lembre das cláusulas exorbitantes: a Administração pode alterar contratos unilateralmente por interesse público, mas os direitos do contratado são preservados.",
    7: "Lei 8.987/1995: emergência e razões técnicas/segurança dispensam aviso prévio para interrupção do serviço.",
    8: "Pense em “ameaça de autorrevisão”: quem executa e quem decide/gerencia não deveria ser a mesma pessoa/firma.",
    9: "O princípio da integridade e objetividade prevalece mesmo sob pressão da administração — não há exceção por valor ou prazo.",
    10: "Neutralidade significa não manter deliberadamente uma estimativa que já se sabe desatualizada só para beneficiar o resultado.",
    11: "O reconhecimento de um ativo ocorre quando ele está “disponível para uso”, não quando o uso efetivamente começa.",
    13: "A Estrutura Conceitual (R2) define recurso econômico pelo seu potencial de gerar benefícios — não pela posse jurídica do bem.",
    14: "Se a arrendatária não pretende ficar com o bem, a depreciação usa o MENOR prazo entre a duração do contrato e a vida útil do ativo.",
    15: "Um segmento é reportável se atingir 10% em UM dos critérios (receita, resultado OU ativos) — não precisa atingir todos.",
    16: "Ativo fiscal diferido só se mantém enquanto for PROVÁVEL a existência de lucro tributável futuro suficiente.",
    17: "A receita só é reconhecida quando o CONTROLE do bem passa ao cliente — normalmente na entrega, não no pagamento ou na nota fiscal.",
    18: "Separe pesquisa (sempre despesa) de desenvolvimento (pode ser capitalizado): construção/teste de protótipos é desenvolvimento; buscar/selecionar alternativas é pesquisa.",
    19: "Reclassificação para o imobilizado: compare o valor contábil “como se nunca tivesse saído” (com a depreciação que teria ocorrido) com o valor recuperável, e use o MENOR dos dois.",
    20: "Perdas anormais de estoque (sinistro) não vão para o custo do produto — são despesa direta, com baixa do estoque.",
    21: "No Ajuste a Valor Presente, o cliente entra pelo valor de face, a receita pelo valor presente, e a diferença fica numa conta retificadora a apropriar.",
    22: "Separe as contas por natureza: ativo e despesa são devedoras; passivo, PL e receita são credoras — mas contas retificadoras invertem essa lógica.",
    23: "A equivalência patrimonial incide sobre o LUCRO LÍQUIDO total do período, não importa quanto foi para reservas ou dividendos.",
    24: "Na DVA, “Remuneração de Capitais de Terceiros” reúne juros, aluguéis e royalties — não inclui despesas com pessoal.",
    25: "Distribua o valor total da venda proporcionalmente entre Caixa, Banco e Duplicatas a Receber, conforme os percentuais informados.",
    26: "Monte a DRE em cascata: Receita bruta → (–) deduções → Receita líquida → (–) CMV/CSP → Lucro bruto → (–) despesas → (–) tributos sobre lucro → Lucro líquido.",
    27: "No custo do estoque: some tudo que faz parte de colocar o bem pronto para uso (frete, seguro, impostos não recuperáveis) e subtraia descontos comerciais e impostos recuperáveis.",
    28: "Só existe provisão quando a perda é PROVÁVEL; se for apenas possível, não há lançamento, só nota explicativa.",
    29: "Método direto e indireto só mudam a FORMA de apresentar o fluxo operacional — o valor total de cada atividade é sempre igual.",
    30: "A presunção de 20% para influência significativa não é absoluta — outras evidências (como assento no conselho) também contam.",
    31: "Não esqueça de descontar a perda por impairment JÁ reconhecida antes de calcular o valor contábil atual do ativo.",
    32: "No custo médio ponderado móvel, recalcule a média a cada COMPRA (dividindo valor total pelo total de unidades) — vendas não alteram a média.",
    33: "Na consolidação, somam-se 100% dos ativos da controlada, mesmo que a participação adquirida seja menor que 100%.",
    34: "Juros pagos têm classificação flexível na DFC: podem ir para operacional OU para financiamento.",
    35: "No custeio por absorção, todo custo fixo E variável de FÁBRICA entra no custo do produto; despesas administrativas/comerciais ficam de fora.",
    36: "Rateio por área ocupada: calcule a proporção de cada setor sobre a área TOTAL e aplique sobre o custo a ratear.",
    37: "Separe: Custo = ligado à produção; Despesa = administrativo/comercial; Investimento = todo gasto que vira ativo (inclusive compra de matéria-prima ainda em estoque).",
    38: "Variação favorável = quando o custo REAL é menor que o custo PADRÃO.",
    39: "Ciclo operacional = tempo de produção/armazenagem + prazo de recebimento. O prazo de pagamento a fornecedores não entra aqui.",
    40: "Ponto de equilíbrio = Custos fixos ÷ Margem de contribuição unitária. Descubra primeiro o custo fixo usando os dados originais.",
    41: "NCG = Ativo Circulante Operacional (recebíveis + estoques) – Passivo Circulante Operacional (fornecedores + outras contas a pagar operacionais), usando prazos médios sobre o valor diário.",
    43: "Atente-se aos detalhes: a mensuração inicial dos ativos de concessão é pelo VALOR JUSTO, e eles precisam ser segregados em classes, como o imobilizado.",
    44: "O princípio da legalidade exige que só se orce receita de tributo já aprovado e regulamentado em lei.",
    45: "Anulação PARCIAL de empenho ocorre quando o valor reservado é MAIOR do que o necessário (o excedente é liberado).",
    46: "Associe pela abrangência: estratégico = diretrizes gerais de longo prazo; tático = metas setoriais; operacional = rotinas do dia a dia.",
    47: "Risco de auditoria é sempre sobre a OPINIÃO do auditor ficar inadequada por distorções não detectadas — não é sobre erro contábil em si.",
    48: "Diante de fraude, o caminho correto é comunicar aos responsáveis pela governança (ex.: Conselho de Administração), não agir unilateralmente.",
    49: "CPC/2015: a prorrogação do prazo pericial é uma FACULDADE do juiz (“poderá”), por metade do prazo original.",
    50: "Calcule o total de dias de férias a que tem direito (30 dias por período completo + proporcional do período incompleto), subtraia os dias já gozados, e aplique o valor do dia com o adicional de 1/3.",
}

HINTS_L2 = {
    1: "Compare palavra por palavra as duas definições e veja qual afirmação sobre elas é literalmente verdadeira, sem forçar interpretação.",
    2: "A substituição do “que” por um substantivo correlato deve manter o MESMO sentido da frase original — desconfie de palavras que mudam o significado.",
    3: "Traga cada fluxo de caixa a valor presente (÷ (1+i)ⁿ) e some até o total ultrapassar o investimento inicial — veja entre quais anos isso acontece.",
    4: "Sistema Price: parcela fixa = PV × [i(1+i)ⁿ] ÷ [(1+i)ⁿ − 1].",
    5: "Releia o Art. 5º da Lei 14.133/2021 de cabeça: nem todo princípio “razoável” está expressamente listado ali — alguns são só doutrina/senso comum.",
    6: "A definição legal de tributo (CTN, art. 3º) tem palavras-chave bem específicas: compulsória, em moeda, não sanção, instituída em lei, atividade plenamente vinculada.",
    7: "Os limites de faturamento do Simples Nacional (LC 123/2006) têm valores fixos e conhecidos para ME e EPP — vale a pena decorá-los.",
    8: "Pense no que é ético em publicidade: divulgar conhecimento técnico é diferente de prometer resultado ou criticar concorrente.",
    9: "O problema não foi a informação estar errada, foi a forma como foi comunicada — pense na habilidade ligada a isso.",
    10: "Neutralidade não é o mesmo que ausência de cautela: um dos conceitos da lista NÃO é sinônimo de viés/tendenciosidade.",
    11: "Uma das funções das demonstrações comparativas é ajudar a enxergar tendências ao longo do tempo — pense em quantos períodos isso exige.",
    12: "Some apenas os itens que representam obrigações da empresa com terceiros (passivo) — todos os três fatos listados aumentam o passivo.",
    13: "Para cada afirmativa, pergunte-se: isso ajuda ou atrapalha a comparabilidade/compreensibilidade/verificabilidade das demonstrações?",
    14: "Propriedade para investimento é sobre terrenos e EDIFÍCIOS — um dos itens do enunciado lista um tipo de bem que não se enquadra nessa norma.",
    15: "Pense: o ativo mantido para venda ainda gera valor por uso contínuo enquanto está à venda, ou o valor vem principalmente da venda?",
    16: "Valor em uso é sobre fluxos de caixa FUTUROS — um dos elementos listados é sobre o passado (o que já foi pago) e não deveria entrar na conta.",
    17: "A razão para não reverter a perda do goodwill tem a ver com o fato de o goodwill não poder ser gerado/reconhecido internamente.",
    18: "Separe cada item pela sua natureza: é encargo sobre salário (Pessoal)? é pagamento a quem alugou um bem (capital de terceiros)? é retorno ao sócio (capital próprio)? é imposto (Governo)?",
    19: "Depreciação nova = (valor contábil atual − novo valor residual) ÷ nova vida útil remanescente. Primeiro descubra o valor contábil em 31/12/2023.",
    20: "Compare cada afirmativa com a definição exata da Estrutura Conceitual: é “propriedade” ou “controle”? é obrigação “presente” ou “futura”?",
    21: "Goodwill = valor pago − (percentual adquirido × valor justo dos ativos líquidos). Mais-valia = percentual adquirido × (valor justo − valor contábil dos ativos líquidos).",
    22: "A NBC TG 18 lista formas específicas de evidenciar influência significativa (conselho, políticas, operações materiais, intercâmbio de gerentes, informação técnica) — uma das opções não está nessa lista.",
    23: "CMV = Estoque Inicial + Compras − Devoluções de Compras − Estoque Final.",
    24: "Só vira provisão o que é PROVÁVEL e tem valor estimável com confiança — cuidado com os itens “remota”, “possível” ou “sem estimativa confiável”.",
    25: "Se a receita não foi lançada, tanto a receita quanto o lucro do período ficam para baixo (subavaliados), não para cima.",
    26: "Recalcule a média ponderada a cada COMPRA (soma do valor total ÷ soma das unidades); as vendas usam essa média para dar baixa, sem alterá-la.",
    27: "No fluxo de caixa operacional, considere só o que efetivamente entrou/saiu de caixa em atividades do negócio — capital integralizado é financiamento, compra de móveis é investimento.",
    28: "Para não haver perda, o valor recuperável (o MAIOR entre valor justo líquido de venda e valor em uso) precisa ficar igual ou acima do valor contábil.",
    29: "A “primeira linha” da DRE é a Receita das atividades operacionais principais — resultado de equivalência patrimonial não entra aí.",
    30: "PEPS: as unidades mais ANTIGAS em estoque são as primeiras a sair a cada venda — monte a ficha de estoque venda por venda.",
    31: "Cuidado com armadilhas de troca de conceitos: recompra de ações em tesouraria não passa pelo resultado, e as descrições de “natureza” e “função” da despesa costumam ser trocadas de propósito.",
    32: "Quando a obra é construída no terreno do próprio cliente, o cliente já “controla” o ativo sendo construído — isso aponta para reconhecimento ao longo do tempo.",
    33: "A isenção de baixo valor dispensa reconhecer ativo de direito de uso e passivo de arrendamento — o pagamento vira direto despesa, de forma linear.",
    34: "Ativos mantidos para venda são mensurados pelo MENOR valor entre o valor contábil e o valor justo líquido de despesas de venda — calcule cada equipamento separadamente.",
    35: "Lembre as definições clássicas (Martins): gasto é sacrifício para adquirir algo (inclusive imobilizado); custo é ligado à produção; despesa, à administração/vendas; perda não entra no custo do produto.",
    36: "Na fórmula do CMV, o estoque inicial é somado — se ele está superavaliado, o que mais fica distorcido no mesmo sentido?",
    37: "No custeio por absorção, os custos fixos de fábrica entram no custo do produto (só são “baixados” quando o produto é vendido); no custeio variável, eles saem direto como despesa do período, sobre o total incorrido.",
    38: "Cada atividade do ABC tem sua própria taxa (custo da atividade ÷ total do direcionador) — aplique a taxa de cada atividade à quantidade consumida por cada produto, depois some ao material e mão de obra direta.",
    39: "Capital próprio = Ativo Total − Passivo Total (Circulante + Não Circulante). Depois divida pelo Ativo Total.",
    40: "Quando um recurso é escasso, o critério para decidir o que priorizar é a margem de contribuição POR UNIDADE DO RECURSO ESCASSO, não a margem por produto.",
    41: "Variação de taxa = (Taxa Real − Taxa Padrão) × Horas Padrão. Variação de eficiência = (Horas Reais − Horas Padrão) × Taxa Padrão.",
    42: "Entram no custo do ativo todos os gastos necessários para colocá-lo em condições de uso (compra, transporte, instalação) — treinamento de pessoal não é um desses gastos.",
    43: "Pergunte-se: os itens comprados são consumidos logo, como suprimento da atividade-fim (operacional), ou viram um ativo de longo prazo (investimento)?",
    44: "Ativos recebidos sem contraprestação (doações, transferências) são mensurados inicialmente pelo VALOR JUSTO na data da aquisição.",
    45: "Receita líquida = quantidade × preço unitário, menos os descontos concedidos sobre esse total.",
    46: "Pense no que junta, ao mesmo tempo, indicadores de desempenho (controladoria) e conformidade com normas (compliance) em uma única atribuição.",
    47: "Para verificar a exatidão matemática de um valor lançado (como uma depreciação linear recorrente), o procedimento de auditoria mais direto é refazer a conta.",
    48: "Pense no valor de reunir mais experiência e pontos de vista logo no planejamento — isso melhora a qualidade técnica do plano, não é sobre proximidade pessoal ou hierarquia.",
}

assert set(HINTS_L2.keys()) == {q["number"] for q in LEVEL2}, "HINTS_L2 keys must match LEVEL2 numbers"
assert set(HINTS_L1.keys()) == {q["number"] for q in LEVEL1}, "HINTS_L1 keys must match LEVEL1 numbers"

# ============================================================
# Assemble and write data/questions.json
# ============================================================

def build_entries(items, prefix, hints):
    entries = []
    for i, item in enumerate(items, start=1):
        entry = {
            "id": f"{prefix}-q{i:02d}",
            "topic": item["topic"],
            "topicLabel": TOPIC_LABELS[item["topic"]],
            "question": item["question"],
            "options": item["options"],
            "correct": item["correct"],
            "explanation": item["explanation"],
        }
        if "number" in item:
            entry["number"] = item["number"]
            entry["hint"] = hints[item["number"]]
        else:
            entry["hint"] = hints[i - 1]
        entries.append(entry)
    return entries


data = {
    "level1": build_entries(LEVEL1, "l1", HINTS_L1),
    "level2": build_entries(LEVEL2, "l2", HINTS_L2),
}

out_path = Path(__file__).resolve().parent.parent / "data" / "questions.json"
out_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Wrote {len(data['level1'])} level1 + {len(data['level2'])} level2 questions to {out_path}")

