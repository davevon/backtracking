import matplotlib.pyplot as plt
import timeit 
def is_safe(board, row, col, n):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check if there is a queen in the left upper diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check if there is a queen in the right upper diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False
    
    return True

def visualize_solution(board):
    n = len(board)
    plt.figure(figsize=(n, n))
    
    for row in range(n):
        for col in range(n):
            if board[row][col] == 1:
                plt.plot(col + 0.5, n - row - 0.5, 'bo', markersize=20)
            else:
                plt.plot(col + 0.5, n - row - 0.5, 'ro', markersize=20)
    
    plt.xlim(0, n)
    plt.ylim(0, n)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xticks([])
    plt.yticks([])
    plt.grid()
    plt.show()

def solve_n_queens_util(board, row, n):
    if row == n:
        return True
    
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve_n_queens_util(board, row + 1, n):
                return True
            board[row][col] = 0
    
    return False

def solve_n_queens_visualized(n):
    board = [[0] * n for _ in range(n)]
    
    setup_code = """
from __main__ import solve_n_queens_util
board = [[0] * {} for _ in range({})]
""".format(n, n)
    
    algorithm_code = """
solve_n_queens_util(board, 0, {})
""".format(n)
    
    time_taken = timeit.timeit(algorithm_code, setup=setup_code, number=1)
    
    if not solve_n_queens_util(board, 0, n):
        print("No solution exists.")
        return
    
    visualize_solution(board)
    print("Time taken: {:.6f} seconds".format(time_taken))

# ...







# Example usage
n = 5  # Change this to the desired board size
solve_n_queens_visualized(n)
