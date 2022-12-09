import keyboard
from time import sleep
from gotoxy import gotoxy
from player import player
import file
import os

x = 10  # gotoxy x좌표
y = 1  # gotoxy y좌표
WIDE_MAP = {i: i + 0xFEE0 for i in range(0x21, 0x7F)}
WIDE_MAP[0x20] = 0x3000


def widen(s):  # full-width character로 변환
    return s.translate(WIDE_MAP)


def flush_input():  # 입력 버퍼 비우기
    try:
        import msvcrt

        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        import sys, termios

        termios.tcflush(sys.stdin, termios.TCIOFLUSH)


def make_player():
    flush_input()
    player_idx = 0
    player_list = []

    while player_idx < 2:  # 플레이어 객체 생성(2명)
        os.system("cls")  # player1 생성
        flush_input()
        player_name = widen(input(f"Player {player_idx+1}의 이름을 입력해주세요 :").strip())
        sleep(0.2)
        if player_name == "" or len(player_name) > 10:
            print("이름은 1자 이상 10자 이하로 입력해주세요.")
            sleep(2)
            continue
        if player_idx == 1:
            if player_list[0].get_team() == player_name:
                print("이미 같은 이름의 팀이 있습니다.")
                sleep(2)
                continue
        player_idx += 1
        p = player(player_name, [0, 0, 0, 0], [])
        player_list.append(p)
        player_list = select_player_color(player_list)  # player color 선택
    flush_input()
    os.system("cls")

    turn = 0  # 기본적으로 p1의 차례부터 시작
    return player_list, turn


def select_player_color(player_list):  # player color 정하는 함수
    cursor_x = 33
    cursor_y = 6

    while True:
        os.system("cls")
        print(f"\n\n\t\t{player_list[-1].get_team()}의 색상을 골라주세요\n\n\n")
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
            if "\033[31m" == player_list[0].get_color():
                print("\n\n\n\n\n\t\t다른 플레이어가 이미 고른 색상입니다")
            else:
                player_list[-1].set_color("\033[31m")  # player, board 둘다 저장?
                print("\n\n\n\n\n\t\t색상 선택이 완료되었습니다")
                sleep(1)
                return player_list
            sleep(1)
        elif input_key == "enter" and cursor_y == 8:  # blue 선택
            sleep(0.2)
            os.system("cls")
            if "\033[34m" == player_list[0].get_color():
                print("\n\n\n\n\n\t\t다른 플레이어가 이미 고른 색상입니다")
            else:
                player_list[-1].set_color("\033[34m")
                print("\n\n\n\n\n\t\t색상 선택이 완료되었습니다")
                sleep(1)
                return player_list
            sleep(1)
        elif input_key == "enter" and cursor_y == 10:  # green 선택
            sleep(0.2)
            os.system("cls")
            if "\033[32m" == player_list[0].get_color():
                print("\n\n\n\n\n\t\t다른 플레이어가 이미 고른 색상입니다")
            else:
                player_list[-1].set_color("\033[32m")
                print("\n\n\n\n\n\t\t색상 선택이 완료되었습니다")
                sleep(1)
                return player_list
            sleep(1)
        elif input_key == "enter" and cursor_y == 12:  # yellow 선택
            sleep(0.2)
            os.system("cls")
            if "\033[33m" == player_list[0].get_color():
                print("\n\n\n\n\n\t\t다른 플레이어가 이미 고른 색상입니다")
            else:
                player_list[-1].set_color("\033[33m")
                print("\n\n\n\n\n\t\t색상 선택이 완료되었습니다")
                sleep(1)
                return player_list
            sleep(1)

    return 0


def print_help():  # 도움말 출력 함수
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


def game_title():  # 게임 타이틀 출력
    cursor_x = 25
    cursor_y = 6

    while True:
        os.system("cls")
        print("\n\n\t\tTRADITIONAL-STICK-PLAY\n\n\n")
        print("\t\tSTART\n")
        print("\t\tLOAD\n")
        print("\t\tHELP\n")
        print("\t\tQUIT")
        gotoxy(cursor_x, cursor_y)
        print("◀")
        gotoxy(cursor_x, cursor_y)
        input_key = keyboard.read_key()
        sleep(0.2)

        if input_key == "down" and cursor_y < 11:  # 아래쪽 방향키 입력
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
            return make_player()

        elif input_key == "enter" and cursor_y == 8:  # LOAD
            try:
                player_list, turn = file.load_data()
                return player_list, turn
            except TypeError:
                continue

        elif input_key == "enter" and cursor_y == 10:  # HELP
            print_help()

        elif input_key == "enter" and cursor_y == 12:  # QUIT
            os.system("cls")
            gotoxy(x, y + 2)
            print("TRADITIONAL-STICK-PLAY")
            gotoxy(x + 6, y + 5)
            print("종료합니다")
            sleep(1)
            exit(0)
