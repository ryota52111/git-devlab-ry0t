import json
import requests

response = requests.get("http://jsonplaceholder.typicode.com/todos")

todos = json.loads(response.text)
print(type(todos))
print(todos)

for task in tods:
    if task["completed"] == True:
        print(task)