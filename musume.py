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


# 数字を選ぶ関数
# 入力された数字が使用可能か判断する関数
def swap_check(rows):
    print(rows)
    number = input("動かしたい数字を入力してね")
    val = int(number)
    if -1 < val < 10:
        return val

    if val == 99:
        return val
    else:
        print("０から９までの数字を入力してね")
        return None
    assert False


# 選択した数字はどこにあるかどうかを調べる。


def area_check(rows, val):
    yaxis, xaxis = np.where(rows == val)
    return [(y, x) for y, x in zip(yaxis, xaxis)]


# 取得した座標をintに置き換える
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


# 範囲内か調べる関数（テスト済み）
def right_check(x):
    # 右側が範囲内であることを示す
    if x + 1 <= 3:
        return True
    else:
        return False


def left_check(x):
    # 左側が範囲内であることを示す
    if x - 1 > -1:
        return True
    else:
        return False


def top_check(y):
    # 上が範囲内であることを示す
    if y - 1 > -1:
        return True
    else:
        return False


def down_check(y):
    # 下側が範囲内であることを示す
    if y + 1 < 5:
        return True
    else:
        return False


# 隣が−１か調べる関数(テスト済み)
def vacant_check_right(rows, x1, y1):
    if rows[y1, x1 + 1] == -1:
        return True
    else:
        return False


def vacant_check_left(rows, x1, y1):
    if rows[y1, x1 - 1] == -1:
        return True
    else:
        return False


def vacant_check_top(rows, x1, y1):
    if rows[y1 - 1, x1] == -1:
        return True
    else:
        return False


def vacant_check_down(rows, x1, y1):
    if rows[y1 + 1, x1] == -1:
        return True
    else:
        return False


def nomal_left(rows, x1, y1):
    rows = swap(rows, y1, x1, y1, x1 - 1)
    return rows


def nomal_right(rows, x1, y1):
    rows = swap(rows, y1, x1, y1, x1 + 1)
    return rows


def nomal_top(rows, x1, y1):
    rows = swap(rows, y1, x1, y1 - 1, x1)
    return rows


def nomal_down(rows, x1, y1):
    rows = swap(rows, y1, x1, y1 + 1, x1)
    return rows


def nomal_swap(rows, x1, y1):

    if (
        left_check(x1)
        and vacant_check_left(rows, x1, y1)
        and top_check(y1)
        and vacant_check_top(rows, x1, y1)
    ):
        a = input("left or top")
        while a == "left" or a == "top":
            if a == "left":
                return nomal_left(rows, x1, y1)
            if a == "top":
                return nomal_top(rows, x1, y1)
            else:
                print("もう一度選んでね")
                continue

    if (
        left_check(x1)
        and vacant_check_left(rows, x1, y1)
        and down_check(y1)
        and vacant_check_down(rows, x1, y1)
    ):
        a = input("left or down")
        while a == "left" or a == "down":
            if a == "left":
                return nomal_left(rows, x1, y1)
            if a == "down":
                return nomal_down(rows, x1, y1)
            else:
                print("もう一度選んでね")
                continue

    if (
        left_check(x1)
        and vacant_check_left(rows, x1, y1)
        and right_check(x1)
        and vacant_check_right(rows, x1, y1)
    ):
        a = input("left or right")
        while a == "left" or a == "right":
            if a == "left":
                return nomal_left(rows, x1, y1)
            if a == "right":
                return nomal_right(rows, x1, y1)
            else:
                print("もう一度選んでね")
                continue

    if (
        right_check(x1)
        and vacant_check_right(rows, x1, y1)
        and vacant_check_top(rows, x1, y1)
        and top_check(y1)
    ):
        a = input("right or top")
        while a == "right" or a == "top":
            if a == "right":
                return nomal_right(rows, x1, y1)
            if a == "top":
                return nomal_top(rows, x1, y1)
            else:
                print("もう一度選んでね")
                continue

    if (
        right_check(x1)
        and vacant_check_right(rows, x1, y1)
        and down_check(y1)
        and vacant_check_down(rows, x1, y1)
    ):
        a = input("right or down")
        while a == "right" or a == "down":
            if a == "right":
                return nomal_right(rows, x1, y1)
            if a == "down":
                return nomal_down(rows, x1, y1)
            else:
                print("もう一度選んでね")
                continue

    if (
        top_check(y1)
        and vacant_check_top(rows, x1, y1)
        and down_check(y1)
        and vacant_check_down(rows, x1, y1)
    ):
        a = input("down or top?")
        while a == "top" or a == "down":
            if a == "top":
                return nomal_top(rows, x1, y1)
            if a == "down":
                return nomal_down(rows, x1, y1)
            else:
                print("もう一度選んでね")
                continue

    if left_check(x1) and vacant_check_left(rows, x1, y1):
        return nomal_left(rows, x1, y1)

    if right_check(x1) and vacant_check_right(rows, x1, y1):
        return nomal_right(rows, x1, y1)

    if top_check(y1) and vacant_check_top(rows, x1, y1):
        return nomal_top(rows, x1, y1)
    if down_check(y1) and vacant_check_down(rows, x1, y1):
        return nomal_down(rows, x1, y1)
    else:
        print("この数字は動かせません")


