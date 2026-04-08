from flask import Flask, request
from app.config.config import Config
from app.db import db
import requests  # Para consumir la API externa
from flask_jwt_extended import JWTManager, create_access_token, jwt_required

app = Flask(__name__)
app.config.from_object(Config)

# Inicializa la base de datos
db.init_app(app)

# Inicializa JWT
jwt = JWTManager(app)

# Importa el modelo Task para crear la tabla
from app.models.task_model import Task

#  Ruta inicial
@app.route("/")
def home():
    return {"message": "Task API working"}

# Login simple para obtener token JWT
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    
    # Usuario fijo para la prueba
    if username == "admin" and password == "1234":
        access_token = create_access_token(identity=username)
        return {"access_token": access_token}, 200
    else:
        return {"error": "Usuario o contraseña incorrectos"}, 401

#  Listar todas las tareas (público)
@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()
    return {"tasks": [t.to_dict() for t in tasks]}

#  Crear una nueva tarea (protegido)
@app.route("/tasks", methods=["POST"])
@jwt_required()
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

#  Actualizar una tarea existente (protegido)
@app.route("/tasks/<int:task_id>", methods=["PUT"])
@jwt_required()
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

# Borrar una tarea (protegido)
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
@jwt_required()
def delete_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return {"error": "Task not found"}, 404

    db.session.delete(task)
    db.session.commit()
    return {"message": "Task deleted successfully"}

# Nuevo endpoint para consumir API externa
@app.route("/external-tasks", methods=["GET"])
def get_external_tasks():
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/todos")
        response.raise_for_status()
        data = response.json()
        # Solo devolver los primeros 5 para no saturar
        return {"external_tasks": data[:5]}, 200
    except requests.exceptions.RequestException as e:
        return {"error": "No se pudo obtener la información externa", "details": str(e)}, 500

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Asegura que la tabla tasks exista
    app.run(debug=True)