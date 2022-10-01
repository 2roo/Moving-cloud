Skip to content
Search or jump to…
Pull requests
Issues
Marketplace
Explore
 
@2roo 
2roo
/
Moving-cloud
Private
Code
Issues
Pull requests
Actions
Projects
Security
Insights
Settings
Moving-cloud/3TextToDict.py /
@2roo
2roo Update 3TextToDict.py
Latest commit 034b38a now
 History
 1 contributor
107 lines (90 sloc)  2.91 KB

import json
import ast

title = []
id = []
parents_title = []
parents_id = []
d_link = []
owner_list = [['김이루'], ['아까먹다남은쿠키']]


n = 0

with open("filelist3.txt", "r", encoding="UTF-8") as txt:
    filelist = txt.readlines()

while True:
    try:
        file = filelist[n]
    except:
        break
    if file == "" or file == " " or file == "\n":
        n += 1
        continue
    file = ast.literal_eval(file)
    #여기까지 file에 각 파일 정보 dict 저장
    
    title.append(file["title"])
    id.append(file["id"])
    try:
        if not file["parents"][0]["isRoot"]: #Root에 존재하지 않는(폴더 내에 존재하는 파일/폴더)
            parents_id.append(file["parents"][0]["id"])
        else: #Root에 있음
            parents_id.append("Root")
    except: #공유받은 파일
#         if file["ownerNames"] in owner_list:
        parents_id.append("None")
#         else: #가현이, 나 아니면 제거
#             title.pop()
#             id.pop()
#             n += 1
#             continue
    try: #File
        d_link.append(file["webContentLink"] + "&confirm=t")
    except: #Folder
        d_link.append("Folder")
    if len(title) == len(id) == len(parents_id) == len(d_link):
        print("OK!!", len(title))
    else:
        print("title:", len(title))
        print("id:", len(id))
        print("parents_id:", len(parents_id))
        print("d_link:", len(d_link))
        break
    
    # #여기부터 parents id 값이 같은 경우 title과 id 출력
    # try:
    # #     print(file["parents"][0]["id"])
    #     # if file["parents"][0]["id"] == "1_aNG8MxUZTKdeIdVB_siDytS0-IPtMSR":
    #     if file["parents"][0]["isRoot"]:
    #         # print(file["title"])
    #         print(file["ownerNames"], "ok")
    #         # print(file["id"])
    #         # break
    #     if file["ownerNames"] not in owner_list:
    #         # print(file["ownerNames"])
    #         try: # 파일의 경우
    #             print(file["webContentLink"])
    #         except: # 폴더의 경우
    #             print(file)
    #             break
    # except:
    #     # if file["ownerNames"] not in owner_list:
    #     #     # print(file["ownerNames"])
    #     #     try: # 파일의 경우
    #     #         print(file["webContentLink"])
    #     #     except: # 폴더의 경우
    #     #         print(file)
    #     #         break
            
    #     n += 1
    #     continue
    
    
    
    n += 1
    
    # print(file)
    # break

with open("9link.txt", "w") as linkfile:
    for link in d_link:
        linkfile.write(str(link) + "\n")

with open("9name.txt", "w") as namefile:
    for name in title:
        namefile.write(str(name) + "\n")

with open("9id.txt", "w") as idfile:
	for ids in id:
		idfile.write(str(ids) + "\n")
        
with open("9parent_id.txt", "w") as parentfile:
    for parids in parents_id:
        parentfile.write(str(parids) + "\n")

print("done")
