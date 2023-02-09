
import musume
import dfs
import numpy as np
import breadth_search as bs

rows = musume.init_puzzle()


bs.breadth_search(rows)

a, b = dfs.dfs(rows)
print("総盤面数は", a, "通りです")
i = 0
c = []
for x in b:
    n = len(x)
    c.append(n)
print(len(c))
d = np.argmin(c)
print(c[d])
