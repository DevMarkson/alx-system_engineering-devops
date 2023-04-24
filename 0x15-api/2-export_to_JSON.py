#!/usr/bin/python3
""" Export to JSON """

if __name__ == '__main__':
    import requests
    import json
    from sys import argv

    todos= requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                     format(argv[1]))
    username = todos.json().get('username')

    todos = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                     format(argv[1]))
    todos_data = todos.json()

    export = {}
    export['{}'.format(argv[1])] = []
    for task in todos_data:
        export['{}'.format(argv[1])].append({
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': username
        })

    with open('{}.json'.format(argv[1]), 'w') as outfile:
        json.dump(export, outfile)