#!/usr/bin/python3
"""
recursive function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    response = requests.get("https://www.reddit.com/r/{}/hot.json?"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False,
                            params={'limit': 100, 'after': after})
    if response.status_code == 200:
        data = response.json()
        children = data['data']['children']
        hot_list.extend(child_data['data']['title'] for child_data in children)
        after = data['data']['after']
        if not after:
            return hot_list
        return recurse(subreddit, hot_list, after=after)
    else:
        return None
