# 現在の位置から移動できる数字を補足する
# 移動できる数字を動かして
# deque内の数字を全て動かす
# 存在する盤面を調べる
# グラフ醸造を作る
#
import musume
import numpy as np
from collections import deque

# rowsを比較できるようにシンプルにするための関数


def num_simple(rows, i):
    new_rows = np.copy(rows)

    num = musume.area_check(rows, i)

    before = musume.split_number(num)

    if 0 < i < 5:
        new_rows[before[0], before[1]] = 4
        new_rows[before[2], before[3]] = 4
        return new_rows
    if 5 < i:
        new_rows[before[0], before[1]] = 6
        return new_rows
    else:
        return new_rows


def board_simple(rows):
    for i in range(10):
        rows = num_simple(rows, i)
    return rows

# 動ける数字を判定する関数、動ける場合は動かせる数字を、動けない場合はNoneを返す


def check_upside(rows, inputnumber):
    num = musume.area_check(rows, inputnumber)
    coordinate = musume.split_number(num)
    y1 = coordinate[0]
    x1 = coordinate[1]

    if inputnumber == 0:
        y2 = coordinate[2]
        x2 = coordinate[3]
        if musume.doble_basic_top(rows, x1, y1, x2, y2):
            return inputnumber
        else:
            return None
    if inputnumber == 5:
        y2 = coordinate[2]
        x2 = coordinate[3]
        if musume.doble_basic_top(rows, x1, y1, x2, y2):
            return inputnumber
        else:
            return None

    if 5 < inputnumber < 10:
        if musume.basic_top(rows, x1, y1):
            return inputnumber
        else:
            return None
    else:

        if musume.basic_top(rows, x1, y1):
            return inputnumber
        else:
            return None


def check_downside(rows, inputnumber):
    num = musume.area_check(rows, inputnumber)
    coordinate = musume.split_number(num)
    y1 = coordinate[0]
    x1 = coordinate[1]

    if inputnumber == 5:
        y2 = coordinate[2]
        x2 = coordinate[3]
        if musume.doble_basic_down(rows, x1, y1, x2, y2):
            return inputnumber
        else:
            return None
    if inputnumber == 0:
        y3 = coordinate[4]
        x3 = coordinate[5]
        y4 = coordinate[6]
        x4 = coordinate[7]
        if musume.doble_basic_down(rows, x3, y3, x4, y4):
            return inputnumber
        else:
            return None

    if 5 < inputnumber < 10:
        if musume.basic_down(rows, x1, y1):
            return inputnumber
        else:
            return None
    else:
        y2 = coordinate[2]
        x2 = coordinate[3]
        if musume.basic_down(rows, x2, y2):
            return inputnumber
        else:
            return None


def check_rightside(rows, inputnumber):
    num = musume.area_check(rows, inputnumber)
    coordinate = musume.split_number(num)
    y1 = coordinate[0]
    x1 = coordinate[1]

    if inputnumber == 0:
        y2 = coordinate[2]
        x2 = coordinate[3]
        y4 = coordinate[6]
        x4 = coordinate[7]
        if musume.doble_basic_right(rows, x2, y2, x4, y4):
            return inputnumber
        else:
            return None

    if 0 < inputnumber < 5:
        y2 = coordinate[2]
        x2 = coordinate[3]
        if musume.doble_basic_right(rows, x1, y1, x2, y2):
            return inputnumber
        else:
            return None

    if inputnumber == 5:
        y2 = coordinate[2]
        x2 = coordinate[3]
        if musume.basic_right(rows, x2, y2):
            return inputnumber
        else:
            return None

    else:
        if musume.basic_right(rows, x1, y1):
            return inputnumber
        else:
            return None


def check_leftside(rows, inputnumber):
    num = musume.area_check(rows, inputnumber)
    coordinate = musume.split_number(num)
    y1 = coordinate[0]
    x1 = coordinate[1]
    if inputnumber == 0:
        y3 = coordinate[4]
        x3 = coordinate[5]
        if musume.doble_basic_left(rows, x1, y1, x3, y3):
            return inputnumber
        else:
            return None
    if 0 < inputnumber < 5:
        y2 = coordinate[2]
        x2 = coordinate[3]
        if musume.doble_basic_left(rows, x1, y1, x2, y2):
            return inputnumber
        else:
            return None
    else:
        if musume.basic_left(rows, x1, y1):
            return inputnumber
        else:
            return None


