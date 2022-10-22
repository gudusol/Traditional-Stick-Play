from game import game


cmd = "mode 100, 40"
os.system(cmd)
p1 = player("페비")
p2 = player("핫산")
t = 1
b = board()
b.move_piece(p1.get_piecelist()[0], 3)
b.show_board()
b.show_pieces_state(p1, p2, 1)
s = input()
