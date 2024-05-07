#!/usr/bin/python3
import requests

"""program that returs a list containing 
the titles of all hot articles for a given subreddit
"""


def recurse(subreddit, hot_list=[], after=""):
    """
    Queries the Reddit API and returns
    a list containing the titles of all hot articles for a given subreddit.

    - If not a valid subreddit, return None.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    req = requests.get(url, 
                            headers="User-Aget":"Custom"
                            params={"after":"after"},
    )

    if req.status_code == 200:
        for GetData in req.json().get("data").get("children"):
            dat = GetData.get("data")
            title = dat.get("title")
            hot_list.append(title)
        after = req.json().get("data").get("after")
        
        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    else:
        return None
    