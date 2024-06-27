from flask import Flask, request, jsonify
from extractor.ai_agent_content_parser import (
    extract_text_from_pdf, extract_names, consolidate_names,
    process_character_details, generate_book_details, get_summary
)
from models.models import db, Character  # Importing from the shared models
from extractor.settings import get_setting
from extractor.upload_routes import upload
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Initialize Flask app
app = Flask(__name__, template_folder='extractor/templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@db:5432/gamedb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy with the app
db.init_app(app)

# Register the upload blueprint
app.register_blueprint(upload, url_prefix='/upload')

@app.route('/')
def home():
    return "Content Creator Home"

@app.route('/extract/characters', methods=['POST'])
def characters():
    with app.app_context():
        db.create_all()  # Ensure tables are created
        db.session.commit()
    
    try:
        # Get settings from the database
        ollama_url = get_setting('ollama_url', db.session)
        ollama_model = get_setting('ollama_model', db.session)
        app.logger.debug(f"Ollama URL: {ollama_url}")
        app.logger.debug(f"Ollama Model: {ollama_model}")

        if not ollama_url or not ollama_model:
            return "Ollama settings are not configured correctly.", 500

        # Check if a file is uploaded
        file = request.files.get('file')
        if not file:
            return "No file uploaded.", 400

        # Read and process the PDF content
        pdf_content = file.read()
        text = extract_text_from_pdf(pdf_content)

        # Extract names and consolidate them
        names = extract_names(text)
        consolidated_names = consolidate_names(names)

        # Generate book details and process character details
        book_details_dict = generate_book_details(text, db.session, ollama_url, ollama_model)
        processed_characters = process_character_details(consolidated_names, db.session, book_details_dict, ollama_url, ollama_model)

        return jsonify(processed_characters)
    finally:
        db.session.close()

@app.route('/extract/quests', methods=['POST'])
def quests():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files.get('file')
    if not file or file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Read and process the PDF content
    pdf_content = file.read()
    text = extract_text_from_pdf(pdf_content)

    try:
        # Get settings from the database
        ollama_url = get_setting('ollama_url', db.session)
        ollama_model = get_setting('ollama_model', db.session)
        summary = get_summary(text, db.session, ollama_url, ollama_model)
        return jsonify({"summary": summary})
    finally:
        db.session.close()

@app.route('/health')
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8001, debug=True)
