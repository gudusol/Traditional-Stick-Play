from board import board
from game import game
from player import player

# for i in range(100):
#     print(f"p1: {p1
# .throw()}, p2: {p2.throw()}")
p1 = player("적")
p2 = player("청")
b = board()
b.show_board()
b.show_tokens_state(p1, p2)
