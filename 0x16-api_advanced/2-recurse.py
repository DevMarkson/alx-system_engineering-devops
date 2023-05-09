#!/usr/bin/python3
'''
Module for storing the recurse() function.
'''
import requests


BASE_URL = 'https://www.reddit.com'
'''Reddit's base API URL.
'''


def recurse(sub, hot_lst=[], num=0, after=None):
    '''Retrieves a list of hot posts from a given subreddit.
    '''
    api_headers = {
        'Accept': 'application/json',
        'User-Agent': ' '.join([
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'AppleWebKit/537.36 (KHTML, like Gecko)',
            'Chrome/97.0.4692.71',
            'Safari/537.36',
            'Edg/97.0.1072.62'
        ])
    }
    sort = 'hot'
    limit = 30
    res = requests.get(
        '{}/r/{}/.json?sort={}&limit={}&count={}&after={}'.format(
            BASE_URL,
            sub,
            sort,
            limit,
            num,
            after if after else ''
        ),
        headers=api_headers,
        allow_redirects=False
    )
    if res.status_code == 200:
        data = res.json()['data']
        posts = data['children']
        count = len(posts)
        hot_lst.extend(list(map(lambda x: x['data']['title'], posts)))
        if count >= limit and data['after']:
            return recurse(sub, hot_lst, num + count, data['after'])
        else:
            return hot_lst if hot_lst else None
    else:
        return hot_lst if hot_lst else None
