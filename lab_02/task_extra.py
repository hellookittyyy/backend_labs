def check(array):
    result_decreasing = True
    result_increasing = True
    result_distance = True
    for i in range(len(array) - 1):
        a = int(array[i])
        b = int(array[i + 1])
        if a <= b:
            result_decreasing = False
        if a >= b:
            result_increasing = False
        if abs(a - b) < 1 or abs(a - b) > 3:
            result_distance = False
    if (result_decreasing or result_increasing) and result_distance:
        return True
    else:
        return False

with open('input_2.txt', 'r') as f:
    for line in f:
        array = line.split(" ")
        if check(array):
            print(line.strip(), "it`s safe", sep=" - ")
        else:
            safe = False
            for i in range(len(array)):
                array2 = array.copy()
                del_num = array2.pop(i)
                if check(array2):
                    safe = True
                    print(line.strip(), "it`s safe by del " + del_num, sep=" - ")
                    break
            if not safe:
                print(line.strip(), "it`s unsafe regardless of which level is removed.", sep=" - ")

    
