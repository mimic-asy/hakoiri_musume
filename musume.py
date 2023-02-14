import numpy as np


def swap(rows, y1, x1, y2, x2):
    rows[y1, x1], rows[y2, x2] = rows[y2, x2], rows[y1, x1]

    return rows


# rowsを定義する関数


def init_puzzle():
    Musume = 0
    Sohu = 1
    Sobo = 2
    Chichi = 3
    Haha = 4
    Kyodai = 5
    Sado = 6
    Syodo = 7
    Kado = 8
    Budo = 9
    Vacant = -1

    rows = np.array(
        [
            [Sohu, Musume, Musume, Sobo],
            [Sohu, Musume, Musume, Sobo],
            [Chichi, Kyodai, Kyodai, Haha],
            [Chichi, Sado, Syodo, Haha],
            [Kado, Vacant, Vacant, Budo],
        ]
    )

    return rows


def area_check(rows, val):
    assert -1 <= val <= 9

    yaxis, xaxis = np.where(rows == val)
    return [(y, x) for y, x in zip(yaxis, xaxis)]


def split_number(num):

    first = 0
    coordinate = []
    x = len(num)

    for i in range(x):
        xy_soordnate = num[first]
        a, b = xy_soordnate
        first += 1
        coordinate.append(a)
        coordinate.append(b)
    return coordinate


def inrange_check_right(x):
    return x + 1 <= 3


def inrange_check_left(x):
    return x - 1 > -1


def inrange_check_top(y):
    return y - 1 > -1


def inrange_check_down(y):
    return y + 1 < 5


def vacant_check_right(rows, y1, x1):
    return rows[y1, x1 + 1] == -1


def vacant_check_left(rows, y1, x1):
    return rows[y1, x1 - 1] == -1


def vacant_check_top(rows, y1, x1):
    return rows[y1 - 1, x1] == -1


def vacant_check_down(rows, y1, x1):
    return rows[y1 + 1, x1] == -1


def move_1x1_to_left(rows, y1, x1):
    rows_copy = np.copy(rows)
    return swap(rows_copy, y1, x1, y1, x1 - 1)


def move_1x1_to_right(rows, y1, x1):
    rows_copy = np.copy(rows)
    return swap(rows_copy, y1, x1, y1, x1 + 1)


def move_1x1_to_top(rows, y1, x1):
    rows_copy = np.copy(rows)
    return swap(rows_copy, y1, x1, y1 - 1, x1)


def move_1x1_to_down(rows, y1, x1):
    rows_copy = np.copy(rows)
    return swap(rows_copy, y1, x1, y1 + 1, x1)


# 1*2のマスを動かす関数(テスト済み)
def move_2x1_to_right(rows, y1, x1, y2, x2):
    rows_copy = np.copy(rows)
    rows_copy = swap(rows_copy, y1, x1, y1, x1 + 1)
    rows_copy = swap(rows_copy, y2, x2, y2, x2 + 1)
    return rows_copy


def move_2x1_to_left(rows, y1, x1, y2, x2):
    rows_copy = np.copy(rows)
    rows_copy = swap(rows_copy, y1, x1, y1, x1 - 1)
    rows_copy = swap(rows_copy, y2, x2, y2, x2 - 1)
    return rows_copy


def move_2x1_to_top(rows, y1, x1, y2, x2):
    rows_copy = np.copy(rows)
    rows_copy = swap(rows_copy, y1, x1, y1 - 1, x1)
    rows_copy = swap(rows_copy, y2, x2, y2 - 1, x2)
    return rows_copy


def move_2x1_to_down(rows, y1, x1, y2, x2):
    rows_copy = np.copy(rows)
    rows_copy = swap(rows_copy, y2, x2, y2 + 1, x2)
    rows_copy = swap(rows_copy, y1, x1, y1 + 1, x1)
    return rows_copy


# 2*1のマスを動かす関数
def move_1x2_to_left(rows, y1, x1, y2, x2):
    rows_copy = np.copy(rows)
    rows_copy = swap(rows_copy, y1, x1, y1, x1 - 1)
    rows_copy = swap(rows_copy, y2, x2, y2, x2 - 1)
    return rows_copy


