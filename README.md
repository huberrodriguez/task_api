# Task API - Prueba Técnica

## Descripción
API REST para gestionar tareas simples. Permite operaciones CRUD y consumo de API externa.

## Tecnologías
- Python 3
- Flask
- Flask SQLAlchemy
- Flask JWT Extended
- PostgreSQL
- Requests

## Instalación

1. Clonar el repositorio:

```bash
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

SECRET_KEY - Clave secreta de Flask
SQLALCHEMY_DATABASE_URI - Conexión a PostgreSQL
JWT_SECRET_KEY - Clave para JWT

Archivo: app/config/config.py

Base de datos

Crear la base de datos task_db en PostgreSQL.
Luego correr migraciones:

python
>>> from main import db
>>> db.create_all()
Endpoints
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
Integración con API externa JSONPlaceholder
