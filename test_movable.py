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


