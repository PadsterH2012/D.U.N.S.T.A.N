from flask import Blueprint, render_template, request, flash
import requests
from .forms import UploadForm
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
                    characters = response.json().get('characters', [])
                    print("Characters received:", characters)  # Debug print to verify received data
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

