#!/usr/bin/python3
"""
This code retrieves the number of subscribers for a specified subreddit by querying the Reddit API.
"""
import requests

def number_of_subscribers(sub):
    try:
        res = requests.get('https://www.reddit.com/r/{}/about.json'.
                            format(sub),
                            headers={'User-Agent': 'custom'},
                            allow_redirects=False)
        return res.json().get('data').get('subscribers')
    except:
        return 0
