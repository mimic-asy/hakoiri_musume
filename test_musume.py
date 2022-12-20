import musume
import numpy as np
import breadth_search as bs
# np.set_printoptions(threshold=sys.maxsize)


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
        [0, 0, 0, 0],
        [1, 1, 1, 1],
        [2, 2, 2, 3],
        [4, 5, 6, 7]
    ])
    assert musume.area_check(a, 0) == [(0, 0), (0, 1), (0, 2), (0, 3)]


def test_right_check():
    assert musume.right_check(0)
    assert not musume.left_check(0)
    assert not musume.top_check(0)
    assert musume.down_check(0)


def test_vacant_check_right():
    a = np.array([[1, -1, 0, 7], [1, -1, 0, 7], [4, 2, 2, 3], [4, 5, 6, 3]])
    assert not musume.vacant_check_down(a, 0, 0)
    assert not musume.vacant_check_down(a, 0, 1)
    assert not musume.vacant_check_down(a, 1, 2)


def test_move():

    rows = np.array([
        [9, 7, 2, 3],
        [9, 0, 0, 3],
        [4, 0, 0, 5],
        [4, 6, 6, 5],
        [8, -1, -1, 1]
    ])
    rows_top = np.array([
        [9, 7, 2, 3],
        [9, 0, 0, 3],
        [4, -1, -1, 5],
        [4, 6, 6, 5],
        [8, 0, 0, 1]]
    )
    rows_left = np.array([
        [9, 7, 2, 3],
        [9, 0, 0, 3],
        [4, 0, 0, 5],
        [-1, 6, 6, 5],
        [8, 4, -1, 1]
    ])
    rows_right = np.array([
        [9, 7, 2, 3],
        [9, 0, 0, 3],
        [4, 0, 0, 5],
        [5, 6, 6, -1],
        [8, -1, 4, 1]
    ])
    down = musume.wide_move(rows, 1, 3, 2, 3)
    top = musume.wide_move(rows_top, 1, 3, 2, 3)
    left = musume.wide_move(rows_left, 1, 3, 2, 3)
    right = musume.wide_move(rows_right, 1, 3, 2, 3)
    np.testing.assert_array_equal(
        np.array([
            [9, 7, 2, 3],
            [9, 0, 0, 3],
            [4, 0, 0, 5],
            [4, -1, -1, 5],
            [8, 6, 6, 1]
        ]),
        down,
    )

    np.testing.assert_array_equal(
        np.array([
            [9, 7, 2, 3],
            [9, 0, 0, 3],
            [4, 6, 6, 5],
            [4, -1, -1, 5],
            [8, 0, 0, 1]
        ]),
        top,
    )

    np.testing.assert_array_equal(
        np.array([
            [9, 7, 2, 3],
            [9, 0, 0, 3],
            [4, 0, 0, 5],
            [6, 6, -1, 5],
            [8, 4, -1, 1]
        ]),
        left,
    )

    np.testing.assert_array_equal(
        np.array([
            [9, 7, 2, 3],
            [9, 0, 0, 3],
            [4, 0, 0, 5],
            [5, -1, 6, 6],
            [8, -1, 4, 1]
        ]),
        right,
    )


def nomal_left(rows, x1, y1):
    rows = musume.swap(rows, y1, x1, y1, x1 - 1)
    return rows


def basic_left(rows, x1, y1):
    if (musume.left_check(x1)
            and musume.vacant_check_left(rows, x1, y1)):
        return True


rows = musume.init_puzzle()

# print(bs.left_move(rows,8))
# print(bs.check_leftside(rows,8))
# print(musume.vacant_check_left(rows, 0, 4))
# print(musume.basic_left(rows, 0, 4))
# print(bs.movable_list(rows))

# print(bs.breadth_search(rows
""""
def b(rows):
    board_state = []
    board_queue = deque()
    board_queue.append(rows)
    while len(board_queue) > 0:
        rows_data  = board_queue.popleft()
        movable = bs.movable_list(rows_data)
        for i in movable:
            new_rows = np.copy(i)
            for n in range(10):
                #area = musume.area_check(new_rows,n)
                comparison = bs.board_simple(new_rows)
                mache_list = bs.what_mache(comparison,)
"""

bs.breadth_search(rows)
