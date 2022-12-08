import random
from yut import yut
from piece import piece


class player:
    team = ""  # 팀 이름
    pieces = []  # 4개의 말을 관리하는 리스트
    results = []  # 윷 던진 결과 임시저장 리스트 추가
    color = ""  # 색깔

    def __init__(self, team):  # 팀 이름을 받아서 초기화
        self.team = str(team)
        self.pieces = [
            piece(self.team),
            piece(self.team),
            piece(self.team),
            piece(self.team),
        ]
        self.results = []

    def throw(self, yut_list):  # 윷 던지기

        ran = random.randrange(1, 21)
        if ran == 1:
            result = "낙"

        # 윷 던진 결과 임시저장 리스트에 추가
        li = [i.throw() for i in yut_list]

        # 윷 결과에 따라 도, 개, 걸, 윷, 모를 반환
        if li.count("등") == 4:
            result = "모"
        elif li.count("등") == 3:
            ran = random.randrange(1, 5)
            if ran == 1:
                result = "빽도"
            else:
                result = "도"
        elif li.count("등") == 2:
            result = "개"
        elif li.count("등") == 1:
            result = "걸"
        elif li.count("등") == 0:
            result = "윷"
        else:
            exit(-1)
        self.results.append(result)

    def get_team(self):  # 팀 이름 반환
        return self.team

    def goal_in_piece(self):  # 골인한 말의 개수를 반환
        count = 0
        for i in self.pieces:
            if i.get_index() >= 30:
                count += 1
        return count

    def get_piecelist(self):  # 말 리스트 반환
        return self.pieces

    def set_color(self, color):
        self.color = color
        return
