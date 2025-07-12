#!/usr/bin/python3
"""
This script uses a REST API to retrieve and display the TODO list progress
of an employee based on their ID. It exports all tasks to a JSON file.

JSON Format:
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


def fetch_employee_todo_progress(employee_id):
    """
    Fetches and displays the TODO list progress for a given employee ID.

    Also writes all tasks to a JSON file.

    Args:
        employee_id (int): The ID of the employee.
    """
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todos_url = (
        f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    )

    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(f"Employee with ID {employee_id} not found.")
        return

    employee_data = user_response.json()
    employee_name = employee_data.get("name")
    username = employee_data.get("username")

    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]
    number_of_done_tasks = len(done_tasks)

    print(f"Employee {employee_name} is done with tasks ({number_of_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")

    # Prepare JSON structure
    json_data = {
        str(employee_id): [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
            }
            for task in todos
        ]
    }

    # Export to JSON file
    filename = f"{employee_id}.json"
    with open(filename, mode="w") as jsonfile:
        json.dump(json_data, jsonfile)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./todo.py <employee_id>")
        sys.exit(1)

    try:
        emp_id = int(sys.argv[1])
    except Val
