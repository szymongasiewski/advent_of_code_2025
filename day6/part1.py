problems = []

with open("input.txt", "r", encoding="utf-8") as file:
    for line in file:
        problems.append(list(line.strip().split()))

t_problems = [list(x) for x in zip(*problems)]
results = []

for x in t_problems:
    if x[-1] == '+':
        results.append(sum(map(int, x[:-1])))
    elif x[-1] == '*':
        result = 1
        for num in map(int, x[:-1]):
            result *= num
        results.append(result)

print(results)
print(sum(results))