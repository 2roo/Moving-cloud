import os

with open("filelist2.txt", "r", encoding="UTF-8") as file:
    filelist = file.readlines()

Break = False
for i in range(0, len(filelist)):
    count = 0
    temp = ""
    index_list = []
    for j in range(0, len(filelist[i])):
        match count:
            case 0:
                temp += filelist[i][j]
                if temp == " ":
                    count += 1
                else:
                    temp = ""
            case 1:
                temp += filelist[i][j]
                if temp == " T" or temp == " F":
                    count += 1
                else:
                    temp = ""
                    count = 0
            case 2:
                temp += filelist[i][j]
                if temp == " Tr" or temp == " Fa":
                    count += 1
                else:
                    temp = ""
                    count = 0
            case 3:
                temp += filelist[i][j]
                if temp == " Tru" or temp == " Fal":
                    count += 1
                else:
                    temp = ""
                    count = 0
            case 4:
                temp += filelist[i][j]
                if temp == " True" or temp == " Fals":
                    count += 1
                else:
                    temp = ""
                    count = 0
            case 5:
                temp += filelist[i][j]
                if temp == " True,":
                    index_list.append(j-4)
                    index_list.append(j)
                    temp = ""
                    count = 0
                elif temp == " False":
                    count += 1
                else:
                    temp = ""
                    count = 0
            case 6:
                temp += filelist[i][j]
                if temp == " False,":
                    index_list.append(j-5)
                    index_list.append(j)
                temp = ""
                count = 0
    if len(index_list) > 0:
        index_list.reverse()
        for k in index_list:
            filelist[i] = filelist[i][:k] + '"' + filelist[i][k:]

    if int(10000*i/(len(filelist)))/10 == int(1000*i/(len(filelist))):
        os.system("clear")
        print(int(1000*i/(len(filelist)))/10)



with open("filelist3.txt", "w") as filelist3:
    for i in filelist:
        filelist3.write(i + "\n")
print("done")