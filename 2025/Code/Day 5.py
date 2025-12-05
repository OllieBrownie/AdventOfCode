with open("../Inputs/inputDay5.txt", "r") as file:
    rows = [line.strip() for line in file]

def parse_input(rows):
    ingredients = []
    ranges = {}
    found_space = False
    for row in rows:
        if not row:
            found_space = True
        elif not found_space:
            start, end = map(int, row.split("-", maxsplit=2))
            if start not in ranges:
                ranges[start] = end
            else:
                ranges[start] = max(ranges[start], end)
        else:
            ingredients.append(int(row))
    return ranges, ingredients

def part_1(ranges, ingredients):
    fresh = 0
    for i in ingredients:
        for start, end in ranges.items():
            if start <= i <= end:
                fresh += 1
                break
    return fresh

def update_ranges(new_start, new_end, ranges):
    for start, end in ranges.items():
        if start <= new_start <= end:
            ranges[start] = max(end, new_end)
            return ranges

    ranges[new_start] = new_end
    return ranges

def part_2(ranges):
    deduped_ranges = {}
    for start, end in sorted(ranges.items()):
        deduped_ranges = update_ranges(start, end, deduped_ranges)

    total = 0
    for start, end in deduped_ranges.items():
        total += end - start + 1
    return total



ranges, ingredients = parse_input(rows)
print(ranges)
print(ingredients)
print(part_1(ranges, ingredients))
print(part_2(ranges))
