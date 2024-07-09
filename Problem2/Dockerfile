FROM python:3.11-slim

# Install necessary tools and Java (OpenJDK 17)
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        wget \
        gnupg \
        ca-certificates \
        procps \
    && apt-get install -y openjdk-17-jdk \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set JAVA_HOME environment variable
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-arm64
ENV PATH=$JAVA_HOME/bin:$PATH

# Verify JAVA_HOME is correctly set
RUN echo $JAVA_HOME && ls -l $JAVA_HOME/bin/java

WORKDIR /problem2

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["sh", "-c", "python generateCSV.py && python anonymiseData.py"]
