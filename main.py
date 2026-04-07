from flask import Flask, request
from app.config.config import Config
from app.db import db

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

# Importa tus modelos para que se creen las tablas
from app.models.task_model import Task

# 🌟 Ruta inicial
@app.route("/")
def home():
    return {"message": "Task API working"}

# 🚀 Ruta para listar todas las tareas
@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()  # Trae todas las tareas de la base de datos
    return {"tasks": [t.to_dict() for t in tasks]}  # Devuelve en JSON

# 🚀 Ruta para crear una tarea nueva
@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()  # Obtiene los datos enviados en JSON
    if not data or "title" not in data:
        return {"error": "title is required"}, 400  # Validación simple

    new_task = Task(
        title=data.get("title"),
        description=data.get("description")  # Descripción opcional
    )
    db.session.add(new_task)
    db.session.commit()  # Guarda la tarea en la base de datos
    return new_task.to_dict(), 201  # Devuelve la tarea creada con código 201

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Crea la tabla tasks en task_db si no existe
    app.run(debug=True)