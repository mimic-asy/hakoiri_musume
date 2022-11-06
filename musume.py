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
    A=np.where(rows == a)
    yaxis= A[0]
    xaxis= A[1]
    yaxis_and_xaxis=[]
    for y,x in zip(yaxis,xaxis):
        yaxis_and_xaxis.append((y,x))
        
    return yaxis_and_xaxis


rows =init_puzzle()
print(area_check(rows,0))
