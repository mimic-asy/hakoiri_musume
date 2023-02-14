import musume
import numpy as np

# flake8: noqa
rows = musume.init_puzzle()

rows1 = np.array(
    [
        [1, 0, 0, 2],
        [1, 0, 0, 2],
        [3, -1, -1, 4],
        [3, 5, 5, 4],
        [6, 7, 8, 9],

    ]
)

rows_top = np.array(
    [
        [6, 0, 0, 2],
        [7, 0, 0, 2],
        [3, -1, -1, 4],
        [3, 5, 5, 4],
        [1, 1, 8, 9],

    ]
)

rows_2x2_top = np.array(
    [
        [1, 5, 5, 2],
        [1, 0, 0, 2],
        [3, 0, 0, 4],
        [3, 6, 7, 4],
        [8, -1, -1, 9],
    ]
)

the_one_before = [(rows1, rows_top), (rows_top, rows_2x2_top), (rows_2x2_top, rows)]

moved_rows = rows1


def test_area_check():
    assert musume.area_check(rows, 0) == [(0, 1), (0, 2), (1, 1), (1, 2)]
    assert musume.area_check(rows, 1) == [(0, 0), (1, 0)]
    assert musume.area_check(rows, 2) == [(0, 3), (1, 3)]
    assert musume.area_check(rows, 3) == [(2, 0), (3, 0)]
    assert musume.area_check(rows, 4) == [(2, 3), (3, 3)]
    assert musume.area_check(rows, 5) == [(2, 1), (2, 2)]
    assert musume.area_check(rows, 6) == [(3, 1)]
    assert musume.area_check(rows, 7) == [(3, 2)]
    assert musume.area_check(rows, 8) == [(4, 0)]
    assert musume.area_check(rows, 9) == [(4, 3)]
    assert musume.area_check(rows, -1) == [(4, 1), (4, 2)]


def test_split_number():

    assert musume.split_number([(0, 0), (1, 0)]) == [0, 0, 1, 0]
    assert musume.split_number([(0, 3), (1, 3)]) == [0, 3, 1, 3]
    assert musume.split_number([(2, 0), (3, 0)]) == [2, 0, 3, 0]
    assert musume.split_number([(2, 3), (3, 3)]) == [2, 3, 3, 3]
    assert musume.split_number([(2, 1), (2, 2)]) == [2, 1, 2, 2]
    assert musume.split_number([(3, 1)]) == [3, 1]
    assert musume.split_number([(3, 2)]) == [3, 2]
    assert musume.split_number([(4, 0)]) == [4, 0]
    assert musume.split_number([(4, 3)]) == [4, 3]
    assert musume.split_number([(4, 1), (4, 2)]) == [4, 1, 4, 2]


def test_right_check():
    assert musume.inrange_check_right(2) == True
    assert musume.inrange_check_right(3) == False


def test_left_check():
    assert musume.inrange_check_left(1) == True
    assert musume.inrange_check_left(0) == False


def test_top_check():
    assert musume.inrange_check_top(1) == True
    assert musume.inrange_check_top(0) == False


def test_down_check():
    assert musume.inrange_check_down(3) == True
    assert musume.inrange_check_down(4) == False


def test_vacant_check_right():
    assert musume.vacant_check_right(rows, 4, 0) == True
    assert musume.vacant_check_right(rows, 4, 1) == True
    assert musume.vacant_check_right(rows, 4, 2) == False
    assert musume.vacant_check_right(rows, 3, 1) == False
    assert musume.vacant_check_right(rows, 3, 2) == False


def test_vacant_check_left():
    assert musume.vacant_check_left(rows, 4, 3) == True
    assert musume.vacant_check_left(rows, 4, 2) == True
    assert musume.vacant_check_left(rows, 4, 1) == False


def test_vacant_check_top():
    assert musume.vacant_check_top(rows1, 3, 1) == True
    assert musume.vacant_check_top(rows1, 3, 2) == True
    assert musume.vacant_check_top(rows1, 2, 1) == False
    assert musume.vacant_check_top(rows1, 2, 2) == False
    assert musume.vacant_check_top(rows1, 1, 1) == False
    assert musume.vacant_check_top(rows1, 1, 2) == False


def test_vacant_check_down():
    assert musume.vacant_check_down(rows, 3, 1) == True
    assert musume.vacant_check_down(rows, 3, 2) == True
    assert musume.vacant_check_down(rows, 2, 1) == False
    assert musume.vacant_check_down(rows, 2, 2) == False


