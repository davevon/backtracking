""" def is_valid(board, row, col, num):
    # Check if the num can be placed at the given position
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    subgrid_row, subgrid_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[subgrid_row + i][subgrid_col + j] == num:
                return False
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

# Example Sudoku puzzle (0 represents empty cells)
puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve_sudoku(puzzle):
    for row in puzzle:
        print(row)
else:
    print("No solution exists.")
 """

import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Solver")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Fonts
font = pygame.font.Font(None, 36)

# Create a 9x9 grid
grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def draw_grid():
    for i in range(10):
        if i % 3 == 0:
            thickness = 4
        else:
            thickness = 1
        pygame.draw.line(screen, BLACK, (0, i * HEIGHT // 9), (WIDTH, i * HEIGHT // 9), thickness)
        pygame.draw.line(screen, BLACK, (i * WIDTH // 9, 0), (i * WIDTH // 9, HEIGHT), thickness)

def draw_numbers():
    for row in range(9):
        for col in range(9):
            if grid[row][col] != 0:
                num = font.render(str(grid[row][col]), True, BLACK)
                x = col * WIDTH // 9 + (WIDTH // 9 - num.get_width()) // 2
                y = row * HEIGHT // 9 + (HEIGHT // 9 - num.get_height()) // 2
                screen.blit(num, (x, y))

def solve_sudoku():
    # Implementation of your Sudoku-solving algorithm
    pass

def main():
    clock = pygame.time.Clock()
    running = True
    selected_cell = None
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    solve_sudoku()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                row = y // (HEIGHT // 9)
                col = x // (WIDTH // 9)
                selected_cell = (row, col)
            if event.type == pygame.KEYDOWN and selected_cell:
                if event.unicode.isdigit():
                    grid[selected_cell[0]][selected_cell[1]] = int(event.unicode)
                    selected_cell = None

        screen.fill(WHITE)
        draw_grid()
        draw_numbers()
        
        if selected_cell:
            pygame.draw.rect(screen, GRAY, (selected_cell[1] * WIDTH // 9, selected_cell[0] * HEIGHT // 9, WIDTH // 9, HEIGHT // 9), 3)
        
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
