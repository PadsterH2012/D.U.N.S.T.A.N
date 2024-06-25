FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app app
COPY run.py run.py

CMD ["python", "run.py"]
