# Minesweeper

Minesweeper is a classic puzzle game where players must uncover a grid of cells without triggering hidden mines. This Python implementation offers a fully interactive command-line version with additional debugging and testing features.

## Features
- **Customizable Board Size**: Choose a board size between 4x4 and 9x9. 
- **Adjustable Mine Count**: Specify the number of mines for the game. 
- **Flagging System**: Flag cells that you suspect contain mines.
- **Debug Mode**: Reveal the entire board for testing or debugging.
- **Victory Check**: Automatically detects when the player wins by uncovering all safe cells.
- **Unit Tests**: Built-in tests to validate key functions like mine placement and neighbor value calculations.

## Rules
1. Reveal cells to uncover the grid.
2. If you reveal a mine, you lose the game.
3. Numbers on cells indicate how many mines are adjacent.
4. Use flags to mark cells you suspect contain mines.
5. Win by uncovering all safe cells without triggering any mines.

## Installation
1. Clone the repository:
   
   \`\`\`bash
   git clone <repository_url>
   \`\`\`
2. Navigate to the project directory:
   \`\`\`bash
   cd Minesweeper
   \`\`\`
3. Run the game:
   \`\`\`bash
   python minesweeper_improve.py
   \`\`\`

## Usage
Start the game by specifying the board size and the number of mines.  
Use the following commands during gameplay:  
- \*\*`r`\*\*: Reveal a cell by entering its row and column.  
- \*\*`f`\*\*: Flag or unflag a cell suspected to contain a mine.  
- \*\*`d`\*\*: Enter debug mode to reveal the entire board.  

### Example Gameplay
\`\`\`
Welcome to Minesweeper!

Rules:
1. Choose a cell to reveal by entering its row and column.
2. Flag cells you suspect contain mines.
3. Reveal all safe cells to win.
4. Hitting a mine results in game over.

Enter board size (4-9): 5
Enter number of mines (1-25): 5

<pre>
    1   2   3   4   5
  +---+---+---+---+---+
1 |   |   |   |   |   |
  +---+---+---+---+---+
2 |   |   |   |   |   |
  +---+---+---+---+---+
3 |   |   |   |   |   |
  +---+---+---+---+---+
4 |   |   |   |   |   |
  +---+---+---+---+---+
5 |   |   |   |   |   |
  +---+---+---+---+---+
</pre>

Enter 'r' to reveal, 'f' to flag/unflag, or 'd' for debug mode:
\`\`\`

### Debug Mode
Debug mode is useful for testing. It reveals the entire board, including mine locations.

To enter debug mode, type \*\*`d`\*\* when prompted during the game.

## Testing
The game includes built-in unit tests to validate the core logic:

- \*\*`test_set_mines`\*\*: Ensures the correct number of mines is placed.  
- \*\*`test_set_values`\*\*: Verifies that neighboring mine counts are calculated correctly.  

### Automatic Testing
Tests are executed automatically when the program starts. If the tests pass, the game will proceed as normal. If a test fails, you will see a message indicating the failure, and the game will terminate.

Example output when tests pass:

\`\`\`
test_set_mines passed!
test_set_values passed!
Starting Minesweeper...
\`\`\`

If a test fails, you might see something like:

\`\`\`
test_set_mines failed: Expected 10 mines, but found 8.
\`\`\`

## Contributing
Feel free to fork the repository, open issues, or submit pull requests. Contributions are welcome!

## Author
Eran Helvitz Developer and maintainer of the project.
