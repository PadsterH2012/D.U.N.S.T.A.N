FROM python:3.9-slim

WORKDIR /app

ENV PYTHONPATH=/app

# Install curl for debugging purposes
RUN apt-get update && apt-get install -y curl

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Download the spaCy language model
RUN python -m spacy download en_core_web_sm

COPY . .

CMD ["python", "run.py"]