def test_move_1x1_to_left():
    rows1 = np.copy(rows)
    a = np.array(
        [
            [1, 0, 0, 2],
            [1, 0, 0, 2],
            [3, 5, 5, 4],
            [3, 6, 7, 4],
            [8, -1, 9, -1],

        ]
    )
    b = musume.move_1x1_to_left(rows1, 4, 3)
    assert np.all(a == b)


def test_move_1x1_to_right():
    rows2 = np.copy(rows)
    a = np.array(
        [
            [1, 0, 0, 2],
            [1, 0, 0, 2],
            [3, 5, 5, 4],
            [3, 6, 7, 4],
            [8, -1, 9, -1],

        ]
    )
    print(rows2)
    b = musume.move_1x1_to_right(rows2, 4, 2)
    assert np.all(a == b)


def test_move_1x1_to_top():
    rows_top_copy = np.copy(rows_top)
    a = np.array(
        [
            [7, 0, 0, 2],
            [6, 0, 0, 2],
            [3, -1, -1, 4],
            [3, 5, 5, 4],
            [1, 1, 8, 9],

        ]
    )
    b = musume.move_1x1_to_top(rows_top_copy, 1, 0)
    assert np.all(a == b)


def test_nomal_down():
    rows3 = np.copy(rows)
    a = np.array(
        [
            [1, 0, 0, 2],
            [1, 0, 0, 2],
            [3, 5, 5, 4],
            [3, -1, 7, 4],
            [8, 6, -1, 9],

        ]
    )

    b = musume.move_1x1_to_down(rows3, 3, 1)
    assert np.all(a == b)


def test_move_2x1_to_right():
    rows4 = np.copy(rows)
    a = np.array(
        [
            [1, 0, 0, 2],
            [1, 0, 0, 2],
            [3, 5, 4, 5],
            [3, 6, 4, 7],
            [8, -1, -1, 9],
        ]
    )
    b = musume.move_2x1_to_right(rows4, 2, 2, 3, 2)
    assert np.all(a == b)


def test_move_2x1_to_left():
    rows5 = np.copy(rows)
    a = np.array(
        [
            [1, 0, 0, 2],
            [1, 0, 0, 2],
            [5, 3, 5, 4],
            [6, 3, 7, 4],
            [8, -1, -1, 9],
        ]
    )
    b = musume.move_2x1_to_left(rows5, 2, 1, 3, 1)
    assert np.all(a == b)


def test_move_2x1_to_top():
    rows6 = np.copy(rows_top)
    a = np.array(
        [
            [6, 0, 0, 2],
            [3, 0, 0, 2],
            [3, -1, -1, 4],
            [7, 5, 5, 4],
            [1, 1, 8, 9],

        ]
    )
    print(rows6)
    b = musume.move_2x1_to_top(rows6, 2, 0, 3, 0)

    print(b)
    assert np.all(a == b)


def test_move_2x1_to_down():
    rows7 = np.copy(rows)
    a = np.array(
        [
            [1, 0, 0, 2],
            [1, 0, 0, 2],
            [3, -1, 5, 4],
            [3, 5, 7, 4],
            [8, 6, -1, 9],
        ]
    )
    b = musume.move_2x1_to_down(rows7, 3, 1, 2, 1)
    np.all(a == b)


def test_move_1x2_to_left():
    rows8 = np.copy(rows)
    a = np.array(
        [
            [1, 0, 0, 2],
            [1, 0, 0, 2],
            [5, 5, 3, 4],
            [3, 6, 7, 4],
            [8, -1, -1, 9],
        ]
    )
    b = musume.move_1x2_to_left(rows8, 2, 1, 2, 2)

    assert np.all(a == b)


def test_move_1x2_to_right():
    rows9 = np.copy(rows)
    a = np.array(
        [
            [1, 0, 0, 2],
            [1, 0, 0, 2],
            [3, 4, 5, 5],
            [3, 6, 7, 4],
            [8, -1, -1, 9],
        ]
    )
    b = musume.move_1x2_to_right(rows9, 2, 1, 2, 2)

    assert np.all(a == b)


def test_move_1x2_to_top():
    rows10 = np.copy(rows_top)
    a = np.array(
        [
            [7, 0, 0, 2],
            [6, 0, 0, 2],
            [3, -1, -1, 4],
            [3, 5, 5, 4],
            [1, 1, 8, 9],

        ]
    )
    b = musume.move_1x2_to_top(rows10, 1, 0, 1, 1)
    assert np.all(a == b)


