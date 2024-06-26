from flask import Flask, request, jsonify, render_template
from extractor.ai_agent_content_parser import extract_text_from_pdf, extract_names, consolidate_names, process_character_details, generate_book_details, get_summary
from extractor.models import SessionLocal
import os

app = Flask(__name__, template_folder='extractor/templates')

@app.route('/')
def home():
    return "Content Creator Home"

@app.route('/extract/characters', methods=['POST'])
def characters():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file:
        pdf_content = file.read()
        text = extract_text_from_pdf(pdf_content)
        names = extract_names(text)
        consolidated_names = consolidate_names(names)
        db = SessionLocal()
        book_details_dict = generate_book_details(text, db)
        processed_characters = process_character_details(consolidated_names, db, book_details_dict)
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
        summary = get_summary(text, db)
        return jsonify({"summary": summary})

@app.route('/upload')
def upload_page():
    return render_template('upload.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8001, debug=True)
