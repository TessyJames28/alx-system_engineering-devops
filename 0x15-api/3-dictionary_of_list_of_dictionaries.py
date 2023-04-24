#!/usr/bin/python3
"""
Python script that uses REST API to fetch his/her todo list based on ID
export to a csv file
"""
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_url = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({user.get("id"): [{
            "username": user.get("username"),
            "task": task.get("title"),
            "completed": task.get("completed")
            } for task in requests.get(url + "users/{}/todos".format(
                user.get("id"))).json()]
            for user in user_url}, jsonfile)
