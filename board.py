from tile import tile
from player import player
from piece import piece
from gotoxy import gotoxy
import os


class board:
    tile_list = []  # 칸의 배열

    def __init__(self):
        for i in range(29):
            self.tile_list.append(tile(i + 1))

    def print_tile(self, idx):
        num_of_pieces = len(self.tile_list[idx - 1].get_pieces())
        if num_of_pieces == 0:
            print("■    ", end="")
        elif num_of_pieces == 1:
            print("❶   ", end="")
        elif num_of_pieces == 2:
            print("❷   ", end="")
        elif num_of_pieces == 3:
            print("❸   ", end="")
        else:
            print("❹   ", end="")

    def show_board(self):
        os.system("cls")
        for i in range(6):
            self.print_tile(11 - i)
        print("\n")
        self.print_tile(12)
        self.print_tile(23)
        print("          ", end="")
        self.print_tile(21)
        self.print_tile(5)
        print("\n")
        self.print_tile(13)
        print("     ", end="")
        self.print_tile(24)
        self.print_tile(22)
        print("     ", end="")
        self.print_tile(4)
        print("\n")
        print("             ", end="")
        self.print_tile(25)
        print("\n")
        self.print_tile(14)
        print("     ", end="")
        self.print_tile(28)
        self.print_tile(26)
        print("     ", end="")
        self.print_tile(3)
        print("\n")
        self.print_tile(15)
        self.print_tile(29)
        print("          ", end="")
        self.print_tile(27)
        self.print_tile(2)
        print("\n")
        for i in range(5):
            self.print_tile(16 + i)
        self.print_tile(1)

    def show_pieces_state(self, player1: player, player2: player):
        player1_piece_list = player1.get_piecelist()
        player2_piece_list = player2.get_piecelist()
        gotoxy(27, 0)
        print(player1.get_team() + " 팀")
        for i in range(len(player1_piece_list)):  # 각 플레이어의 말 상태 출력
            gotoxy(27, i + 1)
            print("%d 번 말 : %d" % (i, player1_piece_list[i].get_index()))
        gotoxy(38, 0)
        print("| " + player2.get_team() + " 팀")
        for i in range(len(player2_piece_list)):
            gotoxy(38, i + 1)
            print("| %d 번 말 : %d" % (i, player2_piece_list[i].get_index()))
        gotoxy(0, 15)
