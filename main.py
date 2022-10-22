from game import game
import os

cmd = "mode 120, 40"
os.system(cmd)
while True:
    g = game()
    g.game_start()
    os.system("cls")
