from yut import yut

class game:
    winner = "" #승리자 string형 변수 처음에는 null
    turn = 1 #현재 턴 int형 변수, 1p부터 시작함, 2p turn은 2
    yut_list = []


    def __init__(self,):
        self.yut_list = [yut(),yut(),yut(),yut()]


    def game_start(): #게임을 구동하는 함수
        while(True):


    def game_over(self): #승리 조건을 판단하고 게임을 종료
        if self.winner == "":
            return 0 #계속 게임 진행
        else:
            return self.winner #승리자 이름 리턴하고 게임 종료


    def change_turn(self): #턴이 넘어갈 때 턴이 저장된 변수 값을 바꿈
        if self.turn == 1:
            self.turn = 0
        else:
            self.turn = 1
