from flask import render_template, request, redirect, url_for
from app import app

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uploaded_file = request.files.get('file')
        if uploaded_file:
            uploaded_file.save(f'uploads/{uploaded_file.filename}')
            return redirect(url_for('result', filename=uploaded_file.filename))
    return render_template('index.html')

@app.route('/resultado/<filename>')
def result(filename):
    return render_template('result.html', filename=filename)