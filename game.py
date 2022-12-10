import keyboard
from statistics import mode
from yut import yut
from board import board
from player import player
from time import sleep
from gotoxy import gotoxy
import os
import pickle
import title

x = 10  # gotoxy x좌표
y = 1  # gotoxy y좌표
WIDE_MAP = {i: i + 0xFEE0 for i in range(0x21, 0x7F)}
WIDE_MAP[0x20] = 0x3000


def flush_input():  # 입력 버퍼 비우기
    try:
        import msvcrt

        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        import sys, termios

        termios.tcflush(sys.stdin, termios.TCIOFLUSH)


class game:  # 게임 클래스
    winner = None  # 승리자 string형 변수 처음에는 null
    turn = 0  # 현재 턴 int형 변수, 1p부터 시작함, 2p turn은 1
    yut_list = []  # yut 객체를 담을 리스트
    b = None  # board 객체

    def __init__(self, player_list, turn):  # 플레이어 리스트와 현재 턴 정보가 존재하는 상태에서 게임 생성
        self.winner = None
        self.turn = turn
        self.yut_list = [yut(), yut(), yut(), yut()]
        self.b = board(player_list)

    def widen(self, s):  # full-width character로 변환
        return s.translate(WIDE_MAP)

    def can_move_back(self, pieces):  # 뒤로 이동할 수 있는 말이 있는지 획인하는 함수
        for piece in pieces:
            if 0 < piece.get_index() and piece.get_index() < 30:
                return True
        return False

    def game_start(self):  # 게임을 구동하는 함수
        flush_input()

        while self.winner is None:  # winner가 정해졌다면 게임 종료후 게임 타이틀 메뉴로 돌아감
            self.b.show_board()
            self.b.show_pieces_state(self.turn)
            gotoxy(55, 20)
            s = input("커맨드를 입력하세요.: ").strip().lower()  # 윷 던지는 변수 아래는 예외 처리 #공백 제거
            if (
                s == "던지기"
                or s == "던지"
                or s == "던"
                or s == "ㄷㅈㄱ"
                or s == "ㄷㅈ"
                or s == "ㄷ"
                or s == "throw"
                or s == "thro"
                or s == "thr"
                or s == "th"
                or s == "t"
            ):
                cur_player = self.b.player_list[self.turn]
                cur_player.throw(self.yut_list)
                cur_result = cur_player.results[-1]

                if (
                    cur_result == "윷" or cur_result == "모"
                ):  # 윷이나 모가 나왔을 때 값을 저장하고 한 번 더 던짐
                    gotoxy(55, 19)
                    print(f"{cur_result}! 한 번더~")
                    sleep(0.5)
                    continue
                elif cur_result == "낙":  # 결과가 낙일 시 결과리스트에서 삭제
                    gotoxy(55, 19)
                    print("낙!")
                    cur_player.results.pop()
                    gotoxy(35, 12)
                    sleep(0.5)
                elif (
                    cur_result == "빽도"
                    and len(cur_player.results) == 1
                    and not self.can_move_back(cur_player.get_piecelist())
                ):  # 결과가 낙일 시 결과리스트에서 삭제
                    gotoxy(55, 19)
                    print("빽도! 움직일 수 있는 말이 없습니다.")
                    cur_player.results.pop()
                    gotoxy(35, 12)
                    sleep(1)
                else:  # 도, 개, 걸일 때는 값을 저장하고 아래 쪽 move_input 함수로 넘어감
                    gotoxy(55, 19)
                    print(f"{cur_result}!")
                    gotoxy(35, 12)
                    sleep(0.5)

            elif s == "빽도":
                self.b.player_list[self.turn].results.append(s)
                if (
                    self.b.player_list[self.turn].results[-1] == "빽도"
                    and len(self.b.player_list[self.turn].results) == 1
                    and not self.can_move_back(
                        self.b.player_list[self.turn].get_piecelist()
                    )
                ):  # 결과가 낙일 시 결과리스트에서 삭제
                    gotoxy(55, 19)
                    print("빽도! 움직일 수 있는 말이 없습니다.")
                    self.b.player_list[self.turn].results.pop()
                    gotoxy(35, 12)
                    sleep(1)
                else:
                    gotoxy(55, 19)
                    print(f"{s}!")
                    gotoxy(35, 12)
                    sleep(0.5)
            elif s == "낙":
                gotoxy(55, 19)
                print("낙!")
                gotoxy(35, 12)
                sleep(0.5)
            elif s == "도" or s == "개" or s == "걸":
                self.b.player_list[self.turn].results.append(s)
                gotoxy(55, 19)
                print(f"{s}!")
                gotoxy(35, 12)
                sleep(0.5)
            elif s == "윷" or s == "모":
                self.b.player_list[self.turn].results.append(s)
                gotoxy(55, 19)
                print(f"{s}! 한 번더~")
                sleep(0.5)
                continue

            elif (
                s == "/ff" or s == "/gg" or s == "종료" or s == "항복" or s == "ㅈㅈ"
            ):  # 항복(종료)
                while True:
                    os.system("cls")

                    input_key = input("중도 포기할 시 패배 처리됩니다. 정말 포기하시겠습니까? (Y/N)").strip()
                    sleep(0.2)
                    if input_key == "Y" or input_key == "y":
                        self.change_turn()
                        self.winner = self.turn
                        break
                    elif input_key == "N" or input_key == "n":
                        break
                    else:
                        print("Y나 N으로 입력해주세요.")
                        sleep(2)
                continue

            elif (
                s == "help"
                or s == "hel"
                or s == "he"
                or s == "h"
                or s == "도움말"
                or s == "도움"
                or s == "ㄷㅇㅁ"
                or s == "ㄷㅇ"
            ):  # 도움말 명령어 처리
                title.print_help()
                continue
            elif (
                s == "save"
                or s == "sav"
                or s == "sa"
                or s == "s"
                or s == "저장하기"
                or s == "저장"
            ):  # 저장 명령어 처리
                game_data = {}
                for i in range(2):
                    p_data = {
                        "name": self.b.player_list[i].team,
                        "color": self.b.player_list[i].color,
                        "pieces": [
                            self.b.player_list[i].pieces[j].get_index()
                            for j in range(4)
                        ],
                        "yut_results": self.b.player_list[i].results,
                        "turn": self.turn == i if True else False,
                    }
                    game_data["player" + str(i + 1)] = p_data
                with open("save_data.pickle", "wb") as fw:
                    pickle.dump(game_data, fw)
                gotoxy(55, 22)
                print("게임이 성공적으로 저장되었습니다.")
                sleep(1)
                break

            else:  # 그 외의 명령어 처리
                gotoxy(55, 21)
                print("올바른 명령어를 입력해주세요")
                gotoxy(55, 22)
                print("명령어군        | 올바른 인자 | 설명")
                gotoxy(55, 23)
                print("throw   던지기  |             | 윷을 던집니다.")
                gotoxy(55, 24)
                print("/ff       항복  |  인자없음   | 항복한 플레이어의 패배")
                gotoxy(55, 25)
                print("help    도움말  |             | 전체 혹은 명령어별 도움말을 출력합니다.")
                gotoxy(55, 26)
                print("save      저장  |             | 현재까지 진행된 데이터를 저장합니다.")
                sleep(2)
                continue  # 윷 던지기 끝
            # os.system("cls")
            self.b.show_board()
            self.b.show_pieces_state(self.turn)

            # move_input 함수로 말을 움직이고 말을 잡았다면 다시 던지기, 그렇지 않으면 턴을 넘김
            if self.move_input(self.b.player_list[self.turn]) == "catch":
                gotoxy(55, 22)
                print("상대편의 말을 잡았습니다. 한 번 더 던집니다~")
                sleep(1)
                continue

        self.game_over()  # 승자가 정해지면 while문을 빠져나와 게임 종료
        flush_input()
        return 0

    def move_input(self, player):  # 움직일 말과 사용할 결과를 입력받아서 말을 움직이는 함수
        ret = ""  # 말을 잡았는지 여부를 반환하기 위한 변수
        while player.results:  # player의 결과 리스트가 비었다면 반복 종료
            self.b.show_board()
            self.b.show_pieces_state(self.turn)
            gotoxy(55, 20)
            s = input("이동할 말과 적용할 값을 입력하세요(예시: 3 걸): ")  # 몇 번 말을 몇 칸 움직일지 입력
            s = s.replace(" ", "")

            # 입력받은 명령어 문법 부합 여부 확인
            try:
                piece_num = int(s[0]) - 1  # 첫번째 글자가 움직일 말의 번호

                if player.pieces[piece_num].get_index() >= 30:  # 골인한 말일 시 문법 위배
                    gotoxy(55, 21)
                    print("이미 골인한 말입니다. 다른 말을 선택해주세요.")
                    sleep(1)
                    continue

                if s[1:] == "빽도":
                    if not self.can_move_back(
                        [player.pieces[piece_num]]
                    ):  # 집에 있는 말이 빽도를 던졌을 시 문법 위배
                        gotoxy(55, 21)
                        print("집에 있는 말은 뒤로 이동할 수 없습니다. 다른 말을 선택해주세요.")
                        sleep(1)
                        continue
                    else:
                        result = player.results.pop(player.results.index(s[1:]))
                if len(s) == 1:  # 사용자가 움직일 말만 입력했을 시
                    if len(player.results) == 1:  # 결과 리스트에 하나뿐이라면 문법 부합
                        if player.results[0] == "빽도" and not self.can_move_back(
                            [player.pieces[piece_num]]
                        ):
                            gotoxy(55, 21)
                            print("집에 있는 말은 뒤로 이동할 수 없습니다. 다른 말을 선택해주세요.")
                            sleep(1)
                            continue
                        result = player.results.pop()  # 결과 리스트에 있던 결과를 움직일 결과로 pop
                    else:  # 아니면 문법 위배
                        gotoxy(55, 21)
                        print("저장된 값이 2개 이상입니다. 값을 특정해주세요.")
                        sleep(1)
                        continue
                elif len(s) > 2:  # 사용자 명령어가 공백 미포함 2글자 초과 시 위배
                    gotoxy(55, 21)
                    print("잘못된 명령어입니다.")
                    sleep(1)
                    continue
                else:
                    result = player.results.pop(
                        player.results.index(s[1])
                    )  # 두번째 글자는 움직일 결과
                gotoxy(55, 21)
                print(f"{piece_num+1}번 말을 {result}만큼 이동합니다.")
                sleep(1)
                if result == "도":
                    result = 1
                elif result == "개":
                    result = 2
                elif result == "걸":
                    result = 3
                elif result == "윷":
                    result = 4
                elif result == "모":
                    result = 5
                elif result == "빽도":
                    result = -1

            except:
                gotoxy(55, 21)
                print("잘못된 명령어입니다.")
                sleep(1)
                continue

            moved_value = self.b.move_piece(player.pieces[piece_num], result)
            if moved_value == 0:  # 말 하나가 골인 할때 마다 플레이어가 승리했는지 확인
                if player.goal_in_piece() == 4:  # 골인한 말이 4개라면 승리
                    self.winner = self.turn
                    return
            elif moved_value == 1:  # 말을 움직였을 때
                continue
            elif moved_value == 2 and (
                result >= -1 and result <= 3
            ):  # 도, 개, 걸로 말을 잡았을 때
                ret = "catch"
                return ret

        if self.turn == 0:  # 잡지도 골인하지도 않았다면 상대 턴으로 넘어감
            self.turn = 1
        else:
            self.turn = 0

        return 0

    def game_over(self):  # 승리 조건을 판단하고 게임을 종료
        if self.winner is not None:
            os.system("cls")
            print(self.b.player_list[self.winner].team, "의 승리!!")  # 승리한 팀 출력
            sleep(3)
            return 0

    def change_turn(self):  # 턴이 넘어갈 때 턴이 저장된 변수 값을 바꿈
        if self.turn == 1:
            self.turn = 0
        else:
            self.turn = 1