def test_move_1x2_to_down():
    rows11 = np.copy(rows)
    a = np.array(
        [
            [1, 0, 0, 2],
            [1, 0, 0, 2],
            [3, 5, 5, 4],
            [8, -1, 7, 4],
            [3, 6, -1, 9],
        ]
    )
    b = musume.move_1x2_to_down(rows11, 3, 0, 3, 1)
    assert np.all(a == b)


def test_move_2x2_left():
    rows12 = np.copy(rows)
    a = np.array(
        [
            [0, 0, 1, 2],
            [0, 0, 1, 2],
            [3, 5, 5, 4],
            [3, 6, 7, 4],
            [8, -1, -1, 9],
        ]
    )
    b = musume.move_2x2_to_left(rows12, 0, 1, 0, 2, 1, 1, 1, 2)
    assert np.all(a == b)
    a2 = np.array(
        [
            [0, 0, 1, 2],
            [0, 0, 1, 2],
            [3, 5, 5, 4],
            [0, 0, 7, 4],
            [0, 0, -1, 9],
        ]
    )
    a3 = np.array(
        [
            [0, 0, 1, 2],
            [0, 0, 1, 2],
            [3, 5, 5, 4],
            [7, 0, 0, 4],
            [-1, 0, 0, 9],
        ]
    )
    b2 = musume.move_2x2_to_left(a3, 3, 1, 3, 2, 4, 1, 4, 2)
    assert np.all(a2 == b2)


def test_move_2x2_right():
    rows13 = np.copy(rows)
    a = np.array(
        [
            [1, 2, 0, 0],
            [1, 2, 0, 0],
            [3, 5, 5, 4],
            [3, 6, 7, 4],
            [8, -1, -1, 9],
        ]
    )
    b = musume.move_2x2_to_right(rows13, 0, 1, 0, 2, 1, 1, 1, 2)
    assert np.all(a == b)
    a2 = np.array(
        [
            [1, 2, 0, 0],
            [1, 2, 0, 0],
            [3, 5, 5, 4],
            [3, 6, 0, 0],
            [8, -1, 0, 0],
        ]
    )
    a3 = np.array(
        [
            [1, 2, 0, 0],
            [1, 2, 0, 0],
            [3, 5, 5, 4],
            [3, 0, 0, 6],
            [8, 0, 0, -1],
        ]
    )
    b2 = musume.move_2x2_to_right(a3, 3, 1, 3, 2, 4, 1, 4, 2)
    assert np.all(a2 == b2)


def test_move_2x2_top():
    rows14 = np.copy(rows_2x2_top)
    a = np.array(
        [
            [1, 0, 0, 2],
            [1, 0, 0, 2],
            [3, 5, 5, 4],
            [3, 6, 7, 4],
            [8, -1, -1, 9],
        ]
    )
    b = musume.move_2x2_to_top(rows14, 1, 1, 1, 2, 2, 1, 2, 2)
    np.all(a == b)


def test_move_2x2_down():
    a = np.array(
        [
            [1, 6, 7, 2],
            [1, -1, -1, 2],
            [3, 5, 5, 4],
            [3, 0, 0, 4],
            [8, 0, 0, 9],
        ]
    )
    a3 = np.array(
        [
            [1, 6, 7, 2],
            [1, -1, -1, 2],
            [3, 0, 0, 4],
            [3, 0, 0, 4],
            [8, 5, 5, 9],
        ]
    )
    b = musume.move_2x2_to_down(a3, 2, 1, 2, 2, 3, 1, 3, 2)
    assert np.all(a == b)


def test_inrange_and_vacant_check_top():
    assert musume.inrange_and_vacant_check_top(rows, 0, 0) == False
    a3 = np.array(
        [
            [1, -1, -1, 2],
            [1, 0, 0, 2],
            [3, 0, 0, 4],
            [3, 6, 7, 4],
            [8, 5, 5, 9],
        ]
    )
    assert musume.inrange_and_vacant_check_top(a3, 1, 1) == True
    assert musume.inrange_and_vacant_check_top(a3, 1, 2) == True


def test_inrange_and_vacant_check_down():
    assert musume.inrange_and_vacant_check_down(rows, 3, 1) == True
    assert musume.inrange_and_vacant_check_down(rows, 3, 2) == True
    assert musume.inrange_and_vacant_check_down(rows, 4, 1) == False


