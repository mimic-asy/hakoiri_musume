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

#−１はどこにあるかどうかを調べる。
def erea_check(rows):
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

#上下左右を判定し、配列外の場合、Falseを返す
def sidecheck(rows,x,y):
    flag1 =rows[y,x-1]
    flag2 =rows[y,x+1]
    flag3 =rows[y-1,x]
    flag4 =rows[y+1,x]
    flag5 =99


    if x-1 >0:
        return True, flag1,11
    if x+1 <5:
        return True,flag2,22
    if y-1 >0:
        return True,flag3,33
    if y+1 <5:
        return True,flag4,44
    else:
        print("この数字は動かせません、他の数字を入力してください")
        return False,flag5,55
# aはどのような場合に移動できるかを定める関数
def sidebyside(rows,a,y1,x1,y2,x2):
    if a == 6 or 7 or 8 or 9:
        swap(rows, y1, x1, y2, x2)




#上下、もしくは左右に移動可能な場合、aがvacantと隣接しているかを確認する
def side_or_notside(rows,a,x1,y1,x2,y2):
    point1 = sidecheck(rows,y1,x1)
    point2 = sidecheck(rows,y2,x2)
  

        
    
        



        

    

