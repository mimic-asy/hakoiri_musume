
import musume
import breadth_search as bs
import dfs

# rowsに初期位置を入れる
rows = musume.init_puzzle()


# 幅探索を回して、
board_state, clear_route = bs.breadth_search(rows)
print("幅探索の結果、探索された盤面は")
print(len(board_state), "個です。")

# 深さ優先探索を回して、幅探索の結果と一致するか確認する
dfs_reslut = dfs.dfs(rows)
print("深さ優先探索の結果、探索された盤面は")
print(dfs_reslut, "個です。")

if dfs_reslut == len(board_state):
    print("深さ優先探索と幅優先探索の結果が一致しました。")
    print("最短経路を出力します")
    musume.shortest_path(clear_route)
