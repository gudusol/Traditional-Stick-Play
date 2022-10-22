from yut import yut
from piece import piece


class player:
    team = ""
    pieces = []  # 4개의 말을 관리하는 리스트
    results = []  # 윷 던진 결과 임시저장 리스트 추가

    def __init__(self, team):
        self.team = str(team)
        self.pieces = [
            piece(self.team),
            piece(self.team),
            piece(self.team),
            piece(self.team),
        ]
        self.results = []

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
            if i.get_index() >= 30:
                count += 1
        return count

    def get_piecelist(self):
        return self.pieces
