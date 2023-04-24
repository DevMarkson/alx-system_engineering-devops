#!/usr/bin/python3
import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python script.py <employee_id>")
    sys.exit()

employee_id = sys.argv[1]

# Retrieve employee name
response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
employee_name = response.json()["name"]

# Retrieve employee's todo_lists
response = requests.get(f"https://jsonplaceholder.typicode.com/todo_lists?userId={employee_id}")
todo_lists = response.json()

# Count number of completed and total tasks
num_completed_tasks = 0
total_num_tasks = len(todo_lists)
completed_task_titles = []
for todo in todo_lists:
    if todo["completed"]:
        num_completed_tasks += 1
        completed_task_titles.append(todo["title"])

# Display todo list progress
print(f"Employee {employee_name} is done with tasks({num_completed_tasks}/{total_num_tasks}):")
for title in completed_task_titles:
    print(f"\t- {title}")
