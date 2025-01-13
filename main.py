import os
import time
import numpy as np

# Function to print the grid
def print_grid(grid):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in grid:
        print(''.join('#' if cell else ' ' for cell in row))
    print()

# Function to compute the next state of the grid
def next_generation(grid):
    rows, cols = grid.shape
    new_grid = np.zeros((rows, cols), dtype=int)  # Use NumPy array

    for r in range(rows):
        for c in range(cols):
            # Count live neighbors
            live_neighbors = 0
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        live_neighbors += grid[nr, nc]  # NumPy indexing

            # Apply Conway's rules
            if grid[r, c] == 1:  # Live cell
                new_grid[r, c] = 1 if live_neighbors in [2, 3] else 0
            else:  # Dead cell
                new_grid[r, c] = 1 if live_neighbors == 3 else 0

    return new_grid

# Main function to run the Game of Life
def game_of_life():
    # Initialize the grid (customize as needed)
    rows, cols = 20, 20
    grid = np.zeros((rows, cols), dtype=int)

    # Add some initial patterns (e.g., glider)
    grid[1, 2] = grid[2, 3] = grid[3, 1] = grid[3, 2] = grid[3, 3] = 1

    # Run the game loop
    generation = 0
    while True:
        print(f"Generation: {generation}")
        print_grid(grid)
        grid = next_generation(grid)
        generation += 1
        time.sleep(0.5)

if __name__ == "__main__":
    game_of_life()