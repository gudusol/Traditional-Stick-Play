from tile import tile
from player import player
from token import token


class board:
    tile_list = []  # 칸의 배열

    def __init__(self):
        for i in range(29):
            self.tile_list.append(tile(i + 1))

    def move_token(self, token, yut_result):
        if token.get_index() == "골인":
            return 0
        else:
            result = self.tile_list[token.get_index()].get_dest_index(yut_result)
            token.set_index(result)
            self.tile_list[result].reach_token(token)

    def print_tile(self, idx):
        num_of_tokens = len(self.tile_list[idx - 1].get_tokens())
        if num_of_tokens == 0:
            print("■  ", end="")
        elif num_of_tokens == 1:
            print("❶ ", end="")
        elif num_of_tokens == 2:
            print("❷ ", end="")
        elif num_of_tokens == 3:
            print("❸ ", end="")
        else:
            print("❹ ", end="")

    def show_board(self):
        for i in range(6):
            self.print_tile(11 - i)
        print("\n")
        self.print_tile(12)
        self.print_tile(23)
        print("      ", end="")
        self.print_tile(21)
        self.print_tile(5)
        print("\n")
        self.print_tile(13)
        print("   ", end="")
        self.print_tile(24)
        self.print_tile(22)
        print("   ", end="")
        self.print_tile(4)
        print("\n")
        print("       ", end="")
        self.print_tile(25)
        print("\n")
        self.print_tile(14)
        self.print_tile(28)
        print("      ", end="")
        self.print_tile(26)
        self.print_tile(3)
        print("\n")
        self.print_tile(15)
        print("   ", end="")
        self.print_tile(29)
        self.print_tile(27)
        print("   ", end="")
        self.print_tile(2)
        print("\n")
        for i in range(5):
            self.print_tile(16 + i)
        self.print_tile(1)
