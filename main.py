# As a professional web game developer, create me a tic tac toe game for one person against computer on a 5*5 matrix in Python

from tkinter import *
import random

def click(r, c):
    global player
    if player == 'X' and states[r][c] == 0 and stop_game == False:
        b[r][c].config(text='X', fg='blue', bg='white')
        states[r][c] = 'X'
        player = 'O'
    if player == 'O' and states[r][c] == 0 and stop_game == False:
        b[r][c].config(text='O', fg='orange', bg='black')
        states[r][c] = 'O'
        player = 'X'
    check_for_winner()

def main():
    global b, states, player, stop_game

    # Initialize the game
    player = 'X'
    stop_game = False
    states = [[0, 0, 0, 0, 0] for _ in range(5)]

    # Create the game board
    root = Tk()
    root.title("Tic Tac Toe")
    b = [[0, 0, 0, 0, 0] for _ in range(5)]
    for i in range(5):
        for j in range(5):
            b[i][j] = Button(font=("Arial", 20), width=4, height=2,
                                command=lambda r=i, c=j: click(r, c))
            b[i][j].grid(row=i, column=j)

    # Start the game
    root.mainloop()

if __name__ == "__main__":
    main()