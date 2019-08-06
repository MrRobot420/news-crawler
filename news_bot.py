"""
    * A Python program to fetch news-headlines from news_api.org
    * NOTES:
        - "articles" : "news-array"
        {
            - "source" : JSON-Object (id, name)
            - "author" : String
            - "title" : String
            - "description" : String with long headline of article
            - "url" : link to page
            - "urlToImage" : link to image
            - "publishedAt" : Date with time
            - "content" : String (long) with the article
        }
"""

import sys
import os
import time
from datetime import datetime as dt
import urllib
import requests
import json

save_folder = "/Users/Maxi/Desktop/atom/python/automation/news_api/data/"
site = "https://newsapi.org/v2/top-headlines?country="
auth = "&apiKey=" + open(save_folder + "key/key.txt").readline()

# Codes for various countries:
c_code = dict(
    de = "de",
    us = "us",
    gb = "gb",
    ru = "ru",
    cn = "cn",
    fr = "fr",
    it = "it",
    es = "es"
)

# Get data for a specific request:
def get_data(request, code):
    print("[*] FETCHING NEWS REQUEST FOR COUNTRY: %s ..." % code.upper())
    response = requests.get(request)
    data = json.loads(response.content)

    return data


def save_data(data, code):
    date = dt.now().strftime("%d-%m-%Y")
    filename = date + "_" + code + ".json"
    print("[√] SAVED JSON FROM COUNTRY [ %s ] AS [ %s ]\n" % (code, filename))

    with open(save_folder + filename, 'w') as outfile:
        json.dump(data, outfile)


def main_loop():
    print("\n\n\n\n#####   STARTING NEWS-BOT   #####\n\n")
    for code in c_code:
        req = site + code + auth
        data = get_data(req, code)
        save_data(data, code)


main_loop()