#!/usr/bin/python3
"""Using what you did in the task #0, extend your Python
script to export data in the JSON format."""

import json
import sys
import urllib.request

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/"
    with urllib.request.urlopen(url + sys.argv[1]) as response:
        data = json.loads(response.read().decode("utf-8"))
        username = data.get("username")
    url = "https://jsonplaceholder.typicode.com/todos?userId="
    with urllib.request.urlopen(url + sys.argv[1]) as response:
        data = json.loads(response.read().decode("utf-8"))
        with open(sys.argv[1] + ".json", mode="w") as file:
            json.dump({sys.argv[1]: [
                {
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": username
                } for task in data
            ]}, file)
