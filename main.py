from player import player
from token import token

p1 = player("red")
p2 = player("red")

# for i in range(100):
#     print(f"p1: {p1.throw()}, p2: {p2.throw()}")

t = token("red")
print(t.get_index())
t.set_index(20)
print(t.get_index())
t.set_index(40)
print(t.get_index())
