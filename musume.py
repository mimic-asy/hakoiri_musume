import numpy as np
def swap(rows, y1, x1, y2, x2):
    rows[y1, x1], rows[y2, x2] = rows[y2, x2], rows[y1, x1]
#

def init_puzzle():
    Musume= 0
    Sohu= 1
    Sobo= 2
    Chichi= 3
    Haha = 4
    Kyodai= 5
    Sado= 6
    Syodo= 7
    Kado= 8
    Budo= 9
    Vacant= -1
    
    rows = np.array([
        [Sohu  , Musume, Musume, Sobo], 
        [Sohu  , Musume, Musume, Sobo],
        [Chichi, Kyodai, Kyodai, Haha],
        [Chichi, Sado  , Syodo , Haha],
        [Kado  , Vacant,  Vacant, Budo]
    ])

    return rows    

def swap_check2(val):

    if val.isdigit():
        a = int(val)
        if -1 < a < 10:
            return a
        else:
            print("０から９までの数字を入力してね")
            return None
    else:
        print("０から９までの数字を入力してね")
        return None

    assert False

#print(init_puzzle())
#入力された数字が使用可能か判断する関数
def swap_check():
    val  = input("動かしたい数字を入力してね")
    swap_check2(val)


#選択した数字はどこにあるかどうかを調べる。

def area_check(rows,a):
    yaxis, xaxis = np.where(rows == a)
    return [(y,x) for y,x in zip(yaxis,xaxis)]

if __name__ == "__main__":
    rows = init_puzzle()
    print(area_check(rows,0))

#範囲内か調べる関数（テスト済み）
def right_check(x):
    #右側が範囲内であることを示す
    if x+1<4:
        return True
    else:
        return False
def left_check(x):
    #左側が範囲内であることを示す
    if x-1>-1:
        return True
    else:
        return False
def top_check(y):
    #上が範囲内であることを示す
    if y-1>-1:
        return True
    else:
        return False
def down_check(y):
    #下側が範囲内であることを示す
    if y+1<5:
        return True
    else:
        return False

#隣が−１か調べる関数(テスト済み)
def vacant_check_right(rows,x1,y1):
    if rows[y1,x1+1] == -1:
        return  True
    else:
        return False
def vacant_check_left(rows,x1,y1):
    if rows[y1,x1-1] == -1:
        return True
    else:
        return False
def vacant_check_top(rows,x1,y1):
    if rows[y1-1,x1] == -1:
        return True
    else:
        print(rows[y1-1,x1])

def vacant_check_down(rows,x1,y1):
    if rows[y1+1,x1] == -1:
        return True
    else:
        return False

#1*2のマスを動かす関数(テスト済み)
def hight_move_right(rows,x1,y1,x2,y2):
    swap(rows,y1, x1, y1, x1+1)
    swap(rows,y2, x2, y2, x2+1)
    return print(rows)
def hight_move_left(rows,x1,y1,x2,y2):
    swap(rows,y1, x1, y1, x1-1)
    swap(rows,y2, x2, y2, x2-1)
    return print(rows)
def hight_move_top(rows,x1,y1,x2,y2):
    swap(rows, y1, x1, y1-1, x1)
    swap(rows, y2, x2, y2-1, x2)
    return print(rows)
def hight_move_down(rows,x1,y1,x2,y2):
    swap(rows, y1, x1, y1+1, x1)
    swap(rows, y2, x2, y2+1, x2)
    return print(rows)

def hight_move(rows,x1,y1,x2,y2):

    if right_check(x1) and vacant_check_right(rows,x1,y1) and vacant_check_right(rows,x2,y2):
        hight_move_right(rows,x1,y1,x2,y2)

    if left_check(x1) and vacant_check_left(rows,x1,y1) and vacant_check_left(rows,x2,y2):
        hight_move_left(rows,x1,y1,x2,y2)
        

    if top_check(y1) and    vacant_check_top(rows,x1,y1) and vacant_check_top(rows,x2,y2):
        hight_move_top(rows,x1,y1,x2,y2)
        

    if down_check(y2) and vacant_check_down(rows,x1,y1) and vacant_check_down(rows,x2,y2):
        hight_move_down(rows,x1,y1,x2,y2)
  
    else:
        print("この数字は動かせません、動かせる数字を選んでください")

