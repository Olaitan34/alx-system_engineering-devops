#!/usr/bin/python3
"""
This is a program that works with the Reddit API
"""

import requests


def number_of_subscribers(subreddit):
    """number_of_subscribers"""
    url = "https://reddit.com/r/{}/about.json".format(subreddit)
    req = requests.get(url)
    if req.status_code == 200:
        data = req.json()
        subs = data["data"]["subscribers"]
        return subs
    else:
        return 0