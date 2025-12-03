banks = []
jolts = []

with open("input.txt", "r", encoding="utf-8") as file:
    for line in file:
        banks.append(line.strip())

for bank in banks:
    bank_length = len(bank)
    best = 0
    suffix_max = bank_length * [0]
    suffix_max[-1] = -1

    if bank_length < 2:
        best = 0
    else:
        for i in range(bank_length - 2, -1, -1):
            suffix_max[i] = max(suffix_max[i+1], int(bank[i+1]))

        for i in range(bank_length-1):
            value = int(bank[i]) * 10 + suffix_max[i]

            if value > best:
                best = value
    jolts.append(best)

print(jolts)
print(sum(jolts))