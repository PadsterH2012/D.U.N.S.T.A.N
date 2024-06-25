import os
import requests
from PyPDF2 import PdfReader

def process_pdf(filepath):
    # Extract text from PDF
    with open(filepath, 'rb') as file:
        pdf = PdfReader(file)
        text = ""
        for page in pdf.pages:
            text += page.extract_text()

    # Process text with Ollama
    ollama_url = os.getenv('OLLAMA_URL')
    ollama_model = os.getenv('OLLAMA_MODEL')
    
    prompt = f"Extract and categorize rules from the following text:\n\n{text}"
    
    response = requests.post(
        f"{ollama_url}/api/generate",
        json={
            "model": ollama_model,
            "prompt": prompt,
            "stream": False
        }
    )
    
    if response.status_code == 200:
        return response.json()['response']
    else:
        return "Error processing PDF"
