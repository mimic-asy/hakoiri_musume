import musume
import numpy as np
from collections import deque


def breadth_search(rows):
    # rows is copy
    rows_copy = np.copy(rows)
    the_one_before = []
    # rowsを比較しやすい形にする
    rows_simple = musume.board_simple(rows_copy)
    # board_state に　比較しやすい形のrowsを入れる
    board_state = set()
    # board_queue に　変換する前の盤面を入れる
    board_queue = deque()
    # 最初の盤面の変換する前を入れる
    board_queue.append(rows_copy)
    # 最初の盤面の変換した後を入れる)
    board_state.add(musume.to_hashable(rows_simple))
    # board_queue が０になるまで実行する
    clear_route = []
    n = 1

    while len(board_queue) > 0:
        n += 1
        print(n)
        # rows_nowにboard_queueから取り出したrowsを入れる
        rows_now = board_queue.popleft()
        # moved_rows_listに現在地点から展開できるノードを収納する
        moved_rows_list = musume.moved_board_list(rows_now)

        # 現在地点から展開できるノード一つ一つが今までに出てきているか確認する
        musume.queue_state_append(moved_rows_list, board_state,
                                  board_queue, rows_now, the_one_before,
                                  clear_route)

    return board_state, clear_route
