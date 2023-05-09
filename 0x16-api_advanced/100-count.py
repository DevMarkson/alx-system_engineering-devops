#!/usr/bin/python3

import requests  # Module for making HTTP requests

"""
This function queries the Reddit API and returns a list containing the titles
of all hot articles for a given subreddit
"""
def count_words(sub, words, hot_list=[], after=''):  # Function that queries the Reddit API
    try: # Try to execute the following:
        r = requests.get('https://www.reddit.com/r/{}/hot.json?after={}'. # URL to query
                         format(sub, after), # Subreddit name and pagination
                         headers={'User-Agent': 'custom'}, # Custom user agent
                         allow_redirects=False)     # Prevents redirection
        if after is None: # If there are no more pages to load, return the hot list
            dictionary = {} # Dictionary to store the words and their count
            for word in words: # Iterates through the words
                for hot_word in hot_list: # Iterates through the hot list of words
                    if word == hot_word: # If the word is in the hot list
                        if word not in dictionary: # If the word is not in the dictionary
                            dictionary[word] = 1 # Add the word to the dictionary
                        else: # If the word is in the dictionary
                            dictionary[word] += 1 # Increment the count of the word
            for word in sorted(dictionary, key=dictionary.get, reverse=True): # Iterates through the sorted dictionary
                if dictionary[word]: # If the word is in the dictionary
                    print('{}: {}'.format(word, dictionary[word]))   # Print the word and its count
            return hot_list # Return the hot list
        for thread in r.json().get('data').get('children'): # Iterates through the threads
            hot_list += thread.get('data').get('title').lower().split() # Adds the title of each thread to the hot list
        after = r.json().get('data').get('after')  # Pagination
        count_words(sub, words, hot_list, after) # Recursive call
        return hot_list # Return the hot list
    except: # If an error occurred,
        return None # Return None
