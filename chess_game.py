import chess
import tkinter as tk

class ChessUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Chess Game")
        self.board = chess.Board()
        self.buttons = [[None for _ in range(8)] for _ in range(8)]
        self.selected_square = None  # Add this line

        for row in range(8):
            for col in range(8):
                color = "white" if (row + col) % 2 == 0 else "black"
                button = tk.Button(root, text="", width=4, height=2, bg=color,
                                   command=lambda r=row, c=col: self.on_square_click(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

        self.update_board()

    # rest of the code remains unchanged


    def update_board(self):
        for row in range(8):
            for col in range(8):
                piece = self.board.piece_at(chess.square(col, 7 - row))
                text = self.get_piece_symbol(piece) if piece else ""
                self.buttons[row][col].config(text=text)

    def on_square_click(self, row, col):
        square = chess.square(col, 7 - row)
        piece = self.board.piece_at(square)

        if not self.selected_square:
            if piece and piece.color == self.board.turn:
                self.selected_square = square
                self.highlight_square(row, col)
        else:
            move = chess.Move(self.selected_square, square)
            if move in self.board.legal_moves:
                self.board.push(move)
                self.selected_square = None
                self.update_board()

    def highlight_square(self, row, col):
        self.buttons[row][col].config(bg="red")

    def get_piece_symbol(self, piece):
        if piece.color == chess.WHITE:
            return piece.symbol().upper()
        else:
            return piece.symbol().lower()

if __name__ == "__main__":
    root = tk.Tk()
    chess_ui = ChessUI(root)
    root.mainloop()
