from re import X
from matplotlib.pyplot import axis, flag
import numpy as np


a = np.array([
                [10,9,8],
                [7,6,5],
                [4,3,2]

            ])
#箱に入っている要素の判定
def can_move_left(X):
    if X - 1 < -1:
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


print ("can_move_left(-1) = ", can_move_left(-1))
print ("can_move_left( 0) = ", can_move_left(0))
print ("can_move_left( 1) = ", can_move_left(1))
print ("can_move_left( 2) = ", can_move_left(2))

print ("can_move_right(0) = ", can_move_right(0))
print ("can_move_right(1) = ", can_move_right(1))
print ("can_move_right(2) = ", can_move_right(2))
print ("can_move_right(3) = ", can_move_right(3))

