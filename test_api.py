import requests

# URL base de tu API
base_url = "http://127.0.0.1:5000/tasks"

# 🔹 Crear una tarea nueva
data = {"title": "Mi primera tarea", "description": "Probando POST"}
response = requests.post(base_url, json=data)
print("POST:", response.json())

# 🔹 Ver todas las tareas
response = requests.get(base_url)
print("GET:", response.json())

# 🔹 Actualizar la tarea (PUT)
update_data = {"title": "Mi tarea actualizada", "completed": True}
response = requests.put(f"{base_url}/1", json=update_data)
print("PUT:", response.json())

# 🔹 Borrar la tarea (DELETE)
response = requests.delete(f"{base_url}/1")
print("DELETE:", response.json())

# 🔹 Ver todas las tareas después de borrar
response = requests.get(base_url)
print("GET después de DELETE:", response.json())