def test_inrange_and_vacant_check_left():
    assert musume.inrange_and_vacant_check_left(rows, 4, 2) == True
    a = np.array(
        [
            [1, -1, -1, 2],
            [1, 0, 0, 2],
            [3, 0, 0, 4],
            [3, 6, 7, 4],
            [-1, 5, 5, 9],
        ]
    )
    assert musume.inrange_and_vacant_check_left(a, 4, 1) == True
    assert musume.inrange_and_vacant_check_left(a, 3, 0) == False


def test_inrange_and_vacant_check_right():
    assert musume.inrange_and_vacant_check_right(rows, 4, 0) == True
    a = np.array(
        [
            [-1, 1, -1, 2],
            [1, 0, 0, 2],
            [3, 0, 0, 4],
            [3, 6, 7, 4],
            [8, 5, 5, -1],
        ]
    )
    assert musume.inrange_and_vacant_check_right(a, 4, 2) == True
    assert musume.inrange_and_vacant_check_right(a, 0, 3) == False


def test_board_simple():
    a = np.array(
        [
            [4, 0, 0, 4],
            [4, 0, 0, 4],
            [4, 5, 5, 4],
            [4, 6, 6, 4],
            [6, -1, -1, 6],
        ]
    )
    b = musume.board_simple(rows)
    assert np.all(a == b)


def test_check_upside():
    rows2 = np.copy(rows1)
    assert musume.check_upside(rows, 0) is None
    assert musume.check_upside(rows, 1) is None
    assert musume.check_upside(rows, 2) is None
    assert musume.check_upside(rows, 3) is None
    assert musume.check_upside(rows, 4) is None
    assert musume.check_upside(rows, 5) is None
    assert musume.check_upside(rows, 6) is None
    assert musume.check_upside(rows, 7) is None
    assert musume.check_upside(rows, 8) is None
    assert musume.check_upside(rows, 9) is None
    assert musume.check_upside(rows2, 5) == 5
    a = np.array(
        [
            [1, -1, -1, 2],
            [1, 0, 0, 2],
            [3, 0, 0, 4],
            [3, 6, 7, 4],
            [8, 5, 5, 9],
        ]
    )
    assert musume.check_upside(a, 0) == 0
    b = np.array(
        [
            [-1, 5, 5, -1],
            [1, 0, 0, 2],
            [1, 0, 0, 2],
            [3, 6, 7, 4],
            [3, 8, 9, 4],
        ]
    )
    assert musume.check_upside(b, 1) == 1
    assert musume.check_upside(b, 2) == 2
    c = np.array(
        [
            [1, 5, 5, 2],
            [1, 0, 0, 2],
            [-1, 0, 0, -1],
            [3, 6, 7, 4],
            [3, 8, 9, 4],
        ]
    )
    assert musume.check_upside(c, 3) == 3
    assert musume.check_upside(c, 4) == 4


def test_check_downside():
    rows2 = np.copy(rows1)
    assert musume.check_downside(rows2, 0) == 0
    assert musume.check_downside(rows2, 1) is None
    assert musume.check_downside(rows2, 2) is None
    assert musume.check_downside(rows2, 3) is None
    assert musume.check_downside(rows2, 4) is None
    assert musume.check_downside(rows2, 5) is None
    assert musume.check_downside(rows2, 6) is None
    assert musume.check_downside(rows2, 7) is None
    assert musume.check_downside(rows2, 8) is None
    assert musume.check_downside(rows2, 9) is None
    assert musume.check_downside(rows, 0) is None
    assert musume.check_downside(rows, 1) is None
    assert musume.check_downside(rows, 2) is None
    assert musume.check_downside(rows, 3) is None
    assert musume.check_downside(rows, 4) is None
    assert musume.check_downside(rows, 5) is None
    assert musume.check_downside(rows, 6) == 6
    assert musume.check_downside(rows, 7) == 7
    assert musume.check_downside(rows, 8) is None
    assert musume.check_downside(rows, 9) is None


