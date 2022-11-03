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

def test_erea_check():
    rows0 = np.array([
        [1,-1,2],
        [-1,3,4],
        [5,6,7],
    ])
    assert musume.erea_check(rows0) == (1,0,0,1)
    
    rows1 = np.array([
        [0,1,-1,2,0],
        [0,-1,3,4,0],
        [0,5,6,7,0],
    ])
    assert musume.erea_check(rows1) == (2,0,1,1)



