#!/usr/bin/python3
'''A module containing functions for working with the Reddit API.
'''
import requests


def sort_histogram(hist={}):
    '''Sorts and prints the given histogram.
    '''
    hist = list(filter(lambda kv: kv[1], hist))
    hist_dict = {}
    for item in hist:
        if item[0] in hist_dict:
            hist_dict[item[0]] += item[1]
        else:
            hist_dict[item[0]] = item[1]
    hist = list(hist_dict.items())
    hist.sort(
        key=lambda kv: kv[0],
        reverse=False
    )
    hist.sort(
        key=lambda kv: kv[1],
        reverse=True
    )
    res_str = '\n'.join(list(map(
        lambda kv: '{}: {}'.format(kv[0], kv[1]),
        hist
    )))
    if res_str:
        print(res_str)


def count_words(subreddit, word_list, hist=[], n=0, after=None):
    '''Counts the number of times each word in a given wordlist
    occurs in a given subreddit.
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
            'https://www.reddit.com',
            subreddit,
            sort,
            limit,
            n,
            after if after else ''
        ),
        headers=api_headers,
        allow_redirects=False
    )
    if not hist:
        word_list = list(map(lambda word: word.lower(), word_list))
        hist = list(map(lambda word: (word, 0), word_list))
    if res.status_code == 200:
        data = res.json()['data']
        posts = data['children']
        titles = list(map(lambda post: post['data']['title'], posts))
        hist = list(map(
            lambda kv: (kv[0], kv[1] + sum(list(map(
                lambda txt: txt.lower().split().count(kv[0]),
                titles
            )))),
            hist
        ))
        if len(posts) >= limit and data['after']:
            count_words(
                subreddit,
                word_list,
                hist,
                n + len(posts),
                data['after']
            )
        else:
            sort_histogram(hist)
    else:
        return