def move_1x2_to_right(rows, y1, x1, y2, x2):
    rows_copy = np.copy(rows)
    rows_copy = swap(rows_copy, y2, x2, y2, x2 + 1)
    rows_copy = swap(rows_copy, y1, x1, y1, x1 + 1)

    return rows_copy


def move_1x2_to_top(rows, y1, x1, y2, x2):
    rows_copy = np.copy(rows)
    rows_copy = swap(rows_copy, y1, x1, y1 - 1, x1)
    rows_copy = swap(rows_copy, y2, x2, y2 - 1, x2)
    return rows_copy


def move_1x2_to_down(rows, y1, x1, y2, x2):
    rows_copy = np.copy(rows)
    rows_copy = swap(rows_copy, y1, x1, y1 + 1, x1)
    rows_copy = swap(rows_copy, y2, x2, y2 + 1, x2)
    return rows_copy


# 2*2のマスを動かす関数
def move_2x2_to_right(rows, y1, x1, y2, x2, y3, x3, y4, x4):
    rows_copy = np.copy(rows)
    rows_copy = swap(rows_copy, y2, x2, y2, x2 + 1)
    rows_copy = swap(rows_copy, y4, x4, y4, x4 + 1)
    rows_copy = swap(rows_copy, y1, x1, y1, x1 + 1)
    rows_copy = swap(rows_copy, y3, x3, y3, x3 + 1)
    return rows_copy


def move_2x2_to_left(rows, y1, x1, y2, x2, y3, x3, y4, x4):
    rows_copy = np.copy(rows)
    rows_copy = swap(rows_copy, y1, x1, y1, x1 - 1)
    rows_copy = swap(rows_copy, y3, x3, y3, x3 - 1)
    rows_copy = swap(rows_copy, y2, x2, y2, x2 - 1)
    rows_copy = swap(rows_copy, y4, x4, y4, x4 - 1)
    return rows_copy


def move_2x2_to_top(rows, y1, x1, y2, x2, y3, x3, y4, x4):
    rows_copy = np.copy(rows)
    rows_copy = swap(rows_copy, y1, x1, y1 - 1, x1)
    rows_copy = swap(rows_copy, y2, x2, y2 - 1, x2)
    rows_copy = swap(rows_copy, y3, x3, y3 - 1, x3)
    rows_copy = swap(rows_copy, y4, x4, y4 - 1, x4)
    return rows_copy


def move_2x2_to_down(rows, y1, x1, y2, x2, y3, x3, y4, x4):
    rows_copy = np.copy(rows)
    rows_copy = swap(rows_copy, y4, x4, y4 + 1, x4)
    rows_copy = swap(rows_copy, y2, x2, y2 + 1, x2)
    rows_copy = swap(rows_copy, y3, x3, y3 + 1, x3)
    rows_copy = swap(rows_copy, y1, x1, y1 + 1, x1)
    return rows_copy


def inrange_and_vacant_check_top(rows, y1, x1):
    if (inrange_check_top(y1)
            and vacant_check_top(rows, y1, x1)):
        return True
    else:
        return False


def inrange_and_vacant_check_down(rows, y1, x1):
    if (inrange_check_down(y1)
            and vacant_check_down(rows, y1, x1)):
        return True
    else:
        return False


def inrange_and_vacant_check_left(rows, y1, x1):
    if (inrange_check_left(x1)
            and vacant_check_left(rows, y1, x1)):
        return True
    else:
        return False


def inrange_and_vacant_check_right(rows, y1, x1):
    if (inrange_check_right(x1)
            and vacant_check_right(rows, y1, x1)):
        return True
    else:
        return False


def clear(moved_rows):
    if (moved_rows[4, 1] == 0 and moved_rows[4, 2] == 0):
        return True


def saitankai(the_one_before):
    shortest = []
    for i in the_one_before:
        print(i[1])
        node = i[1]
        shortest.append(node)
    return shortest


