#!/usr/bin/python3
"""Using what you did in the task #0, extend your Python script to export
data in the CSV format."""

import csv
import json
import sys
import urllib.request

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/"
    with urllib.request.urlopen(url + sys.argv[1]) as response:
        data = json.loads(response.read().decode("utf-8"))
        username = data.get('username')
    url = "https://jsonplaceholder.typicode.com/todos?userId="
    with urllib.request.urlopen(url + sys.argv[1]) as response:
        data = json.loads(response.read().decode("utf-8"))
        with open(sys.argv[1] + ".csv", mode='w', newline="") as file:
            writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
            [writer.writerow(
                [sys.argv[1], username, task.get('completed'),
                 task.get('title')]
            ) for task in data]
