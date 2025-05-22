import os
import PyPDF2
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Ruta del dataset
DATASET_DIR = os.path.join(os.path.dirname(__file__), 'classifier_data')

texts = []
labels = []

# Recorremos cada subcarpeta (factura, boleta, informe, etc.)
for category in os.listdir(DATASET_DIR):
    category_path = os.path.join(DATASET_DIR, category)
    if os.path.isdir(category_path):
        for filename in os.listdir(category_path):
            if filename.endswith('.pdf'):
                file_path = os.path.join(category_path, filename)
                try:
                    with open(file_path, 'rb') as f:
                        reader = PyPDF2.PdfReader(f)
                        text = ''
                        for page in reader.pages:
                            page_text = page.extract_text()
                            if page_text:
                                text += page_text
                        texts.append(text)
                        labels.append(category)
                except Exception as e:
                    print(f"❌ Error procesando {file_path}: {e}")

# Entrenamiento del modelo
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)
y = labels

model = MultinomialNB()
model.fit(X, y)

# Guardamos el modelo y el vectorizador
with open('document_classifier.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)

print("✅ Modelo y vectorizador entrenados y guardados correctamente.")