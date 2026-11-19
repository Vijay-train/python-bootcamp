import requests
 
BASE = "http://127.0.0.1:8000"

 

body = {"title": "Do homework", "done": False}
response = requests.post(BASE + "/tasks", json=body)
print(response.status_code, response.json())

body = {"title": "updated from python code", "done": False}
response = requests.put(BASE + "/tasks/2", json=body)
print(response.status_code, response.json())

response = requests.delete(BASE + "/tasks/2")
print(response.status_code)




# http://127.0.0.1/square/info