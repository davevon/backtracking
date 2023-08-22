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
def visualize_solution(board, time_taken):
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
    
    # Display the time taken on the visualization
    plt.text(0.5, -0.1, "Time taken: {:.6f} seconds".format(time_taken),
             horizontalalignment='center', verticalalignment='center',
             transform=plt.gca().transAxes)
    
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
    
    visualize_solution(board, time_taken)

# Example usage
n = 5  # Change this to the desired board size
solve_n_queens_visualized(n)




############################## Discussion #############################

""" Time Complexity Analysis:

The time complexity of the N-Queens backtracking algorithm is typically upper-bounded by O(n!), where 'n' is the number of rows/columns in the chessboard. However, due to pruning and early stopping, the effective number of recursive calls is much less than n! in practice.

Optimizations:

Early Exit: If the algorithm finds a solution, it can immediately return, as only one solution is required.

Column Check Optimization: The 'is_safe' function can be optimized by maintaining an array of boolean values for each column, left diagonal, and right diagonal to check for conflicts. This can reduce the time complexity of conflict checking.

Symmetry Reduction: Since the N-Queens problem exhibits rotational and reflective symmetries, you can reduce the search space by considering only a subset of solutions and then deriving the rest using symmetry transformations.

Bitwise Operations: Using bitwise operations can improve memory efficiency and speed up the computation of valid positions for queens.

Parallelization: The backtracking process can be parallelized to explore different branches simultaneously, improving overall efficiency.

Remember that while these optimizations can significantly improve the performance of the algorithm, the N-Queens problem's worst-case time complexity remains exponential due to its inherent nature. """