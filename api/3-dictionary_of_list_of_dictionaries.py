#!/usr/bin/python3
"""
Exports all tasks for all employees using a REST API
and saves them to a JSON file: todo_all_employees.json

Format:
{
  "USER_ID": [
    {
      "username": "USERNAME",
      "task": "TASK_TITLE",
      "completed": TASK_COMPLETED_STATUS
    },
    ...
  ],
  ...
}
"""

import json
import requests


def export_all_employees_tasks_to_json():
    """
    Fetches and writes all employees' tasks to todo_all_employees.json
    """
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users_response = requests.get(users_url)
    todos_response = requests.get(todos_url)

    if users_response.status_code != 200 or todos_response.status_code != 200:
        print("Failed to fetch data from the API.")
        return

    users = users_response.json()
    todos = todos_response.json()

    # Build dictionary with user_id as key and list of tasks as value
    all_tasks = {}

    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        user_tasks = [
            {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            for task in todos if task.get("userId") == user_id
        ]
        all_tasks[str(user_id)] = user_tasks

    # Write to JSON file
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_tasks, jsonfile)


if __name__ == "__main__":
    export_all_employees_tasks_to_json()
