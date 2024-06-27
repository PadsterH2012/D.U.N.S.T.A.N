from flask import Blueprint, request, jsonify
import os
import tempfile
from .ai_agent_content_parser import (
    extract_text_from_pdf, extract_names, consolidate_names,
    process_character_details, generate_book_details, get_setting
)
from .models import SessionLocal

upload = Blueprint('upload', __name__)

@upload.route('/api/upload', methods=['POST'])
def upload_api():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    if file:
        # Save the file temporarily
        temp_dir = tempfile.gettempdir()
        temp_path = os.path.join(temp_dir, file.filename)
        file.save(temp_path)

        try:
            with open(temp_path, 'rb') as f:
                pdf_content = f.read()
            text = extract_text_from_pdf(pdf_content)
            names = extract_names(text)
            consolidated_names = consolidate_names(names)
            db_session = SessionLocal()
            ollama_url = get_setting('ollama_url', db_session)
            ollama_model = get_setting('ollama_model', db_session)
            book_details_dict = generate_book_details(text, db_session, ollama_url, ollama_model)
            characters = process_character_details(consolidated_names, db_session, book_details_dict, ollama_url, ollama_model)
            return jsonify({'characters': characters}), 200
        finally:
            # Ensure the temporary file is deleted
            os.remove(temp_path)
    return jsonify({'error': 'File processing failed'}), 500
