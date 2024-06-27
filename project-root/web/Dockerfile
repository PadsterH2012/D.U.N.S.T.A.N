FROM python:3.9-slim

WORKDIR /app

# Install curl for debugging purposes
RUN apt-get update && apt-get install -y curl

# Copy the web requirements file
COPY web/requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the shared models and web files
COPY shared/models /app/models
COPY web /app

# Set the PYTHONPATH
ENV PYTHONPATH=/app:/app/models

CMD ["python", "run.py"]
