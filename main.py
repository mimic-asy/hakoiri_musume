
import musume
import dfs

rows = musume.init_puzzle()


# bs.breadth_search(rows)

a, b = dfs.dfs(rows)
print("総盤面数は", a, "通りです")
x = min(b)
print("最短手数は", len(x), "手です")
print(len(x))
print("最短手数の経路は以下の通りです")
print(x)
