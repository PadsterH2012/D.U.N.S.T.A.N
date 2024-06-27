from flask import Blueprint, render_template, request, flash, jsonify
import requests
from .forms import UploadForm
from .models import db, Character
import os

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
                # Send the file to content-creator service
                response = requests.post('http://content-creator:8001/upload/api/upload', files={'file': file})
                if response.status_code == 200:
                    characters = response.json().get('characters', {})
                    print("Characters received:", characters)  # Debug print to verify received data

                    # Add IDs to characters if they do not exist
                    for idx, (key, character) in enumerate(characters.items(), start=1):
                        character['id'] = idx

                    return render_template('characters.html', characters=characters)
                else:
                    flash('File processing failed', 'danger')
        else:
            print("Form validation failed")
            for field, errors in form.errors.items():
                for error in errors:
                    print(f"Error in {field}: {error}")
            flash('Form validation failed', 'danger')
    return render_template('upload.html', form=form)

@upload.route('/api/save_characters', methods=['POST'])
def save_characters_api():
    data = request.json
    character_ids = data.get('character_ids', [])
    
    print("Received character IDs:", character_ids)  # Debug log to verify received data
    
    if not character_ids or not all(character_ids):
        print("No valid character IDs provided")  # Debug log
        return jsonify({'error': 'No valid character IDs provided'}), 400
    
    try:
        # Assuming you have a way to fetch characters by their IDs
        characters = Character.query.filter(Character.id.in_(character_ids)).all()
        print("Fetched characters from DB:", characters)  # Debug log to verify fetched characters
        # Do something with characters, e.g., mark them as saved or update
        for character in characters:
            character.saved = True  # Example field
            print(f"Updated character {character.id}: {character.name}")  # Debug log for each updated character
        db.session.commit()
        print("Commit successful")  # Debug log for successful commit
        return jsonify({'success': True}), 200
    except Exception as e:
        db.session.rollback()
        print("Error during DB transaction:", str(e))  # Debug log for errors
        return jsonify({'error': str(e)}), 500
    finally:
        db.session.close()
