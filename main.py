
import musume
import breadth_search as bs

rows = musume.init_puzzle()

short = []

board_state, clear_route = bs.breadth_search(rows)
print(len(board_state))
print(len(clear_route))

for i in clear_route:
    f = len(i)
    short.append(f)

x = short.index(min(short))
print("最短手順は")
print(clear_route[x])
print("となります")
print("最短手は", min(short), "手です")
