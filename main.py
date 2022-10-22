from board import board
from player import player
import os
from gotoxy import gotoxy

# for i in range(100):
#     print(f"p1: {p1
# .throw()}, p2: {p2.throw()}")
p1 = player("적")
p2 = player("청")
b = board()
os.system("cls")
b.move_piece(p1.get_piecelist()[0], 3)
b.show_board()
b.show_pieces_state(p1, p2)
gotoxy(0, 0)
