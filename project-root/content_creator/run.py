from flask import Flask, request, jsonify, render_template
from extractor.ai_agent_content_parser import extract_text_from_pdf, extract_names, consolidate_names, process_character_details, generate_book_details, get_summary
from extractor.models import SessionLocal
from extractor.settings import get_setting
from api.endpoints import api  # Import the blueprint
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__, template_folder='extractor/templates')
app.register_blueprint(api)  # Register the blueprint

@app.route('/')
def home():
    return "Content Creator Home"

@app.route('/extract/characters', methods=['POST'])
def characters():
    db = SessionLocal()
    ollama_url = get_setting('ollama_url', db)
    ollama_model = get_setting('ollama_model', db)
    app.logger.debug(f"Ollama URL: {ollama_url}")
    app.logger.debug(f"Ollama Model: {ollama_model}")

    if not ollama_url or not ollama_model:
        return "Ollama settings are not configured correctly.", 500

    file = request.files['file']
    if not file:
        return "No file uploaded.", 400

    pdf_content = file.read()
    text = extract_text_from_pdf(pdf_content)

    names = extract_names(text)
    consolidated_names = consolidate_names(names)

    book_details_dict = generate_book_details(text, db, ollama_url, ollama_model)
    processed_characters = process_character_details(consolidated_names, db, book_details_dict, ollama_url, ollama_model)

    return jsonify(processed_characters)

@app.route('/extract/quests', methods=['POST'])
def quests():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file:
        pdf_content = file.read()
        text = extract_text_from_pdf(pdf_content)
        db = SessionLocal()
        ollama_url = get_setting('ollama_url', db)
        ollama_model = get_setting('ollama_model', db)
        summary = get_summary(text, db, ollama_url, ollama_model)
        return jsonify({"summary": summary})

@app.route('/health')
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8001, debug=True)
