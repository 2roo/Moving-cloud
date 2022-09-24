import requests

def download_file(url, filename):
    local_filename = filename
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024): 
                f.write(chunk)
    return local_filename

with open("link.txt", "r") as linkfile:
    urls = linkfile.readlines()

with open("name.txt", "r") as namefile:
    names = namefile.readlines()

for i in range(0, len(urls)):
    urllen = len(urls[i])
    urls[i] = urls[i][0:urllen-1]
    namelen = len(names[i])
    names[i] = "./download/" + names[i][0:namelen-1]

for i in range(0, len(urls)):
    if urls[i] == "Folder":
        continue
    print(download_file(urls[i], names[i]))
    temp = input("continue? (y/n) >")
    if temp == "n":
        break