def num_simple(rows, i):
    new_rows = np.copy(rows)

    num = area_check(rows, i)

    before = split_number(num)

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
    num = area_check(rows, inputnumber)
    coordinate = split_number(num)
    y1 = coordinate[0]
    x1 = coordinate[1]
    y2 = coordinate[2]
    x2 = coordinate[3]
    if (inrange_and_vacant_check_top(rows, y1, x1) and
            inrange_and_vacant_check_top(rows, y2, x2)):
        return inputnumber
    else:
        return None


def check_upside1_9(rows, inputnumber):
    num = area_check(rows, inputnumber)
    coordinate = split_number(num)
    y1 = coordinate[0]
    x1 = coordinate[1]
    if inrange_and_vacant_check_top(rows, y1, x1):
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
    num = area_check(rows, inputnumber)
    coordinate = split_number(num)
    y3 = coordinate[4]
    x3 = coordinate[5]
    y4 = coordinate[6]
    x4 = coordinate[7]
    if (inrange_and_vacant_check_down(rows, y3, x3) and
            inrange_and_vacant_check_down(rows, y4, x4)):
        return inputnumber
    else:
        return None


def check_downside5(rows, inputnumber):
    num = area_check(rows, inputnumber)
    coordinate = split_number(num)
    y1 = coordinate[0]
    x1 = coordinate[1]
    y2 = coordinate[2]
    x2 = coordinate[3]
    if (inrange_and_vacant_check_down(rows, y1, x1) and
            inrange_and_vacant_check_down(rows, y2, x2)):
        return inputnumber
    else:
        return None


def check_downside6_9(rows, inputnumber):
    num = area_check(rows, inputnumber)
    coordinate = split_number(num)
    y1 = coordinate[0]
    x1 = coordinate[1]
    if inrange_and_vacant_check_down(rows, y1, x1):
        return inputnumber
    else:
        return None


def check_downside1_4(rows, inputnumber):
    num = area_check(rows, inputnumber)
    coordinate = split_number(num)
    y2 = coordinate[2]
    x2 = coordinate[3]
    if inrange_and_vacant_check_down(rows, y2, x2):
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
    num = area_check(rows, inputnumber)
    coordinate = split_number(num)
    y1 = coordinate[0]
    x1 = coordinate[1]

    if inputnumber == 0:
        y2 = coordinate[2]
        x2 = coordinate[3]
        y4 = coordinate[6]
        x4 = coordinate[7]
        if (inrange_and_vacant_check_right(rows, y2, x2) and
                inrange_and_vacant_check_right(rows, y4, x4)):
            return inputnumber
        else:
            return None

    if 0 < inputnumber < 5:
        y2 = coordinate[2]
        x2 = coordinate[3]
        if (inrange_and_vacant_check_right(rows, y1, x1) and
                inrange_and_vacant_check_right(rows, y2, x2)):
            return inputnumber
        else:
            return None

    if inputnumber == 5:
        y2 = coordinate[2]
        x2 = coordinate[3]
        if inrange_and_vacant_check_right(rows, y2, x2):
            return inputnumber
        else:
            return None

    else:
        if inrange_and_vacant_check_right(rows, y1, x1):
            return inputnumber
        else:
            return None


def check_leftside(rows, inputnumber):
    num = area_check(rows, inputnumber)
    coordinate = split_number(num)
    y1 = coordinate[0]
    x1 = coordinate[1]
    if inputnumber == 0:
        y3 = coordinate[4]
        x3 = coordinate[5]
        if (inrange_and_vacant_check_left(rows, y1, x1) and
                inrange_and_vacant_check_left(rows, y3, x3)):
            return inputnumber
        else:
            return None
    if 0 < inputnumber < 5:
        y2 = coordinate[2]
        x2 = coordinate[3]
        if (inrange_and_vacant_check_left(rows, y1, x1) and
                inrange_and_vacant_check_left(rows, y2, x2)):
            return inputnumber
        else:
            return None
    else:
        if inrange_and_vacant_check_left(rows, y1, x1):
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
    num = area_check(rows, i)
    coordinate = split_number(num)

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
            return move_2x2_to_top(
                rows_data,
                y1, x1, y2, x2, y3, x3, y4, x4)

        if (i == 1
            or i == 2
            or i == 3
                or i == 4):
            rows_data = np.copy(rows)
            y2 = coordinate[2]
            x2 = coordinate[3]
            return move_2x1_to_top(rows_data, y1, x1, y2, x2)

        if i == 5:
            rows_data = np.copy(rows)
            y2 = coordinate[2]
            x2 = coordinate[3]
            return move_1x2_to_top(rows_data, y1, x1, y2, x2)

        if (i == 6
            or i == 7
            or i == 8
                or i == 9):
            rows_data = np.copy(rows)
            return move_1x1_to_top(rows_data, y1, x1)


