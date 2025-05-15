from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'clave_secreta_segura'

from app import routes