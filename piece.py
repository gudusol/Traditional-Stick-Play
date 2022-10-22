class piece:
    idx = 0
    team = ""

    def __init__(self, team):
        self.idx = 0
        self.team = str(team)

    def set_index(self, idx):
        self.idx = idx

    def get_index(self):
        return self.idx

    def get_team(self):
        return self.team
