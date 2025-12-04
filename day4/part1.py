init_matrix = []

with open("input.txt", "r", encoding="utf-8") as file:
    for line in file:
        init_matrix.append(list(line.strip()))

init_matrix_num = [[1 if x == '@' else 0 for x in y] for y in init_matrix]

sum_init_matrix = sum([sum(x) for x in init_matrix_num])

kernel = [[1, 1, 1],
          [1, 0, 1],
          [1, 1, 1]]

from scipy.signal import convolve2d

sum_matrix = convolve2d(init_matrix_num, kernel, mode='same', boundary='fill', fillvalue=0)


sum_matrix = [[0 if init_matrix_num[i][j] == 0 or sum_matrix[i][j] < 4 else 1 
               for j in range(len(sum_matrix[0]))] for i in range(len(sum_matrix))]

sum_sum_matrix = sum([sum(x) for x in sum_matrix])

print(sum_init_matrix)
print(sum_sum_matrix)
print(sum_init_matrix - sum_sum_matrix)
