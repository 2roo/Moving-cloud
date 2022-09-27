with open("9id.txt", "r") as idfile:
    ids = idfile.readlines()
    
with open("9name.txt", "r") as namefile:
    names = namefile.readlines()
    
with open("9parent_id.txt", "r") as paridfile:
    parids = paridfile.readlines()

for i in range(0, len(names)):
    length = len(names[i])
    names[i] = str(names[i][:length - 1])

nextid = []
l = len(ids)

fast_id = []
fast_name = []
fast_parid = []
n = 0

while True:
    n += 1
    count = 0
    count2 = 0
    for i in range(0, l):
        if n != 1:
            if nextid[i] == "Root\n" or nextid[i] == "None\n": #상위 폴더가 없을 때
                continue
            count += 1
            if nextid[i] in fast_id:
                count2 += 1
                index = fast_id.index(nextid[i])
                nextid[i] = fast_parid[index]
                names[i] = fast_name[index] + "/" + names[i]
            else:
                try:
                    index = ids.index(nextid[i])
                    nextid[i] = parids[index]
                    names[i] = names[index] + "/" + names[i]
                    fast_id.append(ids[index])
                    fast_name.append(names[index])
                    fast_parid.append(parids[index])
                    print(len(fast_id))
                except:
                    nextid[i] = "None\n"
        else:
            print(i)
            nextid.append(parids[i])
    print(n, count, count2)
    if n != 1 and count == 0:
        break

# for i in range(0, length):
#     names[i] = "./" + names[i]

with open("9path.txt", "w") as pathfile:
    for path in names:
        pathfile.write(str(path) + "\n")