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

# Change the path how you wish:
save_folder_mac = "/Users/Maxi/Desktop/atom/python/automation/news_api/data/"
save_folder_win = "C:/Users/PC/code/py/automation/news-crawler/data/"

# Change the link how you wish:
site = "https://newsapi.org/v2/top-headlines?country="

save_folder = ""
auth = ""

# Check for operation system (if multiple operating systems in use):
if os.name == 'nt':
    print("[info] running on windows...\n\n\n")
    auth_win = "&apiKey=" + open(save_folder_win + "key/key.txt").readline()
    save_folder = save_folder_win
    auth = auth_win
else:
    print("[info] running on mac / unix...\n\n\n")
    auth_mac = "&apiKey=" + open(save_folder_mac + "key/key.txt").readline()
    save_folder = save_folder_mac
    auth = auth_mac

# Codes for various countries:
c_code = dict(
    de = "de",
    us = "us",
    gb = "gb",
    ru = "ru",
    cn = "cn",
    fr = "fr",
    it = "it"
)

# The ressemblance of the core routine:
def main_loop():
    print("\n\n\n\n#####   STARTING NEWS-BOT   #####")
    for code in c_code:
        req = site + code + auth            # Build requests
        data = get_data(req, code)          # Request the data
        save_data(data, code, 1)            # Save the data


# Get data for a specific request:
def get_data(request, code):
    print("[*] FETCHING NEWS REQUEST FOR COUNTRY: %s ..." % code.upper())
    response = requests.get(request)
    response = requests.utils.get_unicode_from_response(response)
    data = json.loads(response, encoding='utf-8')
    return data


# Saves the JSON-data and formats it
def save_data(data, code, num):
    folder_name = dt.now().strftime("%d-%m-%Y")                    # Get the current date
    path = save_folder + folder_name

    make_dir(path, folder_name)                             # Check if a folder has to be made
    filename = assemble_filename(num, code)                 # Assemble the filename for saving the data
     
    if not os.path.isfile(path + '/' + filename):
        with io.open(path + '/' + filename,'w', encoding="utf-8") as outfile:
            outfile.write(json.dumps(data, ensure_ascii=False, indent=4))    
        print("[√] SAVED JSON FROM COUNTRY [ %s ] IN [ %s ]\n" % (code, filename))
    else:
        num += 1
        save_data(data, code, num)  # Recursively check if the file exists
        

# Check if there already is a folder for the current day:
def make_dir(path, fn):
    if not os.path.isdir(path + "/"):
        os.mkdir(path + "/", 0o777)
        print("[+] CREATED NEW FOLDER [ %s ] FOR THE CURRENT DAY." % fn)


# Builds the filename:
def assemble_filename(num, code):
    if num < 10:
        filename = '0' + str(num) + "_" + code + ".json"
    else:
        filename = str(num) + "_" + code +".json"

    return filename


main_loop()