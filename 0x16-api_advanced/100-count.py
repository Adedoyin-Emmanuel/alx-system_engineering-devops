#!/usr/bin/python3
"""A recursive function that queries the Reddit API,
parses the title of all hot articles, and prints a sorted
count of given keywords (case-insensitive, delimited by spaces.
Javascript should count as javascript, but java should not).
"""
import requests
from collections import Counter


def count_words(subreddit, word_list, after=None):
    """Prints counts of given words found in hot posts of a given subreddit.

    Args:
        subreddit (str): The subreddit to search.
        word_list (list): The list of words to search for in post titles.
        instances (obj): Key/value pairs of words/counts.
        after (str): The parameter for the next page of the API results.
        count (int): The parameter of results matched thus far.
    """
    user_agent = "MyRedditBot/1.0"
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"after": after} if after else {}
    headers = {"User-Agent": user_agent}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        titles = [post["data"]["title"].lower() for post in posts]
        keywords = [word.lower() for word in word_list]
        keyword_counter = Counter()
        for title in titles:
            for keyword in keywords:
                if f' {keyword} ' in f' {title} ':
                    keyword_counter[keyword] += 1
        if "after" in data["data"] and data["data"]["after"] is not None:
            return count_words(subreddit,
                               word_list, after=data["data"]["after"])
        else:
            sorted_keywords = sorted(keyword_counter.items(),
                                     key=lambda item: (-item[1], item[0]))
            for keyword, count in sorted_keywords:
                print(f"{keyword}: {count}")
    elif response.status_code == 404:
        print("Invalid subreddit or no results found.")
    else:
        print(f"Error: {response.status_code}")
