import musume
import numpy as np

rows = musume.init_puzzle()


def musume_puzzle(rows):

    musume.swap_check(rows)
    select_number = musume.swap_check(rows)
    num = musume.area_check(select_number)
    musumecoordinate = musume.split_number(num)

    if select_number == 0:
        y1 = musumecoordinate[0]
        x1 = musumecoordinate[1]
        y2 = musumecoordinate[2]
        x2 = musumecoordinate[3]
        y3 = musumecoordinate[4]
        x3 = musumecoordinate[5]
        y4 = musumecoordinate[6]
        x4 = musumecoordinate[7]

        musume.musume_swap(rows, x1, y1, x2, y2, x3, y3, x4, y4)
        print(rows)

    if 0 < select_number < 5:
        y1 = musumecoordinate[0]
        x1 = musumecoordinate[1]
        y2 = musumecoordinate[2]
        x2 = musumecoordinate[3]
        musume.hight_move(rows, x1, y1, x2, y2)
        print(rows)

    if select_number == 5:
        y1 = musumecoordinate[0]
        x1 = musumecoordinate[1]
        y2 = musumecoordinate[2]
        x2 = musumecoordinate[3]
        musume.wide_move(rows, x1, y1, x2, y2)
        print(rows)

    if 5 < select_number < 10:
        y1 = musumecoordinate[0]
        x1 = musumecoordinate[1]
        musume.nomal_swap(rows, x1, y1)
        print(rows)

    else:
        print("エラー")


musume_puzzle(rows)
