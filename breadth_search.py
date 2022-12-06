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

# 動かしてrowsを返す関数、動かせない（noneを渡されている）場合はそのままNoneを返すよ


def auto_move_upside(rows, inputnumber):
    num = musume.area_check(rows, inputnumber)
    coordinate = musume.split_number(num)
    y1 = coordinate[0]
    x1 = coordinate[1]
    up_num = check_upside(rows, inputnumber)
    if up_num == 0:
        y2 = coordinate[2]
        x2 = coordinate[3]
        y3 = coordinate[4]
        x3 = coordinate[5]
        y4 = coordinate[6]
        x4 = coordinate[7]
        return musume.musume_move_top(rows, x1, y1, x2, y2, x3, y3, x4, y4)
    if (up_num == 1
        or up_num == 2
        or up_num == 3
            or up_num == 4):
        y2 = coordinate[2]
        x2 = coordinate[3]
        return musume.hight_move_top(rows, x1, y1, x2, y2)
    if check_upside(rows, inputnumber) == 5:
        y2 = coordinate[2]
        x2 = coordinate[3]
        return musume.wide_move_top(rows, x1, y1, x2, y2)
    if (up_num == 6
        or up_num == 7
        or up_num == 8
            or up_num == 9):
        return musume.nomal_top(rows, x1, y1)
    else:
        return None


def auto_move_downside(rows, inputnumber):
    num = musume.area_check(rows, inputnumber)
    coordinate = musume.split_number(num)
    y1 = coordinate[0]
    x1 = coordinate[1]
    down_num = check_downside(rows, inputnumber)
    if down_num == 0:
        y2 = coordinate[2]
        x2 = coordinate[3]
        y3 = coordinate[4]
        x3 = coordinate[5]
        y4 = coordinate[6]
        x4 = coordinate[7]
        r = musume.musume_move_downswap(rows, x1, y1, x2, y2, x3, y3, x4, y4)
        return r
    if (down_num == 1
        or down_num == 2
        or down_num == 3
            or down_num == 4):
        y2 = coordinate[2]
        x2 = coordinate[3]
        return musume.hight_move_down(rows, x1, y1, x2, y2)
    if down_num == 5:
        y2 = coordinate[2]
        x2 = coordinate[3]
        return musume.wide_move_down(rows, x1, y1, x2, y2)
    if (down_num == 6
        or down_num == 7
        or down_num == 8
            or down_num == 9):
        return musume.nomal_down(rows, x1, y1)
    else:
        return None


def auto_move_rightside(rows, inputnumber):
    num = musume.area_check(rows, inputnumber)
    coordinate = musume.split_number(num)
    y1 = coordinate[0]
    x1 = coordinate[1]
    right = check_rightside(rows, inputnumber)
    if right == 0:
        y2 = coordinate[2]
        x2 = coordinate[3]
        y3 = coordinate[4]
        x3 = coordinate[5]
        y4 = coordinate[6]
        x4 = coordinate[7]
        return musume.musume_move_right(rows, x1, y1, x2, y2, x3, y3, x4, y4)
    if (right == 1
        or right == 2
        or right == 3
            or right == 4):
        y2 = coordinate[2]
        x2 = coordinate[3]
        return musume.hight_move_right(rows, x1, y1, x2, y2)
    if right == 5:
        y2 = coordinate[2]
        x2 = coordinate[3]
        return musume.wide_move_right(rows, x1, y1, x2, y2)
    if (right == 6
        or right == 7
        or right == 8
            or right == 9):
        return musume.nomal_right(rows, x1, y1)
    else:
        return None


def auto_move_leftside(rows, inputnumber):
    num = musume.area_check(rows, inputnumber)
    coordinate = musume.split_number(num)
    y1 = coordinate[0]
    x1 = coordinate[1]
    left = check_leftside(rows, inputnumber)
    if left == 0:
        y2 = coordinate[2]
        x2 = coordinate[3]
        y3 = coordinate[4]
        x3 = coordinate[5]
        y4 = coordinate[6]
        x4 = coordinate[7]
        return musume.musume_move_left(rows, x1, y1, x2, y2, x3, y3, x4, y4)
    if (left == 1
        or left == 2
        or left == 3
            or left == 4):
        y2 = coordinate[2]
        x2 = coordinate[3]
        return musume.hight_move_left(rows, x1, y1, x2, y2)
    if left == 5:
        y2 = coordinate[2]
        x2 = coordinate[3]
        return musume.wide_move_left(rows, x1, y1, x2, y2)
    if (left == 6
        or left == 7
        or left == 8
            or left == 9):
        return musume.nomal_left(rows, x1, y1)
    else:
        None

# 現在のrowsから動かせる数字を確認して動かす。動けた場合はrowsを返して動かせなかった場合はcontinueするよ。


def move_board_up(rows, inputnumber):
    movable_up = auto_move_upside(rows, inputnumber)
    if movable_up is not None:
        return movable_up


def move_board_down(rows, inputnumber):
    movable_down = auto_move_downside(rows, inputnumber)
    if movable_down is not None:
        return movable_down


def move_board_right(rows, inputnumber):
    movable_right = auto_move_rightside(rows, inputnumber)
    if movable_right is not None:
        return movable_right


def move_boerd_left(rows, inputnumber):
    movable_left = auto_move_leftside(rows, inputnumber)
    if movable_left is not None:
        return movable_left


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
