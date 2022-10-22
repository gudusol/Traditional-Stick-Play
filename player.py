from yut import yut
from piece import piece


class player:
    team = ""
    pieces = []
    results = []  # 윷 던진 결과 임시저장 리스트

    def __init__(self, team):
        self.team = team
        self.pieces = [
            piece(self.team),
            piece(self.team),
            piece(self.team),
            piece(self.team),
        ]

    # 나중에 윷리스트는 게임으로 옮기고 yut_list를 throw 함수의 인자로 받음

    def throw(self, yut_list):
        li = [i.throw() for i in yut_list]

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

    def goal_in_piece(self):
        count = 0
        for i in self.pieces:
            if i.is_goal_in:
                count += 1
        return count

    def get_piecelist(self):
        return self.pieces
