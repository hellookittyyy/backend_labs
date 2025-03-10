first = []
second = []

with open('input_1.txt', 'r', encoding='utf-8') as f:
    for line in f:
            row = line.split("   ")
            first.append(int(row[0].strip()))
            second.append(int(row[1].strip()))

result = 0

for num in first:
    ammount = second.count(num)
    result += ammount * num

print(result)
        