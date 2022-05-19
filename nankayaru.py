
from logging.config import valid_ident
import numpy as np
from pyparsing import one_of




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
    return vacant1,vacant2

def can_move_left(x1):
    if (x1- 1 > -1):
        return True
    else:
        return False

def can_move_right(x1):
    if (x1+ 1 < 4):
        return True
    else:
        return False
    
def can_move_up(y1):
    if (y1- 1 > -1):
        return True
    else:
        return False

def can_move_down(y1):
    if (y1+ 1 < 5):
        return True
    else:
        return False



def swap_checker(x1,y1,rows):
    if can_move_left(x1) == True:
        swapx_plus = x1 + 1
        swap_check_left = rows[y1,swapx_plus]

        return swap_check_left

    elif can_move_right(x1) == True:
        swapx_minus = x1 - 1
        swap_check_right = rows[y1,swapx_minus]

        return swap_check_right

    elif can_move_up(y1) == True:
        swapy_minus = y1 - 1
        swap_check_up = rows[swapy_minus,x1]

        return swap_check_up

    
    elif can_move_down(y1) == True:
        swapy_plus = y1 +1
        swap_check_down = rows[swap_check_down,x1]

        return swap_check_down


print(swap_checker(1,4,return_rows))





    

         


       
     
    
    

    






 


   
   
   




return_rows = init_puzzle()
vacant_where(return_rows)