# 1*2のマスを動かす関数(テスト済み)
def hight_move_right(rows, x1, y1, x2, y2):
    rows = swap(rows, y1, x1, y1, x1 + 1)
    rows = swap(rows, y2, x2, y2, x2 + 1)
    return rows


def hight_move_left(rows, x1, y1, x2, y2):
    rows = swap(rows, y1, x1, y1, x1 - 1)
    rows = swap(rows, y2, x2, y2, x2 - 1)
    return rows


def hight_move_top(rows, x1, y1, x2, y2):
    rows = swap(rows, y1, x1, y1 - 1, x1)
    rows = swap(rows, y2, x2, y2 - 1, x2)
    return rows


def hight_move_down(rows, x1, y1, x2, y2):
    rows = swap(rows, y2, x2, y2 + 1, x2)
    rows = swap(rows, y1, x1, y1 + 1, x1)
    return rows


def hight_move(rows, x1, y1, x2, y2):
    if (
        top_check(y1)
        and down_check(y2)
        and vacant_check_top(rows, x1, y1)
        and vacant_check_down(rows, x2, y2)
    ):
        responce = input("top or down? = ")
        while responce == "top" or responce == "down":
            if responce == "top":
                return hight_move_top(rows, x1, y1, x2, y2)
            if responce == "down":
                return hight_move_down(rows, x1, y1, x2, y2)

    if (
        right_check(x1)
        and vacant_check_right(rows, x1, y1)
        and vacant_check_right(rows, x2, y2)
    ):
        return hight_move_right(rows, x1, y1, x2, y2)

    if (
        left_check(x1)
        and vacant_check_left(rows, x1, y1)
        and vacant_check_left(rows, x2, y2)
    ):
        return hight_move_left(rows, x1, y1, x2, y2)

    if top_check(y1) and vacant_check_top(rows, x1, y1):
        return hight_move_top(rows, x1, y1, x2, y2)

    if down_check(y2) and vacant_check_down(rows, x2, y2):
        return hight_move_down(rows, x1, y1, x2, y2)

    else:
        print("この数字は動かせません、動かせる数字を選んでください")
        return None


# 2*1のマスを動かす関数
def wide_move_left(rows, x1, y1, x2, y2):
    rows = swap(rows, y1, x1, y1, x1 - 1)
    rows = swap(rows, y2, x2, y2, x2 - 1)
    return rows


def wide_move_right(rows, x1, y1, x2, y2):

    rows = swap(rows, y2, x2, y2, x2 + 1)
    rows = swap(rows, y1, x1, y1, x1 + 1)

    return rows


