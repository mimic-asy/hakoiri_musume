
# musume.pyには箱入り娘を動かす上で必要な関数と探索を行う上で必要な関数が入っているよ
import musume
# bfs。pyには幅優先探索を行う関数が入っているよ
import bfs as bs
# Dfs。pyには深さ優先探索を行う関数が入っているよ
import dfs

# rowsに初期位置を入れる
rows = musume.init_puzzle()


# 幅探索を回す
board_state, clear_route = bs.breadth_first_search(rows)
print("幅探索の結果、探索された盤面は")
print(len(board_state), "個です。")

# 深さ優先探索を回して、幅探索の結果と一致するか確認する
dfs_reslut = dfs.depth_first_search(rows)
print("深さ優先探索の結果、探索された盤面は")
print(dfs_reslut, "個です。")
# 一致した場合、探索結果が正しいと仮定して、最短経路を求める
if dfs_reslut == len(board_state):
    print("深さ優先探索と幅優先探索の結果が一致しました。")
    print("最短経路を出力します")
    shortest_index = musume.shortest_path(clear_route)
    print("最短手順は")
    print(clear_route[shortest_index])
    print("となります")
    print("最短手は", len(clear_route[shortest_index]), "手です")
