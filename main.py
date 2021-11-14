"""
Jawad Taj
2021-11-13
Calculate the area of a circle given its radius
Calculate the distance between 2 points on a cartesian plane
"""


class Circle:
    """
        :param rad: The radius of the circle
    """

    def __init__(self, rad):
        self.pi = 3.14
        self.rad = rad

    """
        :radius_to_area: Gets the area of a Circle with a radius
    
        :return: area of the circle
    """

    def radius_to_area(self):
        return self.pi * self.rad ** 2


class CartesianPlane:
    """
        :param x1: Point Value of x1
        :param x2: Point Value of x2
        :param y1: Point Value of y1
        :param y2: Point Value of y2
    """

    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    """
        :distance_2_points: Gets the distance of 2 points

        :return: distance of two points
    """

    def distance_2_points(self):
        return ((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2) ** 0.5


if __name__ == '__main__':
    # Circle
    print("Circle")
    radius = ""

    # Checks if user enter numbers
    while not radius.isdigit():
        radius = input("Enter The Radius Of The Circle: ")

    radius = int(radius)
    c = Circle(rad=radius)
    print(c.radius_to_area())


    # Cartesian Plane
    print("\nCartesian Plane")
    x1, x2, y1, y2 = "", "", "", ""

    # Keeps in loop until all variables are 0
    while x1 + x2 + y1 + y2 != 0.0:
        x1, x2, y1, y2 = "", "", "", ""

        # Checks if user enter numbers
        while not x1.isdigit() or not x2.isdigit() or \
                not y1.isdigit() or not y2.isdigit():
            x1 = input("Enter The Number For x1: ")
            x2 = input("Enter The Number For x2: ")
            y1 = input("Enter The Number For y1: ")
            y2 = input("Enter The Number For y2: ")

        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int(y2)
        cp = CartesianPlane(x1, x2, y1, y2)
        print(cp.distance_2_points(), "\n")