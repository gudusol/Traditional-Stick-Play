from tile import tile
from player import player
from piece import piece
from gotoxy import gotoxy
import os

GOALIN = 0
MOVE = 1
CATCH = 2


class board:
    tile_list = []  # 칸의 배열

    def __init__(self):
        for i in range(29):
            self.tile_list.append(tile(i + 1))

    def move_token(self, token, yut_result) -> int:
        i = -1
        if token.get_index() == "골인":
            return GOALIN
        else:
            i = MOVE
            result = self.tile_list[token.get_index()].get_dest_index(
                yut_result
            )  # result변수에 윷 결과에 맞는 도착할 칸의 인덱스 저장
            if len(self.tile_list[result].get_tokens()) > 0:
                if (
                    self.tile_list[result].get_tokens()[0].get_team()
                    != token.get_team()
                ):  # result칸에 있는 타일의 말 리스트를 가져와 리스트에 적팀 말이 있는지 조사
                    for i in self.tile_list[result].get_tokens():
                        i.set_index(0)  # 있으면 적팀 말 집으로 다 보내버리고 해당 칸의 말 리스트 clear()
                    self.tile_list[result].get_tokens().clear()
                    i = CATCH  # i값을 catch로 설정
            for i in self.tile_list[token.get_index()]:
                self.tile_list[result].reach_token(token)
                token.set_index(result)

        return i

    def print_tile(self, idx):
        num_of_tokens = len(self.tile_list[idx - 1].get_tokens())
        if num_of_tokens == 0:
            print("■    ", end="")
        elif num_of_tokens == 1:
            print("❶   ", end="")
        elif num_of_tokens == 2:
            print("❷   ", end="")
        elif num_of_tokens == 3:
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

    def show_tokens_state(self, player1: player, player2: player):
        player1_token_list = player1.get_tokenlist()
        player2_token_list = player2.get_tokenlist()
        gotoxy(28, 0)
        print(player1.get_team() + " 팀")
        for i in range(len(player1_token_list)):  # 각 플레이어의 말 상태 출력
            gotoxy(28, i + 1)
            print("%d 번 말 : %d" % (i + 1, player1_token_list[i].get_index()))
        gotoxy(39, 0)
        print("| " + player2.get_team() + " 팀")
        for i in range(len(player2_token_list)):
            gotoxy(39, i + 1)
            print("| %d 번 말 : %d" % (i + 1, player2_token_list[i].get_index()))

    def show_yut_result(self, player: player):
        gotoxy(28, 7)
        print("윷 결과")
