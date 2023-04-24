#!/usr/bin/python3
"""
Python script that uses REST API to fetch his/her todo list based on ID
export to a csv file
"""
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    todo = requests.get(url + "users/{}/todos".format(user_id)).json()

    total_task = 0
    task_completed = 0
    list_completed = []

    name = user.get("username")

    with open("{}.csv".format(user_id), "w") as file:
        for task in todo:
            title = task.get("title")
            task_status = task.get("completed")
            write_rows = '"{}","{}","{}","{}"\n'.format(
                user_id, name, task_status, title)
            file.write(write_rows)
