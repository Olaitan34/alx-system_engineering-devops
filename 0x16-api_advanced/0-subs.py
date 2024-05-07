#!/usr/bin/python3
"""
This program work with the Reddit API
"""

import requests


def number_of_subscribers(subreddit):
    """number_of_subscribers"""
    url = "https://reddit.com/r/{}/about.json".format(subreddit)
    req = requests.get(url)

    if req.status_code == 200:
        data = req.json()
        cribers = data["data"]["subscribers"]
        return cribers
    elif req.status_code == 302:
        return 0
    else:
        return 0