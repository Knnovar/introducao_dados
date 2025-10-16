# Databricks notebook source
# MAGIC %md
# MAGIC # **Introdução ao SQL**
# MAGIC
# MAGIC Para aproveitar todas as facilidades que o banco de dados nos fornece, faremos uma breve demonstração das funcionalidades mais basicas do SQL, a fim de explorar os dados e suas possibilidades

# COMMAND ----------

# MAGIC %md
# MAGIC ## É importante começar pelos fundamentos, afinal, o que significa SQL?
# MAGIC
# MAGIC SQL = Structured Query Language 
# MAGIC Traduzindo, o SQL é uma linguagem de programação com foco na exploração dos dados dentro dos diversos tipos de bases que existem por ai

# COMMAND ----------

# MAGIC %md
# MAGIC ## Conheça seus dados
# MAGIC Antes de iniciarmos a nossa análise de dados, é importante conehcer a base em que estaremos trabalhando, utilizaremos um comando do SQL chamada **describe**
# MAGIC
# MAGIC Comando este que exibirá a estrutura da tabela, contendo nome das colunas, partições e toda informação necessária para iniciar.
# MAGIC
# MAGIC Veja no exemplo prático a baixo:
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC describe default.titanic

# COMMAND ----------

# MAGIC %md
# MAGIC Agora que temos nossa estrutura de colunas, e tipos de data, podemos começar a explorar o significado de cada uma.
# MAGIC
# MAGIC ### **Vamos ao freestyle**:
# MAGIC
# MAGIC **PassengerId**: Nosso identificador unico de cada um dos passageiros, coluna essa que poderá ser utilizada para evitar valores duplicados.
# MAGIC
# MAGIC **Survived**: Identificador binario de sobreviventes, percebemos que esta como bigint na coluna data_type, logo, nossas opções de valores na coluna são limitadas a números. (0 = Não, 1 = Sim)
# MAGIC
# MAGIC **Pclass**: Identificador da Classe em que o passageiro estava dentro do navio, é uma ótima coluna para fazer um batimento com os sobreviventes, e retirar uma base de quantos sobreviventes por classe, lembrando que temos 3 classes diferentes dentro do dataset. 
# MAGIC
# MAGIC Name: Nome dos passageiros
# MAGIC
# MAGIC Age: Idade dos Passageiros
# MAGIC
# MAGIC SibSp: Numéro de irmãos a bordo
# MAGIC
# MAGIC Parch: Número de Pais e filhos a bordo
# MAGIC
# MAGIC Ticket: Identificador da passagem
# MAGIC
# MAGIC Fare: Preço de passagem
# MAGIC
# MAGIC Cabin: Cabine do passageiro
# MAGIC
# MAGIC Embarked: Local onde o passageiro embarcou no titanic, sendo dividido entre as cidades. (C = Cherbourg, Q = Queenstown, S = Southamption)

# COMMAND ----------

# MAGIC %md
# MAGIC # Destrinchando o SQL
# MAGIC
# MAGIC Diferente de uma linguagem de programação convencional, o SQL contém uma sintaxe mais próxima de nosso vocabulario.
# MAGIC
# MAGIC Sua estrutura básica para visualização dos dados envolve os comandos:
# MAGIC
# MAGIC ----------------------**BASICO**-------------------------------------------
# MAGIC
# MAGIC **SELECT** - Comando que utilizaremos para selecionar quais colunas serão exibidas e processadas na nossa Query
# MAGIC
# MAGIC **FROM** - Comando que é responsável por selecionar qual tabela será utilizada como fonte dos dados
# MAGIC
# MAGIC **WHERE** - Comando que será utilizado como filtro, onde realizaremos a limpeza dos nossos dados
# MAGIC
# MAGIC ----------------------**INTERMEDIARIO**-------------------------------------
# MAGIC
# MAGIC **JOIN** - Comando utilizado para realizar validações cruzadas e batimento de tabelas, utiliza a teoria dos conjuntos como base para funcionamento.
# MAGIC
# MAGIC **GROUP BY** - Comando utilizado para realizar o agrupamento dos dados a partir de alguma função como trazendo o valor maximo ou minimo de uma coluna 
# MAGIC
# MAGIC **ORDER BY** - Comando utilizado para ordenar a visualização dos dados a partir de uma coluna (Podemos utilizar uma coluna de data ou de idade como exemplo de visualização)
# MAGIC
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### Vamos a prática 
# MAGIC Como não há melhor professor que a prática, realizaremos nosso primeiro SELECT para verificar os dados contidos em cada uma das colunas do nosso dataset
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC *
# MAGIC FROM default.titanic

# COMMAND ----------

# MAGIC %md
# MAGIC O que está acontecendo a partir desse código?
# MAGIC
# MAGIC Como visto anteriormente, o comando select traz as colunas selecionadas para a visualização, utilizamos o * como um identificador para "Tudo", então teremos a visualização de todas as colunas sem a necessidade de chamar uma por uma.
# MAGIC
# MAGIC o comando FROM é de onde realizaremos a extração da informação, nesse caso, do DATABASE Default, extrairemos a tabela titanic.
# MAGIC
# MAGIC Com isto visualizamos 2 dos 3 comandos basicos, bora ver como o **WHERE** funciona.

# COMMAND ----------

# MAGIC %md
# MAGIC Suponhamos que, precisamos fazer um balanço de quantos sobreviventes houveram deste acidente, vamos há validação.

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC   count(PassengerId) as Sobreviventes
# MAGIC FROM default.titanic
# MAGIC WHERE Survived = 1

# COMMAND ----------

# MAGIC %md
# MAGIC Bom, vamos a explicação
# MAGIC
# MAGIC Usamos o comando count() na coluna PassengerID (Que é o identificador unico dos passageiros) e utilizamos o "as" para renomear a coluna.
# MAGIC
# MAGIC Utilizamos o Where Survived = 1 para filtrar apenas os passageiros que sobreviveram.
# MAGIC
# MAGIC é uma validação descente para o problema proposto, mas vamos deixar um pouco mais interessante?

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC   Survived,
# MAGIC   count(PassengerId) as Quantidade_Passageiros
# MAGIC FROM default.titanic
# MAGIC Group BY Survived
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Utilizamos o Group BY para agrupar os dados por cada referencia dos sobreviventes, isto é, 0 e 1, conseguimos uma visualização melhor do total de sobreviventes.