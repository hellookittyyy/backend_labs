with open('input_5.txt', 'r') as f:
    counter = 0
    for line in f:
        blues = []
        reds = []
        greens = []
        first_split = line.split(":")
        # print("first_split:", first_split)
        second_split = first_split[1].strip().split(";")
        # print("second_split:", second_split)
        for i in second_split:
            third_split = i.strip().split(",")
            # print("third_split:", third_split)
            for j in third_split:
                fourth_split = j.strip().split(" ")
                # print("fourth_split:", fourth_split)
                if fourth_split[1] == "blue":
                    blues.append(int(fourth_split[0]))
                if fourth_split[1] == "red":
                    reds.append(int(fourth_split[0]))
                if fourth_split[1] == "green":
                    greens.append(int(fourth_split[0]))
                    
        # print(greens)
        counter += max(blues)*max(greens)*max(reds)
    print(counter)