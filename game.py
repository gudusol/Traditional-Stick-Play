import re
from yut import yut
from board import board
from player import player
from time import sleep
from gotoxy import gotoxy
import keyboard
import os

x = 10  # gotoxy x좌표
y = 1  # gotoxy y좌표


class game:
    winner = ""  # 승리자 string형 변수 처음에는 null
    turn = 1  # 현재 턴 int형 변수, 1p부터 시작함, 2p turn은 2
    yut_list = []
    b = None

    def __init__(self):
        self.yut_list = [yut(), yut(), yut(), yut()]
        self.b = board()

    def game_start(self):  # 게임을 구동하는 함수

        os.system("cls")  # player1 생성
        gotoxy(x, y + 2)
        print("Player 1의 이름을 입력해주세요 :")
        gotoxy(x + 33, y + 2)
        p1_name = input()
        p1 = player(p1_name)

        os.system("cls") # player2 생성
        gotoxy(x, y + 2)
        print("Player 2의 이름을 입력해주세요 :")
        gotoxy(x + 5, y + 3)
        p2_name = input()
        p2 = player(p2_name)

        b = board()

        os.system("cls")
        
        while self.turn == 1:  # player1 턴

            b.show_board()
            b.show_pieces_state(p1, p2)

            gotoxy(27, 12)
            print("던지기 :")
            gotoxy(35, 12)
            s = input()  # 윷 던지는 변수 아래는 예외 처리
            if (
                s == "던진다"
                or s == "던지"
                or s == "던"
                or s == "ㄷㅈㄱ"
                or s == "ㄷㅈ"
                or s == "ㄷ"
                or s == "throw"
                or s == "thro"
                or s == "thr"
                or s == "th"
                or s == "t"
            ):
                p1.results.append(p1.throw(self.yut_list))
                
                if (
                    p1.results[len(p1.results) - 1] == "윷"
                    or p1.results[len(p1.results) - 1] == "모"
                ):
                    gotoxy(27, 11)
                    print("%s! 한 번더~"%(p1.results[len(p1.results) - 1]))
                    gotoxy(35, 12)
                    sleep(1)
                    continue
                else:
                    gotoxy(27, 11)
                    print("%s!" %(p1.results[len(p1.results) - 1]))
                    gotoxy(35, 12)
                    sleep(1)
            else:
                print("올바른 명령어를 입력해주세요")
                continue  # 윷 던지기 끝
            
            # 움직일 말 번호 및 어떤 결과로 이동할 지 입력


            # 해당 말이 골인하지 않았고 저장되어있는 결과인가?

            # 말 이동 및 사용한 결과 삭제

            # 상대 말을 잡았는가?

            # 본인 말이 업혔는가?

            # 도착 위치가 출발점을 넘어갔는가?

            # 사용할 결과가 남았는가?

            # 상대턴으로 넘어감
        return 0

    def move_input(self, player):  # 움직일 말과 사용할 결과를 입력받아서 말을 움직이는 함수
        while player.results:  # player의 결과 리스트가 비었다면 반복 종료
            s = input("이동할 말과 적용할 값을 입력하세요(예시: 3 걸): ")
            s = s.replace(" ", "")

            # 입력받은 명령어 문법 부합 여부 확인
            try:
                piece_num = int(s[0])  # 첫번째 글자가 움직일 말의 번호

                if player.pieces[piece_num].idx > 30:  # 골인한 말일 시 문법 위배
                    print("이미 골인한 말입니다. 다른 말을 선택해주세요.")
                    continue

                if len(s) == 1:  # 사용자가 움직일 말만 입력했을 시
                    if len(player.results) == 1:  # 결과 리스트에 하나뿐이라면 문법 부합
                        result = player.results.pop()  # 결과 리스트에 있던 결과를 움직일 결과로 pop
                    else:  # 아니면 문법 위배
                        print("적용할 결과를 입력해주세요.")
                        continue
                elif len(s) > 2:  # 사용자 명령어가 공백 미포함 2글자 초과 시 위배
                    print("잘못된 명령어입니다.")
                    continue
                else:
                    result = player.results.pop(
                        player.results.index(s[1])
                    )  # 두번째 글자는 움직일 결과
                if result == "도":
                    result = 1
                elif result == "개":
                    result = 2
                elif result == "걸":
                    result = 3
                elif result == "윷":
                    result = 4
                elif result == "모":
                    result = 5

            except:
                print("잘못된 명령어입니다.")
                continue

            self.b.move_piece(player.pieces[piece_num], result)  # 말 이동

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
