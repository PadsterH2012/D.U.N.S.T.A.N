FROM python:3.9-slim

WORKDIR /app

# Install curl for debugging purposes
RUN apt-get update && apt-get install -y curl

# Copy the content_creator requirements file
COPY content_creator/requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Download the spaCy language model
RUN python -m spacy download en_core_web_sm

# Copy the shared models and content creator files
COPY shared/models /app/models
COPY content_creator /app

# Set the PYTHONPATH
ENV PYTHONPATH=/app:/app/models

CMD ["python", "run.py"]
