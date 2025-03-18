with open('input_4.txt', 'r') as f:
    array = []
    print("- / (dir)")
    is_ls = False
    t_counter = 0
    directories = []
    stack = ["/"]
    sizes = {}
    total_sum = 0
    for line in f:
        array.append(line)

    for i in range(len(array)):
        if array[i].find("dir") >= 0:
            dir_split = array[i].split(" ")
            directories.append(dir_split[1].strip())


        x = array[i].strip().split(" ")    

        if x[1] == "cd" and x[2] == "..":
            t_counter -= 1
            # print(sizes)
            # print(stack)
            size = stack.pop()
            if stack[-1] not in sizes.keys():
                sizes[stack[-1]] = sizes[size]
            else:
                sizes[stack[-1]] += sizes[size]
        for j in directories:
            if array[i].find("cd") >= 0:
                x = array[i].strip().split(" ")
                if x[1] == "cd" and  x[2] == j:
                    t_counter += 1
                    print("  "*t_counter + "-", j, "(dir)")
                    # path = "/"
                    path = stack[-1] + j + "/"
                    stack.append(path)
                    break
        if x[0] != "$" and x[0] != "dir":
            dir_file = array[i].strip().split(" ")
            print("  "*(t_counter+1) + "-", dir_file[1],"(file, size = "+dir_file[0]+")")
            if stack[-1] not in sizes.keys():
                sizes[stack[-1]] = int(dir_file[0])
            else:
                sizes[stack[-1]] += int(dir_file[0])

    # print(sizes)

    for i in sizes:
        if sizes[i] <= 100000:
            total_sum += sizes[i]
    print("",total_sum)
                    # print(x)
                # if array[i].find("cd") >= 0:
                #     is_ls = False

                # if is_ls:
                #     print(array[i].strip())
                
                # if array[i].find("ls") >= 0:
                #     is_ls = True

    # print(directories)  
        
        # a = line.find("$ cd")
        

        