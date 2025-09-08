# Análise de empréstimos dos acervos do sistema de bibliotecas da UFRN

# Problema de negócio
A biblioteca universitária possui um vasto acervo de materiais informacionais (físicos e digitais), mas não possui clareza sobre como esses recursos estão sendo utilizados pelos diferentes perfis de usuários (alunos, professores, pesquisadores). A falta de visibilidade sobre padrões de uso, materiais subutilizados e demandas não atendidas dificulta a tomada de decisão sobre aquisição, descarte, organização e estratégias de incentivo ao uso.

Como analista de dados, o seu objetivo é:
é compreender o comportamento de uso dos materiais informacionais, identificar oportunidades para aumentar a eficiência e relevância do acervo e, assim, apoiar a instituição no objetivo de fomentar a produção de conhecimento.

# Contexto
Um dos objetivos de um sistema de bibliotecas universitárias é garantir o uso da informação para que seja produzido mais conhecimento. 

Nesse contexto, o Analista de Dados tem um papel fundamental para coletar, analisar e gerar insights afim de ajudar a instituição aprimorar a utilização dos materiais informacionais.

# Premissas de análise
1. A análise utilizou os dados públicos da UFRN dos anos de 2010 a 2022.
2. Todos os valores dos registros do sistema dos exemplares foram removidos.
3. A análise considerou apenas os exemplares da UFRN.

# Estratégia da solução
O método de Análise Exploratória de Dados (EDA - Exploratory Data Analysis) foi usado para conduzir esse projeto.

Esse método consiste em um conjunto de técnicas estatísticas e de visualização que permitem compreender a estrutura do conjunto de dados, identificar padrões de comportamento, testar hipóteses iniciais e detectar anomalias ou inconsistências.

## Passo 1: Entendimento dos Dados
 - Análise descritiva Inicial - foi realizada uma análise descritiva com o objetivo de entender o tamanho, a estrutura, as colunas disponíveis e as estatísticas básicas dos dados, identificando padrões iniciais e possíveis inconsistências.
 - Descrição das colunas da Base de dados:
    - **id_emprestimo** - Identificador do empréstimo
    - **codigo_barras** - Código de barras do item do acervo
    - **data_renovacao** - Data da renovação do empréstimo.
    - **data_emprestimo** - Data da realização do empréstimo.
    - **data_devolucao** - Data da devolução do item
    - **matricula_ou_siape** - Matricula ou siape do usuário que realizou o
    empréstimo.
    - **tipo_vinculo_usuario** - Tipo do vínculo do usuário (servidor, discente,
    docente, etc.). 


## Passo 2: Tratamento Inicial
 - Limpeza de valores nulos e inconsistentes.
 - Classificação do arcevo da biblioteca (CDU).
 - Corrreção dos nomes dos níveis de ensino com ftfy.
 - Criação de um novo dataframe contendo os emprestimos e exemplares.
 - Criação de um novo dataframe contendo os emprestimos dos alunos de 2018 e 2019 de Graduação
 - Criação de um novo dataframe contendo os emprestimos dos alunos de 2018 e 2019 de Pós-Graduação

<!-- 
## Passo 3: Definição da coluna Fato
O Fato é a coluna de interesse que representa o ponto focal da análise. Nesse caso, a coluna "Gasto-Clientes" representa o faturamento de cada cliente dentro da campanha e será o objetivo da nossa análise, dado que o problema envolve aumento do faturamento na próxima campanha de Marketing.

## Passo 4: Identificação das Dimensões
As colunas foram agrupadas em dimensões comuns que fornecem mais detalhes sobre o Fato que será analisado. Foram organizadas as seguintes dimensões:

1. Cliente
  - Salário
  - Idade
  - Faixa-Etária
  - Estado-Civil
  - Formação
  - Crianças-Casa
  - Adolescentes-Casa
  - Recência

2. Produto
  - Qtde-Vinhos
  - Qtde-Frutas
  - Qtde-Carnes
  - Qtde-Peixes
  - Qtde-Doces
  - Qtde-Premium

