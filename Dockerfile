FROM python:3.11-slim

# establish the working dir for the container
WORKDIR /app

# let's install git
RUN apt-get update && \
    apt-get install -y git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src

# let's copy the service account JSON to the container
COPY sa-order-generator.json ./sa-order-generator.json

EXPOSE 8080

ENV GOOGLE_APPLICATION_CREDENTIALS="sa-order-generator.json"

# execute the python app
CMD ["python", "src/main.py"]