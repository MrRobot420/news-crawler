import os
import json


# Change the path how you wish:
save_folder_mac = "/Users/Maxi/Desktop/atom/python/automation/news_api/data/"
save_folder_win = "C:/Users/PC/code/py/automation/news-crawler/data/"

save_folder = ""

# Check for operation system (if multiple operating systems in use):
if os.name == 'nt':
    save_folder = save_folder_win
else:
    save_folder = save_folder_mac


# The main part of the program
def main_loop():
    print("\n\n\n\n######   STARTING NEWS-INFO   ######\n\n")
    file_pathes, counter, files = index_data()
    show_info(file_pathes, counter, files)


# Logs info to the console:
def show_info(pathes, count, files):
    for i in range(count):
        print("[+]  (%i) Spotted file-path: %s" % (i + 1, pathes[i]))
        print(" |-- [file]: %s" % files[i])
    print(" |\n[√] Found %i files\n" % count)

    for path in pathes:
        #print("[*] Loading new data from path: %s\n" % path)
        data = open(path, 'r', encoding='utf-8')
        news_object = json.load(data)

        articles = news_object["articles"]
        #print(articles)

        counter = 0
        
        for article in articles:
            counter += 1
            title = article["title"]
            author = article["author"]
            url = article["url"]
            pubAt = article["publishedAt"]

            print("[+] ARTICLE (%i)" % counter)
            print(" - Title: %s" % title)
            print(" - Author: %s" % author)
            print(" - URL: %s" % url)
            print(" - Date: %s" % pubAt)
        
        print("\n")


# Index data in order to get infos out of them:
def index_data():
    print("[*] Indexing data...")
    folders = index_folders()
    file_pathes, counter, files = index_files(folders)
    return file_pathes, counter, files


# Index all folders within data:
def index_folders():
    print("\n[*] Indexing folders...")
    dirs = os.listdir(save_folder)
    data_dirs = []

    for i in range(len(dirs)):
        if (dirs[i] == ".DS_Store") or (dirs[i] == "key"):
            pass
        else:
            directory = dirs[i]
            print("[+] Found folder '%s' " % directory)
            data_dirs.append(directory)
    return data_dirs


# Index all files in the subfolders:
def index_files(folders):
    print("\n[*] Indexing files...")
    pathes = []
    filenames = []
    files = []
    counter = 0

    # Iterate through each folder and get the filenames:
    for folder in folders:
        path = save_folder + folder
        files = os.listdir(path)
        
        for f in files:
            counter += 1
            pathes.append(path + "/" + f)
            filenames.append(f)
    
    return pathes, counter, filenames

main_loop()