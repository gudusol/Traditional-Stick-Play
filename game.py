from yut import yut
from board import board
from time import sleep
import keyboard
from gotoxy import gotoxy
import os


class game:
    winner = ""  # 승리자 string형 변수 처음에는 null
    turn = 1  # 현재 턴 int형 변수, 1p부터 시작함, 2p turn은 2
    yut_list = []

    def __init__(self):
        self.yut_list = [yut(), yut(), yut(), yut()]

    def game_start():  # 게임을 구동하는 함수

        return 0

    def game_over(self):  # 승리 조건을 판단하고 게임을 종료
        if self.winner == "":
            return 0  # 계속 게임 진행
        else:
            return self.winner  # 승리자 이름 리턴하고 게임 종료

    def change_turn(self):  # 턴이 넘어갈 때 턴이 저장된 변수 값을 바꿈
        if self.turn == 1:
            self.turn = 0
        else:
            self.turn = 1


def game_title(self):
    cursor_x = 20
    cursor_y = 5
    x = 10
    y = 1
    os.system("cls")
    while True:

        gotoxy(x, y + 0)
        print("TRADITIONAL-STICK-PLAY")
        gotoxy(x, y + 4)
        print("START")
        gotoxy(x, y + 6)
        print("QUIT")
        gotoxy(x, y + 8)
        print("HELP")

        gotoxy(cursor_x, cursor_y)
        print("◀")

        if keyboard.is_pressed(80) and cursor_y < 9:  # 아래쪽 방향키 입력
            sleep(0.2)
            cursor_y += 2
            os.system("cls")
        if keyboard.is_pressed(72) and cursor_y > 5:  # 위쪽 방향키 입력
            sleep(0.2)
            cursor_y -= 2
            os.system("cls")

        if keyboard.is_pressed("enter") and cursor_y == 5:  # START
            os.system("cls")
            gotoxy(x, y + 2)
            print("TRADITIONAL-STICK-PLAY")
            gotoxy(x + 6, y + 5)
            print("시작합니다")
            sleep(1)
            return 0  # 리턴 값으로 다른 동작 수행?

        if keyboard.is_pressed("enter") and cursor_y == 7:  # QUIT
            os.system("cls")
            gotoxy(x, y + 2)
            print("TRADITIONAL-STICK-PLAY")
            gotoxy(x + 6, y + 5)
            print("종료합니다")
            sleep(1)
            return 0

        if keyboard.is_pressed("enter") and cursor_y == 9:  # HELP
            print("help")
            return 0
