
with open('input.txt', 'r') as f:
    grid = f.readlines()

splits = 0
beams = {grid[0].index('S')}

for row in grid:
    next_beams = set()
    for i in beams:
        if row[i] == '^':
            splits += 1
            next_beams.add(i - 1)
            next_beams.add(i + 1)
        else:
            next_beams.add(i)
    beams = next_beams

print(splits)