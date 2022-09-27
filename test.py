with open("filelist3.txt","r") as file:
    string = file.readlines()

with open("error.txt", "r") as error:
    err = error.readlines()

for i in range(0, len(err)):
    err[i] = int(err[i])

for i in err:
    if string[i] != "\n":
        print(string[i], end="|QWERTY|")