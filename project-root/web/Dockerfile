FROM python:3.9-slim

WORKDIR /app

COPY web/requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the app directory
COPY app app

# Copy the run.py file
COPY run.py run.py

CMD ["python", "run.py"]
