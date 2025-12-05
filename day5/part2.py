ranges = []

with open("input.txt", "r", encoding="utf-8") as file:
    for line in file:
        if '-' in line:
            ranges.append(tuple(map(int, line.strip().split('-'))))

ranges = sorted(ranges, key=lambda x: x[0])

valid_ids = 0
curr_max_id = 0

for start, end in ranges:
    if end >= curr_max_id:
        valid_ids += end - max(start, curr_max_id) + 1
        curr_max_id = end + 1

print(valid_ids)
        