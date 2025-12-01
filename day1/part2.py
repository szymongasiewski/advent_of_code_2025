dial = 50
rotations = []
zeros = 0 

with open("input.txt", "r", encoding="utf-8") as file:
    for line in file:
        rotations.append(line)

for rotation in rotations:
    direction = rotation[0]
    clicks = int(rotation[1:])
    
    if direction == "R":
        new_pos = dial + clicks
        zeros += new_pos // 100
        dial = new_pos % 100
    else:
        if dial == 0:
            new_pos = dial - clicks
            zeros += abs(new_pos // 100) - 1
            dial = new_pos % 100
        else:
            new_pos = dial - clicks
            zeros += abs(new_pos // 100)
            dial = new_pos % 100
        if dial == 0:
            zeros += 1
    

print(dial)
print(zeros)