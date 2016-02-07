from solver import solve
from sudoku import Sudoku

inp = input()
if len(inp) != 81:
    print("Please input a 81 characters long string of numbers 0-9")
data = []
for c in inp:
    data.append(int(c))
s = Sudoku(data)
solved = solve(s)
out = ""
for n in solved.getRawData():
    out += str(n)
print(out)
