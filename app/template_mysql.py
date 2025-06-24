from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("MySQL JDBC Example") \
    .config("spark.driver.extraClassPath", "/drivers/mysql-connector-java-8.0.30.jar") \
    .getOrCreate()

url = "jdbc:mysql://mysql:3306/dados"  # <--- CORRETO!
tabela = "cliente"
usuario = "root"
senha = "root"

df = spark.read.format("jdbc") \
    .option("url", url) \
    .option("driver", "com.mysql.cj.jdbc.Driver") \
    .option("dbtable", tabela) \
    .option("user", usuario) \
    .option("password", senha) \
    .load()

df.show()