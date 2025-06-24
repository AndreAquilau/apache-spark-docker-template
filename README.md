# Spark + MySQL Docker Template

Este projeto é um template para integração entre Apache Spark e MySQL utilizando Docker e Docker Compose. O objetivo é facilitar o desenvolvimento e testes de pipelines PySpark que interagem com bancos relacionais via JDBC.

## Tecnologias

- Apache Spark 3.5.x
- MySQL 8.x
- Docker & Docker Compose
- JDBC Driver MySQL

## Como usar
docker network create rede_spark

docker network connect rede_spark mysql
docker network connect rede_spark mongodb
docker network connect rede_spark spark-submit
docker network connect rede_spark spark-worker
docker network connect rede_spark spark-master

docker network inspect rede_spark

# Agora dentro do container
docker exec -it spark-submit bash

cp /drivers/mysql-connector-java-8.0.30.jar /opt/spark/jars/

spark-submit /app/template_mysql.py
