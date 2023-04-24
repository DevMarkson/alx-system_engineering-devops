# README

## Task Description

The task involves writing a Python script that gathers data from a REST API. The script returns information about the progress of the TODO list of a given employee ID. The script should display the employee TODO list progress in a specific format, as well as export data in CSV and JSON formats.

### Gathering Data from API

- The script uses the `urllib` or `requests` module.
- It accepts an integer as a parameter, which is the employee ID.
- It displays on the standard output the employee TODO list progress in the following format:

```
Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
```
- EMPLOYEE_NAME is the name of the employee
- NUMBER_OF_DONE_TASKS is the number of completed tasks
- TOTAL_NUMBER_OF_TASKS is the total number of tasks, which is the sum of completed and non-completed tasks
- The second and N next lines display the title of completed tasks in the following format:

```
    TASK_TITLE
```

### Export to CSV

- The script exports data in CSV format.
- It records all tasks that are owned by an employee.
- The format of each row is:

```
USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE
```

- The file name must be in the format USER_ID.csv

### Export to JSON

- The script exports data in JSON format.
- It records all tasks that are owned by an employee.
- The format of each row is:

```
{"USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}
```

- The file name must be in the format USER_ID.json

### Dictionary of List of Dictionaries

- The script exports data in JSON format.
- It records all tasks from all employees.
- The format of each row is:

```
{"USER_ID": [{"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], "USER_ID": [{"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}
```

- The file name must be todo_all_employees.json