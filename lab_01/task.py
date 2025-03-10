first = []
second = []
distances = []

with open('input_1.txt', 'r', encoding='utf-8') as f:
        for line in f:
            row = line.split("   ")
            first.append(int(row[0].strip()))
            second.append(int(row[1].strip()))

# print(first)
# print(second)

while len(first) != 0 and len(second) != 0:
    distances.append(abs(min(first)-min(second)))
    first.remove(min(first))
    second.remove(min(second))

# print(distances)
result = sum(distances)
print(result)
   