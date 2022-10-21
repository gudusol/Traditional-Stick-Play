from token import token
from board import board

# for i in range(100):
#     print(f"p1: {p1.throw()}, p2: {p2.throw()}")

b = board()
li = b.tile_list

for i in li:
    print(f"{i.index}번째 칸에서 이동: ", end="")
    for j in range(5):
        print(f"{j+1}: {i.get_dest_index(j+1)}   ", end="")
    print()
