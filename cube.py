'''

    Program : Rubik's
    Author  : Maximilian Dean
    Date    : 3/1/19
    Purpose : File to import all classes for Rubik's program.

'''

class Cube:
    ''' Class to represent entire cube. '''

    def __init__(self):

        colors = ['white', 'yellow', 'red', 'orange', 'green', 'blue']
        self.side = []

        for i in range(len(colors)):
            self.side[i] = Side(colors[i])

    def turnSide(self, color):

        for i in self.side:
            if i.colorGetter() == color:
                i.turnClock()

    def turnSideReverse(self, color):

        for i in self.side:
            if i.colorGetter() == color:
                i.turnAntiClock()

    def turnCentre(self, color):

        for i in self.side:
            if i.colorGetter() == color:
                pass

    def turnCenterReverse(self, color):

        for i in self.side:
            if i.colorGetter() == color:
                pass

class Side(Cube):
    ''' Class to represent each of the six sides on cube. '''

    def __init__(self, color):
        self.name = color
        self._1 = Square(color)
        self._2 = Square(color)
        self._3 = Square(color)
        self._4 = Square(color)
        self._5 = Square(color)
        self._6 = Square(color)
        self._7 = Square(color)
        self._8 = Square(color)

    def turnClock(self):
        pass

    def turnAntiClock(self):
        pass

    # def swapTopBottom(self):
    #     pass
    #
    # def sqapSides(self):
    #     pass

    def colorGetter(self):
        return self.name

class Square(Side):
    ''' class to represent each square on each side of a cube. '''

    def __init__(self, color):
        self.name = color

