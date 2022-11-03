
import numpy as np





def swap(rows, y1, x1, y2, x2):
    rows[y1, x1], rows[y2, x2] = rows[y2, x2], rows[y1, x1]

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


def init_puzzle():

    
    rows = np.array([
        [Sohu  , Musume, Musume, Sobo], 
        [Sohu  , Musume, Musume, Sobo],
        [Chichi, Kyodai, Kyodai, Haha],
        [Chichi, Sado  , Syodo , Haha],
        [Kado  , Vacant,  Vacant, Budo]
    ])

    return rows    

return_rows = init_puzzle()

def vacant_where(rows):
    ys, xs = np.where(rows == -1)
    x1 = xs[0]
    x2 = xs[1]
    y1 = ys[0]
    y2 = ys[1]
    vacant1 = [y1,x1]
    vacant2 = [y2,x2]
    print (vacant1,vacant2)
    return x1,y1,x2,y2
vacant_where(return_rows)


"""def can_move_left(x1):
    if (x1- 1 > -1):
        return True
    else:
        return False

def can_move_side(x1,y1):
    if(x1 == 0):
        ringt_move(x1,y1)
    else:
        left_move(x1,y1)

def can_move_upanddown(x1,y1):
    if(y1 == 0):
        down_move(x1,y1)
    else:
        up_move(x1,y1)




#def can_move_right(x1):
    if (x1+ 1 < 4):
        return True
    else:
        return False
    
#def can_move_up(y1):
    if (y1- 1 > -1):
        return True
    else:
        return False

#def can_move_down(y1):
    if (y1+ 1 < 5):
        return True
    else:
        return False



def side_element(x1,y1,rows):
    if can_move_side(x1) == True:
        swapx_plus = x1 - 1
        element_left = rows[y1,swapx_plus]

        return element_left

    elif can_move_right(x1) == True:
        swapx_minus = x1 + 1
        element_right = rows[y1,swapx_minus]

        return element_right

    elif can_move_up(y1) == True:
        swapy_minus = y1 - 1
        element_up = rows[swapy_minus,x1]

        return element_up

    
    elif can_move_down(y1) == True:
        swapy_plus = y1 +1
        element_down = rows[swapy_plus,x1]

        return element_down

#ここまででvacantの隣にある数値の判定をする
#これ以降、１*１の場合はswap、１* ２の時はvacantの上下のチェック、2*1の時はもう一方のvacantの隣を確認
print(side_element(1,4,return_rows))

def v2_leftmove(vx2,vy2,rows):
    v2_leftside = rows[vx1 - 1,]

def swap_checker(element,rows,x1,y1,x2,y2):
   if element == 6 or 7 or 8 or 9:
       ay,ax= np.where(rows == element)
       swap = swap(rows,x1,y1,ax,ay)
    
    elif element == 1 or 2 or 3 or 4 : #　v2の右隣がelementと一致することを確認する関数を作る
        can_move_left(x1) == True 
         
        s1,s2 = swap(rows,x1,y1,ax,ay)
        by = s1[0]
        bx = s1[1]
        

        swap_2 = swap(rows,bx,by,x2,y2)
 


   


        return

element_return = side_element()
return_rows = init_puzzle()
vacant_where(return_rows) 
vx1,vy1,vx2,vy2 = vacant_where(return_rows)
swap_checker(element_return,return_rows,vx1,vy1,vx2,vy2)
v2_leftmove(vx2,vy2,return_rows)
"""



