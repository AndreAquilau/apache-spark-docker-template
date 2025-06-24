from pyspark.sql import SparkSession

# Cria uma SparkSession
spark = SparkSession.builder.appName("HelloWorld").getOrCreate()

# Exemplo básico: criar um DataFrame e exibir na tela
data = [("Hello, World!",)]
df = spark.createDataFrame(data, ["mensagem"])

df.show()

spark.stop()