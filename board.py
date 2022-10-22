from tile import tile
from player import player
from piece import piece
from gotoxy import gotoxy
from time import sleep
import os

GOALIN = 0
MOVE = 1
CATCH = 2


class board:
    tile_list = []  # 칸의 배열
    color_list = ["\033[31m", "\033[34m"]  # color 배열 순서대로 0 : red , 1 : blue
    team_list = []

    def __init__(self):
        self.tile_list = [tile(-1)]  # 칸의 배열
        self.tile_list.pop()
        for i in range(29):
            self.tile_list.append(tile(i + 1))

    def move_piece(self, piece: piece, yut_result):
        dest = 0
        if piece.get_index() == 0:  # 집에서 출발
            dest = yut_result
            dest_tile = self.tile_list[dest - 1]
            if len(dest_tile.get_pieces()) == 0:
                piece.set_index(dest)
                dest_tile.set_pieces([piece])
                return MOVE
            else:
                if dest_tile.get_pieces()[0].get_team() != piece.get_team():  # 잡을 때
                    for i in dest_tile.get_pieces():
                        i.set_index(0)
                    dest_tile.set_pieces([])
                    piece.set_index(dest)
                    dest_tile.reach_piece(piece)
                    return CATCH
                else:
                    piece.set_index(dest)
                    dest_tile.reach_piece(piece)
                    return MOVE

        else:  # 집 아닐때
            dest = self.tile_list[piece.get_index() - 1].get_dest_index(yut_result)
            if dest >= 30:
                start_tile_idx = self.tile_list[piece.get_index() - 1].index
                for i in self.tile_list[piece.get_index() - 1].get_pieces():
                    i.set_index(30)
                self.tile_list[start_tile_idx - 1].set_pieces([])
                return GOALIN
            dest_tile = self.tile_list[dest - 1]
            if len(dest_tile.get_pieces()) != 0:
                if dest_tile.get_pieces()[0].get_team() != piece.get_team():
                    for i in dest_tile.get_pieces():
                        i.set_index(0)
                    dest_tile.set_pieces([])
                    dest_tile.set_pieces(
                        self.tile_list[piece.get_index() - 1].get_pieces()
                    )
                    self.tile_list[piece.get_index() - 1].set_pieces([])
                    for i in dest_tile.get_pieces():
                        i.set_index(dest)
                    return CATCH
                else:  # 업을때
                    dest_tile.set_pieces(
                        dest_tile.get_pieces()
                        + self.tile_list[piece.get_index() - 1].get_pieces()
                    )
                    self.tile_list[piece.get_index() - 1].set_pieces([])
                    for i in dest_tile.get_pieces():
                        i.set_index(dest)
                    return MOVE
            else:
                dest_tile.set_pieces(self.tile_list[piece.get_index() - 1].get_pieces())
                self.tile_list[piece.get_index() - 1].set_pieces([])
                for i in dest_tile.get_pieces():
                    i.set_index(dest)
                return MOVE

    def print_tile(self, idx, p1: player, p2: player):
        num_of_pieces = self.tile_list[idx - 1].get_num_pieces()  # 타일 안에 있는 pieces의 갯수
        if num_of_pieces == 0:
            print("■  ", end="")
        else:
            if self.tile_list[idx - 1].pieces[0].get_team() == p1.get_team():
                if num_of_pieces == 1:
                    print("\033[31m" + "❶  " + "\033[0m", end="")  # reset
                elif num_of_pieces == 2:
                    print("\033[31m" + "❷  " + "\033[0m", end="")
                elif num_of_pieces == 3:
                    print("\033[31m" + "❸  " + "\033[0m", end="")
                else:
                    print("\033[31m" + "❹  " + "\033[0m", end="")
            else:
                if num_of_pieces == 1:
                    print("\033[34m" + "❶  " + "\033[0m", end="")  # reset
                elif num_of_pieces == 2:
                    print("\033[34m" + "❷  " + "\033[0m", end="")
                elif num_of_pieces == 3:
                    print("\033[34m" + "❸  " + "\033[0m", end="")
                else:
                    print("\033[34m" + "❹  " + "\033[0m", end="")

    def show_board(self, p1: player, p2: player):
        os.system("cls")
        gotoxy(20, 10)
        for i in range(6):
            self.print_tile(10 - i, p1, p2)
        print()
        gotoxy(20, 12)
        self.print_tile(11, p1, p2)
        self.print_tile(23, p1, p2)
        print("        ", end="")
        self.print_tile(21, p1, p2)
        self.print_tile(4, p1, p2)
        print()
        gotoxy(20, 14)
        self.print_tile(12, p1, p2)
        print("    ", end="")
        self.print_tile(24, p1, p2)
        self.print_tile(22, p1, p2)
        print("    ", end="")
        self.print_tile(3, p1, p2)
        print()
        gotoxy(20, 15)
        print("          ", end="")
        self.print_tile(25, p1, p2)
        print()
        gotoxy(20, 16)
        self.print_tile(13, p1, p2)
        print("    ", end="")
        self.print_tile(28, p1, p2)
        self.print_tile(26, p1, p2)
        print("    ", end="")
        self.print_tile(2, p1, p2)
        print()
        gotoxy(20, 18)
        self.print_tile(14, p1, p2)
        self.print_tile(29, p1, p2)
        print("        ", end="")
        self.print_tile(27, p1, p2)
        self.print_tile(1, p1, p2)
        print()
        gotoxy(20, 20)
        for i in range(6):
            self.print_tile(15 + i, p1, p2)
        print()

    def show_pieces_state(self, p1: player, p2: player, turn):
        p1_piece_list = p1.get_piecelist()
        p2_piece_list = p2.get_piecelist()
        gotoxy(55, 10)
        print("\033[31m" + p1.get_team() + " 팀")
        for i in range(len(p1_piece_list)):  # 각 플레이어의 말 상태 출력
            gotoxy(55, i + 11)
            print_idx = (
                "골인"
                if p1_piece_list[i].get_index() >= 30
                else p1_piece_list[i].get_index()
            )
            print(f"{i + 1} 번 말 : {print_idx}")
        print("\033[0m")
        gotoxy(68, 10)
        print("\033[34m  " + p2.get_team() + " 팀")
        for i in range(len(p2_piece_list)):
            gotoxy(70, i + 11)
            print_idx = (
                "골인"
                if p2_piece_list[i].get_index() >= 30
                else p2_piece_list[i].get_index()
            )
            print(f"{i + 1} 번 말 : {print_idx}")
        print("\033[0m")
        gotoxy(55, 16)
        if turn == 0:
            print("\033[31m" + "[%s의 던진 윷 현황]" % p1.get_team())
            gotoxy(55, 17)
            print(p1.results)
            print("\033[0m")
        else:
            print("\033[34m" + "[%s의 던진 윷 현황]" % p2.get_team())
            gotoxy(55, 17)
            print(p2.results)
            print("\033[0m")
