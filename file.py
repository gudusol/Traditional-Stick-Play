import pickle
import os
from time import sleep
from player import player


def load_data():  # 파일 읽기
    try:
        with open("save_data.pickle", "rb") as fr:
            game_data = pickle.load(fr)
    except FileNotFoundError:
        os.system("cls")
        print("저장 파일이 존재하지 않습니다.")
        sleep(2)
        return -1

    player_list = []

    if filecheck(game_data):  # 무결성 검사
        p1 = game_data["player1"]
        p2 = game_data["player2"]

        player_list.append(player(p1["name"], p1["pieces"], p1["yut_results"]))
        player_list[-1].set_color(p1["color"])
        player_list.append(player(p2["name"], p2["pieces"], p2["yut_results"]))
        player_list[-1].set_color(p2["color"])

        turn = 0 if p1["turn"] == True else 1

        return player_list, turn  # 파일 안의 정보로 플레이어 객체 리스트, 현재 턴정보 리턴 (p1 턴이면 0)
    else:
        os.system("cls")
        print("파일 무결성 검사 결과 결함 발견. 파일의 형식이 올바른 지 확인해주세요.")
        sleep(3)
        return -1


def filecheck(game_data):  # 무결성 검사 진행
    p1 = game_data["player1"]
    p2 = game_data["player2"]

    if p1 == None or p2 == None:  # p1과 p2가 값을 갖고있는가?
        return False
    elif p1["name"] == p2["name"]:  # p1과 p2의 이름이 다른가?
        return False
    elif p1["color"] == p2["color"]:  # p1과 p2의 색이 다른가?
        return False
    elif p1["turn"] == p2["turn"]:  # p1과 p2의 턴이 다른가?
        return False
    elif (p1["turn"] == False and p1["yut_results"]) or (
        p2["turn"] == False and p2["yut_results"]
    ):
        # 본인 턴이 아니면 결과 리스트가 비었는가?
        return False
    else:  # 파일 내용이 유효하면 True 리턴
        return True