def up_move(rows, i):
    num = musume.area_check(rows, i)
    coordinate = musume.split_number(num)

    y1 = coordinate[0]
    x1 = coordinate[1]
    if check_upside(rows, i) is not None:

        if i == 0:
            rows_data = np.copy(rows)
            y2 = coordinate[2]
            x2 = coordinate[3]
            y3 = coordinate[4]
            x3 = coordinate[5]
            y4 = coordinate[6]
            x4 = coordinate[7]
            return musume.musume_move_top(
                rows_data,
                x1, y1, x2, y2, x3, y3, x4, y4)

        if (i == 1
            or i == 2
            or i == 3
                or i == 4):
            rows_data = np.copy(rows)
            y2 = coordinate[2]
            x2 = coordinate[3]
            return musume.hight_move_top(rows_data, x1, y1, x2, y2)

        if i == 5:
            rows_data = np.copy(rows)
            y2 = coordinate[2]
            x2 = coordinate[3]
            return musume.wide_move_top(rows_data, x1, y1, x2, y2)

        if (i == 6
            or i == 7
            or i == 8
                or i == 9):
            rows_data = np.copy(rows)
            return musume.nomal_top(rows_data, x1, y1)


def down_move(rows, i):
    num = musume.area_check(rows, i)
    coordinate = musume.split_number(num)

    y1 = coordinate[0]
    x1 = coordinate[1]
    if check_downside(rows, i) is not None:

        if i == 0:
            rows_data = np.copy(rows)
            y2 = coordinate[2]
            x2 = coordinate[3]
            y3 = coordinate[4]
            x3 = coordinate[5]
            y4 = coordinate[6]
            x4 = coordinate[7]
            return musume.musume_move_downswap(
                rows_data, x1, y1, x2, y2, x3, y3, x4, y4)

        if (i == 1
            or i == 2
            or i == 3
                or i == 4):
            rows_data = np.copy(rows)
            y2 = coordinate[2]
            x2 = coordinate[3]
            return musume.hight_move_down(rows_data, x1, y1, x2, y2)

        if i == 5:
            rows_data = np.copy(rows)
            y2 = coordinate[2]
            x2 = coordinate[3]
            return musume.wide_move_down(rows_data, x1, y1, x2, y2)

        if (i == 6
            or i == 7
            or i == 8
                or i == 9):
            rows_data = np.copy(rows)
            return musume.nomal_down(rows_data, x1, y1)


def right_move(rows, i):
    num = musume.area_check(rows, i)
    coordinate = musume.split_number(num)
    y1 = coordinate[0]
    x1 = coordinate[1]
    if check_rightside(rows, i) is not None:

        if i == 0:
            rows_data = np.copy(rows)
            y2 = coordinate[2]
            x2 = coordinate[3]
            y3 = coordinate[4]
            x3 = coordinate[5]
            y4 = coordinate[6]
            x4 = coordinate[7]
            return musume.musume_move_right(
                rows_data, x1, y1, x2, y2, x3, y3, x4, y4)

        if (i == 1
            or i == 2
            or i == 3
                or i == 4):
            rows_data = np.copy(rows)
            y2 = coordinate[2]
            x2 = coordinate[3]
            return musume.hight_move_right(rows_data, x1, y1, x2, y2)

        if i == 5:
            rows_data = np.copy(rows)
            y2 = coordinate[2]
            x2 = coordinate[3]
            return musume.wide_move_right(rows_data, x1, y1, x2, y2)

        if (i == 6
            or i == 7
            or i == 8
                or i == 9):
            rows_data = np.copy(rows)

            return musume.nomal_right(rows_data, x1, y1)


def left_move(rows, i):
    num = musume.area_check(rows, i)
    coordinate = musume.split_number(num)

    y1 = coordinate[0]
    x1 = coordinate[1]
    if check_leftside(rows, i) is not None:

        if i == 0:
            rows_data = np.copy(rows)
            y2 = coordinate[2]
            x2 = coordinate[3]
            y3 = coordinate[4]
            x3 = coordinate[5]
            y4 = coordinate[6]
            x4 = coordinate[7]
            return musume.musume_move_left(
                rows_data, x1, y1, x2, y2, x3, y3, x4, y4)

        if (i == 1
            or i == 2
            or i == 3
                or i == 4):
            rows_data = np.copy(rows)
            y2 = coordinate[2]
            x2 = coordinate[3]
            return musume.hight_move_left(rows_data, x1, y1, x2, y2)

        if i == 5:
            rows_data = np.copy(rows)
            y2 = coordinate[2]
            x2 = coordinate[3]
            return musume.wide_move_left(rows_data, x1, y1, x2, y2)

        if (i == 6
            or i == 7
            or i == 8
                or i == 9):
            rows_data = np.copy(rows)
            return musume.nomal_left(rows_data, x1, y1)

