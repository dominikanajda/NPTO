import math

from point import Point

class Vector:
    def __init__(self, x1, y1, x2, y2):
        self.pointA = Point(x1, y1)
        self.pointB = Point(x2, y2)
    def length(self) -> float:
        return math.sqrt(math.pow(self.pointB.x - self.pointA.x, 2)
                         + math.pow(self.pointB.y - self.pointA.y, 2))