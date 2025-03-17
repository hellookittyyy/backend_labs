with open('input_5.txt', 'r') as f:
    counter = 0
    for line in f:
        blues = []
        reds = []
        greens = []
        game_info = line.split(":")
        sets = game_info[1].split(";")
        title = game_info[0]
        ids = title.split(" ")
        num = ids[1]
        for cube_set in sets:
            w_comma = cube_set.strip().split(",")
            # print("W_comma:", w_comma)
            for i in range(len(w_comma)):
                elem = w_comma[i].strip().split(" ")
                # print(elem)
                if elem[1] == "blue":
                    blues.append(elem[0])
                if elem[1] == "red":
                    reds.append(elem[0])
                if elem[1] == "green":
                    greens.append(elem[0])
        # print(title, blues)

        for i in range(len(blues)):
            blues[i] = int(blues[i])
        
        for i in range(len(reds)):
            reds[i] = int(reds[i])

        for i in range(len(greens)):
            greens[i] = int(greens[i])

        if max(blues) <= 14 and max(greens) <= 13 and max(reds) <= 12:
            # print(num)
            counter += int(num)

    print(counter)

