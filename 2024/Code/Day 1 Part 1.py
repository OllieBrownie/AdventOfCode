with open("../Inputs/inputDay1.txt", "r") as file:
    lines = [line.strip() for line in file]

list1 = []
list2 = []

for line in lines:
    values = line.split()
    list1.append(int(values[0]))
    list2.append(int(values[1]))

list1.sort()
list2.sort()

output = 0

for i, num in enumerate(list1):
    output += abs(num - list2[i])

print(output)