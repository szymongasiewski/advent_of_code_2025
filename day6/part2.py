problems = []

with open("input.txt", "r", encoding="utf-8") as file:
    for line in file:
        problems.append(list(line.strip("\n")))

r_problems = [row[::-1] for row in problems]
operators = r_problems[-1]
operators = [x for x in operators if x.strip() != '']
t_problems = [list(x) for x in zip(*r_problems[:-1])]
l_problems = []

for x in t_problems:
    if ''.join(x).strip() != '':
        l_problems.append(''.join(x).strip())
    else:
        l_problems.append(operators[0])
        operators = operators[1:]

l_problems.append(operators[0])

operation = []
results = []

for x in l_problems:
    if x == '+':
        sum_result = sum(operation)
        results.append(sum_result)
        operation = []
    elif x == '*':
        prod_result = 1
        for num in operation:
            prod_result *= num
        results.append(prod_result)
        operation = []
    else:
        operation.append(int(x))


print(results)
print(sum(results))
