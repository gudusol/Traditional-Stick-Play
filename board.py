from tile import tile
from player import player
from piece import piece
from gotoxy import gotoxy
import unicodedata
import os

# 말이 움직인 결과에 따라 값을 반환하기 위한 상수
GOALIN = 0
MOVE = 1
CATCH = 2


class board:
    tile_list = []  # 칸의 배열
    team_list = []  # 팀을 저장하는 배열
    player_list = []  # player 객체를 담을 리스트

    # def __init__(self):  # 보드 생성
    #     self.player_list = [player("")]
    #     self.player_list.pop()
    #     self.tile_list = [tile(-1)]
    #     self.tile_list.pop()
    #     for i in range(29):
    #         self.tile_list.append(tile(i + 1))  # 칸의 배열 초기화

    def __init__(self, player_list):  # 플레이어 리스트가 존재하는 상태에서 보드 생성
        self.player_list = player_list
        self.tile_list = [tile(-1)]
        self.tile_list.pop()
        for i in range(29):
            self.tile_list.append(tile(i + 1))

    # def __init__(self, game_data):  # 생성자 오버로딩: 저장 데이터를 불러올 때
    #     p1 = game_data["player1"]
    #     p2 = game_data["player2"]

    #     # self.color_dic = {p1["name"]: p1["color"], p2["name"]: p2["color"]}
    #     self.player_list = [
    #         player(p1["name"], p1["pieces"], p1["yut_result"]),
    #         player(p2["name"], p2["pieces"], p2["yut_result"]),
    #     ]
    #     self.tile_list = [tile(-1)]
    #     self.tile_list.pop()
    #     for i in range(29):
    #         self.tile_list.append(tile(i + 1))

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

    def print_tile(self, idx):  # 칸을 출력하는 함수
        num_of_pieces = self.tile_list[idx - 1].get_num_pieces()  # 타일 안에 있는 pieces의 갯수
        if num_of_pieces == 0:  # 말이 없을 때
            print("■  ", end="")
        else:  # 말이 있을 때, 말의 갯수에 따라 다른 숫자를 출력, 말의 팀에 따라 다른 색깔을 출력
            cur_color = ""
            if (
                self.player_list[0].get_team()
                == self.tile_list[idx - 1].pieces[0].get_team()
            ):
                cur_color = self.player_list[0].get_color()
            else:
                cur_color = self.player_list[1].get_color()

            if num_of_pieces == 1:  # color_dic의 키값으로 value를 접근
                print(
                    cur_color + "❶  " + "\033[0m",
                    end="",
                )  # reset
            elif num_of_pieces == 2:
                print(
                    cur_color + "❷  " + "\033[0m",
                    end="",
                )
            elif num_of_pieces == 3:
                print(
                    cur_color + "❸  " + "\033[0m",
                    end="",
                )
            else:
                print(
                    cur_color + "❹  " + "\033[0m",
                    end="",
                )

    def show_board(self):  # 보드를 출력하는 함수
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

    def show_pieces_state(self, turn):  # 현황판 출력하는 함수 (말의 상태, 팀, 턴)
        x = 55
        y = 10
        x_temp = 0

        # 각 플레이어의 말 상태 출력
        for i in self.player_list:  # 저장된 플레이어 객체 순서대로 출력
            cur_color = i.get_color()
            gotoxy(x + x_temp, y)
            print(cur_color + i.get_team() + " 팀")
            player_piece_list = i.get_piecelist()
            for j in range(len(player_piece_list)):
                gotoxy(x + x_temp, y + 1 + j)
                print_idx = (
                    "골인"
                    if player_piece_list[j].get_index() >= 30
                    else player_piece_list[j].get_index()
                )
                print(f"{j + 1} 번 말 : {print_idx}")
            print("\033[0m")
            x_temp += 25

        # 현재 턴인 플레이어의 윷 결과 출력
        gotoxy(x, y + 6)
        print(
            self.player_list[turn].get_color()
            + f"[{self.player_list[turn].get_team()}의 던진 윷 현황]"
        )
        gotoxy(x, y + 7)
        print(self.player_list[turn].results)
        print("\033[0m")
