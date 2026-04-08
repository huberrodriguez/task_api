Task API - Prueba Técnica
Descripción
API REST para gestionar tareas simples. Permite operaciones CRUD y consumo de API externa.

Tecnologías
Python 3
Flask
Flask SQLAlchemy
Flask JWT Extended
PostgreSQL
Requests
Instalación
Clonar el repositorio:
git clone https://github.com/huberrodriguez/task_api.git
cd task_api
Crear entorno virtual:
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # Linux/Mac
Instalar dependencias:
pip install -r requirements.txt
Configuración

Variables importantes:

class Config:
    SECRET_KEY = "mi_clave_secreta"
    SQLALCHEMY_DATABASE_URI =     "postgresql://postgres:159357@localhost:5432/task_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "mi_jwt_secreto"

Archivo: app/config/config.py

Base de datos

Crear la base de datos task_db en PostgreSQL.python main.py

Esto ejecuta db.create_all() y crea la tabla tasks.

Luego correr migraciones:

python
>>> from main import db
>>> db.create_all()
Endpoints
Login
POST /login
JSON
{
  "username": "admin",
  "password": "1234"
}
Retorna token JWT

Método	Ruta	Descripción	Requiere Token
GET	/tasks	Listar tareas	
POST	/tasks	Crear tarea	
PUT	/tasks/<id>	Actualizar tarea	
DELETE	/tasks/<id>	Borrar tarea	
GET	/external-tasks	Obtener tareas externas	
POST	/login	Obtener token JWT	
Ejecución
python main.py


Servidor por defecto: http://127.0.0.1:5000

Tests

Para probar la API:

python test_api.py
Extras
Código organizado en módulos (models, config, db)
Uso de JWT para endpoints protegidos
Integración con API externa JSONPlaceholderAutor

Huber Rodriguez
Repositorio: https://github.com/huberrodriguez/task_api