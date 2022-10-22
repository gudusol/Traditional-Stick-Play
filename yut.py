import random


class yut:
    value = ""
    
    def get_value(self):
        return self.value

    def throw(self):
        ran = random.randrange(1, 4)
        if ran == 1:
            self.value = "등"
        else:
            self.value = "배"
        return self.get_value()
