import musume
import numpy as np
from collections import deque
import dfs


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

    return new_rows


def board_simple(rows):
    for i in range(10):
        rows = num_simple(rows, i)
    return rows


def check_upside0_5(rows, inputnumber):
    num = musume.area_check(rows, inputnumber)
    coordinate = musume.split_number(num)
    y1 = coordinate[0]
    x1 = coordinate[1]
    y2 = coordinate[2]
    x2 = coordinate[3]
    if (musume.inrange_and_vacant_check_top(rows, y1, x1) and
            musume.inrange_and_vacant_check_top(rows, y2, x2)):
        return inputnumber
    else:
        return None


def check_upside1_9(rows, inputnumber):
    num = musume.area_check(rows, inputnumber)
    coordinate = musume.split_number(num)
    y1 = coordinate[0]
    x1 = coordinate[1]
    if musume.inrange_and_vacant_check_top(rows, y1, x1):
        return inputnumber
    else:
        return None


def check_upside(rows, inputnumber):
    if (inputnumber == 0
            or inputnumber == 5):
        return check_upside0_5(rows, inputnumber)
    else:
        return check_upside1_9(rows, inputnumber)


def check_downside0(rows, inputnumber):
    num = musume.area_check(rows, inputnumber)
    coordinate = musume.split_number(num)
    y3 = coordinate[4]
    x3 = coordinate[5]
    y4 = coordinate[6]
    x4 = coordinate[7]
    if (musume.inrange_and_vacant_check_down(rows, y3, x3) and
            musume.inrange_and_vacant_check_down(rows, y4, x4)):
        return inputnumber
    else:
        return None


def check_downside5(rows, inputnumber):
    num = musume.area_check(rows, inputnumber)
    coordinate = musume.split_number(num)
    y1 = coordinate[0]
    x1 = coordinate[1]
    y2 = coordinate[2]
    x2 = coordinate[3]
    if (musume.inrange_and_vacant_check_down(rows, y1, x1) and
            musume.inrange_and_vacant_check_down(rows, y2, x2)):
        return inputnumber
    else:
        return None


def check_downside6_9(rows, inputnumber):
    num = musume.area_check(rows, inputnumber)
    coordinate = musume.split_number(num)
    y1 = coordinate[0]
    x1 = coordinate[1]
    if musume.inrange_and_vacant_check_down(rows, y1, x1):
        return inputnumber
    else:
        return None


def check_downside1_4(rows, inputnumber):
    num = musume.area_check(rows, inputnumber)
    coordinate = musume.split_number(num)
    y2 = coordinate[2]
    x2 = coordinate[3]
    if musume.inrange_and_vacant_check_down(rows, y2, x2):
        return inputnumber
    else:
        return None


def check_downside(rows, inputnumber):
    if inputnumber == 5:
        return check_downside5(rows, inputnumber)

    if inputnumber == 0:
        return check_downside0(rows, inputnumber)

    if 5 < inputnumber < 10:
        return check_downside6_9(rows, inputnumber)

    else:
        return check_downside1_4(rows, inputnumber)


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
        if (musume.inrange_and_vacant_check_right(rows, y2, x2) and
                musume.inrange_and_vacant_check_right(rows, y4, x4)):
            return inputnumber
        else:
            return None

    if 0 < inputnumber < 5:
        y2 = coordinate[2]
        x2 = coordinate[3]
        if (musume.inrange_and_vacant_check_right(rows, y1, x1) and
                musume.inrange_and_vacant_check_right(rows, y2, x2)):
            return inputnumber
        else:
            return None

    if inputnumber == 5:
        y2 = coordinate[2]
        x2 = coordinate[3]
        if musume.inrange_and_vacant_check_right(rows, y2, x2):
            return inputnumber
        else:
            return None

    else:
        if musume.inrange_and_vacant_check_right(rows, y1, x1):
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
        if (musume.inrange_and_vacant_check_left(rows, y1, x1) and
                musume.inrange_and_vacant_check_left(rows, y3, x3)):
            return inputnumber
        else:
            return None
    if 0 < inputnumber < 5:
        y2 = coordinate[2]
        x2 = coordinate[3]
        if (musume.inrange_and_vacant_check_left(rows, y1, x1) and
                musume.inrange_and_vacant_check_left(rows, y2, x2)):
            return inputnumber
        else:
            return None
    else:
        if musume.inrange_and_vacant_check_left(rows, y1, x1):
            return inputnumber
        else:
            return None


# 動かせる数字をリスト化


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


def move_board_up(rows, i):
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
            return musume.move_2x2_to_top(
                rows_data,
                y1, x1, y2, x2, y3, x3, y4, x4)

        if (i == 1
            or i == 2
            or i == 3
                or i == 4):
            rows_data = np.copy(rows)
            y2 = coordinate[2]
            x2 = coordinate[3]
            return musume.move_2x1_to_top(rows_data, y1, x1, y2, x2)

        if i == 5:
            rows_data = np.copy(rows)
            y2 = coordinate[2]
            x2 = coordinate[3]
            return musume.move_1x2_to_top(rows_data, y1, x1, y2, x2)

        if (i == 6
            or i == 7
            or i == 8
                or i == 9):
            rows_data = np.copy(rows)
            return musume.move_1x1_to_top(rows_data, y1, x1)


