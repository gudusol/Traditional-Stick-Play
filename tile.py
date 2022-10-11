class tile:
    index = 0
    tokens = []

    def __init__(self, index):
        self.index = index

    def reach_token(self, token):
        self.tokens.append(token)

    # 1번 6번 11번 16번 25번
    def get_dest_index(self, yut_result):
        if self.index == 6:
            if yut_result == 1 or yut_result == 2:
                return self.index + yut_result
            elif yut_result == 3:
                return 25
            elif yut_result == 4 or yut_result == 5:
                return self.index + 18 + yut_result
        elif self.index == 11:
            return self.index + 11 + yut_result
        elif self.index >= 23:
            if self.index + yut_result == 28:
                return 1
            elif self.index + yut_result > 29:
                return 30
        else:
            return self.index + yut_result
