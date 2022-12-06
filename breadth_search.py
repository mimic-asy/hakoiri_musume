# 現在の位置から移動できる数字を補足する
# 移動できる数字を動かして
# deque内の数字を全て動かす
# 存在する盤面を調べる
# グラフ醸造を作る
#
import musume


# rowsを比較できるようにシンプルにするための関数
def num_simple(rows, change_num):
    num = musume.area_check(rows, change_num)
    before = musume.split_number(num)
    if 0 < change_num < 5:
        rows[before[0], before[1]] = 4
        rows[before[2], before[3]] = 4
        return rows
    if 5 < change_num:
        rows[before[0], before[1]] = 6
        return rows
    else:
        return rows


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

    if (inputnumber == 0
            or inputnumber == 5):
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
        y2 = coordinate[2]
        x2 = coordinate[3]
        if musume.basic_top(rows, x2, y2):
            return inputnumber
        else:
            return None


def check_downside(rows, inputnumber):
    num = musume.area_check(rows, inputnumber)
    coordinate = musume.split_number(num)
    y1 = coordinate[0]
    x1 = coordinate[1]

    if (inputnumber == 0
            or inputnumber == 5):
        y2 = coordinate[2]
        x2 = coordinate[3]
        if musume.doble_basic_down(rows, x1, y1, x2, y2):
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

    if (-1 < inputnumber < 5
            or inputnumber == 0):
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

    if (-1 < inputnumber < 5
            or inputnumber == 0):
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


"""""
def breadth_search(rows):
    board_state = []
    board_queue = deque()
    board_queue.append(rows)
    while len(board_queue) > 0:
        rows = board_queue.popleft()
        movable_list = can_movable_number(rows)
        for rows_data in movable_list:
            comparison = board_simple(rows_data)
            if #boad_stateの中にcomparisionと同じ盤面がない
                board_state.append(comparison)
                board_queue.append(rows_data)

    return board_state """
