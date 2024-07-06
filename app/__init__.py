from flask import Flask
from app.routes import bp  # Blueprint

app = Flask(__name__)
app.register_blueprint(bp)  # Register Blueprint with the app
