FROM python:3.9-slim

WORKDIR /app

# Install curl for debugging purposes
RUN apt-get update && apt-get install -y curl nano

# Copy the rpg-content-api requirements file
COPY rpg-content-api/requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the shared models and rpg-content-api files
COPY shared/models /app/models
COPY rpg-content-api /app

# Set the PYTHONPATH
ENV PYTHONPATH=/app:/app/models

CMD ["python", "run.py"]
