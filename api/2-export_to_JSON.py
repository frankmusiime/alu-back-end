#!/usr/bin/python3
"""
This script retrieves an employee's TODO list from a REST API
and exports all of the employee's tasks to a JSON file.

Format:
{
  "USER_ID": [
    {
      "task": "TASK_TITLE",
      "completed": TASK_COMPLETED_STATUS,
      "username": "USERNAME"
    },
    ...
  ]
}
"""

import json
import requests
import sys


def export_employee_tasks_to_json(employee_id):
    """
    Exports all tasks of a specific employee into USER_ID.json

    Args:
        employee_id (int): The ID of the employee.
    """
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'

    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(f"Employee with ID {employee_id} not found.")
        return

    user_data = user_response.json()
    username = user_data.get("username")

    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Prepare data
    user_tasks = [
        {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        }
        for task in todos
    ]

    json_data = {str(employee_id): user_tasks}

    # Write to JSON file
    filename = f"{employee_id}.json"
    with open(filename, "w") as jsonfile:
        json.dump(json_data, jsonfile)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        emp_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    export_employee_tasks_to_json(emp_id)
