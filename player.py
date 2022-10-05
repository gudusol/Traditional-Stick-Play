from yut import yut


class player:
    yut_list = [yut(), yut(), yut(), yut()]  # 나중에 윷리스트는 게임으로 옮김

    def throw(self):
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
