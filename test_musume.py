import musume
import numpy as np

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



