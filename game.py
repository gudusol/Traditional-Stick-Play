import re
from statistics import mode
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
    winner = None  # 승리자 string형 변수 처음에는 null
    turn = 0  # 현재 턴 int형 변수, 1p부터 시작함, 2p turn은 2
    yut_list = []
    b = None

    def __init__(self):
        self.yut_list = [yut(), yut(), yut(), yut()]
        self.b = board()

    def game_start(self):  # 게임을 구동하는 함수
        self.game_title()
        input(" ")
        player_list = []
        for i in range(0, 2):
            os.system("cls")  # player1 생성
            player_name = input("Player %d의 이름을 입력해주세요 :" % (i + 1))
            player_list.append(player(player_name))

        b = board()
        os.system("cls")

        while self.winner is None:  # winner가 정해졌다면 반복 종료

            b.show_board()
            b.show_pieces_state(player_list[0], player_list[1], self.turn)

            gotoxy(27, 12)
            print("던지기 :")
            gotoxy(35, 12)
            s = input()  # 윷 던지는 변수 아래는 예외 처리
            if (
                s == "던지기"
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
                player_list[self.turn].results.append(
                    player_list[self.turn].throw(self.yut_list)
                )

                if (
                    player_list[self.turn].results[
                        len(player_list[self.turn].results) - 1
                    ]
                    == "윷"
                    or player_list[self.turn].results[
                        len(player_list[self.turn].results) - 1
                    ]
                    == "모"
                ):
                    gotoxy(27, 11)
                    print(
                        "%s! 한 번더~"
                        % (
                            player_list[self.turn].results[
                                len(player_list[self.turn].results) - 1
                            ]
                        )
                    )
                    gotoxy(35, 12)
                    sleep(0.5)
                    continue
                else:
                    gotoxy(27, 11)
                    print(
                        "%s!"
                        % (
                            player_list[self.turn].results[
                                len(player_list[self.turn].results) - 1
                            ]
                        )
                    )
                    gotoxy(35, 12)
                    sleep(0.5)
            else:
                print("올바른 명령어를 입력해주세요")
                continue  # 윷 던지기 끝

            # 움직일 말 번호 및 어떤 결과로 이동할 지 입력

            # 해당 말이 골인하지 않았고 저장되어있는 결과인가?

            # 말 이동 및 사용한 결과 삭제

            # 상대 말을 잡았는가?

            self.move_input(player_list[self.turn])

        # 승자가 정해졌다면 게임 종료 함수 호출 (추가 요망)

        return 0

    def print_help(self):  # 도움말 출력 함수
        os.system("cls")
        print("전통 막대기 놀이 : TRADITIONAL STICK PLAY")
        print("우리 나라의 민속놀이인 윷놀이 게임 프로그램입니다.\n")
        print("### 게임 규칙 ###")
        print(
            "두 명의 플레이어가 번갈아가며 윷을 던져 나온 결과로 4개의 말을 움직입니다. \n윷을 던진 결과로 윷이나 모가 나오면 한 번 더 던질 수 있습니다."
        )
        print("4개의 말을 먼저 모두 골인시키는 플레이어가 승리합니다.\n상대방의 말을 잡거나 본인의 말에 업힐 수 있습니다.\n")
        print("### 조작 방법 ###")
        print("키보드를 통한 명령어 입력 후 Enter 키를 누르면 동작합니다.")
        print("입력한 명령어가 각 프롬프트의 명령어 문법에 위배되는 경우 프로그램이 정상적으로 동작하지 않을 수 있습니다.\n")
        print("esc키를 누르면 이전 화면으로 이동합니다.")
        keyboard.wait("esc")
        return 0

    def move_input(self, player):  # 움직일 말과 사용할 결과를 입력받아서 말을 움직이는 함수
        while player.results:  # player의 결과 리스트가 비었다면 반복 종료
            gotoxy(27, 12)
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

            moved_value = self.b.move_piece(
                player.pieces[piece_num], result
            )  # 말 이동, 이동한 결과 저장
            if moved_value == 1 and result <= 3:  # 도/개/걸로 잡았을 시 다시 던짐
                return
            elif moved_value == 0:  # 골인했을 시 모든 말이 골인했는지 판단
                if player.goal_in_piece() == 4:  # 모든 말이 골인했다면 현재 턴인 팀의 승리
                    self.winner = self.turn
                    return

        if self.turn == 0:  # 잡지도 골인하지도 않았다면 상대 턴으로 넘어감
            self.turn = 1
        else:
            self.turn = 0

        return 0

    def game_over(self):  # 승리 조건을 판단하고 게임을 종료
        if self.winner is not None:
            return

    def change_turn(self):  # 턴이 넘어갈 때 턴이 저장된 변수 값을 바꿈
        if self.turn == 1:
            self.turn = 0
        else:
            self.turn = 1

    def game_title(self):
        cursor_x = 25
        cursor_y = 6
        os.system("cls")

        print("\n\n\t\tTRADITIONAL-STICK-PLAY\n\n\n")
        print("\t\tSTART\n")
        print("\t\tQUIT\n")
        print("\t\tHELP")
        gotoxy(cursor_x, cursor_y)
        print("◀", end="")
        while True:

            input_key = keyboard.read_key()
            sleep(0.2)

            if input_key == "down" and cursor_y < 9:  # 아래쪽 방향키 입력
                cursor_x -= 1
                gotoxy(cursor_x, cursor_y)
                print("  ", end="")
                cursor_x += 1
                cursor_y += 2
                gotoxy(cursor_x, cursor_y)
                print("◀", end="")
            elif input_key == "up" and cursor_y > 6:  # 위쪽 방향키 입력
                cursor_x -= 1
                gotoxy(cursor_x, cursor_y)
                print("  ", end="")
                cursor_x += 1
                cursor_y -= 2
                gotoxy(cursor_x, cursor_y)
                print("◀", end="")

            elif input_key == "enter" and cursor_y == 6:  # START
                os.system("cls")
                gotoxy(x, y + 2)
                print("TRADITIONAL-STICK-PLAY")
                gotoxy(x + 6, y + 5)
                print("시작합니다")
                sleep(1)
                os.system("cls")

                return 0  # 리턴 값으로 다른 동작 수행?

            elif input_key == "enter" and cursor_y == 8:  # QUIT
                os.system("cls")
                gotoxy(x, y + 2)
                print("TRADITIONAL-STICK-PLAY")
                gotoxy(x + 6, y + 5)
                print("종료합니다")
                sleep(1)
                exit(0)

            elif input_key == "enter" and cursor_y == 10:  # HELP
                self.print_help()
                self.game_title()
