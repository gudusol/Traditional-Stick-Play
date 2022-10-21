from yut import yut
from piece import piece


class player:
    team = ""
    tokens = []

    def __init__(self, team):
        self.team = team
        self.tokens = [
            piece(self.team),
            piece(self.team),
            piece(self.team),
            piece(self.team),
        ]

    # 나중에 윷리스트는 게임으로 옮기고 yut_list를 throw 함수의 인자로 받음

    def throw(self, yut_list):
        li = [i.throw() for i in self.yut_list]

        if li.count("등") == 4:
            return "모"
        elif li.count("등") == 3:
            return "도"
        elif li.count("등") == 2:
            return "개"
        elif li.count("등") == 1:
            return "걸"
        elif li.count("등") == 0:
            return "윷"
        else:
            return "error"

    def get_team(self):
        return self.team

    def goal_in_token(self):
        count = 0
        for i in self.tokens:
            if i.is_goal_in:
                count += 1
        return count

    def get_tokenlist(self):
        return self.tokens