# 上に動かせる数字をリスト化


def up_movable_list(rows):
    up_list = []
    for inputnumber in range(10):
        up_movable = check_upside(rows, inputnumber)
        if up_movable is not None:
            up_list.append(up_movable)
    return up_list


def down_movable_list(rows):
    down_list = []
    for inputnumber in range(10):
        down_movable = check_downside(rows, inputnumber)
        if down_movable is not None:
            down_list.append(down_movable)
    return down_list


def right_movable_list(rows):
    right_list = []
    for inputnumber in range(10):
        right_movable = check_rightside(rows, inputnumber)
        if right_movable is not None:
            right_list.append(right_movable)
    return right_list


def left_movable_list(rows):
    left_list = []
    for inputnumber in range(10):
        left_movable = check_leftside(rows, inputnumber)
        if left_movable is not None:
            left_list.append(left_movable)
    return left_list


def move_up(rows):
    rows_list = []
    up_list = up_movable_list(rows)
    for i in up_list:
        n = up_move(rows, i)
        rows_list.append(n)
    return rows_list


def move_down(rows):
    rows_list = []
    down_list = down_movable_list(rows)
    for i in down_list:
        n = down_move(rows, i)
        rows_list.append(n)
    return rows_list


def move_right(rows):
    rows_list = []
    right_list = right_movable_list(rows)
    for i in right_list:
        n = right_move(rows, i)
        rows_list.append(n)
    return rows_list


def move_left(rows):
    rows_list = []
    left_list = left_movable_list(rows)
    for i in left_list:
        n = left_move(rows, i)
        rows_list.append(n)
    return rows_list


def movable_list(rows):
    movable = []
    up = move_up(rows)
    down = move_down(rows)
    right = move_right(rows)
    left = move_left(rows)

    if len(up) == 1:

        movable.append(up[0])

    if len(up) == 2:

        movable.append(up[0])
        movable.append(up[1])

    if len(down) == 1:
        movable.append(down[0])
    if len(down) == 2:
        movable.append(down[0])
        movable.append(down[1])

    if len(right) == 1:
        movable.append(right[0])
    if len(right) == 2:
        movable.append(right[0])
        movable.append(right[1])

    if len(left) == 1:
        movable.append(left[0])
    if len(left) == 2:
        movable.append(left[0])
        movable.append(left[1])

    return movable


def what_mache(simple_bord, board_state):
    for n in board_state:
        if np.array_equal(n, simple_bord):
            return False
        else:
            continue
    return True


def queue_state_append(moved_rows_list, board_state, board_queue):
    for moved_rows in moved_rows_list:
        # ノードを比較しやすい形に変換する
        simple_borad = board_simple(moved_rows)
        # 比較しやすい形にしたノードをboard_state(比較しやすくなったノードを入れてあるところ)
        # のものと比較する
        # 比較して、board_state内にsimple_boardがなければ リストとキューに追加
        if what_mache(simple_borad, board_state):
            print("追加したノード")
            print(moved_rows)
            print(simple_borad)

            board_state.append(simple_borad)
            board_queue.append(moved_rows)
        else:
            continue


def breadth_search(rows):
    n = 0

    # rows is copy
    rows_copy = np.copy(rows)
    # rowsを比較しやすい形にする
    rows_simple = board_simple(rows_copy)
    # board_state に　比較しやすい形のrowsを入れる
    board_state = []
    # board_queue に　変換する前の盤面を入れる
    board_queue = deque()
    # 最初の盤面の変換する前を入れる
    board_queue.append(rows_copy)
    # 最初の盤面の変換した後を入れる
    board_state.append(rows_simple)
    # board_queue が０になるまで実行する

    while len(board_queue) > 0:
        n += 1
        print("始点からの距離", n)

        # rows_nowにboard_queueから取り出したrowsを入れる
        rows_now = board_queue.popleft()
        # moved_rows_listに現在地点から展開できるノードを収納する
        moved_rows_list = movable_list(rows_now)

        # 現在地点から展開できるノード一つ一つが今までに出てきているか確認する
        queue_state_append(moved_rows_list, board_state, board_queue)
    return board_state