3. Comportamento de Compra
  - Qtde-Compras
  - Qtde-Compras-Web
  - Qtde-Compras-Loja
  - Visitas-Site-Mes
4. Comportamento de Mkt
  - Reclamaçoes

## Passo 5: Hipóteses Analíticas
Fato(Medida) + Dimensão(Detalhes) + Comparação

As hipóteses analíticas são construídas a partir da combinação do Fato com as Dimensões, usando sempre um valor de comparação como maior, menor ou igual.

Fato + Dimensão: Cliente - Atributos: Idade.

1. O faturamento dos clientes abaixo de 30 anos é maior do que nas outras faixas etárias.
2. O faturamento dos clientes entre 20 e 30 anos é maior do que nas outras faixas etárias.
3. O faturamento dos clientes acima dis 30 anos do que nas outras faixas etárias.

Fato + Dimensão: Cliente - Atributos: Estado Civil.

4. Clientes solteiros gastam mais do que os outros segmentos de clientes.
5. Clientes solteiros gastam menos do que os outros segmentos de clientes.
6. Clientes casados gastam mais do que os outros segmentos de clientes.

Fato + Dimensão: Cliente - Atributos: Estado Civil + Idade.

7. Clientes solteiros acima dos 30 anos gastam mais do que clientes casados acima dos 30 anos.

Fato + Dimensão: Cliente - Atributos: Formação.

8. Clientes com formações avançadas (Doutorado) gastam mais do que clientes com Ensino Fundamental.
9. Clientes com maiores salários tem nível de escolaridade maior.

## Passo 6: Critérios de Priorização
Critério 1: Dados disponíveis

Critério 2: Insights Acionável

## Passo 7: Priorização das Hipóteses Analíticas
Hipótese 1. Clientes abaixo dos 30 anos gastam mais com produtos do iFood do que as outras faixas etárias.

![Hipótese 1](img/hipotese1.png)

Hipótese 2. Clientes solteiros gastam menos do que os outros segmentos de clientes.

![Hipótese 2](img/hipotese2.png)

Hipótese 3. Clientes solteiros abaixo dos 30 anos gastam mais com produtos do iFood do que as outras faixas etárias.

![Hipótese 3](img/hipotese3.png)

Hipótese 4. Clientes com crianças em casa compram mais pelo ifood.

![Hipótese 4](img/hipotese4.png)

Hipótese 5. Clientes que compram mais carne também compram mais vinho.

![Hipótese 5](img/hipotese5.png)

# Insights da análise
### Visão geral da campanha de Marketing
![Visão Geral](img/visao-geral.png)

### Visão Clientes
![Visão Cliente](img/visao-clientes.png)

### Conclusão: Visão Resultado Cliente
![Visão Resultado Cliente](img/visao-clientes-completa.png)

### Conclusão: Visão Produto
![Visão Produto](img/visao-produto.png)

# Resultados
Conclusão: o melhor segmento da campanha foram os clientes casados com idade entre 41 e 50 anos de idade, sem filhos em casa em com graduação completa.

O pior segmento de clientes foram os viúvos de todas as faixas etárias, clientes abaixo dos 30 anos de todos os estados civis com 2 ou mais crianças em casa e somente ensino fundamental.

Para maximizar o lucro da próxima campanha, o marketing precisa direcionar suas ações ao melhor segmento apresentado e reduzir o investimento nos outros segmentos, especialmente o mencionado.

## Visualize a análise completa:
[Análise Completa](https://lookerstudio.google.com/reporting/9536ef1a-3c05-4347-b335-ae914e3c92d5)

# Próximos Passos
1. Explorar mais características ods clientes.
2. Automatizar a coleta e a análise para acompanhamento.
3. Agrupar os clientes em grupos de maior e menor faturamento para entender se há similaridades ou não.
4. Montar um dashboard de acompanhamento das métricas das futuras campanhas de marketing. -->