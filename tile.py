class tile:
    index = 0
    pieces = []

    def __init__(self, index):
        self.index = index

    def set_pieces(self, pieces):
        self.pieces = pieces
        return

    def get_pieces(self):
        return self.pieces

    def reach_piece(self, piece):
        self.pieces.append(piece)

    # 5번 10번 15번 20번 25번
    def get_dest_index(self, yut_result):
        dest_index = -1
        if self.index == 20:
            dest_index = 30
        elif self.index == 5:
            if yut_result == 1 or yut_result == 2:
                dest_index = self.index + 15 + yut_result
            elif yut_result == 3:
                dest_index = 25
            elif yut_result == 4 or yut_result == 5:
                dest_index = self.index + 19 + yut_result
        elif self.index == 10:
            dest_index = self.index + 12 + yut_result
        elif self.index >= 15 and self.index <= 20:
            if self.index + yut_result > 20:
                dest_index = 30
            else:
                dest_index = self.index + yut_result
        elif self.index == 21:
            if yut_result == 1:
                dest_index = self.index + yut_result
            elif yut_result == 2:
                dest_index = 25
            elif yut_result == 3 or yut_result == 4:
                dest_index = self.index + 4 + yut_result
            elif yut_result == 5:
                dest_index = 15
        elif self.index == 22:
            if yut_result == 1:
                dest_index = 25
            elif yut_result == 2 or yut_result == 3:
                dest_index = self.index + 4 + yut_result
            elif yut_result == 4 or yut_result == 5:
                dest_index = self.index - 11 + yut_result
            else:
                return  # error
        elif self.index >= 23 and self.index <= 27:
            if self.index + yut_result == 28:
                dest_index = 20
            elif self.index + yut_result > 28:
                dest_index = 30
            else:
                dest_index = self.index + yut_result
        elif self.index == 28:
            if yut_result == 1:
                dest_index = self.index + yut_result
            elif yut_result > 1:
                dest_index = self.index - 15 + yut_result
        elif self.index == 29:
            dest_index = self.index - 15 + yut_result
        else:
            dest_index = self.index + yut_result

        self.pieces.clear()
        return dest_index
