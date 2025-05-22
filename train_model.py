# train_model.py
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# Datos de entrenamiento (puedes personalizar o extender)
X_train = [
    "Informe de actividades realizadas durante el mes de abril",
    "Carta de solicitud de vacaciones",
    "Boleta de pago correspondiente a marzo",
    "Informe financiero anual",
    "Carta de renuncia",
    "Boleta de pago del mes de febrero"
]

y_train = [
    "informe",
    "carta",
    "boleta",
    "informe",
    "carta",
    "boleta"
]

# Crear y entrenar el modelo
model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(X_train, y_train)

# Guardar el modelo entrenado
with open('document_classifier.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Modelo entrenado y guardado como document_classifier.pkl")