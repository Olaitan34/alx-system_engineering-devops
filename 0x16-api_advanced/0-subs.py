#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0
"""

import requests


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API
    - If not a valid subreddit, return 0.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    req = requests.get(url, headers={"User-Agent": "Custom"})

    if req.status_code == 200:
        data = req.json()
        criber = data["data"]["subbscribers"]
        return criber
    else:
        return 0