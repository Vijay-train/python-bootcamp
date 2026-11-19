import json

student = {"name": "Asha", "age": 17,
           "enrolled": True, "marks": None}
print(type(student))

text = json.dumps(student)
print(type(text))
print(text)
print(type(text))

back = json.loads(text)
print(back["name"], type(back))
