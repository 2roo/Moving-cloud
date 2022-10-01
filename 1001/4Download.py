import os
import requests

def download_file(url, filename):
    local_filename = filename
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024): 
                f.write(chunk)
    return local_filename

with open("9link.txt", "r") as linkfile:
    urls = linkfile.readlines()

with open("9path.txt", "r") as namefile:
    names = namefile.readlines()

if not os.path.exists("./download/"):
    os.makedirs("./download/")
    
for i in range(0, len(urls)):
    urllen = len(urls[i])
    urls[i] = urls[i][:urllen-1]
    namelen = len(names[i])
    names[i] = "./download/" + names[i][0:namelen-1]
    


    
for i in range(0, len(urls)):
    if urls[i] == "Folder":
        continue
    folders = names[i].split("/")
    folderlen = len(folders)
    folders = folders[:folderlen-1]
    paths = "/".join(folders)
    if not os.path.exists(paths):
        os.makedirs(paths)
    print(download_file(urls[i], names[i]))
    temp = input("continue? (y/n) >")
    if temp == "n":
        break