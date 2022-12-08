import random


class yut:
    value = ""  # 윷 객체의 값 (도, 개, 걸 , 윷, 모)중 하나를 가짐

    def get_value(self):  # 윷 객체의 값을 반환
        return self.value

    def throw(self):  # 윷 객체의 값을 정해진 확률에 따라 랜덤으로 설정
        ran = random.randrange(1, 6)
        if ran >= 1 and ran <= 2:
            self.value = "등"
        else:
            self.value = "배"
        return self.get_value()