def test_check_rightside():
    rows2 = np.array([
        [1, 0, 0, 2],
        [1, 0, 0, 2],
        [3, 5, 5, 4],
        [3, 6, 7, 4],
        [9, -1, 8, -1],
    ])
    assert musume.check_rightside(rows2, 0) is None
    assert musume.check_rightside(rows2, 1) is None
    assert musume.check_rightside(rows2, 2) is None
    assert musume.check_rightside(rows2, 3) is None
    assert musume.check_rightside(rows2, 4) is None
    assert musume.check_rightside(rows2, 5) is None
    assert musume.check_rightside(rows2, 6) is None
    assert musume.check_rightside(rows2, 7) is None
    assert musume.check_rightside(rows2, 8) == 8
    assert musume.check_rightside(rows2, 9) == 9


def test_check_leftside():
    rows2 = np.array([
        [1, 0, 0, 2],
        [1, 0, 0, 2],
        [3, 5, 5, 4],
        [3, 6, 7, 4],
        [-1, 8, 9, -1],
    ])
    assert musume.check_leftside(rows2, 0) is None
    assert musume.check_leftside(rows2, 1) is None
    assert musume.check_leftside(rows2, 2) is None
    assert musume.check_leftside(rows2, 3) is None
    assert musume.check_leftside(rows2, 4) is None
    assert musume.check_leftside(rows2, 5) is None
    assert musume.check_leftside(rows2, 6) is None
    assert musume.check_leftside(rows2, 7) is None
    assert musume.check_leftside(rows2, 8) == 8
    assert musume.check_leftside(rows2, 9) is None


def test_up_movable_list():
    a = np.array([
        [1, -1, -1, 2],
        [1, 0, 0, 2],
        [3, 0, 0, 4],
        [3, 5, 5, 4],
        [8, 7, 6, 9],
    ])
    b = musume.up_movable_list(a)
    c = [0]
    assert b == c


def test_down_movable_list():
    a = np.array([
        [1, 0, 0, 2],
        [1, 0, 0, 2],
        [3, 5, 5, 4],
        [3, 6, 7, 4],
        [8, -1, -1, 9],
    ])
    b = musume.down_movable_list(a)
    c = [6, 7]
    assert b == c


def test_right_movable_list():
    a = np.array([
        [1, 0, 0, 2],
        [1, 0, 0, 2],
        [3, 5, 5, 4],
        [3, 6, 7, 4],
        [8, -1, 9, -1],
    ])
    b = musume.right_movable_list(a)
    c = [8, 9]
    assert b == c


def test_left_movable_list():
    a = np.array([
        [1, 0, 0, 2],
        [1, 0, 0, 2],
        [3, 5, 5, 4],
        [3, 6, 7, 4],
        [-1, 8, -1, 9],
    ])
    b = musume.left_movable_list(a)
    c = [8, 9]
    assert b == c


def test_move_board_up():
    a1 = np.array([
        [1, -1, -1, 2],
        [1, 0, 0, 2],
        [3, 0, 0, 4],
        [3, 6, 7, 4],
        [8, 5, 5, 9],
    ])
    a2 = np.array([
        [1, 0, 0, 2],
        [1, 0, 0, 2],
        [3, -1, -1, 4],
        [3, 6, 7, 4],
        [8, 5, 5, 9],
    ])
    b1 = 0
    c1 = musume.move_board_up(a1, b1)
    assert np.all(a2 == c1)

    a3 = np.array([
        [-1, 0, 0, 2],
        [1, 0, 0, 2],
        [1, 8, -1, 4],
        [3, 6, 7, 4],
        [3, 5, 5, 9],
    ])

    a4 = np.array([
        [1, 0, 0, 2],
        [1, 0, 0, 2],
        [-1, 8, -1, 4],
        [3, 6, 7, 4],
        [3, 5, 5, 9],
    ])
    a5 = np.array([
        [-1, 0, 0, 2],
        [1, 0, 0, 2],
        [1, 8, 7, 4],
        [3, 6, -1, 4],
        [3, 5, 5, 9],
    ])

    c2 = musume.move_board_up(a3, 1)
    c3 = musume.move_board_up(a3, 7)
    assert np.all(c2 == a4)
    assert np.all(c3 == a5)


