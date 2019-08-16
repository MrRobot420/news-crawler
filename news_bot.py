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
import io

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

def main_loop():
    print("\n\n\n\n#####   STARTING NEWS-BOT   #####\n\n")
    for code in c_code:
        req = site + code + auth            # Build requests
        data = get_data(req, code)          # Request the data
        save_data(data, code, 1)               # Save the data


# Get data for a specific request:
def get_data(request, code):
    print("[*] FETCHING NEWS REQUEST FOR COUNTRY: %s ..." % code.upper())
    response = requests.get(request)
    response = requests.utils.get_unicode_from_response(response)
    data = json.loads(response, encoding='utf-8')
    return data


def save_data(data, code, num):
    date = dt.now().strftime("%d-%m-%Y")
    folder_name = date
    path = save_folder + folder_name

    if not os.path.isdir(path):
        os.mkdir(path, 755)

    if num < 10:
        filename = '0' + str(num) + "_" + code + ".json"
    else:
        filename = str(num) + "_" + code +".json"
    
    if not os.path.isfile(path + '/' + filename):
        with io.open(path + '/' + filename,'w', encoding="utf-8") as outfile:
            outfile.write(json.dumps(data, ensure_ascii=False, indent=4))    
        print("[√] SAVED JSON FROM COUNTRY [ %s ] IN [ %s ]\n" % (code, filename))
    else:
        num += 1
        save_data(data, code, num)  # Recursively check if file exists
        


main_loop()