def move_board_down(rows, i):
    num = area_check(rows, i)
    coordinate = split_number(num)

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
            return move_2x2_to_down(
                rows_data, y1, x1, y2, x2, y3, x3, y4, x4)

        if (i == 1
            or i == 2
            or i == 3
                or i == 4):
            rows_data = np.copy(rows)
            y2 = coordinate[2]
            x2 = coordinate[3]
            return move_2x1_to_down(rows_data, y1, x1, y2, x2)

        if i == 5:
            rows_data = np.copy(rows)
            y2 = coordinate[2]
            x2 = coordinate[3]
            return move_1x2_to_down(rows_data, y1, x1, y2, x2)

        if (i == 6
            or i == 7
            or i == 8
                or i == 9):
            rows_data = np.copy(rows)
            return move_1x1_to_down(rows_data, y1, x1)


def move_board_right(rows, i):
    num = area_check(rows, i)
    coordinate = split_number(num)
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
            return move_2x2_to_right(
                rows_data, y1, x1, y2, x2, y3, x3, y4, x4)

        if (i == 1
            or i == 2
            or i == 3
                or i == 4):
            rows_data = np.copy(rows)
            y2 = coordinate[2]
            x2 = coordinate[3]
            return move_2x1_to_right(rows_data, y1, x1, y2, x2)

        if i == 5:
            rows_data = np.copy(rows)
            y2 = coordinate[2]
            x2 = coordinate[3]
            return move_1x2_to_right(rows_data, y1, x1, y2, x2)

        if (i == 6
            or i == 7
            or i == 8
                or i == 9):
            rows_data = np.copy(rows)

            return move_1x1_to_right(rows_data, y1, x1)


def move_board_left(rows, i):
    num = area_check(rows, i)
    coordinate = split_number(num)

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
            return move_2x2_to_left(
                rows_data, y1, x1, y2, x2, y3, x3, y4, x4)

        if (i == 1
            or i == 2
            or i == 3
                or i == 4):
            rows_data = np.copy(rows)
            y2 = coordinate[2]
            x2 = coordinate[3]
            return move_2x1_to_left(rows_data, y1, x1, y2, x2)

        if i == 5:
            rows_data = np.copy(rows)
            y2 = coordinate[2]
            x2 = coordinate[3]
            return move_1x2_to_left(rows_data, y1, x1, y2, x2)

        if (i == 6
            or i == 7
            or i == 8
                or i == 9):
            rows_data = np.copy(rows)
            return move_1x1_to_left(rows_data, y1, x1)


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
                       board_queue, rows_now, the_one_before,
                       clear_route):

    for moved_rows in moved_rows_list:

        simpled_borad = board_simple(moved_rows)
        hash_board = to_hashable(simpled_borad)
        if hash_board not in board_state:
            the_one_before.append((rows_now, moved_rows))
            board_state.add(hash_board)
            board_queue.append(moved_rows)
            if clear(moved_rows):
                clear_route.append(route(the_one_before, moved_rows))


def route(the_one_before, moved_rows):
    new = moved_rows
    one_route = []
    one_route.append(new)
    while len(the_one_before):
        for mn in reversed(the_one_before):
            if np.all(mn[1] == new):
                one_route.append(mn[0])
                new = mn[0]
        return one_route


def to_hashable(array):
    x = array.flatten()
    return ''.join(map(lambda i: chr(66-i), x))


def shortest_path(clear_route):
    len_all = []
    for i in clear_route:
        length = len(i)
        len_all.append(length)

    x = len_all.index(min(len_all))
    print("最短手順は")
    print(clear_route[x])
    print("となります")
    print("最短手は", min(len_all), "手です")
