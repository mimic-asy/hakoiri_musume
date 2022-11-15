import musume
import numpy as np
import io

def test_swap_check2():
    assert musume.swap_check2("a") is None
    assert musume.swap_check2("1") == 1
    assert musume.swap_check2("99") is None
    assert musume.swap_check2("-1") is None
    assert musume.swap_check2("0") == 0
    assert musume.swap_check2("9") == 9
    assert musume.swap_check2("10") is None

def test_area_check(): 
    a = np.array([
        [0,0,0,0],
        [1,1,1,1],
        [2,2,2,3],
        [4,5,6,7]
    ])
    assert musume.area_check(a,0) == [(0,0),(0,1),(0,2),(0,3)]

def test_right_check():
    a = np.array([
        [1,0,0,7],
        [1,0,0,7],
        [4,2,2,3],
        [4,5,6,3]
    ])
    assert musume.right_check(0) == True
    assert musume.left_check(0) == False
    assert musume.top_check(0) == False
    assert musume.down_check(0) == True

def test_vacant_check_right():
    a = np.array([
        [1,-1,0,7],
        [1,-1,0,7],
        [4,2,2,3],
        [4,5,6,3]
    ])
    assert musume.vacant_check_down(a,0,0) ==False
    assert musume.vacant_check_down(a,0,1) == False
    assert musume.vacant_check_down(a,1,2) == False

def test_move():
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
        [Vacant  , Musume, Musume, Sobo], 
        [Vacant  , Musume, Musume, Sobo],
        [Sohu, Chichi, Sado, Haha],
        [Sohu, Chichi, Syodo , Haha],
        [Kado  , Kyodai,  Kyodai, Budo]
    ])
    assert musume.hight_move(rows,0,2,0,3) == print(rows)
