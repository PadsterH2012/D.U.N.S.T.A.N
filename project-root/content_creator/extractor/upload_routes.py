from flask import Blueprint, render_template, request
from .forms import UploadForm
from .models import SessionLocal
from .ai_agent_content_parser import (
    extract_text_from_pdf, extract_names, consolidate_names,
    process_character_details, generate_book_details, get_setting
)

upload = Blueprint('upload', __name__)

@upload.route('/upload', methods=['GET', 'POST'])
def upload_page():
    print("Inside upload_page route")
    form = UploadForm()
    if request.method == 'POST':
        print("Received POST request")
        if form.validate_on_submit():
            print("Form validated successfully")
            file = form.file.data
            if file:
                print("File received:", file.filename)
                pdf_content = file.read()
                text = extract_text_from_pdf(pdf_content)
                names = extract_names(text)
                consolidated_names = consolidate_names(names)
                db_session = SessionLocal()
                ollama_url = get_setting('ollama_url', db_session)
                ollama_model = get_setting('ollama_model', db_session)
                book_details_dict = generate_book_details(text, db_session, ollama_url, ollama_model)
                characters = process_character_details(consolidated_names, db_session, book_details_dict, ollama_url, ollama_model)
                return render_template('characters.html', characters=characters)
    return render_template('upload.html', form=form)
