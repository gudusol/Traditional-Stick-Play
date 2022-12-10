from game import game
from board import board
from player import player
import os
import pickle
import title

cmd = "mode 130, 40"  # 콘솔 사이즈 조절
os.system(cmd)


def flush_input():  # 입력 버퍼 비우기
    try:
        import msvcrt

        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        import sys, termios

        termios.tcflush(sys.stdin, termios.TCIOFLUSH)


while True:  # 게임 종료 후 다시 타이틀 화면으로 돌아가기 위한 WHILE 문
    player_list, turn = title.game_title()
    g = game(player_list, turn)  # 게임 객체 생성
    g.game_start()  # 게임 시작
    os.system("cls")  # 게임 종료되면 콘솔 초기화 후 다시 시작
