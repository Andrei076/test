class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Coord(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"x: {self.x}, y: {self.y}"


def line_length(point_1, point_2):
    return ((point_1.x - point_2.x) ** 2 + (point_2.y - point_1.y) ** 2) ** 0.5


