"""
CIS 211 Spring 2021

Project: Point

Author: Mindy Tran

Credit: N/A
"""


class Point:
    """An (x,y) coordinate pair"""

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def move(self, dx: int, dy: int):
        """increase self.x by dx and increase self.y by dy."""
        self.x += dx
        self.y += dy

    def __eq__(self, other: "Point"):
        """(x, y) == (dx, dy)"""
        if self.x == other.x and self.y == other.y:
            return Point(self.x == other.x, self.y == other.y)
        return False

    def __str__(self) -> str:
        """returns string representation"""
        return f"({str(self.x)}, {str(self.y)})"
