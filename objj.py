
class Square():
    square_list = []

    def __init__(self, w):
        self.weight = w
        self.square_list.append(self.weight)
        print(self.weight, self.weight, self.weight, self.weight)

    def change_size(self, w):
        self.weight = self.weight + w
        print('横幅を{}に変更しました'.format(self.weight))

    def calculate_perimeter(self):
        return self.weight * 4

    def comp(self, obj1, obj2):
        if obj1 is obj2:
            print('True')
        else:
            print('False')


square = Square(40)
print(square.square_list)
obj = Square(40)

square.comp(square, square)