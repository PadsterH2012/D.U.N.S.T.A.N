FROM python:3.9-slim

WORKDIR /app

ENV PYTHONPATH=/app:/app/content_creator:/app/content_creator/extractor

COPY web/requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Download the spaCy language model
RUN python -m spacy download en_core_web_sm

# Copy the app directory
COPY web/app app

# Explicitly copy the content_creator directory and add an empty __init__.py file
COPY content_creator content_creator
RUN touch /app/content_creator/__init__.py

# Copy the run.py file
COPY web/run.py run.py

# Print PYTHONPATH and list contents of /app directory during build
RUN echo "PYTHONPATH is set to: $PYTHONPATH" && ls -la /app && ls -la /app/content_creator

CMD PYTHONPATH=$PYTHONPATH python run.py
