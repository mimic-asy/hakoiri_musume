# 現在の位置から移動できる数字を補足する
# 移動できる数字を動かして
# deque内の数字を全て動かす

# 現在の盤面の更新→

# 存在する盤面を調べる
# グラフ醸造を作る
#
import musume
from collections import deque

boad_state = []
boad_que = deque()


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


def boad_simle(rows):
    for i in range(10):
        rows = num_simple(rows, i)
    return rows
