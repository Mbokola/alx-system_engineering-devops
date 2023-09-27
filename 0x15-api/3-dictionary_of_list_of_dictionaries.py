#!/usr/bin/python3
"""
2-export_to_JSON module
Python script that, using this [REST API](https://jsonplaceholder.typicode.com)
, for all employees, returns
information about his/her TODO list progress.
 export data in the JSON format.
"""

import json
import requests

if __name__ == "__main__":
    todo_url = "https://jsonplaceholder.typicode.com/todos"
    todo_url_response = requests.get(todo_url)
    todo_url_data = todo_url_response.json()
    for_export = {}
    users_url = "https://jsonplaceholder.typicode.com/users"
    users_response = requests.get(users_url)
    users_data = users_response.json()
    file_name = "todo_all_employees.json"

    for user in users_data:
        username = user['username']
        user_data = []
        user_id = user['id']

        for data in todo_url_data:
            if data['userId'] == user_id:
                dict_user_data = {
                        'username': username,
                        'task': data['title'],
                        'completed': data['completed']
                        }
                user_data.append(dict_user_data)
        for_export[str(user_id)] = user_data

    with open(file_name, 'w') as file:
        file.write(json.dumps(for_export))
