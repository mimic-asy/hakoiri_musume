import numpy as np

def swap(rows, x1, y1, x2, y2):
    rows[y1, x1], rows[y2, x2] = rows[y2, x2], rows[y1, x1]


def init_puzzle():
    Musume= 0
    Sohu= 1
    Sobo= 2
    Chichi= 3
    Kyodai = 4
    Haha= 5
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

    print(rows)
    swap(rows, 3, 4, 2, 4)
    print(rows)

init_puzzle()