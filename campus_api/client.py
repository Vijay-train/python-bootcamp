import requests

BASE = "http://127.0.0.1:8000"

response = requests.post(BASE + "/tasks", json={"title": ""})
print(response.status_code)
print(response.json())
