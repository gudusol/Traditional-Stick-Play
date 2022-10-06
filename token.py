class token:
    idx = 0
    team = ""

    def __init__(self, team):
        self.team = str(team)

    def set_index(self, idx):
        self.idx = idx

    def get_index(self):
        if self.idx == 0:
            return "집"
        elif self.idx > 0 and self.idx < 30:
            return self.idx
        elif self.idx >= 30:
            return "골인"
        else:
            return "Index error"  # idx 음수값

    def get_team(self):
        return self.team