#2*1のマスを動かす関数
def wide_move(rows,x1,y1,x2,y2):
    if top_check(y1) and   vacant_check_top(rows,x1,y1) and vacant_check_top(rows,x2,y2):
        swap(rows, y1, x1, y1-1, x1)
        swap(rows, y2, x2, y2-1,x2)
        print (rows)

    if down_check(y1) and vacant_check_down(rows,x1,y1) and vacant_check_down(rows,x2,y2):
        swap(rows, y1, x1, y1+1, x1)
        swap(rows, y2, x2, y2+1, x2)
        print(rows)

    if right_check(x1) and vacant_check_right(rows,x1,y1) and vacant_check_right(rows,x2,y2):
        swap(rows, y1, x1, y1, x1+1)
        swap(rows, y2, x2, y2, x2+1)
        print(rows)

    if left_check(x2) and vacant_check_left(rows,x1,y1) and vacant_check_left(rows,x2,y2):
        swap(rows, y1, x1, y1, x1-1)
        swap(rows, y2, x2, y2, x2-1)
        print(rows)
    else:
        print("この数字は動かせません、他の数字を選んでね")

#2*2のマスを動かす関数
def musume_move_right(rows,x1,y1,x2,y2,x3,y3,x4,y4):
    if right_check(x2) and vacant_check_right(rows,x2,y2) and vacant_check_right(rows,x4,y4):
        swap(rows,y2,x2,y2,x2+1)
        swap(rows,y4,x4,y4,x4+1)
        swap(rows,y1,x1,y1,x1+1)
        swap(rows,y3,x3,y3,x3+1)
        return rows
def musume_move_left(rows,x1,y1,x2,y2,x3,y3,x4,y4):
        swap(rows,y1, x1, y1, x1-1)
        swap(rows,y3, x3, y3, x3-1)
        swap(rows,y2, x2, y2, x2-1)
        swap(rows,y4, x4, y4, x4-1)
        return rows
def musume_move_top(rows,x1,y1,x2,y2,x3,y3,x4,y4):
        swap(rows,y1, x1, y1+1, x1)
        swap(rows,y2, x2, y2+1, x2)
        swap(rows,y3, x3, y3+1, x3)
        swap(rows,y4, x4, y4+1, x4)
        return rows
def musume_move_downswap(rows,x1,y1,x2,y2,x3,y3,x4,y4):
        swap(rows,y3, x3, y3-1, x3)
        swap(rows,y2, x2, y2-1, x2)
        swap(rows,y1, x1, y1-1, x1)
        swap(rows,y4, x4, y4-1, x4)
        return rows


def musume_swap(rows,x1,y1,x2,y2,x3,y3,x4,y4):
    if right_check(x1) and vacant_check_right(rows,x2,y2) and vacant_check_right(rows,x4,y4):
        musume_move_right(rows,x1,y1,x2,y2,x3,y3,x4,y4)

    if left_check(x1) and vacant_check_left(rows,x1,y1) and vacant_check_left(rows,x3,y3):
        musume_move_left(rows,x1,y1,x2,y2,x3,y3,x4,y4)

    if top_check(y1) and vacant_check_top(rows,x1,y1) and vacant_check_top(rows,x2,y2):
        musume_move_top(rows,x1,y1,x2,y2,x3,y3,x4,y4)
    
    if down_check(y3) and vacant_check_down(rows,x3,y3) and vacant_check_down(rows,x4,y4):
        musume_move_downswap(rows,x1,y1,x2,y2,x3,y3,x4,y4)