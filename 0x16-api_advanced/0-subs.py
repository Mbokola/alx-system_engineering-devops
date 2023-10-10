#!/usr/bin/python3
"""
0-subs module
"""


import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    header = {
        "User-Agent": "Custom/1.0"
        }
    response = requests.get(url, headers=header)
    data = response.json()

    return data["data"]["subscribers"] if response.status_code == 200 else 0
