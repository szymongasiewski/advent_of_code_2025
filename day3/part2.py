banks = []
jolts = []

with open("input.txt", "r", encoding="utf-8") as file:
    for line in file:
        banks.append(line.strip())


for bank in banks:
    remove_count = len(bank) - 12
    stack = []
    for digit in bank:
        while stack and remove_count > 0 and stack[-1] < digit:
            stack.pop()
            remove_count -= 1

        stack.append(digit)

    jolts.append(int("".join(stack[:12])))


print(jolts)
print(sum(jolts))