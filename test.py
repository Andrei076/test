from coord import Coord, line_length


def test_a1():
    a1 = Coord(8, 8)
    a2 = Coord(2, 1)
    assert line_length(a1, a2) == 9.219544457292887


def test_a2():
    a1 = Coord(4, 4)
    a2 = Coord(2, 7)
    assert line_length(a1, a2) == 3.605551275463989
