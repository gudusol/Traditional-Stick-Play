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

    def __init__(self):
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

    def print_tile(self, idx):
        num_of_pieces = len(self.tile_list[idx - 1].get_pieces())
        if num_of_pieces == 0:
            print("■  ", end="")
        elif num_of_pieces == 1:
            print("❶  ", end="")
        elif num_of_pieces == 2:
            print("❷  ", end="")
        elif num_of_pieces == 3:
            print("❸  ", end="")
        else:
            print("❹  ", end="")

    def show_board(self):
        os.system("cls")
        gotoxy(20, 10)
        for i in range(6):
            self.print_tile(10 - i)
        print()
        gotoxy(20, 12)
        self.print_tile(11)
        self.print_tile(23)
        print("        ", end="")
        self.print_tile(21)
        self.print_tile(4)
        print()
        gotoxy(20, 14)
        self.print_tile(12)
        print("    ", end="")
        self.print_tile(24)
        self.print_tile(22)
        print("    ", end="")
        self.print_tile(3)
        print()
        gotoxy(20, 15)
        print("          ", end="")
        self.print_tile(25)
        print()
        gotoxy(20, 16)
        self.print_tile(13)
        print("    ", end="")
        self.print_tile(28)
        self.print_tile(26)
        print("    ", end="")
        self.print_tile(2)
        print()
        gotoxy(20, 18)
        self.print_tile(14)
        self.print_tile(29)
        print("        ", end="")
        self.print_tile(27)
        self.print_tile(1)
        print()
        gotoxy(20, 20)
        for i in range(6):
            self.print_tile(15 + i)
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
        if turn == 1:
            print("[%s의 던진 윷 현황]" % player1.get_team())
            gotoxy(55, 17)
            print(player1.results)
        else:
            print("[%s의 던진 윷 현황]" % player2.get_team())
            gotoxy(55, 17)
            print(player2.results)
        # player1이랑 player2 results 공유되는듯 ㅇㅅㅇ ㅋㅋ몰?루
