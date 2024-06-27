FROM python:3.9-slim

WORKDIR /app

# Install curl
RUN apt-get update && apt-get install -y curl nano

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

EXPOSE 8000

CMD ["python", "run.py"]
