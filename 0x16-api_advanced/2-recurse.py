#!/usr/bin/python3
import requests

"""
This function queries the Reddit API and returns a list containing the titles
of all hot articles for a given subreddit
"""
def recurse(sub, hot_lst=[], aftr=''): 
    try:
        r = requests.get('https://www.reddit.com/r/{}/hot.json?after={}'.
                         format(sub, aftr),
                         headers={'User-Agent': 'custom'},
                         allow_redirects=False)
        if aftr is None: # If there are no more pages to load, return the hot list
            return hot_lst # Return the hot list
        for thread in r.json().get('data').get('children'): # Iterates through the threads
            hot_lst += [thread.get('data').get('title')] # Adds the title of each thread to the hot list
        aftr = r.json().get('data').get('after')    # Pagination
        recurse(sub, hot_lst, aftr) # Recursive call
        return hot_lst # Return the hot list
    except: # If an error occurred,
        return None # Return None
