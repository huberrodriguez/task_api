import requests

# ======================================
# 1️⃣ LOGIN - Obtener token JWT
# ======================================
login_url = "http://127.0.0.1:5000/login"
login_data = {"username": "admin", "password": "1234"}

login_response = requests.post(login_url, json=login_data)
print("LOGIN:", login_response.status_code, login_response.json())

# Guardamos el token para usarlo en endpoints protegidos
token = login_response.json().get("access_token")
headers = {"Authorization": f"Bearer {token}"}

# ======================================
# 2️⃣ URL base de tareas
# ======================================
base_url = "http://127.0.0.1:5000/tasks"

# ======================================
# 3️⃣ Crear una nueva tarea (POST)
# ======================================
data = {"title": "Mi primera tarea", "description": "Probando POST"}
response = requests.post(base_url, json=data, headers=headers)
print("POST:", response.status_code, response.json())

# Guardamos el id de la tarea creada
task_id = response.json().get("id")

# ======================================
# 4️⃣ Ver todas las tareas (GET) - público
# ======================================
response = requests.get(base_url)
print("GET:", response.status_code, response.json())

# ======================================
# 5️⃣ Actualizar la tarea (PUT) - protegido
# ======================================
update_data = {"title": "Mi tarea actualizada", "completed": True}
response = requests.put(f"{base_url}/{task_id}", json=update_data, headers=headers)
print("PUT:", response.status_code, response.json())

# ======================================
# 6️⃣ Borrar la tarea (DELETE) - protegido
# ======================================
response = requests.delete(f"{base_url}/{task_id}", headers=headers)
print("DELETE:", response.status_code, response.json())

# ======================================
# 7️⃣ Ver todas las tareas después de borrar
# ======================================
response = requests.get(base_url)
print("GET después de DELETE:", response.status_code, response.json())