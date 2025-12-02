with open("../Inputs/inputDay2.txt", "r") as file:
    lines = [line.strip() for line in file]
    parsed_list = [[int(num) for num in string.split()] for string in lines]
    print(parsed_list)

    safe = 0

    for l in parsed_list:
        curr_safe = 1
        for i in range(1, len(l)):
            if i == 1:
                direction = ""
                if l[i - 1] > l[i]:
                    direction = "dec"
                elif l[i - 1] < l[i]:
                    direction = "inc"
                else:
                    break

            diff = l[i-1] - l[i]
            if direction == "dec":
                if not(1 <= diff <= 3):
                    curr_safe=0

            if direction == "inc":
                if not(-3 <= diff <= -1):
                    curr_safe=0

            if i == len(l) - 1:
                safe += curr_safe

    print(safe)

