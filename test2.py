import unittest
from coord import Coord, line_length


class TestLengthLine(unittest.TestCase):
    point1 = Coord(5, 5)
    point2 = Coord(5, 4)
    point3 = Coord(1, 5)
    point4 = Coord(5, 8)
    point5 = Coord(6, 5)
    point6 = Coord(9, 9)
    point7 = Coord(8, 3)
    point8 = Coord(1, 3)
    point9 = Coord(2, 8)
    point10 = Coord(-5, 5)
    point11 = Coord(-5, -5)
    point12 = Coord(5, -5)
    point13 = Coord(0, 0)
    point14 = Coord(0, 0)
    point15 = Coord(6, -8)

    def test_ut1(self):
        self.assertEqual(1.0, line_length(self.point1, self.point2))

    def test_ut2(self):
        self.assertEqual(4.0, line_length(self.point1, self.point3))

    def test_ut3(self):
        self.assertEqual(3.0, line_length(self.point1, self.point4))

    def test_ut4(self):
        self.assertEqual(1.0, line_length(self.point1, self.point5))

    def test_ut5(self):
        self.assertEqual(5.656854249492381, line_length(self.point1,
                                                       self.point6))

    def test_ut6(self):
        self.assertEqual(3.605551275463989, line_length(self.point1,
                                                       self.point7))

    def test_ut7(self):
        self.assertEqual(4.47213595499958, line_length(self.point1,
                                                       self.point8))

    def test_ut8(self):
        self.assertEqual(4.242640687119285, line_length(self.point1,
                                                       self.point9))

    def test_ut9(self):
        self.assertEqual(10.0, line_length(self.point1, self.point10))

    def test_ut10(self):
        self.assertEqual(14.142135623730951, line_length(self.point1,
                                                      self.point11))

    def test_ut11(self):
        self.assertEqual(10.0, line_length(self.point1, self.point12))

    def test_ut12(self):
        self.assertEqual(7.0710678118654755, line_length(self.point1,
                                                         self.point13))

    def test_ut13(self):
        self.assertEqual(0.0, line_length(self.point13, self.point14))

    def test_ut14(self):
        self.assertEqual(13.038404810405298, line_length(self.point1,
                                                         self.point15))
