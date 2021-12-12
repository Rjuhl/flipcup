import numpy as np


def findExpTime(c, r1, r2):
    p = 1 / (1 + (r1 / r2)) #Prob of success
    e1 = 1 / (r1 + r2)  #E[e_1 | e_1 < e_2] where e_1 ~ exp(r1)
    e2 = 1 / (r1 + r2) #E[e_2 | e_2 < e_1] where e_2 ~ exp(r2)

    start = (c - 1) / 2
    assert start.is_integer() and start > 0

    var_matrix = np.zeros((c, c))
    intercept_matrix = np.zeros(c)

    for i in range(c):
        var_matrix[i][i] = 1
        if i < c - 2:
            var_matrix[i + 1][i] = -1 + p
            var_matrix[i + 1][i + 2] = -p

    for i in range(1, c - 1):
        intercept_matrix[i] = (p * e1) + ((1 - p) * e2)

    ans_arr = np.linalg.solve(var_matrix, intercept_matrix)
    return ans_arr[int(start)]





