
# musume.pyには箱入り娘を動かす上で必要な関数と探索を行う上で必要な関数が入っているよ
import musume
# bfs。pyには幅優先探索を行う関数が入っているよ
import bfs as bs


# rowsに初期位置を入れる
rows = musume.init_puzzle()


# 幅探索を回す
board_state, clear_route = bs.breadth_first_search(rows)
print("幅探索の結果、探索された盤面は")
print(len(board_state), "個です。")

shortest_index = musume.shortest_path(clear_route)
print("最短手順は")
print(clear_route[shortest_index])
print("となります")
print("最短手は", len(clear_route[shortest_index]), "手です")
