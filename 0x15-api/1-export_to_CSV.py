#!/usr/bin/python3
""" Export to CSV """

if __name__ == '__main__':
    import requests
    import csv
    from sys import argv

    todos = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                     format(argv[1]))
    username = todos.json().get('username')

    todos = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                     format(argv[1]))
    data = todos.json()

    with open('{}.csv'.format(argv[1]), mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"',
                                quoting=csv.QUOTE_ALL)
        
        for task in data:
            csv_writer.writerow([argv[1], username, task.get('completed'),
                                 task.get('title')])