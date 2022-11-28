import keyboard
from statistics import mode
from yut import yut
from board import board
from player import player
from time import sleep
from gotoxy import gotoxy
import os

x = 10  # gotoxy x좌표
y = 1  # gotoxy y좌표


def flush_input():  # 입력 버퍼 비우기
    try:
        import msvcrt

        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        import sys, termios

        termios.tcflush(sys.stdin, termios.TCIOFLUSH)


class game:  # 게임 클래스
    winner = None  # 승리자 string형 변수 처음에는 null
    turn = 0  # 현재 턴 int형 변수, 1p부터 시작함, 2p turn은 2
    yut_list = []  # yut 객체를 담을 리스트
    b = None  # board 객체

    def __init__(self):  # 게임 객체 생성자
        self.winner = None
        self.turn = 0
        self.yut_list = [yut(), yut(), yut(), yut()]
        self.b = board()

    def game_start(self):  # 게임을 구동하는 함수
        self.game_title()  # 게임 타이틀 메뉴 출력
        flush_input()
        player_idx = 0
        while player_idx < 2:  # 플레이어 객체 생성(2명)
            os.system("cls")  # player1 생성
            flush_input()
            player_name = input(f"Player {player_idx+1}의 이름을 입력해주세요 :").strip()
            sleep(0.2)
            if player_name == "" or len(player_name) > 10:
                print("이름은 1자 이상 10자 이하로 입력해주세요.")
                sleep(2)
                continue
            if player_idx == 1:
                if self.b.player_list[0].get_team() == player_name:
                    print("이미 같은 이름의 팀이 있습니다.")
                    sleep(2)
                    continue
            player_idx += 1
            p = player(player_name)
            self.b.player_list.append(p)

            self.select_player_color(p) # player color 선택
        flush_input()
        os.system("cls")

        while self.winner is None:  # winner가 정해졌다면 게임 종료후 게임 타이틀 메뉴로 돌아감
            self.b.show_board()
            self.b.show_pieces_state(
                self.turn
            )
            gotoxy(55, 20)
            s = input("커맨드를 입력하세요.: ").strip().lower()  # 윷 던지는 변수 아래는 예외 처리 #공백 제거
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
                self.b.player_list[self.turn].results.append(
                    self.b.player_list[self.turn].throw(self.yut_list)
                )

                if (
                    self.b.player_list[self.turn].results[
                        len(self.b.player_list[self.turn].results) - 1
                    ]
                    == "윷"
                    or self.b.player_list[self.turn].results[
                        len(self.b.player_list[self.turn].results) - 1
                    ]
                    == "모"
                ):  # 윷이나 모가 나왔을 때 값을 저장하고 한 번 더 던짐
                    gotoxy(55, 19)
                    print(
                        "%s! 한 번더~"
                        % (
                            self.b.player_list[self.turn].results[
                                len(self.b.player_list[self.turn].results) - 1
                            ]
                        )
                    )
                    sleep(0.5)
                    continue
                elif (
                    self.player_list[self.turn].results[
                        len(self.player_list[self.turn].results) - 1
                    ]
                    == "낙"
                ):  # 결과가 낙일 시 결과리스트에서 삭제
                    gotoxy(55, 19)
                    print(
                        "%s!"
                        % (
                            self.player_list[self.turn].results.pop(
                                len(self.player_list[self.turn].results) - 1
                            )
                        )
                    )
                    gotoxy(35, 12)
                    sleep(0.5)

                else:  # 도, 개, 걸일 때는 값을 저장하고 아래 쪽 move_input 함수로 넘어감
                    gotoxy(55, 19)
                    print(
                        "%s!"
                        % (
                            self.b.player_list[self.turn].results[
                                len(self.b.player_list[self.turn].results) - 1
                            ]
                        )
                    )
                    gotoxy(35, 12)
                    sleep(0.5)

            elif (
                s == "/ff" or s == "/gg" or s == "종료" or s == "항복" or s == "ㅈㅈ"
            ):  # 항복(종료)
                while True:
                    os.system("cls")

                    input_key = input("중도 포기할 시 패배 처리됩니다. 정말 포기하시겠습니까? (Y/N)").strip()
                    sleep(0.2)
                    if input_key == "Y" or input_key == "y":
                        self.change_turn()
                        self.winner = self.turn
                        break
                    elif input_key == "N" or input_key == "n":
                        break
                    else:
                        print("Y나 N으로 입력해주세요.")
                        sleep(2)
                continue

            elif (
                s == "help"
                or s == "hel"
                or s == "he"
                or s == "h"
                or s == "도움말"
                or s == "도움"
                or s == "ㄷㅇㅁ"
                or s == "ㄷㅇ"
            ):  # 도움말 명령어 처리
                self.print_help()
                continue
            else:  # 그 외의 명령어 처리
                gotoxy(55, 21)
                print("올바른 명령어를 입력해주세요")
                gotoxy(55, 22)
                print("명령어군        | 올바른 인자 | 설명")
                gotoxy(55, 23)
                print("throw   던지기  |             | 윷을 던집니다.")
                gotoxy(55, 24)
                print("/ff       항복  |  인자없음   | 항복한 플레이어의 패배")
                gotoxy(55, 25)
                print("help    도움말  |             | 전체 혹은 명령어별 도움말을 출력합니다.")
                sleep(2)
                continue  # 윷 던지기 끝
            # os.system("cls")
            self.b.show_board()
            self.b.show_pieces_state(
                self.turn
            )

            # move_input 함수로 말을 움직이고 말을 잡았다면 다시 던지기, 그렇지 않으면 턴을 넘김
            if self.move_input(self.b.player_list[self.turn]) == "catch":
                gotoxy(55, 22)
                print("상대편의 말을 잡았습니다.")
                sleep(1)
                continue

        self.game_over()  # 승자가 정해지면 while문을 빠져나와 게임 종료
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
        keyboard.wait("esc")  # esc키를 누를 때까지 대기
        return 0

    def select_player_color(self, player: player):  # player color 정하는 함수
        cursor_x = 33
        cursor_y = 6

        while True:
            os.system("cls")
            print(f"\n\n\t\t{player.get_team()}의 색상을 골라주세요\n\n\n")
            print("\t\t\t\033[31m" + "RED" + "\033[0m\n")
            print("\t\t\t\033[34m" + "BLUE" + "\033[0m\n")
            print("\t\t\t\033[32m" + "GREEN" + "\033[0m\n")
            print("\t\t\t\033[33m" + "YELLOW" + "\033[0m\n")
            gotoxy(cursor_x, cursor_y)
            print("◀")
            gotoxy(cursor_x, cursor_y)
            flush_input()
            input_key = keyboard.read_key()
            sleep(0.2)

            if input_key == "down" and cursor_y < 12:  # 아래쪽 방향키 입력
                print("  ")
                gotoxy(cursor_x, cursor_y)
                cursor_y += 2
                print("◀")
                gotoxy(cursor_x, cursor_y)
            elif input_key == "up" and cursor_y > 6:  # 위쪽 방향키 입력
                print("  ")
                gotoxy(cursor_x, cursor_y)
                cursor_y -= 2
                print("◀")
                gotoxy(cursor_x, cursor_y)
            elif input_key == "enter" and cursor_y == 6:  # red 선택
                sleep(0.2)
                os.system("cls")
                if "\033[31m" in self.b.color_dic.values():
                    print("\n\n\n\n\n\t\t다른 플레이어가 이미 고른 색상입니다")
                else:
                    player.set_color("\033[31m")  # player, board 둘다 저장?
                    self.b.color_dic[player.get_team()] = "\033[31m"
                    print("\n\n\n\n\n\t\t색상 선택이 완료되었습니다")
                    sleep(1)
                    return 0
                sleep(1)
            elif input_key == "enter" and cursor_y == 8:  # blue 선택
                sleep(0.2)
                os.system("cls")
                if "\033[34m" in self.b.color_dic.values():
                    print("\n\n\n\n\n\t\t다른 플레이어가 이미 고른 색상입니다")
                else:
                    player.set_color("\033[34m")
                    self.b.color_dic[player.get_team()] = "\033[34m"
                    print("\n\n\n\n\n\t\t색상 선택이 완료되었습니다")
                    sleep(1)
                    return 0
                sleep(1)
            elif input_key == "enter" and cursor_y == 10:  # green 선택
                sleep(0.2)
                os.system("cls")
                if "\033[32m" in self.b.color_dic.values():
                    print("\n\n\n\n\n\t\t다른 플레이어가 이미 고른 색상입니다")
                else:
                    player.set_color("\033[32m")
                    self.b.color_dic[player.get_team()] = "\033[32m"
                    print("\n\n\n\n\n\t\t색상 선택이 완료되었습니다")
                    sleep(1)
                    return 0
                sleep(1)
            elif input_key == "enter" and cursor_y == 12:  # yellow 선택
                sleep(0.2)
                os.system("cls")
                if "\033[33m" in self.b.color_dic.values():
                    print("\n\n\n\n\n\t\t다른 플레이어가 이미 고른 색상입니다")
                else:
                    player.set_color("\033[33m")
                    self.b.color_dic[player.get_team()] = "\033[33m"
                    print("\n\n\n\n\n\t\t색상 선택이 완료되었습니다")
                    sleep(1)
                    return 0
                sleep(1)

        return 0

    def move_input(self, player):  # 움직일 말과 사용할 결과를 입력받아서 말을 움직이는 함수
        ret = ""  # 말을 잡았는지 여부를 반환하기 위한 변수
        while player.results:  # player의 결과 리스트가 비었다면 반복 종료
            self.b.show_board()
            self.b.show_pieces_state(
                self.turn
            )
            gotoxy(55, 20)
            s = input("이동할 말과 적용할 값을 입력하세요(예시: 3 걸): ")  # 몇 번 말을 몇 칸 움직일지 입력
            s = s.replace(" ", "")

            # 입력받은 명령어 문법 부합 여부 확인
            try:
                piece_num = int(s[0]) - 1  # 첫번째 글자가 움직일 말의 번호

                if player.pieces[piece_num].get_index() >= 30:  # 골인한 말일 시 문법 위배
                    gotoxy(55, 21)
                    print("이미 골인한 말입니다. 다른 말을 선택해주세요.")
                    sleep(1)
                    continue

                if len(s) == 1:  # 사용자가 움직일 말만 입력했을 시
                    if len(player.results) == 1:  # 결과 리스트에 하나뿐이라면 문법 부합
                        result = player.results.pop()  # 결과 리스트에 있던 결과를 움직일 결과로 pop
                    else:  # 아니면 문법 위배
                        gotoxy(55, 21)
                        print("저장된 값이 2개 이상입니다. 값을 특정해주세요.")
                        sleep(1)
                        continue
                elif len(s) > 2:  # 사용자 명령어가 공백 미포함 2글자 초과 시 위배
                    gotoxy(55, 21)
                    print("잘못된 명령어입니다.")
                    sleep(1)
                    continue
                else:
                    result = player.results.pop(
                        player.results.index(s[1])
                    )  # 두번째 글자는 움직일 결과
                gotoxy(55, 21)
                print(f"{piece_num+1}번 말을 {result}만큼 이동합니다.")
                sleep(1)
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
                elif result == "빽도":
                    result = -1

            except:
                gotoxy(55, 21)
                print("잘못된 명령어입니다.")
                sleep(1)
                continue

            moved_value = self.b.move_piece(
                player.pieces[piece_num], result
            )  # 말을 움직이고 상태에 따라 GOALIN, MOVE, CATCH중 하나를 반환
            # for i in self.player_list:
            #     print("★팀" + i.get_team())
            #     for j in i.get_piecelist():   #단위별 검사
            #         print(j.get_index())
            #     print()
            # 말 이동, 이동한 결과 저장

            if moved_value == 0:  # 말 하나가 골인 할때 마다 플레이어가 승리했는지 확인
                if player.goal_in_piece() == 4:  # 골인한 말이 4개라면 승리
                    self.winner = self.turn
                    return
            elif moved_value == 1:  # 말을 움직였을 때
                continue
            elif moved_value == 2 and (
                result >= 1 and result <= 3
            ):  # 도, 개, 걸로 말을 잡았을 때
                ret = "catch"
                return ret

            # if moved_value == 1 and result <= 3:  # 도/개/걸로 잡았을 시 다시 던짐
            #     return
            # elif moved_value == 0:  # 골인했을 시 모든 말이 골인했는지 판단
            #     if player.goal_in_piece() == 4:  # 모든 말이 골인했다면 현재 턴인 팀의 승리
            #         self.winner = self.turn
            #         return

        if self.turn == 0:  # 잡지도 골인하지도 않았다면 상대 턴으로 넘어감
            self.turn = 1
        else:
            self.turn = 0

        return 0

    def game_over(self):  # 승리 조건을 판단하고 게임을 종료
        if self.winner is not None:
            os.system("cls")
            print(self.player_list[self.winner].team, "의 승리!!")  # 승리한 팀 출력
            sleep(3)
            return 0

    def change_turn(self):  # 턴이 넘어갈 때 턴이 저장된 변수 값을 바꿈
        if self.turn == 1:
            self.turn = 0
        else:
            self.turn = 1

    def game_title(self):  # 게임 타이틀 출력
        cursor_x = 25
        cursor_y = 6

        while True:
            os.system("cls")
            print("\n\n\t\tTRADITIONAL-STICK-PLAY\n\n\n")
            print("\t\tSTART\n")
            print("\t\tQUIT\n")
            print("\t\tHELP")
            gotoxy(cursor_x, cursor_y)
            print("◀")
            gotoxy(cursor_x, cursor_y)
            input_key = keyboard.read_key()
            sleep(0.2)

            if input_key == "down" and cursor_y < 9:  # 아래쪽 방향키 입력
                print("  ")
                cursor_y += 2
                gotoxy(cursor_x, cursor_y)
                print("◀")
                gotoxy(cursor_x, cursor_y)

            elif input_key == "up" and cursor_y > 6:  # 위쪽 방향키 입력
                print("  ")
                cursor_y -= 2
                gotoxy(cursor_x, cursor_y)
                print("◀")
                gotoxy(cursor_x, cursor_y)

            elif input_key == "enter" and cursor_y == 6:  # START
                os.system("cls")
                gotoxy(x, y + 2)
                print("TRADITIONAL-STICK-PLAY")
                gotoxy(x + 6, y + 5)
                print("시작합니다")
                sleep(1)
                os.system("cls")

                return 0

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
