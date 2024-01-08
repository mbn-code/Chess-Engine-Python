# Chess Game using Tkinter

This is a simple chess game implemented in Python using the `chess` library for the game logic and `tkinter` for the graphical user interface.

## Installation

Make sure you have Python installed on your system. You can install the required dependencies using the following command:

```bash
pip install chess
```

## Usage

Run the `chess_game.py` script to start the chess game. You can make moves by clicking on the squares representing the chessboard. The selected square will be highlighted in red, and legal moves will be updated accordingly.

```bash
python chess_game.py
```

## Code Overview

The code consists of a `ChessUI` class that manages the GUI using Tkinter and interacts with the `chess` library for the chess game logic. The chessboard is represented as buttons in an 8x8 grid. Clicking on a square selects or moves a chess piece.

```python
import chess
import tkinter as tk

class ChessUI:
    # ... (constructor and other methods)

    def on_square_click(self, row, col):
        # ... (handling square clicks)

    def update_board(self):
        # ... (update the GUI based on the current game state)

    def highlight_square(self, row, col):
        # ... (highlight the selected square)

    def get_piece_symbol(self, piece):
        # ... (get the symbol for a chess piece)

if __name__ == "__main__":
    root = tk.Tk()
    chess_ui = ChessUI(root)
    root.mainloop()
```

Feel free to customize and enhance the code to add more features or improve the user interface. Happy playing!
