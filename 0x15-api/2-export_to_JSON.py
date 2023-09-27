#!/usr/bin/python3
"""
2-export_to_JSON module
Python script that, using this [REST API](https://jsonplaceholder.typicode.com)
, for a given employee ID, returns
information about his/her TODO list progress.
 export data in the JSON format.
"""

import json
import requests
import sys

if __name__ == "__main__":
    employee_ID = sys.argv[1]
    todo_url = f"https://jsonplaceholder.typicode.com/todos?\
userId={employee_ID}"
    users_url = f"https://jsonplaceholder.typicode.com/users?id={employee_ID}"
    todo_response = requests.get(todo_url)
    users_response = requests.get(users_url)
    json_file = f"{employee_ID}.json"
    if all(response.status_code == 200 for response in
           (todo_response, users_response)):
        todo_json_data = todo_response.json()
        users_json_data = users_response.json()
        username = users_json_data[0]['username']
        to_export = []

    for data in todo_json_data:
        json_reresenation = {
            "task": data["title"],
            "completed": data["completed"],
            "username": username
            }
        to_export.append(json_reresenation)

    dict_data = {f"{employee_ID}": to_export}

    with open(json_file, 'w') as file:
        file.write(json.dumps(dict_data))
