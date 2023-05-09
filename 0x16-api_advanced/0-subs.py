#!/usr/bin/python3
import requests     

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json" # url of the subreddit
    headers = {'User-Agent': 'Mozilla/5.0'} # User-Agent to avoid 429 error
    response = requests.get(url, headers=headers, allow_redirects=False) # GET request
    if response.status_code == 200: # if status code is 200
        data = response.json() # get the json data
        return data['data']['subscribers']  # return the number of subscribers
    else:
        return 0 # if status code is not 200, return 0
    
print(number_of_subscribers("python"))  # Prints the number of subscribers for the r/python subreddit
print(number_of_subscribers("programming"))  # Prints the number of subscribers for the r/programming subreddit
