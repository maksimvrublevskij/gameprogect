class Square:
    def __init__(self, side=10):
        self.side = side

    def calculate_area(self):
        return self.side ** 2

    def draw(self):
        for i in range(self.side):
            print(' * ' * self.side)


a1 = Square(5)
print(a1.calculate_area())
a1.draw()