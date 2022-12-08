from piece import piece


class tile:
    index = 0  # 칸의 인덱스
    pieces = []  # 칸에 있는 말들

    def __init__(self, index):  # 칸의 인덱스를 받아 초기화
        self.pieces = [piece("a")]
        self.pieces.pop()
        self.index = index
        self.pieces = [piece(" ")]
        self.pieces.clear()

    def get_num_pieces(self):  # 칸에 있는 말의 개수를 반환
        return len(self.pieces)

    def get_pieces(self):  # 칸에 있는 말들을 반환
        return self.pieces

    def set_pieces(self, pieces):  # 배열을 인자로 받아서 칸의 말들을 설정
        self.pieces = pieces
        return

    def reach_piece(self, piece):  # 말 객체를 인자로 받아서 칸에 배열에 추가
        self.pieces.append(piece)

    def get_dest_index(self, yut_result):  # 윷의 결과를 인자로 받아서 도착 칸의 인덱스를 반환
        dest_index = -1
        if yut_result == -1:  # 윷의 결과가 빽도인 경우
            if self.index == 1:
                dest_index = 20
            elif self.index == 15:
                dest_index = 29
            elif self.index == 20:
                dest_index = 27
            elif self.index == 21:
                dest_index = 5
            elif self.index == 23:
                dest_index = 10
            elif self.index == 25:
                dest_index = 22
            elif self.index == 28:
                dest_index = 25
            else:
                dest_index = self.index - 1

        else:  # 윷의 결과가 빽도가 아닌 경우
            if self.index == 20:  # 20번 칸인 경우 어떤 값이어도 골인
                dest_index = 30
            elif self.index == 5:  # 5번 칸인 경우 지름길 쪽 인덱스 반환
                if yut_result == 1 or yut_result == 2:  # 도, 개인 경우
                    dest_index = self.index + 15 + yut_result
                elif yut_result == 3:  # 걸인 경우
                    dest_index = 25
                elif yut_result == 4 or yut_result == 5:  # 윷, 모인 경우
                    dest_index = self.index + 19 + yut_result
            elif self.index == 10:  # 10번 칸인 경우 지름길 쪽 인덱스 반환
                dest_index = self.index + 12 + yut_result
            elif self.index >= 15 and self.index <= 20:  # 15번 칸부터 20번 칸인 경우
                if self.index + yut_result > 20:  # 골인 처리
                    dest_index = 30
                else:
                    dest_index = self.index + yut_result
            elif self.index == 21:  # 21번 칸인 경우
                if yut_result == 1:  # 도인 경우
                    dest_index = self.index + yut_result
                elif yut_result == 2:  # 개인 경우
                    dest_index = 25
                elif yut_result == 3 or yut_result == 4:  # 걸, 윷인 경우
                    dest_index = self.index + 4 + yut_result
                elif yut_result == 5:  # 모인 경우
                    dest_index = 15
            elif self.index == 22:  # 22번 칸인 경우
                if yut_result == 1:  # 도인 경우
                    dest_index = 25
                elif yut_result == 2 or yut_result == 3:  # 개, 걸인 경우
                    dest_index = self.index + 4 + yut_result
                elif yut_result == 4 or yut_result == 5:  # 윷, 모인 경우
                    dest_index = self.index - 11 + yut_result
            elif (
                self.index >= 23 and self.index <= 27
            ):  # 23번 칸부터 27번 칸인 경우 (좌측 상단에서 우측 하단으로 내려오는 대각선)
                if self.index + yut_result == 28:  # 20번 칸에 도착한 경우
                    dest_index = 20
                elif self.index + yut_result > 28:  # 골인 처리
                    dest_index = 30
                else:
                    dest_index = self.index + yut_result  # 그 외의 경우
            elif self.index == 28:  # 28번 칸인 경우
                if yut_result == 1:  # 도인 경우 29번 칸으로 이동
                    dest_index = self.index + yut_result
                elif yut_result > 1:  # 그 외의 15 ~ 18번 칸으로 이동
                    dest_index = self.index - 15 + yut_result
            elif self.index == 29:  # 29번 칸인 경우 15 ~ 19번 칸으로 이동
                dest_index = self.index - 15 + yut_result
            else:  # 그 외의 경우 나온 결과 만큼 이동
                dest_index = self.index + yut_result

        return dest_index
