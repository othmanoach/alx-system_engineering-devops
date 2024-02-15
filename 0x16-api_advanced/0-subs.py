#!/usr/bin/python3
"""test"""

import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"othmanoach": "othmano"}
    response = requests.get(url, headers=headers)

    # Check if the response is successful
    if response.status_code == 200:
        data = response.json()

        # Check if the subreddit exists
        if data["kind"] == "t5":
            return data["data"]["subscribers"]
        else:
            return 0
    else:
        return 0
