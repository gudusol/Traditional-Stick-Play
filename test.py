from tile import tile
from player import player
from piece import piece
from gotoxy import gotoxy
import time
import os

GOALIN = 0
MOVE = 1
CATCH = 2
CARRY = 3


class board:
    tile_list = []  # 칸의 배열
    color_list = ["\033[31m", "\033[34m"]  # color 배열 순서대로 0 : red , 1 : blue

    def __init__(self):
        self.tile_list = [tile(-1)]
        self.tile_list.pop()
        for i in range(29):
            self.tile_list.append(tile(i + 1))

    def move_piece(self, piece, yut_result) -> int:
        ret = MOVE
        if piece.get_index() == 0:
            dest = yut_result
            dest_tile = self.tile_list[dest - 1]
            dest_pieces = dest_tile.get_pieces()
            if len(dest_pieces) > 0:
                if (
                    dest_pieces[0].get_team() != piece.get_team()
                ):  # result칸에 있는 타일의 말 리스트를 가져와 리스트에 적팀 말이 있는지 조사
                    for i in dest_pieces:
                        i.set_index(0)  # 있으면 적팀 말 집으로 다 보내버리고 해당 칸의 말 리스트 clear()
                    dest_tile.set_pieces([])
                    ret = CATCH  # i값을 catch로 설정
                else:  # 엎히기
                    ret = CARRY
            dest_tile.reach_piece(piece)
            piece.set_index(dest)
        else:
            dest = self.tile_list[piece.get_index() - 1].get_dest_index(
                yut_result
            )  # result변수에 윷 결과에 맞는 도착할 칸의 인덱스 저장
            dest_tile = self.tile_list[dest - 1]
            dest_pieces = dest_tile.get_pieces()
            start_tile = self.tile_list[piece.get_index() - 1]

            if dest >= 30:
                return GOALIN
            if len(dest_pieces) > 0:
                if (
                    dest_pieces[0].get_team() != piece.get_team()
                ):  # dest칸에 있는 타일의 말 리스트를 가져와 리스트에 적팀 말이 있는지 조사
                    for i in dest_pieces:
                        i.set_index(0)  # 있으면 적팀 말 집으로 다 보내버리고 해당 칸의 말 리스트 clear()
                    dest_tile.set_pieces([])
                    ret = CATCH  # i값을 catch로 설정
                else:  # 업히기
                    # dest_tile.set_pieces(dest_pieces + start_tile.get_pieces())
                    # start_tile.set_pieces([])
                    # for i in dest_pieces:
                    #     i.set_index(dest)
                    ret = CARRY
            dest_tile.set_pieces(dest_pieces + start_tile.get_pieces())
            start_tile.set_pieces([])
            for i in dest_pieces:
                i.set_index(dest)

        return ret

    def print_tile(self, idx, p1: player, p2: player):
        num_of_pieces = self.tile_list[idx - 1].get_num_pieces()  # 타일 안에 있는 pieces의 갯수
        if num_of_pieces == 0:
            print("■  ", end="")
        else:
            if self.tile_list[idx - 1].pieces[0].get_team() == p1.get_team():
                if num_of_pieces == 1:
                    print(self.color_list[0] + "❶  " + "\033[0m", end="")  # reset
                elif num_of_pieces == 2:
                    print(self.color_list[0] + "❷  " + "\033[0m", end="")
                elif num_of_pieces == 3:
                    print(self.color_list[0] + "❸  " + "\033[0m", end="")
                else:
                    print(self.color_list[0] + "❹  " + "\033[0m", end="")
            else:
                if num_of_pieces == 1:
                    print(self.color_list[1] + "❶  " + "\033[0m", end="")  # reset
                elif num_of_pieces == 2:
                    print(self.color_list[1] + "❷  " + "\033[0m", end="")
                elif num_of_pieces == 3:
                    print(self.color_list[1] + "❸  " + "\033[0m", end="")
                else:
                    print(self.color_list[1] + "❹  " + "\033[0m", end="")

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

    def show_pieces_state(self, player1: player, player2: player, turn):
        player1_piece_list = player1.get_piecelist()
        player2_piece_list = player2.get_piecelist()
        gotoxy(55, 10)
        print(player1.get_team() + " 팀")
        for i in range(len(player1_piece_list)):  # 각 플레이어의 말 상태 출력
            gotoxy(55, i + 11)
            print("%d 번 말 : %d" % (i + 1, player1_piece_list[i].get_index()))
        gotoxy(70, 10)
        print(" | " + player2.get_team() + " 팀")
        for i in range(len(player2_piece_list)):
            gotoxy(70, i + 11)
            print(" | %d 번 말 : %d" % (i + 1, player2_piece_list[i].get_index()))
        gotoxy(55, 16)
        if turn == 0:
            print("[%s의 던진 윷 현황]" % player1.get_team())
            gotoxy(55, 17)
            print(player1.results)
        else:
            print("[%s의 던진 윷 현황]" % player2.get_team())
            gotoxy(55, 17)
            print(player2.results)
