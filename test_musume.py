import musume

rows = musume.init_puzzle()


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
