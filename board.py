from tile import tile
from player import player
from piece import piece
from gotoxy import gotoxy
from time import sleep
import os

# 말이 움직인 결과에 따라 값을 반환하기 위한 상수
GOALIN = 0
MOVE = 1
CATCH = 2


class board:
    tile_list = []  # 칸의 배열
    team_list = []  # 팀을 저장하는 배열

    def __init__(self):  # 보드 생성
        self.tile_list = [tile(-1)]
        self.tile_list.pop()
        for i in range(29):
            self.tile_list.append(tile(i + 1))  # 칸의 배열 초기화

    def move_piece(self, piece: piece, yut_result):  # 말을 움직이는 함수
        dest = 0  # 도착지의 인덱스
        if piece.get_index() == 0:  # 집에서 출발
            dest = yut_result
            dest_tile = self.tile_list[dest - 1]
            if len(dest_tile.get_pieces()) == 0:  # 도착지에 말이 없을 때
                piece.set_index(dest)
                dest_tile.set_pieces([piece])
                return MOVE
            else:  # 도착지에 말이 있을 때
                if (
                    dest_tile.get_pieces()[0].get_team() != piece.get_team()
                ):  # 도착지에 상대팀 말이 있을 때(잡기)
                    for i in dest_tile.get_pieces():
                        i.set_index(0)
                    dest_tile.set_pieces([])
                    piece.set_index(dest)
                    dest_tile.reach_piece(piece)
                    return CATCH
                else:  # 도착지에 같은 팀 말이 있을 때(업기)
                    piece.set_index(dest)
                    dest_tile.reach_piece(piece)
                    return MOVE

        else:  # 집 이외의 칸에서 출발
            dest = self.tile_list[piece.get_index() - 1].get_dest_index(yut_result)
            if dest >= 30:  # 도착지가 골인일 때
                start_tile_idx = self.tile_list[piece.get_index() - 1].index
                for i in self.tile_list[piece.get_index() - 1].get_pieces():
                    i.set_index(30)
                self.tile_list[start_tile_idx - 1].set_pieces([])
                return GOALIN
            dest_tile = self.tile_list[dest - 1]  # 도착지의 타일
            if len(dest_tile.get_pieces()) != 0:  # 도착지에 말이 있을 때
                if (
                    dest_tile.get_pieces()[0].get_team() != piece.get_team()
                ):  # 도착지에 상대팀 말이 있을 때(잡기)
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
                else:  # 도착지에 같은 팀 말이 있을 때(업기)
                    dest_tile.set_pieces(
                        dest_tile.get_pieces()
                        + self.tile_list[piece.get_index() - 1].get_pieces()
                    )
                    self.tile_list[piece.get_index() - 1].set_pieces([])
                    for i in dest_tile.get_pieces():
                        i.set_index(dest)
                    return MOVE
            else:  # 잡거나 업지 않고 이동 할 때
                dest_tile.set_pieces(self.tile_list[piece.get_index() - 1].get_pieces())
                self.tile_list[piece.get_index() - 1].set_pieces([])
                for i in dest_tile.get_pieces():
                    i.set_index(dest)
                return MOVE

    def print_tile(self, idx, p1: player, p2: player):  # 칸을 출력하는 함수
        num_of_pieces = self.tile_list[idx - 1].get_num_pieces()  # 타일 안에 있는 pieces의 갯수
        if num_of_pieces == 0:  # 말이 없을 때
            print("■  ", end="")
        else:  # 말이 있을 때, 말의 갯수에 따라 다른 숫자를 출력, 말의 팀에 따라 다른 색깔을 출력
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

    def show_board(self, p1: player, p2: player):  # 보드를 출력하는 함수
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

    def show_pieces_state(
        self, p1: player, p2: player, turn
    ):  # 현황판 출력하는 함수 (말의 상태, 팀, 턴)
        p1_piece_list = p1.get_piecelist()  # 플레이어 1의 말 리스트
        p2_piece_list = p2.get_piecelist()  # 플레이어 2의 말 리스트
        gotoxy(55, 10)
        print("\033[31m" + p1.get_team() + " 팀")

        # 각 플레이어의 말 상태 출력
        for i in range(len(p1_piece_list)):
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

        # 현재 턴인 플레이어의 윷 결과 출력
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
