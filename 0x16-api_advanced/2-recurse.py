#!/usr/bin/python3
"""
2-recurse module
"""

import requests


def recurse(subreddit, hot_list=[], after=None, count=0):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "Custom/1.0"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 404:
        return None

    data = response.json().get("data")
    hot_list.extend([child.get("data").get("title") for child in data.get
                     ("children")])

    return recurse(subreddit, hot_list, after=data.get("after"),
                   count=count+data.get
                   ("dist")) if data.get("after") else hot_list
