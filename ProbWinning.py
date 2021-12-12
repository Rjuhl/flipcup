import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def findWinningChances(c, r1, r2):
    p = 1 / (1 + (r1 / r2)) #Find prob player1 wins at checkpoint
    ends = (c - 1) / 2
    assert ends.is_integer() and ends > 0

    trans_matrix = np.zeros((c - 2, c - 2))
    s_matrix = np.zeros((2, c-2))
    s_matrix[0][0] = 1 - p # Fill in s_matrix
    s_matrix[1][c - 3] = p # Fill in s_matrix
    for i in range(c - 2): # Fills transition matrix
        trans_matrix[i][i] = 1
        if i < c - 3:
            trans_matrix[i + 1][i] = -p
            trans_matrix[i][i + 1] = -1 + p
    inverse_matrix = np.linalg.inv(trans_matrix)
    ans_matrix = np.matmul(s_matrix, inverse_matrix) # Compute answers for each state
    p1_win_prob = ans_matrix[0][int((c - 3) / 2)] # Find answer for game start state
    return p1_win_prob

def graph3D(ranges, const_dim, c=None, r1=None, r2=None):
    if const_dim == 0:
        r1vals = [i for i in range(1, ranges[0])]
        r2vals = [i for i in range(1, ranges[1])]
        X, Y = np.meshgrid(r1vals, r2vals)
        Z = np.zeros(X.shape)
        for i in range(X.shape[0]):
            for j in range(X.shape[1]):
                Z[i][j] = findWinningChances(c, X[i][j], Y[i][j])
        ax = plt.axes(projection='3d')
        ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                        cmap='viridis', edgecolor='none')
        ax.set_title(f'Chance of player 1 winning (Checkpoints = {c})')
        ax.set_xlabel('Rate of Player 1')
        ax.set_ylabel('Rate of Player 2')
        ax.set_zlabel('Chance of Player 1 Winning')
        plt.show()
    elif const_dim == 1:
        c_vals = [i for i in range(5, ranges[0], 2)]
        r2_vals = [i for i in range(1, ranges[1])]
        X, Y = np.meshgrid(c_vals, r2_vals)
        Z = np.zeros(X.shape)
        for i in range(X.shape[0]):
            for j in range(X.shape[1]):
                Z[i][j] = findWinningChances(X[i][j], r1, Y[i][j])
        ax = plt.axes(projection='3d')
        ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                        cmap='viridis', edgecolor='none')
        ax.set_title(f'Chance of player 1 winning (R1 = {r1})')
        ax.set_xlabel('Number of Checkpoints')
        ax.set_ylabel('Rate of Player 2')
        ax.set_zlabel('Chance of Player 1 Winning')
        plt.show()
    elif const_dim == 2:
        c_vals = [i for i in range(5, ranges[0], 2)]
        r1_vals = [i for i in range(1, ranges[1])]
        X, Y = np.meshgrid(c_vals, r1_vals)
        Z = np.zeros(X.shape)
        for i in range(X.shape[0]):
            for j in range(X.shape[1]):
                Z[i][j] = findWinningChances(X[i][j], Y[i][j], r2)
        ax = plt.axes(projection='3d')
        ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                        cmap='viridis', edgecolor='none')
        ax.set_title(f'Chance of player 1 winning (R1 = {r2})')
        ax.set_xlabel('Number of Checkpoints')
        ax.set_ylabel('Rate of Player 1')
        ax.set_zlabel('Chance of Player 1 Winning')
        plt.show()
    else:
        print(f"Error const_dim = {const_dim} not a # between 1 and 2 inclusive")

def graph2D(r1, r2, ran):
    c_vals = [i for i in range(5, ran, 2)]
    results = []
    for num in c_vals:
        results.append(findWinningChances(num, r1, r2))
    plt.plot(c_vals, results)
    plt.title(f'Chance player 1 wins when rate 1 = {r1} and rate 2 = {r2}')
    plt.xlabel('Number of Checkpoints')
    plt.ylabel('Chance of winning for player 1')
    plt.show()




