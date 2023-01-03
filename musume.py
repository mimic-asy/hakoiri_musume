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
