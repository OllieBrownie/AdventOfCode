with open("../Inputs/exampleInputDay1.txt", "r") as file:
    lines = [line.strip() for line in file]

dial = 50
password = 0

def go_left(curr, num_left):
    num_zeros = 0
    while num_left > 0:
        curr -= 1
        if curr < 0:
            curr = 99
        if curr == 0:
            num_zeros += 1
        num_left -= 1
    return curr, num_zeros

def go_right(curr, num_right):
    num_zeros = 0
    while num_right > 0:
        curr += 1
        if curr > 99:
            curr = 0
        if curr == 0:
            num_zeros += 1
        num_right -= 1
    return curr, num_zeros

temp_pw = 0
for instruction in lines:
    if instruction.startswith("L"):
        dial, temp_pw = go_left(dial, int(instruction[1:]))
    elif instruction.startswith("R"):
        dial, temp_pw = go_right(dial, int(instruction[1:]))
    else:
        print("Started with weird char! " + instruction)

    password += temp_pw
    temp_pw = 0

print("Final password is ", password)
