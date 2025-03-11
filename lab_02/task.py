with open('input_2.txt', 'r') as f:
    counter = 0
    for line in f:
        array = line.split(" ")
        result_decreasing = True
        result_increasing = True
        result_distance = True
        for i in range(len(array) - 1):
            a=int(array[i])
            b=int(array[i + 1])
            if a <= b:
                result_decreasing = False
            if a >= b:
                result_increasing = False
            if abs(a - b) < 1 or abs(a - b) > 3:
                result_distance = False
        if (result_decreasing or result_increasing) and result_distance:
            print(line.strip(), "it`s safe", sep=" - ")
            counter += 1
        else:
            print(line.strip(), "it`s not safe", sep=" - ")
            
    print(counter)   
