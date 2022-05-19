
from sqlite3 import Row
from turtle import end_fill
import numpy as np


def swap(rows, y1, x1, y2, x2):
    rows[y1, x1], rows[y2, x2] = rows[y2, x2], rows[y1, x1]


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

# "X" はvacantのx座標、”Y”には、y座標が入る
#箱に入っている要素の判定
def can_move_left(X):
    if X- 1 < -1:
        return True
    else:
        return False

def can_move_right(X):
    if X + 1  > 3:
        return True
    else:
        return False

def can_move_up(Y):
    if Y - 1 < -1:
        return True
    else:
        return False

def can_move_down(Y):
    if Y + 1 > 3:
        return True
    else:
        return False

returned_rows = init_puzzle()
can_move_left(returned_rows)

#四方の要素の確認
def element_checker_left():
    
    if (can_move_left()):
        left_element = rows(x1-1, y1)
    else:
        return False


def vacant_checker_y():
    if (row(x1,y1+1) == -1
    or row(x1,y1-1 == -1)):
        return True
    else:
       return False



def move_element_checker_left():
    if (left_element == 6 
        or left_element == 7 
        or left_element == 8 
        or left_element == 9):
       
       return True
    
    elif (left_element ==1 or 2 or 3 or 4):
        vacant_checker_y()
        