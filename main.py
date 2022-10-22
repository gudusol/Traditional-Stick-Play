from game import game
from board import board
from player import player
import os

b = board()
p1 = player("red")
p2 = player("blue")
b.move_piece(p1.get_piecelist()[0], 3)
b.move_piece(p1.get_piecelist()[0], 2)
os.system("cls")
b.show_board()
b.show_pieces_state(p1, p2)
