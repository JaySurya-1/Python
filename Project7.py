print("Jay Surya \n1AY24AI048 \nAIML 'M' ")
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, corner, width, height):
        self.corner = corner     
        self.width = width
        self.height = height

class Circle:
    def __init__(self, center, radius):
        self.center = center  
        self.radius = radius

def point_in_circle(circle, point):
    dx = point.x - circle.center.x
    dy = point.y - circle.center.y
    distance = math.hypot(dx, dy)
    return distance <= circle.radius

def rect_in_circle(circle, rect):
    corners = [
        rect.corner,
        Point(rect.corner.x + rect.width, rect.corner.y),
        Point(rect.corner.x, rect.corner.y + rect.height),
        Point(rect.corner.x + rect.width, rect.corner.y + rect.height)
    ]
    return all(point_in_circle(circle, corner) for corner in corners)

def rect_circle_overlap(circle, rect):
    corners = [
        rect.corner,
        Point(rect.corner.x + rect.width, rect.corner.y),
        Point(rect.corner.x, rect.corner.y + rect.height),
        Point(rect.corner.x + rect.width, rect.corner.y + rect.height)
    ]
    if any(point_in_circle(circle, corner) for corner in corners):
        return True
    if (rect.corner.x <= circle.center.x <= rect.corner.x + rect.width and
        rect.corner.y <= circle.center.y <= rect.corner.y + rect.height):
        return True
    return False

circle = Circle(Point(150, 100), 75)
rectangle = Rectangle(Point(120, 80), 40, 30)
point = Point(160, 110)
print("Point in Circle:", point_in_circle(circle, point))
print("Rectangle fully in Circle:", rect_in_circle(circle, rectangle))
print("Rectangle overlaps Circle:", rect_circle_overlap(circle, rectangle))
