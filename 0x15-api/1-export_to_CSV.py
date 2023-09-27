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
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId=\
{employee_ID}"
    users_url = f"https://jsonplaceholder.typicode.com/users?id={employee_ID}"
    todo_response = requests.get(todo_url)
    users_response = requests.get(users_url)
    if todo_response.status_code == 200 and users_response.status_code == 200:
        todo_json_data = todo_response.json()
        users_json_data = users_response.json()
        username = users_json_data[0]['username']

    csv_file = f'{employee_ID}.csv'
    data = []
    for csv_data in todo_json_data:
        data.append([employee_ID, username, csv_data['completed'],
                     csv_data['title']])
    with open(csv_file, mode='w') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerows(data)
