import os


# Change the path how you wish:
save_folder_mac = "/Users/Maxi/Desktop/atom/python/automation/news_api/data/"
save_folder_win = "C:/Users/PC/code/py/automation/news-crawler/data/"


save_folder = ""

# Check for operation system (if multiple operating systems in use):
if os.name == 'nt':
    save_folder = save_folder_win
else:
    save_folder = save_folder_mac



def main_loop():
    print("\n\n\n\n######   STARTING NEWS-INFO   ######\n\n")
    index_data()


def index_data():
    print("[*] Indexing data...")
    folders = index_folders()
    file_pathes = index_files(folders)
    print(file_pathes)                    # Just for debug


def index_folders():
    print("[*] Indexing folders...")
    dirs = os.listdir(save_folder)
    data_dirs = []

    for i in range(len(dirs)-1):
        directory = dirs[i]
        print("[+] Found folder '%s' " % directory)
        data_dirs.append(directory)
    return data_dirs



def index_files(folders):
    print("[*] Indexing files...")
    pathes = []
    files = []

    for folder in folders:
        path = save_folder + "/" + folder
        files = os.listdir(path)
        
        for f in files:
            pathes.append(path + "/" + f)
    
    return pathes

main_loop()