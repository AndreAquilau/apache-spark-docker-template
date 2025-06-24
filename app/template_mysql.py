from pyspark.sql import SparkSession
from pyspark.sql.functions import upper, trim

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

sql = "(SELECT * FROM cliente WHERE nome = 'Ana Silva') AS clientes_ana"

df = spark.read.format("jdbc") \
    .option("url", url) \
    .option("driver", "com.mysql.cj.jdbc.Driver") \
    .option("user", usuario) \
    .option("password", senha) \
    .option("dbtable", sql) \
    .load()

df_transformado = df.withColumn('nome', upper(trim(df['nome'])))
df_transformado.show()


# Primeira consulta
sql1 = "(SELECT * FROM cliente WHERE nome = 'Ana Silva') AS clientes_sp"
df1 = spark.read.format("jdbc") \
    .option("url", url) \
    .option("driver", "com.mysql.cj.jdbc.Driver") \
    .option("user", usuario) \
    .option("password", senha) \
    .option("dbtable", sql1) \
    .load()

# Segunda consulta
sql2 = "(SELECT * FROM cliente WHERE nome = 'Ana Silva') AS clientes_rj"
df2 = spark.read.format("jdbc") \
    .option("url", url) \
    .option("driver", "com.mysql.cj.jdbc.Driver") \
    .option("user", usuario) \
    .option("password", senha) \
    .option("dbtable", sql2) \
    .load()


# INNER JOIN
df_join = df1.join(df2, df1.id == df2.id, 'inner')

# LEFT JOIN
df_join = df1.join(df2, df1.id == df2.id, 'left')

# RIGHT JOIN
df_join = df1.join(df2, df1.id == df2.id, 'right')

# FULL OUTER JOIN
df_join = df1.join(df2, df1.id == df2.id, 'outer')

df_join.show()