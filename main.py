from game import game
from time import sleep
import os

cmd = "mode 120, 40"
os.system(cmd)
g = game()
while True:
    g.game_start()
    os.system("cls")
    print(g.winner, "님이 승리하셨습니다!")
    sleep(2)
