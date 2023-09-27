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
    todo_url = "https://jsonplaceholder.typicode.com/todos"
    users_url = "https://jsonplaceholder.typicode.com/users"
    todo_response = requests.get(todo_url)
    users_response = requests.get(users_url)
    if todo_response.status_code == 200 and users_response.status_code == 200:
        todo_json_data = todo_response.json()
        users_json_data = users_response.json()
        for user in users_json_data:
            if user['id'] == int(employee_ID):
                username = user['name']
        titles = [title['title'] for title in todo_json_data
                  if title['userId'] == int(employee_ID)
                  and title['completed'] is True]
        titles1 = [title['title'] for title in todo_json_data
                   if title['userId'] == int(employee_ID)]

        print(f"Employee {username} is done with tasks\
    ({len(titles)}/{len(titles1)}):")
        for title in titles:
            print(title)
