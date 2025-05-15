from flask import render_template, request, redirect, url_for
from app import app
from app.utils import extract_text_from_pdf
import os

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uploaded_file = request.files.get('file')
        if uploaded_file:
            upload_path = os.path.join('uploads', uploaded_file.filename)
            uploaded_file.save(upload_path)
            return redirect(url_for('result', filename=uploaded_file.filename))
    return render_template('index.html')

@app.route('/resultado/<filename>')
def result(filename):
    file_path = os.path.join('uploads', filename)
    content = extract_text_from_pdf(file_path)
    
    # Por ahora, sin clasificar, solo mostramos el texto
    return render_template('result.html', filename=filename, content=content)