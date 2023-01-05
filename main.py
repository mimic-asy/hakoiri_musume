import breadth_search as bs
import musume


rows = musume.init_puzzle()


bs.networkx_dfs(rows)
