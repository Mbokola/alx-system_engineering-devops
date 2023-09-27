#!/usr/bin/python3
"""
0-gather_data_from_an_API module
Python script that, using this [REST API](https://jsonplaceholder.typicode.com)
, for a given employee ID, returns
information about his/her TODO list progress.
"""

import requests
import sys

if __name__ == "__main__":
    employee_ID = sys.argv[1]
    true_todo_url = f"https://jsonplaceholder.typicode.com/todos?\
userId={employee_ID}&completed=true"
    todo_url = f"https://jsonplaceholder.typicode.com/todos?\
userId={employee_ID}"
    users_url = f"https://jsonplaceholder.typicode.com/users?id={employee_ID}"
    todo_response = requests.get(todo_url)
    users_response = requests.get(users_url)
    true_todo_url_response = requests.get(true_todo_url)
    if all(response.status_code == 200 for response in
           (todo_response, users_response, true_todo_url_response)):
        todo_json_data = todo_response.json()
        users_json_data = users_response.json()
        true_todo_url_data = true_todo_url_response.json()
        username = users_json_data[0]['name']

        print(f"Employee {username} is done with tasks\
({len(true_todo_url_data)}/{len(todo_json_data)}):")
        for title in true_todo_url_data:
            print(f"\t {title['title']}")
