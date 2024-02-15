import requests

def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns the number of subscribers for a given subreddit.
    If an invalid subreddit is given, the function should return 0.
    """
    headers = {"User-Agent": "Custom User Agent"}  # Set a custom User-Agent

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)  # Do not follow redirects

    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]  # Return the number of subscribers
    else:
        return 0  # Return 0 for invalid subreddit or other errors
