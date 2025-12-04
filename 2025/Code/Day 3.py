with open("../Inputs/inputDay3.txt", "r") as file:
    blocks = [line.strip() for line in file]

total = 0

def insert_into_max_array(char, curr_max_array, curr_index, row_length):
    starting_max_index = len(curr_max_array) - min(len(curr_max_array), row_length - curr_index)

    has_found = False
    for i in range(starting_max_index, len(curr_max_array)):
        if has_found:
            curr_max_array[i] = -1
        elif char > curr_max_array[i]:
            curr_max_array[i] = char
            has_found = True
    return curr_max_array

for block in blocks:
    max_array = [-1] * 2
    curr_best = 0
    max_array[0] = int(block[0])
    for i in range(1,len(block)):
        c = int(block[i])
        max_array = insert_into_max_array(c,max_array,i,len(block))
    total_str = "".join(map(str,max_array))
    total += int(total_str)

print(total)