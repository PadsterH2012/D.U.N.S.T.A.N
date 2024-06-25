from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import os
from dotenv import load_dotenv
from pdf_processor import process_pdf

load_dotenv()

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'})
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No selected file'})
        if file and file.filename.endswith('.pdf'):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            results = process_pdf(filepath)
            return render_template('results.html', results=results)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)