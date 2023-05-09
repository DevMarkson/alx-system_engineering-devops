#!/usr/bin/python3
"""
This code retrieves the number of subscribers for a specified subreddit by querying the Reddit API.
"""
import requests

def number_of_subscribers(sub):
    try:
        res = requests.get('https://www.reddit.com/r/{}/about.json'.    # URL to query
                            format(sub),    # Subreddit name
                            headers={'User-Agent': 'custom'},   # Custom user agent
                            allow_redirects=False)  # Prevents redirection  
        return res.json().get('data').get('subscribers')    # Returns the number of subscribers
    except:
        return 0  # Returns 0 if an error occurred
