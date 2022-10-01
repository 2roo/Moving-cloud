split_index = 0
split_count = 0
split_list = []
split_temp = ""

prev_index = 0

err_count = 0
err_list = []
err_temp = ""

file_list = []

print('Generating Data List...')

with open('filelist1.txt', 'r', encoding="UTF-8") as file:
    temp = file.readline()

for char in temp:
    match split_count:
        case 0:
            if char == "d":

                split_temp += char
                split_count += 1
            else:
                split_temp = ""
                split_count = 0
        case 1:
            split_temp += char
            if split_temp == "dr":
                split_count += 1
            else:
                split_temp = ""
                split_count = 0

        case 2:
            split_temp += char
            if split_temp == "dri":
                split_count += 1
            else:
                split_temp = ""
                split_count = 0
        case 3:
            split_temp += char
            if split_temp == "driv":
                split_count += 1
            else:
                split_temp = ""
                split_count = 0
        case 4:
            split_temp += char
            if split_temp == "drive":
                split_count += 1
            else:
                split_temp = ""
                split_count = 0
        case 5:
            split_temp += char
            if split_temp == "drive#":
                split_count += 1
            else:
                split_temp = ""
                split_count = 0
        case 6:
            split_temp += char
            if split_temp == "drive#f":
                split_count += 1
            else:
                split_temp = ""
                split_count = 0
        case 7:
            split_temp += char
            if split_temp == "drive#fi":
                split_count += 1
            else:
                split_temp = ""
                split_count = 0
        case 8:
            split_temp += char
            if split_temp == "drive#fil":
                split_count += 1
            else:
                split_temp = ""
                split_count = 0
        case 9:
            split_temp += char
            if split_temp == "drive#file":
                split_list.append(temp[prev_index: split_index-19])
                prev_index = split_index-19
                split_temp = ""
                # print('split', end=" ")
            split_count = 0
    split_index += 1
split_list.append(temp[prev_index:])
print("Split Complete")

n = 0
while True:
    n += 1
    print(f"Error Correction in progress... {n}")
    err_no = 0
    error_list = []
    length = len(split_list)
    i = 0
    while i < length:
        split_count = 0
        split_temp = ""
        split_index = 0
        temp = split_list[i]
        if temp == "":
            del split_list[i]
            i -= 1
        elif temp[10:20] != "drive#file":
            print(f'error {i:<5} {temp[:50]}')
            split_list[i-1] += split_list[i]
            split_list[i] = ""
            i -= 2
        else:
            for char in temp:
                match split_count:
                    case 0:
                        if char == "d":
                            split_temp += char
                            split_count += 1
                        else:
                            split_temp = ""
                            split_count = 0
                    case 1:
                        split_temp += char
                        if split_temp == "dr":
                            split_count += 1
                        else:
                            split_temp = ""
                            split_count = 0

                    case 2:
                        split_temp += char
                        if split_temp == "dri":
                            split_count += 1
                        else:
                            split_temp = ""
                            split_count = 0
                    case 3:
                        split_temp += char
                        if split_temp == "driv":
                            split_count += 1
                        else:
                            split_temp = ""
                            split_count = 0
                    case 4:
                        split_temp += char
                        if split_temp == "drive":
                            split_count += 1
                        else:
                            split_temp = ""
                            split_count = 0
                    case 5:
                        split_temp += char
                        if split_temp == "drive#":
                            split_count += 1
                        else:
                            split_temp = ""
                            split_count = 0
                    case 6:
                        split_temp += char
                        if split_temp == "drive#f":
                            split_count += 1
                        else:
                            split_temp = ""
                            split_count = 0
                    case 7:
                        split_temp += char
                        if split_temp == "drive#fi":
                            split_count += 1
                        else:
                            split_temp = ""
                            split_count = 0
                    case 8:
                        split_temp += char
                        if split_temp == "drive#fil":
                            split_count += 1
                        else:
                            split_temp = ""
                            split_count = 0
                    case 9:
                        split_temp += char
                        if split_temp == "drive#file":
                            if split_index != 19:
                                split_list.append(temp[:split_index-19])
                                temp = temp[split_index-19:]
                                print(f'split {i:<5} {split_index:<6} {temp[10:20]}')
                            split_temp = ""
                        split_count = 0
                split_index += 1
        i+=1
        length = len(split_list)
    
    print(f'Checking Errors... {n}')
    Err = False
    for l in split_list:
        if l[10:20] != "drive#file":
            Err = True
        else:
            temp = l
            if temp == "":
                Err = True
            else:
                split_temp = ""
                split_count = 0
                split_count2 = 0
                for char in temp:
                    match split_count:
                        case 0:
                            if char == "d":
                                split_temp += char
                                split_count += 1
                            else:
                                split_temp = ""
                                split_count = 0
                        case 1:
                            split_temp += char
                            if split_temp == "dr":
                                split_count += 1
                            else:
                                split_temp = ""
                                split_count = 0

                        case 2:
                            split_temp += char
                            if split_temp == "dri":
                                split_count += 1
                            else:
                                split_temp = ""
                                split_count = 0
                        case 3:
                            split_temp += char
                            if split_temp == "driv":
                                split_count += 1
                            else:
                                split_temp = ""
                                split_count = 0
                        case 4:
                            split_temp += char
                            if split_temp == "drive":
                                split_count += 1
                            else:
                                split_temp = ""
                                split_count = 0
                        case 5:
                            split_temp += char
                            if split_temp == "drive#":
                                split_count += 1
                            else:
                                split_temp = ""
                                split_count = 0
                        case 6:
                            split_temp += char
                            if split_temp == "drive#f":
                                split_count += 1
                            else:
                                split_temp = ""
                                split_count = 0
                        case 7:
                            split_temp += char
                            if split_temp == "drive#fi":
                                split_count += 1
                            else:
                                split_temp = ""
                                split_count = 0
                        case 8:
                            split_temp += char
                            if split_temp == "drive#fil":
                                split_count += 1
                            else:
                                split_temp = ""
                                split_count = 0
                        case 9:
                            split_temp += char
                            if split_temp == "drive#file":
                                split_count2 += 1
                                if split_count2 == 2:
                                    Err = True
                            split_temp = ""
                            split_count = 0
    if Err:
        print("Error found")
    else:
        print("Done")
        break

true = True
while true:
    true = False
    for i in range(0, len(split_list)):
        if split_list[i][-1] != "}":
            true = True
            end = len(split_list[i])
            split_list[i] = split_list[i][:end-1]

print("json error correction")
            
true = True
while true:
    for i in range(0, len(split_list)):
        true = False
        count = 0
        index = 0
        index_list = []
        index_temp = 0
        for char in split_list[i]:
            if count == 0 and char == '"':
                count += 1
                index_temp = index
            elif count == 1:
                if char == '"' and index == index_temp+1:
                    index_list.append(index)
                count = 0
            index += 1
        if len(index_list) > 0:
            index_list.reverse()
            for j in index_list:
                split_list[i] = split_list[i][:j] + split_list[i][j+1:]
            true = True
            


        
print("Writing...")
with open("filelist2.txt", "w") as test2files:
    for i in split_list:
        test2files.write(str(i)+"\n")
print("Complete")