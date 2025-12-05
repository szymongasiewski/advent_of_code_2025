ranges = []
ids = []

with open("input.txt", "r", encoding="utf-8") as file:
    for line in file:
        if '-' in line:
            ranges.append(tuple(map(int, line.strip().split('-'))))
        elif line != '\n':
            ids.append(int(line.strip()))

available_ids = {}

for start, end in ranges:
    for id in ids:
        if start <= id <= end:
            available_ids[id] = True

print(available_ids)
print(len(available_ids))