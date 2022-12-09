class piece:
    idx = 0  # 말의 인덱스
    team = ""  # 팀 이름

    # def __init__(self, team):  # 팀 이름을 받아서 초기화
    #     self.idx = 0
    #     self.team = str(team)

    def __init__(self, team, idx):  # 생성자 오버로딩: 저장 데이터를 불러올 때
        self.idx = idx
        self.team = str(team)

    def set_index(self, idx):  # 말의 인덱스를 설정
        self.idx = idx

    def get_index(self):  # 말의 인덱스를 반환
        return self.idx

    def get_team(self):  # 팀 이름을 반환
        return self.team
