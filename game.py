from yut import yut
from board import board
from player import player

from time import sleep
import keyboard
from gotoxy import gotoxy
import os

x = 10 #gotoxy x좌표
y = 1 #gotoxy y좌표

class game:
    winner = ""  # 승리자 string형 변수 처음에는 null
    turn = 1  # 현재 턴 int형 변수, 1p부터 시작함, 2p turn은 2
    yut_list = []
    

    def __init__(self):
        self.yut_list = [yut(), yut(), yut(), yut()]

    def game_start(self):  # 게임을 구동하는 함수

        os.system("cls") # player1 생성
        gotoxy(x, y + 2)
        print("Player 1의 이름을 입력해주세요 :")
        gotoxy(x + 5, y + 3)
        p1_name = input()
        p1 = player(p1_name)

        # os.system("cls") # player2 생성
        # gotoxy(x, y + 2)
        # print("Player 2의 이름을 입력해주세요 :")
        # gotoxy(x + 5, y + 3)
        # p2_name = input()
        # p2 = player(p2_name)

        b = board() # 보드 생성
        os.system("cls")
        while(self.turn == 1): # player1 턴 
            print("던지세요 :")
            if(input() == "던진다"): # 윷 던지기 시작
                p1.results.append(p1.throw(self.yut_list))
                print(p1.results)
                if(p1.results[len(p1.results) - 1] == "윷" or p1.results[len(p1.results) - 1] == "모"):
                    continue
            else:
                print("올바른 명령어를 입력해주세요")
                continue # 윷 던지기 끝
            
            

            break
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
