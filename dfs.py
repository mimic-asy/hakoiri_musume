import musume
import numpy as np


rows = musume.init_puzzle()


def depth_first_search(rows):
    stack = []
    # 取り出す盤面（変換前）を入れる
    clear_route = []
    # 経路を保存する盤面（変換前）を入れる
    comparison_rows = set()
    # 比較する盤面(変換後)を入れる
    all_boards = []
    # 全ての盤面を保存する
    rows_copy = np.copy(rows)
    simple_rows = musume.board_simple(rows_copy)
    # 比較用の変換後の初期位置を作成
    stack.append(rows_copy)
    comparison_rows.add(musume.to_hashable(simple_rows))

    while len(stack) > 0:
        rows_now = stack.pop()
        # 現在の盤面を出力
        movable_list = musume.moved_board_list(rows_now)
        # print(movable_list)
        # 現在の位置から動ける盤面をリスト化

        for n in movable_list:
            # 現在地点から動ける点を探す
            simple_n = musume.board_simple(n)
            # 比較できる形にする
            if musume.to_hashable(simple_n) not in comparison_rows:
                # これまでに未踏の点であった場合
                # setのあまりにも早いin、俺でなきゃ見逃しちゃうね

                if musume.clear(n):
                    # clearした場合
                    simple_n = musume.board_simple(n)
                    # 盤面を比較できるように変換
                    stack.append(n)
                    # クリアした盤面の形をstackに保存
                    stack_copy = np.copy(stack)
                    comparison_rows.add(musume.to_hashable(simple_n))
                    clear_route.append(stack_copy)
                    rows_now = n
                    # スタック（これまでの道筋）を保存

                else:
                    stack.append(n)
                    # stackに点を追加
                    comparison_rows.add(musume.to_hashable(simple_n))
                    # 比較用リストに点を追加
                    all_boards.append(n)
                    # 盤面を保存するリストに追加
                    rows_now = n
                    # 現在地を更新

    return len(comparison_rows)
