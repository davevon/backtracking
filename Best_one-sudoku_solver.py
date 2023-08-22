import pygame
import sys
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

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

def draw_congratulations():
    congrats_text = font.render("Congratulations! Puzzle solved!", True, BLACK)
    x = (WIDTH - congrats_text.get_width()) // 2
    y = HEIGHT // 2
    screen.blit(congrats_text, (x, y))

def is_solved():
    for row in grid:
        if 0 in row:
            return False
    return True

def solve_sudoku():
    # Implementation of your Sudoku-solving algorithm
    pass

def main():
    global grid  # Declare grid as global
    global taskbar_congrats

    clock = pygame.time.Clock()
    running = True
    selected_cell = None
    solved = False
    solved_timer = None
    taskbar_congrats = False  # Flag for displaying congratulation message in taskbar
    
    
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
        
        if is_solved() and not solved:
            solved = True
            solved_timer = pygame.time.get_ticks()
            start_time = datetime.now()
        
        screen.fill(WHITE)
        draw_grid()
        draw_numbers()
        
        if solved:
            draw_congratulations()
            if pygame.time.get_ticks() - solved_timer > 10000:  # Wait for 10 seconds
                solved = False
                grid = [  # Reset the grid
                    [5, 3, 0, 0, 7, 0, 0, 0, 0],
                    [6, 0, 0, 1, 9, 5, 0, 0, 0],
                    [0, 9, 8, 0, 0, 0, 0, 6, 0],
                    [8, 0, 0, 0, 6, 0, 0, 0, 3],
                    [4, 0, 0, 8, 0, 3, 0, 0, 1],
                    [7, 0, 0, 0, 2, 0, 0, 0, 6],
                    [0, 6, 0, 0, 0, 0, 2, 8, 0],
                    [0, 0, 0, 4, 1, 9, 0, 0, 5],
                    [0, 0, 0, 0, 8, 0, 0, 7, 9]
                 #   
                ]
                solved_timer = None
                if start_time:
                    end_time = datetime.now()
                    time_difference = end_time - start_time
                    popup_window(time_difference.total_seconds())
                start_time = None
        
        if selected_cell is not None:
            pygame.draw.rect(screen, GRAY, (selected_cell[1] * WIDTH // 9, selected_cell[0] * HEIGHT // 9, WIDTH // 9, HEIGHT // 9), 3)
        
        pygame.display.flip()
        clock.tick(60)
        if taskbar_congrats:
            pygame.display.set_caption("Sudoku Solver - Congratulations!")

        else:
            pygame.display.set_caption("Sudoku Solver")
    pygame.quit()
    sys.exit()

def popup_window(time_elapsed):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Time Elapsed", f"Time Elapsed: {time_elapsed:.2f} seconds")
    root.destroy()    

if __name__ == "__main__":
    main()
