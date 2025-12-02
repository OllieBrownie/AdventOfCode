with open("../Inputs/inputDay2.txt", "r") as file:
    blocks = [line.split(",") for line in file][0] # only 1 row

def get_possible_pattern_lengths(length):
    # we can only have patterns that exactly divide into the length of the id
    patterns = []
    for i in range(1, length):
        if length % i == 0:
            patterns.append(i)
    return patterns


def is_repeating(id):
    str_id = str(id)
    length = len(str_id)
    possible_pattern_lengths = get_possible_pattern_lengths(length)
    print(possible_pattern_lengths)
    for pattern_length in possible_pattern_lengths:
        curr_index = 0
        while curr_index < length - pattern_length:
            first_chunk = str_id[curr_index:curr_index+pattern_length]
            second_chunk = str_id[curr_index+pattern_length:curr_index + 2*pattern_length]
            if first_chunk != second_chunk:
                break
            curr_index += pattern_length
        if curr_index + pattern_length == length:
            return True
    return False


def get_score_for_id_range(block):
    first, second = block.split("-")
    scores = []
    print(first, "and", second)
    for i in range(int(first), int(second)+1): # have to add one to avoid missing
        if is_repeating(i):
            print("found match ", i)
            scores.append(i)
    return sum(scores)

final_score = 0
for block in blocks:
    final_score += get_score_for_id_range(block)

print("final score is ", final_score)