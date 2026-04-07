from flask import Flask
from app.config.config import Config
from app.db import db

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

# Importa tus modelos para que se creen las tablas
from app.models.task_model import Task

@app.route("/")
def home():
    return {"message": "Task API working"}

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Crea la tabla tasks en task_db
    app.run(debug=True)