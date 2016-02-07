from sudoku import Sudoku


def solve(s: Sudoku):
    pos = s.getFirstFreePosition()
    if pos is None:
        return s
    x, y = pos
    for v in range(1, 10):
        if s.isMoveCorrect(x, y, v):
            newS = s.clone()
            newS.setAtPosition(x, y, v)
            solved = solve(newS)
            if solved is not None:
                return solved
    return None


if __name__ == "__main__":
    """
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    """
    s = Sudoku(
        [3, 0, 0, 1, 5, 0, 0, 0, 2,
         0, 0, 0, 0, 0, 7, 5, 1, 0,
         0, 0, 1, 4, 0, 0, 0, 0, 7,
         0, 0, 0, 0, 0, 0, 0, 7, 6,
         0, 1, 0, 0, 4, 0, 0, 3, 0,
         8, 6, 0, 0, 0, 0, 0, 0, 0,
         7, 0, 0, 0, 0, 3, 6, 0, 0,
         0, 8, 5, 9, 0, 0, 0, 0, 0,
         4, 0, 0, 0, 2, 1, 0, 0, 8]
    )
    print(solve(s))

    s2 = Sudoku(
        [
            0, 0, 1, 9, 0, 8, 0, 0, 7,
            8, 9, 0, 0, 0, 0, 0, 0, 0,
            5, 0, 7, 0, 1, 0, 6, 0, 0,
            4, 0, 0, 6, 0, 0, 0, 5, 0,
            9, 0, 0, 0, 0, 0, 0, 0, 1,
            0, 5, 0, 0, 0, 3, 0, 0, 2,
            0, 0, 5, 0, 3, 0, 8, 0, 9,
            0, 0, 0, 0, 0, 0, 0, 2, 6,
            1, 0, 0, 8, 0, 9, 5, 0, 0
        ]
    )
    print(solve(s2))
