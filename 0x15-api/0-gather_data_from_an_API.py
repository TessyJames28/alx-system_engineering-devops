#!/usr/bin/python3
"""Python script that uses REST API to fetch his/her todo list based on ID"""
import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(id)).json()
    todo = requests.get(url + "users/{}/todos".format(id)).json()

    total_task = 0
    task_completed = 0
    list_completed = []

    for task in todo:
        total_task += 1
        if task.get("completed") is True:
            task_completed += 1
            list_completed.append(task.get("title"))

    statement = "Employee {} is done with tasks({}/{}):"
    print(statement.format(user.get("name"), task_completed, total_task))
    for tasks in list_completed:
        print("\t {}".format(tasks))
