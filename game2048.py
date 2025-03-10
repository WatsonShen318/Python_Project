import os
from game_functions import *

def main():
    # Initialize the game with a 4x4 grid
    grid = create_matrix()
    
    while True:
        try:
            # Clear the screen for better visualization (Windows: cls, Unix: clear)
            os.system('cls' if os.name == 'nt' else 'clear')
            
            # Display the current state of the game grid
            display_grid(grid)
            
            # Get user input for movement or commands
            move = input("Enter input to move (w/a/s/d), 'h' for help, or 'exit' to quit: ").lower()
            
            # Exit the game if user enters 'exit'
            if move == 'exit':
                print("Thanks for playing!")
                break
            
            # Show help message with key instructions and rules if user enters 'h'
            if move == 'h':
                print("\n=== 2048 Game Help ===")
                print("Key Instructions:")
                print("  w - Move Up")
                print("  a - Move Left")
                print("  s - Move Down")
                print("  d - Move Right")
                print("  h - Show this help")
                print("  exit - Quit the game")
                print("Rules:")
                print("  - Use w/a/s/d to slide tiles in the desired direction.")
                print("  - Same numbers merge into their sum when they touch.")
                print("  - A new 2 appears after each move.")
                print("  - Reach 2048 to win!")
                print("  - Game ends when no moves are possible.")
                input("Press Enter to continue...")
                continue
                
            # Validate input; raise error if not a valid move
            if move not in ['w', 'a', 's', 'd']:
                raise ValueError("Invalid input! Use w/a/s/d, h for help, or exit to quit.")
            
            # Process the move based on user input
            grid, moved = make_move(grid, move)
            
            # If a move was successful, add a new 2 to the grid
            if moved:
                add_new(grid)
            
            # Check if the player has won by reaching 2048
            if c_win_2048(grid):
                display_grid(grid)
                print("Congratulations! You reached 2048!")
                play_again = input("Play again? (y/n): ").lower()
                if play_again == 'y':
                    grid = create_matrix()  # Restart with a new grid
                else:
                    print("Thanks for playing!")
                    break
                    
            # Check if no more moves are possible (game over)
            if not move_available(grid):
                display_grid(grid)
                print("Game Over! No more moves possible.")
                play_again = input("Play again? (y/n): ").lower()
                if play_again == 'y':
                    grid = create_matrix()  # Restart with a new grid
                else:
                    print("Thanks for playing!")
                    break
                    
        except ValueError as e:
            print(e)
            input("Press Enter to continue...")

if __name__ == "__main__":
    # Start the game
    main()
