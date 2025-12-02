with open("../Inputs/inputDay2.txt", "r") as file:
    blocks = [line.split(",") for line in file][0] # only 1 row

def get_score_for_id_range(block):
    first, second = block.split("-")
    scores = []
    print(first, "and", second)
    for i in range(int(first), int(second)+1): # have to add one to avoid missing
        str_i = str(i)
        length = len(str_i)
        if(length % 2 == 0
        and str_i[:length//2] == str_i[length//2:]):
            print("found match ", i)
            scores.append(i)
    return sum(scores)

final_score = 0
for block in blocks:
    final_score += get_score_for_id_range(block)

print("final score is ", final_score)