def wide_move_top(rows, x1, y1, x2, y2):
    rows = swap(rows, y1, x1, y1 - 1, x1)
    rows = swap(rows, y2, x2, y2 - 1, x2)
    return rows


def wide_move_down(rows, x1, y1, x2, y2):
    rows = swap(rows, y1, x1, y1 + 1, x1)
    rows = swap(rows, y2, x2, y2 + 1, x2)
    return rows


def wide_move(rows, x1, y1, x2, y2):
    if (
        top_check(y1)
        and vacant_check_top(rows, x1, y1)
        and vacant_check_top(rows, x2, y2)
    ):
        return wide_move_top(rows, x1, y1, x2, y2)

    if (
        down_check(y1)
        and vacant_check_down(rows, x1, y1)
        and vacant_check_down(rows, x2, y2)
    ):
        return wide_move_down(rows, x1, y1, x2, y2)

    if right_check(x2) and vacant_check_right(rows, x2, y2):

        return wide_move_right(rows, x1, y1, x2, y2)

    if left_check(x1) and vacant_check_left(rows, x1, y1):
        return wide_move_left(rows, x1, y1, x2, y2)
    else:
        print("この数字は動かせません、他の数字を選んでほしいぞい")


# 2*2のマスを動かす関数
def musume_move_right(rows, x1, y1, x2, y2, x3, y3, x4, y4):
    rows = swap(rows, y2, x2, y2, x2 + 1)
    rows = swap(rows, y4, x4, y4, x4 + 1)
    rows = swap(rows, y1, x1, y1, x1 + 1)
    rows = swap(rows, y3, x3, y3, x3 + 1)
    return rows


def musume_move_left(rows, x1, y1, x2, y2, x3, y3, x4, y4):
    rows = swap(rows, y1, x1, y1, x1 - 1)
    rows = swap(rows, y3, x3, y3, x3 - 1)
    rows = swap(rows, y2, x2, y2, x2 - 1)
    rows = swap(rows, y4, x4, y4, x4 - 1)
    return rows


def musume_move_top(rows, x1, y1, x2, y2, x3, y3, x4, y4):
    rows = swap(rows, y1, x1, y1 - 1, x1)
    rows = swap(rows, y2, x2, y2 - 1, x2)
    rows = swap(rows, y3, x3, y3 - 1, x3)
    rows = swap(rows, y4, x4, y4 - 1, x4)
    return rows


def musume_move_downswap(rows, x1, y1, x2, y2, x3, y3, x4, y4):
    rows = swap(rows, y4, x4, y4 + 1, x4)
    rows = swap(rows, y2, x2, y2 + 1, x2)
    rows = swap(rows, y3, x3, y3 + 1, x3)
    rows = swap(rows, y1, x1, y1 + 1, x1)
    return rows


def musume_swap(rows, x1, y1, x2, y2, x3, y3, x4, y4):
    if (
        right_check(x1)
        and vacant_check_right(rows, x2, y2)
        and vacant_check_right(rows, x4, y4)
    ):
        rows = musume_move_right(rows, x1, y1, x2, y2, x3, y3, x4, y4)

    if (
        left_check(x1)
        and vacant_check_left(rows, x1, y1)
        and vacant_check_left(rows, x3, y3)
    ):
        rows = musume_move_left(rows, x1, y1, x2, y2, x3, y3, x4, y4)

    if (
        top_check(y1)
        and vacant_check_top(rows, x1, y1)
        and vacant_check_top(rows, x2, y2)
    ):
        rows = musume_move_top(rows, x1, y1, x2, y2, x3, y3, x4, y4)

    if (
        down_check(y3)
        and vacant_check_down(rows, x3, y3)
        and vacant_check_down(rows, x4, y4)
    ):
        rows = musume_move_downswap(rows, x1, y1, x2, y2, x3, y3, x4, y4)


def clear(rows):
    if rows[4, 1] == 0 and rows[4, 2] == 0:
        print("puzzle clear!")
        return True
    else:
        return False
