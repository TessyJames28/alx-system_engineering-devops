#!/usr/bin/python3
"""
function that queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    response = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        children = data['data']['children']
        for child_data in children:
            print("{}".format(child_data['data']['title']))
    else:
        print("None")
