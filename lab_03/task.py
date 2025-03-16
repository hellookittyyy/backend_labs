with open('input_3.txt', 'r') as f:
    counter = 0

    for line in f:
        first_last = ""
        for i in range(len(line)):
            if line[i].isdigit():
                first_last += line[i]
                break
        for i in range(len(line)):
            if line[len(line)-i - 1].isdigit():
                first_last += line[len(line)-i - 1]
                break
        
        counter += int(first_last)
    
    print(counter)


