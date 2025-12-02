with open("../Inputs/inputDay1.txt", "r") as file:
    lines = [line.strip() for line in file]

dial = 50
password = 0

for instruction in lines:
    if instruction.startswith("L"):
        dial = (dial - int(instruction[1:])) % 100
    elif instruction.startswith("R"):
        dial = (dial + int(instruction[1:])) % 100
    else:
        print("Started with weird char! " + instruction)

    if dial == 0:
        password += 1
        print("It's back to zero. Password now ", password)

print("Final password is ", password)