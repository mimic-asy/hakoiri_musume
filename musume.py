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

#print(init_puzzle())
#入力された数字が使用可能か判断する関数
def swap_check():
    val  = input("動かしたい数字を入力してね")
    if val.isdigit():
        a = int(val)
        if -1 < a < 10:
            return a
        if a <-1 or 10 < a:
            print("０から９までの数字を入力してね")
            return None

    else:
        print("０から９までの数字を入力してね")
        return None

swap_check()   
#−１はどこにあるかどうかを調べる。
def erea_check(rows,a):
    ys,xs =np.where(rows == -1)
    x1 = xs[0]
    x2 = xs[1]
    y1 = ys[0]
    y2 = ys[1]
    #一つ目の−１の位置
    vacant1 = [y1,x1]
    #2つ目の−１の位置
    vacant2 = [y2,x2]
    return x1,y1,x2,y2

#-1の隣に入力した要素があるかどうかを判別する
def side_or_notside(rows,a,x1,y1,x2,y2):
    if (x1- 1 > -1):
        left = rows[x1-1,y1]
    if (x1+ 1 < 4):
        right = rows[x1+1,y1]
    if (y1+ 1 <5):
        low = rows[x1,y1+1]
    if (y1- 1 <-1):
        high = rows[x1,y1-1]

    

