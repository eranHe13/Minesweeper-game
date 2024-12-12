import random
from collections import deque
import time

class MSSquare:
    """Represents a single square on the Minesweeper board."""
    def __init__(self, has_mine=False, hidden=True, neighbor_mines=0):
        self.has_mine = has_mine
        self.hidden = hidden
        self.neighbor_mines = neighbor_mines

class MinesweeperBoard:
    """Handles the board logic for Minesweeper."""
    def __init__(self, size, mine_count):
        if mine_count > size * size:
            raise ValueError("Number of mines cannot exceed total squares on the board.")
        self.size = size
        self.mine_count = mine_count
        self.board = [[MSSquare() for _ in range(size)] for _ in range(size)]
        self.visible_cells = []  # Tracks visible cells to prevent duplication
        self.flagged_cells = set()  # Tracks flagged cells

        self._set_mines()
        self._set_values()

    def _set_mines(self):
        """Randomly places mines on the board."""
        placed_mines = 0
        while placed_mines < self.mine_count:
            row, col = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
            if not self.board[row][col].has_mine:
                self.board[row][col].has_mine = True
                placed_mines += 1

    def _count_mines_around(self, row, col):
        """Counts mines around a given cell."""
        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, -1), (-1, 1), (1, -1), (1, 1)
        ]
        count = 0
        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if 0 <= nr < self.size and 0 <= nc < self.size and self.board[nr][nc].has_mine:
                count += 1
        return count

    def _set_values(self):
        """Sets the neighbor mine counts for all squares."""
        for row in range(self.size):
            for col in range(self.size):
                if not self.board[row][col].has_mine:
                    self.board[row][col].neighbor_mines = self._count_mines_around(row, col)

    def reveal(self, row, col):
        """Reveals the cell at (row, col) and its neighbors if safe."""
        if self.board[row][col].has_mine:
            return False  # Mine hit

        queue = deque([(row, col)])
        while queue:
            r, c = queue.popleft()

            if not self.board[r][c].hidden:
                continue

            self.board[r][c].hidden = False
            self.visible_cells.append((r, c))

            if self.board[r][c].neighbor_mines == 0:
                directions = [
                    (-1, 0), (1, 0), (0, -1), (0, 1),
                    (-1, -1), (-1, 1), (1, -1), (1, 1)
                ]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < self.size and 0 <= nc < self.size and self.board[nr][nc].hidden:
                        queue.append((nr, nc))

        return True

    def toggle_flag(self, row, col):
        """Flags or unflags a cell."""
        if (row, col) in self.flagged_cells:
            self.flagged_cells.remove((row, col))
        else:
            self.flagged_cells.add((row, col))

    def is_victory(self):
        """Checks if the player has won the game."""
        return len(self.visible_cells) == (self.size * self.size - self.mine_count)

    def print_board(self, reveal_all=False):
        """Prints the current state of the board."""
        print("\n    " + "   ".join(map(str, range(1, self.size + 1))))
        for row in range(self.size):
            print("+---" * self.size + "+")
            print(f"{row + 1} |", end="")
            for col in range(self.size):
                cell = self.board[row][col]
                if reveal_all or not cell.hidden:
                    if cell.has_mine:
                        print(" x |", end="")
                    else:
                        print(f" {cell.neighbor_mines} |", end="")
                elif (row, col) in self.flagged_cells:
                    print(" F |", end="")
                else:
                    print("   |", end="")
            print()
        print("+---" * self.size + "+")

    def debug_reveal_board(self):
        """Reveals the entire board for debugging purposes."""
        self.print_board(reveal_all=True)

def get_valid_input(prompt, min_val, max_val):
    """Gets a valid integer input within a range."""
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            print(f"Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")


def main():
    print("Welcome to Minesweeper!\n")
    print("Rules:")
    print("1. Choose a cell to reveal by entering its row and column.")
    print("2. Flag cells you suspect contain mines.")
    print("3. Reveal all safe cells to win.")
    print("4. Hitting a mine results in game over.\n")

    size = get_valid_input("Enter board size (4-9): ", 4, 9)
    mine_count = get_valid_input(f"Enter number of mines (1-{size * size}): ", 1, size * size)

    board = MinesweeperBoard(size, mine_count)
    start_time = time.time()

    while True:
        board.print_board()
        action = input("Enter 'r' to reveal, 'f' to flag/unflag, or 'd' for debug mode: ").lower()

        if action not in ['r', 'f', 'd']:
            print("Invalid action. Please enter 'r', 'f', or 'd'.")
            continue

        if action == 'd':
            print("\nDebug Mode: Revealing entire board.")
            board.debug_reveal_board()
            continue

        row = get_valid_input("Enter row: ", 1, size) - 1
        col = get_valid_input("Enter column: ", 1, size) - 1

        if action == 'r':
            if not board.reveal(row, col):
                board.print_board(reveal_all=True)
                print("\nYou hit a mine. Game over!")
                return
        elif action == 'f':
            board.toggle_flag(row, col)

        if board.is_victory():
            board.print_board(reveal_all=True)
            end_time = time.time()
            print(f"\nCongratulations! You cleared the board in {round(end_time - start_time, 2)} seconds.")
            return


def test_set_mines():
    """Unit test for _set_mines method."""
    board = MinesweeperBoard(5, 5)
    mine_count = sum(1 for row in board.board for cell in row if cell.has_mine)
    assert mine_count == 5, f"Expected 5 mines, found {mine_count}"
    print("test_set_mines passed!")


def test_set_values():
    """Unit test for _set_values method."""
    board = MinesweeperBoard(3, 0)  # Initialize a 3x3 board with no mines
    # Manually place mines
    board.board[0][0].has_mine = True  # Place mine at (0,1)
    board.board[2][2].has_mine = True  # Place mine at (1,1)
    board._set_values()

    # Define expected neighbor mine counts
    expected_counts = [
        [-1, 1, 0],  # -1 for mine, others based on adjacency
        [1, 2, 1],
        [0, 1, -1]
    ]
    # Validate each cell against the expected counts
    for r in range(3):
        for c in range(3):
            actual = board.board[r][c].neighbor_mines if not board.board[r][c].has_mine else -1
            assert actual == expected_counts[r][c], f"Mismatch at ({r}, {c}): Expected {expected_counts[r][c]}, got {actual}"
    print("test_set_values passed!")


if __name__ == "__main__":
    test_set_mines()
    test_set_values()
    main()