def move_board_down(rows, i):
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
            return musume.move_2x2_to_down(
                rows_data, y1, x1, y2, x2, y3, x3, y4, x4)

        if (i == 1
            or i == 2
            or i == 3
                or i == 4):
            rows_data = np.copy(rows)
            y2 = coordinate[2]
            x2 = coordinate[3]
            return musume.move_2x1_to_down(rows_data, y1, x1, y2, x2)

        if i == 5:
            rows_data = np.copy(rows)
            y2 = coordinate[2]
            x2 = coordinate[3]
            return musume.move_1x2_to_down(rows_data, y1, x1, y2, x2)

        if (i == 6
            or i == 7
            or i == 8
                or i == 9):
            rows_data = np.copy(rows)
            return musume.move_1x1_to_down(rows_data, y1, x1)


def move_board_right(rows, i):
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
            return musume.move_2x2_to_right(
                rows_data, y1, x1, y2, x2, y3, x3, y4, x4)

        if (i == 1
            or i == 2
            or i == 3
                or i == 4):
            rows_data = np.copy(rows)
            y2 = coordinate[2]
            x2 = coordinate[3]
            return musume.move_2x1_to_right(rows_data, y1, x1, y2, x2)

        if i == 5:
            rows_data = np.copy(rows)
            y2 = coordinate[2]
            x2 = coordinate[3]
            return musume.move_1x2_to_right(rows_data, y1, x1, y2, x2)

        if (i == 6
            or i == 7
            or i == 8
                or i == 9):
            rows_data = np.copy(rows)

            return musume.move_1x1_to_right(rows_data, y1, x1)


def move_board_left(rows, i):
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
            return musume.move_2x2_to_left(
                rows_data, y1, x1, y2, x2, y3, x3, y4, x4)

        if (i == 1
            or i == 2
            or i == 3
                or i == 4):
            rows_data = np.copy(rows)
            y2 = coordinate[2]
            x2 = coordinate[3]
            return musume.move_2x1_to_left(rows_data, y1, x1, y2, x2)

        if i == 5:
            rows_data = np.copy(rows)
            y2 = coordinate[2]
            x2 = coordinate[3]
            return musume.move_1x2_to_left(rows_data, y1, x1, y2, x2)

        if (i == 6
            or i == 7
            or i == 8
                or i == 9):
            rows_data = np.copy(rows)
            return musume.move_1x1_to_left(rows_data, y1, x1)


def move_up(rows):
    rows_list = []
    up_list = up_movable_list(rows)
    for i in up_list:
        n = move_board_up(rows, i)
        rows_list.append(n)
    return rows_list


def move_down(rows):
    rows_list = []
    down_list = down_movable_list(rows)
    for i in down_list:
        n = move_board_down(rows, i)
        rows_list.append(n)
    return rows_list


def move_right(rows):
    rows_list = []
    right_list = right_movable_list(rows)
    for i in right_list:
        n = move_board_right(rows, i)
        rows_list.append(n)
    return rows_list


def move_left(rows):
    rows_list = []
    left_list = left_movable_list(rows)
    for i in left_list:
        n = move_board_left(rows, i)
        rows_list.append(n)
    return rows_list


def moved_board_list(rows):
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


def what_mache(simpled_bored, board_state):
    for n in board_state:
        if np.all(n == simpled_bored):

            return False
        else:
            continue
    return True


def queue_state_append(moved_rows_list, board_state,
                       board_queue, rows_now, the_one_before):

    for moved_rows in moved_rows_list:

        simpled_borad = board_simple(moved_rows)
        hash_board = dfs.to_hashable(simpled_borad)
        if hash_board not in board_state:
            the_one_before.append((rows_now, moved_rows))
            board_state.add(hash_board)
            board_queue.append(moved_rows)


def breadth_search(rows):
    # rows is copy
    rows_copy = np.copy(rows)
    the_one_before = []
    # rowsを比較しやすい形にする
    rows_simple = board_simple(rows_copy)
    # board_state に　比較しやすい形のrowsを入れる
    board_state = set()
    # board_queue に　変換する前の盤面を入れる
    board_queue = deque()
    # 最初の盤面の変換する前を入れる
    board_queue.append(rows_copy)
    # 最初の盤面の変換した後を入れる)
    board_state.add(dfs.to_hashable(rows_simple))
    # board_queue が０になるまで実行する
    n = 1

    while len(board_queue) > 0:
        n += 1
        print(n)
        # rows_nowにboard_queueから取り出したrowsを入れる
        rows_now = board_queue.popleft()
        # moved_rows_listに現在地点から展開できるノードを収納する
        moved_rows_list = moved_board_list(rows_now)

        # 現在地点から展開できるノード一つ一つが今までに出てきているか確認する
        queue_state_append(moved_rows_list, board_state,
                           board_queue, rows_now, the_one_before)

    return board_state, the_one_before
