import breadth_search as bs
import musume


rows = musume.init_puzzle()

bs.breadth_search(rows)
# bs.networkx_dfs(rows)