def test_move_board_down():
    a = np.array([
        [1, 5, 5, 2],
        [1, 0, 0, 2],
        [3, 0, 0, 4],
        [3, -1, -1, 9],
        [-1, 5, 5, -1],
    ])

    a1 = np.array([
        [1, 5, 5, 2],
        [1, -1, -1, 2],
        [3, 0, 0, 4],
        [3, 0, 0, 9],
        [-1, 5, 5, -1],
    ])

    a1_1 = np.array([
        [1, 5, 5, 2],
        [1, 0, 0, 2],
        [-1, 0, 0, 4],
        [3, -1, -1, 9],
        [3, 5, 5, -1],
    ])

    a1_2 = np.array([
        [1, 5, 5, 2],
        [1, 0, 0, 2],
        [3, 0, 0, 4],
        [3, -1, -1, -1],
        [-1, 5, 5, 9],
    ])

    a2 = np.array([
        [8, 6, 7, 2],
        [1, 5, 5, 2],
        [1, 0, 0, 4],
        [3, 0, 0, 4],
        [3, -1, -1, 9],
    ])
    a3 = np.array([
        [8, 6, 7, 2],
        [1, 5, 5, 2],
        [1, -1, -1, 4],
        [3, 0, 0, 4],
        [3, 0, 0, 9],
    ])

    b = musume.move_board_down(a, 0)
    b1_1 = musume.move_board_down(a, 3)
    b1_2 = musume.move_board_down(a, 9)
    b2 = musume.move_board_down(a2, 0)

    assert np.all(b == a1)
    assert np.all(b1_1 == a1_1)
    assert np.all(b1_2 == a1_2)
    assert np.all(b2 == a3)


def test_move_board_right():
    a = np.array([
        [1, 0, 0, 2],
        [1, 0, 0, 2],
        [3, 5, 5, 4],
        [3, 6, 7, 4],
        [-1, 8, 9, -1],
    ])
    a2 = np.array([
        [1, 0, 0, 2],
        [1, 0, 0, 2],
        [3, 5, 5, 4],
        [3, 6, 7, 4],
        [-1, 8, -1, 9],
    ])
    b = musume.move_board_right(a, 9)
    assert np.all(a2 == b)


def test_move_board_left():
    a = np.array([
        [1, 0, 0, 2],
        [1, 0, 0, 2],
        [3, 5, 5, 4],
        [3, 6, 7, 4],
        [8, -1, 9, -1],
    ])
    b = musume.move_board_left(rows, 9)
    assert np.all(a == b)


def test_move_up():
    aa = []
    a1 = np.array([
        [1, -1, -1, 2],
        [1, 0, 0, 2],
        [3, 0, 0, 4],
        [3, 6, 7, 4],
        [8, 5, 5, 9],
    ])
    a2 = np.array([
        [1, 0, 0, 2],
        [1, 0, 0, 2],
        [3, -1, -1, 4],
        [3, 6, 7, 4],
        [8, 5, 5, 9],
    ])
    aa.append(a2)
    b2 = musume.move_up(a1)
    assert np.all(aa == b2[0])


def test_move_down():
    a = np.array([
        [1, 0, 0, 2],
        [1, 0, 0, 2],
        [3, 5, 5, 4],
        [3, -1, 7, 4],
        [8, 6, -1, 9],
    ])
    a2 = np.array([
        [1, 0, 0, 2],
        [1, 0, 0, 2],
        [3, 5, 5, 4],
        [3, 6, -1, 4],
        [8, -1, 7, 9],
    ])

    b = musume.move_down(rows)
    assert np.all(a == b[0])
    assert np.all(a2 == b[1])


def test_move_right():
    a = np.array([
        [1, 0, 0, 2],
        [1, 0, 0, 2],
        [3, 5, 5, 4],
        [3, 6, 7, 4],
        [-1, 8, -1, 9],
    ])
    b = musume.move_right(rows)
    assert np.all(a == b[0])


def test_move_left():
    a = np.array([
        [1, 0, 0, 2],
        [1, 0, 0, 2],
        [3, 5, 5, 4],
        [3, 6, 7, 4],
        [-1, 8, -1, 9],
    ])
    a0 = np.array([
        [1, 0, 0, 2],
        [1, 0, 0, 2],
        [3, 5, 5, 4],
        [3, 6, 7, 4],
        [8, -1, -1, 9],
    ])
    a1 = np.array([
        [1, 0, 0, 2],
        [1, 0, 0, 2],
        [3, 5, 5, 4],
        [3, 6, 7, 4],
        [-1, 8, 9, -1],
    ])

    b = musume.move_left(a)

    assert np.all(a0 == b[0])
    assert np.all(a1 == b[1])


def test_saintankan():

    a = musume.saitankai(the_one_before)
    print(rows1)
    for i in a:
        print("return is")
        print(i)
    assert np.all(a[0] == rows1)
    assert np.all(a[1] == rows_top)
    assert np.all(a[2] == rows_2x2_top)
