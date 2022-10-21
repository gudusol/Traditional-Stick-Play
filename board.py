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
        num_of_tokens = len(self.tile_list[idx].get_tokens())
        if num_of_tokens == 0:
            print("■  ")
        elif num_of_tokens == 1:
            print("❶ ")
        elif num_of_tokens == 2:
            print("❷ ")
        elif num_of_tokens == 3:
            print("❸ ")
        else:
            print("❹ ")

    def show_board(self):
        for i in range(6):
            self.print_tile(11 - i)
        print("\n\n")
        self.print_tile(12)
        self.print_tile(23)
        print("      ")
        self.print_tile(21)
        self.print_tile(5)
        print("\n\n")
        self.print_tile(13)
        print("   ")
        self.print_tile(24)
        self.print_tile(22)
        print("   ")
        self.print_tile(4)
        print("\n\n")
        print("       ")
        self.print_tile(25)
        print("\n\n")
