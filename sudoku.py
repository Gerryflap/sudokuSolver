class Sudoku:
    def __init__(self, data=None):
        if data is None or len(data) != 81:
            self.data = [0 for i in range(9 * 9)]
        else:
            self.data = data

    def getRow(self, row):
        return self.data[row * 9: (row + 1)*9]

    def getColumn(self, column):
        return [self.data[i * 9 + column] for i in range(9)]

    def getSquare(self, x, y):
        return [self.data[i % 3 + 3 * x + 3 * 9 * y + 9 * (i // 3)] for i in range(9)]

    def getAtPosition(self, x, y):
        return self.data[x + 9 * y]

    def setAtPosition(self, x, y, value):
        self.data[x + 9 * y] = value

    def clone(self):
        return Sudoku(self.data[:])

    def getRawData(self):
        return self.data

    def isMoveCorrect(self, x, y, value):
        return value not in self.getRow(y) and \
               value not in self.getColumn(x) and \
               value not in self.getSquare(x // 3, y // 3)

    def getFreePositions(self):
        return [(i % 9, i // 9) for i in range(81) if self.data[i] == 0]

    def getFirstFreePosition(self):
        for i in range(81):
            if self.data[i] == 0:
                return i % 9, i // 9
        return None

    def __repr__(self):
        string = ""
        for i in range(81):
            if i%(9*3) == 0:
                string += "\n"
            if i % 9 == 0:
                string += "\n"
            elif i % 3 == 0:
                string += "\t"
            string += "%i\t" % self.data[i]
        return string


if __name__ == "__main__":
    s = Sudoku()
    print("Columns:")
    print(s.getColumn(0))
    print(s.getColumn(1))
    print("Rows:")
    print(s.getRow(0))
    print(s.getRow(1))
    print("Squares:")
    print(s.getSquare(0, 0))
    print(s.getSquare(1, 0))
    print("Position:")
    print(s.getAtPosition(0, 0))
    print(s.getAtPosition(0, 5))
