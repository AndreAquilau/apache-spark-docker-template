FROM openjdk:11-jdk-slim

RUN apt-get update && \
    apt-get install -y wget tar bash procps python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*
    
RUN wget https://downloads.apache.org/spark/spark-3.5.6/spark-3.5.6-bin-hadoop3.tgz && \
    tar xzf spark-3.5.6-bin-hadoop3.tgz -C /opt && \
    mv /opt/spark-3.5.6-bin-hadoop3 /opt/spark && \
    rm spark-3.5.6-bin-hadoop3.tgz

ENV SPARK_HOME=/opt/spark
ENV PATH=$PATH:/opt/spark/bin:/opt/spark/sbin

WORKDIR /opt/spark

CMD ["bash"]