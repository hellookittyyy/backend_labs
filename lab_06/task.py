def check_inst(me):
    if me == "X":
        return 1
    elif me == "Y":
        return 2
    elif me == "Z":
        return 3
    else:
        return 0

with open('input_6.txt', 'r') as f:
    your_score = 0
    #A = X = 1 # rock
    #B = Y = 2 # paper
    #C = Z = 3 # scissors

    # AX = draw (4), AY = my win(8), AZ = my f(3)
    # BX = my f(1), BY = draw(5), BZ = my win(9)
    # CX = my win (7), CY = my f(2), CZ = draw(6)

    for line in f:
        array = line.strip().split(" ")
        opp = array[0]
        me = array[1]
            
        if (opp == "A" and me == "X") or (opp == "B" and me == "Y") or (opp == "C" and me == "Z"):
            your_score += 3 + check_inst(me)
        elif (opp == "A" and me == "Y") or (opp == "B" and me == "Z") or (opp == "C" and me == "X"):
            your_score +=6 + check_inst(me)
        else:
            your_score += check_inst(me) 

    print(your_score)
        
            

