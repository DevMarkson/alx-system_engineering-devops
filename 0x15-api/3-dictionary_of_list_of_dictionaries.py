#!/usr/bin/python3
"""
For all employees, export to JSON information about TODO list progress
"""

if __name__ == '__main__':
    import requests
    import json
    from sys import argv

    # Create a set to hold all user IDs
    all_id = set()

    # Send a GET request to retrieve data from the 'posts' endpoint
    todos = requests.get('https://jsonplaceholder.typicode.com/posts')

    # Extract JSON data from the response object
    data = todos.json()

    # Loop through the data and add each unique user ID to the set
    for user in data:
        all_id.add(user.get('userId'))

    # Create a dictionary to hold the export data
    export = {}

    # Loop through each user ID in the set
    for user in all_id:

        # Send a GET request to retrieve data about the user
        todos = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                         format(user))

        # Extract the username from the user data
        username = todos.json().get('username')

        # Send a GET request to retrieve data about the user's TODO list
        todos = requests.get('https://jsonplaceholder.typicode.com/' +
                         'todos?userId={}'.format(user))

        # Extract JSON data from the response object
        data = todos.json()

        # Create a list to hold the TODO list data for this user
        export['{}'.format(user)] = []

        # Loop through the TODO list data and add each task to the list
        for task in data:
            export['{}'.format(user)].append({
                'task': task.get('title'),
                'completed': task.get('completed'),
                'username': username
            })

    # Write the export data to a JSON file
    with open('todo_all_employees.json', 'w') as outfile:
        json.dump({int(r): export[r] for r in export.keys()},
                  outfile, sort_keys=True)
