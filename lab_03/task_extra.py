with open('input_3.txt', 'r') as f:
    counter = 0
    dictionary = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    for line in f:
        temporarry = ""
        first_last = ""

        for i in range(len(line)):
            if line[i].isdigit():
                temporarry += line[i]

            else:
                for j in dictionary:
                    if len(j)+i <= len(line):
                        part_line = line[i:i+len(j)]
                        if part_line == j:
                            temporarry += dictionary[j]
        for i in range(len(temporarry)):
            if temporarry[i].isdigit():
                first_last += temporarry[i]
                break
        for i in range(len(temporarry)):
            if temporarry[len(temporarry)-i - 1].isdigit():
                first_last += temporarry[len(temporarry)-i - 1]
                break
        
        counter += int(first_last)
    
    print(counter)
        
            

