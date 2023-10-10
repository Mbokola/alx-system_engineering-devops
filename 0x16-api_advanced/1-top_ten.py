#!/usr/bin/python3
"""
1-top_ten module
"""


import requests


def top_ten(subreddit):
    limit = 10
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit={limit}"
    headers = {
        "User-Agent": "Custom/1.0"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        children = data["data"]["children"]

        [print(child["data"]["title"]) for child in children]

    else:
        print("None")
