with open("../Inputs/inputDay4.txt","r") as file:
    lines = [line.strip() for line in file]
    parsed_list = [list(string) for string in lines]
    print(parsed_list)

print(parsed_list[2][2])

directions = [
    #x, y
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, 1),
    (0, -1),
    (1, -1),
    (1, 0),
    (1, 1)
]

def is_valid_spot(row_i, col_i, max_x, max_y):
    if row_i < 0 or col_i < 0 or row_i > max_x or col_i > max_y:
        return False
    return True

def check_all_directions(present_map, directions, row_i, col_i):
    paper_count = 0
    for d in directions:
        new_row_i = row_i + d[0]
        new_col_i = col_i + d[1]
        if is_valid_spot(new_row_i, new_col_i, len(present_map)-1, len(present_map[0])-1):
            if present_map[new_row_i][new_col_i] == "@":
                paper_count += 1

    if paper_count < 4:
        return True
    return False

def attempt_more(parsed_list, directions, curr_locations):
    this_round_locations = curr_locations
    keep_going = False
    for row in range(len(parsed_list)):
        for col in range(len(parsed_list[0])):
            if parsed_list[row][col] == "@" and check_all_directions(parsed_list, directions, row, col):
                print("Found in row ", row, " and col ", col)
                parsed_list[row][col] = "x"
                this_round_locations += 1

    if this_round_locations > curr_locations:
        keep_going = True
    return this_round_locations, keep_going

go = True
total = 0
while go:
    total, go = attempt_more(parsed_list, directions, total)

print(total)