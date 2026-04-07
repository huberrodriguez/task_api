from flask import Flask, request
from app.config.config import Config
from app.db import db

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

# Importa el modelo Task para crear la tabla
from app.models.task_model import Task

# 🌟 Ruta inicial
@app.route("/")
def home():
    return {"message": "Task API working"}

# 🚀 Listar todas las tareas
@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()
    return {"tasks": [t.to_dict() for t in tasks]}

# 🚀 Crear una nueva tarea
@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    if not data or "title" not in data:
        return {"error": "title is required"}, 400

    new_task = Task(
        title=data.get("title"),
        description=data.get("description")
    )
    db.session.add(new_task)
    db.session.commit()
    return new_task.to_dict(), 201

# 🚀 Actualizar una tarea existente
@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return {"error": "Task not found"}, 404

    data = request.get_json()
    task.title = data.get("title", task.title)
    task.description = data.get("description", task.description)
    task.completed = data.get("completed", task.completed)
    db.session.commit()
    return task.to_dict()

# 🚀 Borrar una tarea
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return {"error": "Task not found"}, 404

    db.session.delete(task)
    db.session.commit()
    return {"message": "Task deleted successfully"}

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Asegura que la tabla tasks exista
    app.run(debug=True)