from player import player

p1 = player()
p2 = player()

for i in range(100):
    print(f"p1: {p1.throw()}, p2: {p2.throw()}")
