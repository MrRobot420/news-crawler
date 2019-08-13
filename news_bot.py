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

save_folder_mac = "/Users/Maxi/Desktop/atom/python/automation/news_api/data/"
save_folder_win = "C:/Users/PC/code/py/automation/news-crawler/data/"
site = "https://newsapi.org/v2/top-headlines?country="

save_folder = ""
auth = ""

if os.name == 'nt':
    auth_win = "&apiKey=" + open(save_folder_win + "key/key.txt").readline()
    save_folder = save_folder_win
    auth = auth_win
else:
    auth_mac = "&apiKey=" + open(save_folder_mac + "key/key.txt").readline()
    save_folder = save_folder_mac
    auth = save_folder_mac


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