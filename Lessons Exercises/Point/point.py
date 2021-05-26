class Point:
    """Implement your Point class in here!"""
    def __init__(self, x=0, y=0):
        self.x_cord = x
        self.y_cord = y

    def __add__(self, other):
        return Point(self.x_cord + other.x_cord, self.y_cord + other.y_cord)

    def __str__(self):
        return f"Point({self.x_cord}, {self.y_cord})"


if __name__ == '__main__':
    # This won't work until you finish implementing the Point class.
    origin = Point()
    point = Point(4, 1)
    other_point = Point(3, -3)
    third_point = point + other_point

    print(point)
    print(other_point)
    print(third_point)
