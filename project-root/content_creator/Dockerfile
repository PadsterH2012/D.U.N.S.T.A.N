FROM python:3.9-slim

WORKDIR /app

ENV PYTHONPATH=/app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Download the spaCy language model
RUN python -m spacy download en_core_web_sm

COPY . .

CMD ["python", "run.py"]