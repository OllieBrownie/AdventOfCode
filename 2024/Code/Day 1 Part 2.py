from collections import Counter

with open("../Inputs/inputDay1.txt", "r") as file:
    lines = [line.strip() for line in file]

list1 = []
list2 = []

for line in lines:
    values = line.split()
    list1.append(int(values[0]))
    list2.append(int(values[1]))

list2Count = Counter(list2)
output = 0

for num in list1:
    output += num * list2Count.get(num, 0)

print(output)