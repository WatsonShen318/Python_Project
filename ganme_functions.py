import random as r

def create_matrix():
    """Initialize a 4x4 grid with two random 2s"""
    grid = [[0 for _ in range(4)] for _ in range(4)]
    add_new(grid)
    add_new(grid)
    return grid

def display_grid(grid):
    """Display the game grid with only * for borders"""
    for row in grid:
        print("********************") 
        print("|", end="")
        for cell in row:
            if cell == 0:
                print("    ", end="|")
            else:
                print(f"{cell:^4}", end="|")
        print()
    print("********************")  

def add_new(grid):
    """Add a new 2 in a random empty cell"""
    empty_cells = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 0]
    if empty_cells:
        i, j = r.choice(empty_cells)
        grid[i][j] = 2

def merge_left(grid):
    """Merge cells left and return if any move was made"""
    moved = False
    for i in range(4):
        # First move all numbers to left
        row = [x for x in grid[i] if x != 0]
        row += [0] * (4 - len(row))
        
        # Then merge adjacent equal numbers
        for j in range(3):
            if row[j] != 0 and row[j] == row[j + 1]:
                row[j] *= 2
                row[j + 1] = 0
                moved = True
        
        # Move numbers left again after merging
        new_row = [x for x in row if x != 0]
        new_row += [0] * (4 - len(new_row))
        
        if grid[i] != new_row:
            moved = True
        grid[i] = new_row
    
    return moved

def make_move(grid, direction):
    """Process a move in given direction"""
    # Create a copy of grid to rotate
    temp_grid = [row[:] for row in grid]
    moved = False
    
    if direction == 'a':  # Left
        moved = merge_left(temp_grid)
    elif direction == 'd':  # Right
        # Reverse rows, merge left, reverse back
        for i in range(4):
            temp_grid[i] = temp_grid[i][::-1]
        moved = merge_left(temp_grid)
        for i in range(4):
            temp_grid[i] = temp_grid[i][::-1]
    elif direction == 'w':  # Up
        # Transpose, merge left, transpose back
        temp_grid = list(map(list, zip(*temp_grid)))
        moved = merge_left(temp_grid)
        temp_grid = list(map(list, zip(*temp_grid)))
    elif direction == 's':  # Down
        # Transpose, reverse, merge left, reverse, transpose back
        temp_grid = list(map(list, zip(*temp_grid)))
        for i in range(4):
            temp_grid[i] = temp_grid[i][::-1]
        moved = merge_left(temp_grid)
        for i in range(4):
            temp_grid[i] = temp_grid[i][::-1]
        temp_grid = list(map(list, zip(*temp_grid)))
    
    if moved:
        for i in range(4):
            grid[i] = temp_grid[i][:]
    
    return grid, moved

def c_win_2048(grid):
    """Check if 2048 is reached"""
    return any(2048 in row for row in grid)

def move_available(grid):
    """Check if any move is possible"""
    # Check if there are empty cells
    if any(0 in row for row in grid):
        return True
    
    # Check if any adjacent cells can merge
    for i in range(4):
        for j in range(3):
            if grid[i][j] == grid[i][j + 1]:
                return True
    for i in range(3):
        for j in range(4):
            if grid[i][j] == grid[i + 1][j]:
                return True
    return False
