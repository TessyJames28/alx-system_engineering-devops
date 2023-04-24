#!/usr/bin/python3
"""
Python script that uses REST API to fetch his/her todo list based on ID
export to a csv file
"""
import json
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    todo = requests.get(url + "users/{}/todos".format(user_id)).json()
    name = user.get("username")

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": name
            } for task in todo]}, jsonfile)
