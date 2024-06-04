import tkinter as tk
from tkinter import messagebox
import math

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # 1-dimensional list of board cells
        self.current_winner = None  # track the winner!
        self.current_player = 'X'

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False

    def minimax(self, state, player):
        max_player = self.current_player
        other_player = 'O' if player == 'X' else 'X'

        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() + 1)}
        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}
        for possible_move in state.available_moves():
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player)

            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move

            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best

class TicTacToeGUI:
    def __init__(self):
        self.game = TicTacToe()
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.buttons = [tk.Button(self.root, height=3, width=3, command=lambda i=i: self.make_move(i)) for i in range(9)]
        for i in range(9):
            self.buttons[i].grid(row=i//3, column=i%3)

    def make_move(self, i):
        if self.game.make_move(i, 'X'):
            self.buttons[i]['text'] = 'X'
            if self.game.current_winner:
                messagebox.showinfo("Game Over", "X wins!")
                self.restart_game()
            else:
                i = self.game.minimax(self.game, 'O')['position']
                if self.game.make_move(i, 'O'):
                    self.buttons[i]['text'] = 'O'
                    if self.game.current_winner:
                        messagebox.showinfo("Game Over", "O wins!")
                        self.restart_game()

    def restart_game(self):
        self.game = TicTacToe()  # Reset the game state
        for i in range(9):  # Clear all the buttons
            self.buttons[i]['text'] = ''

if __name__ == "__main__":
    TicTacToeGUI().root.mainloop()