class piece:
    idx = 0
    team = ""

    def __init__(self, team):
        self.idx = 0
        self.team = str(team)

    def set_index(self, idx):
        self.idx = idx

    def get_index(self):
        # if self.idx == 0:
        #    return 0
        # elif self.idx > 0 and self.idx < 30:
        #    return self.idx
        # elif self.idx >= 30:
        #    return self.idx
        # else:
        #    return self.idx  # idx 음수값
        return self.idx

    def get_team(self):
        return self.team
