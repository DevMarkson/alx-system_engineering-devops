#!/usr/bin/python3
"""
This code retrieves the top 10 hot posts for a specified subreddit by querying the Reddit API.
"""
import requests


def top_ten(subreddit_name):   # Function that queries the Reddit API
    try:   # Try to execute the following:
        response = requests.get('https://www.reddit.com/r/{}/hot.json?limit=10'.    # URL to query
                                format(subreddit_name),     # Subreddit name
                                headers={'User-Agent': 'custom'},   # Custom user agent
                                allow_redirects=False)  # Prevents redirection
        for thread in response.json().get('data').get('children'):  # Iterates through the threads
            print(thread.get('data').get('title')) # Prints the title of each thread
    except: # If an error occurred, print None
        print('None')
