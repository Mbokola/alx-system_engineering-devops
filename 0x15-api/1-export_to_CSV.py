#!/usr/bin/python3
"""
0-gather_data_from_an_API module
Python script that, using this [REST API](https://jsonplaceholder.typicode.com)
, for a given employee ID, returns
information about his/her TODO list progress.
"""

import csv
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

    csv_file = 'USER_ID.csv'
    data = []
    for csv_data in todo_json_data:
        data.append([employee_ID, username, csv_data['completed'],
                     csv_data['title']])
    with open(csv_file, mode='w') as file:
        writer = csv.writer(file)
        writer.writerows(data)
