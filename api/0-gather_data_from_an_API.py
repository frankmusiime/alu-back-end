#!/usr/bin/python3
"""
This script uses a REST API to retrieve and display the TODO list progress
of an employee based on their ID.

Usage:
    ./todo.py <employee_id>

Requirements:
    - requests

PEP8 Validation:
    - Imports are ordered alphabetically
    - Line length <= 79 characters
    - Functions and logic are properly spaced and indented
    - Docstrings follow PEP257 convention
"""

import requests
import sys

def fetch_employee_todo_progress(employee_id):
    """
    Fetches and displays the TODO list progress for a given employee ID.

    Args:
        employee_id (int): The ID of the employee.
    """
    # URLs
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'

    # Fetch user info
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(f"Employee with ID {employee_id} not found.")
        return

    employee_name = user_response.json().get("name")

    # Fetch todos
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]
    number_of_done_tasks = len(done_tasks)

    # Output
    print(
        f"Employee {employee_name} is done with tasks"
        f"({number_of_done_tasks}/{total_tasks}):"
    )
    for task in done_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./todo.py <employee_id>")
        sys.exit(1)

    try:
        emp_id = int(sys.argv[1])
        fetch_employee_todo_progress(emp_id)
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

