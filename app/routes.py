from app import app 
from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename
import PyPDF2
import pickle

# Ruta donde está el modelo entrenado
MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'document_classifier.pkl')

# Cargar modelo entrenado
with open(MODEL_PATH, 'rb') as f:
    model = pickle.load(f)

# Configuración de la carpeta de subida
UPLOAD_FOLDER = os.path.join('static', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Inicialización de Flask
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    print("✅ Entrando a la ruta principal '/'")  # Depuración
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            filename = secure_filename(uploaded_file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            uploaded_file.save(file_path)

            # Extraer texto del PDF
            with open(file_path, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                content = ""
                for page in reader.pages:
                    content += page.extract_text() or ""

            # Clasificar el contenido
            predicted_category = model.predict([content])[0]

            return render_template('result.html',
                                   filename=filename,
                                   content=content,
                                   category=predicted_category)

    return render_template('index.html')

@app.route('/result')
def result():
    print("🧪 Entrando a la ruta /result")
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)