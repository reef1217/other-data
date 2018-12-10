import math

class Horse:
    def __init__(self, s, r):
        self.strong = s
        self.rider = r

class Rider:
    def __init__(self, name):
        self.name = name

class Apple:
    def __init__(self, w, f, c, s):
        self.weight = w
        self.fromm = f
        self.color = c
        self.size = s
        print('インスタンス作成完了')

class Circle:
    def __init__(self, h):
        self.half = h
        print('半径格納')

    def area(self):
        return self.half * self.half * math.pi

class Triangle:
    def __init__(self, h, w):
        self.height = h
        self.weight = w
        print('三角形作成')

    def area(self):
        return self.height * self.weight / 2

class Hexagon:
    def __init__(self, l):
        self.length = l
        print('１辺の長さ格納')

    def calculate_perimeter(self):
        return self.length * 6

class Shape:
    def what_am_i(self):
        return  'I am a shape'
'''
circle = Circle(90)
print(circle.area())
'''
'''
triangle = Triangle(50, 100)
print(triangle.area())
'''
'''
hexagon = Hexagon(5)
print(hexagon.calculate_perimeter())
'''

'''Ractangle = 長方形'''

class Rectangle(Shape):
    def __init__(self, w, h):
        self.weight = w
        self.height = h

    def calculate_perimeter(self):
        return self.weight * self.height * 2

class Square(Shape):
    def __init__(self, r):
        self.radius = r

    def change_size(self, r):
        self.radius = self.radius + r
        print('半径を{}に変更しました'.format(self.radius))

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

'''
ractangle = Rectangle(10, 6)
square = Square(5)

print(ractangle.calculate_perimeter())
print(square.calculate_perimeter())

square.change_size(-1)
print(square.calculate_perimeter())

print(ractangle.what_am_i())'''

rider = Rider('湊あかね')
horse = Horse('Super', rider)
print(horse.rider.name)