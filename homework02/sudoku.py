from typing import Tuple, List, Set, Optional
import random


def read_sudoku(filename: str) -> List[List[str]]:
    digits = [c for c in open(filename).read() if c in '123456789.']
    grid = group(digits, 9)
    return grid


def display(grid: List[List[str]]) -> None:
    width = 2
    line = '+'.join(['-' * (width * 3)] * 3)
    for row in range(9):
        print(''.join(grid[row][col].center(width) + ('|' if str(col) in '25' else '') for col in range(9)))
        if str(row) in '25':
            print(line)
    print()


def group(values: List[str], n: int) -> List[List[str]]:
    d = len(values) // n
    divide_list = []
    for i in range(d):
        divide_list.append([])
        for j in range(n):
            x = values[i * n + j]
            divide_list[i].append(x)
    return divide_list


def get_row(grid: List[List[str]], pos: Tuple[int, int]) -> List[str]:
    d = int(pos[0])
    a = []
    for i in range(len(grid[d])):
        a.append(grid[d][i])
    return a


def get_col(grid: List[List[str]], pos: Tuple[int, int]) -> List[str]:
    d = int(pos[1])
    b = []
    for i in range(len(grid)):
        b.append(grid[i][d])
    return b


def get_block(grid: List[List[str]], pos: Tuple[int, int]) -> List[str]:
    m = 0
    n = 0
    while abs(3 * m + 1 - pos[0]) > 1:
        m = m + 1
    while abs(3 * n + 1 - pos[1]) > 1:
        n = n + 1
    m = 3 * m
    n = 3 * n
    c = []
    for i in range(m, m + 3):
        for j in range(n, n + 3):
            c.append(grid[i][j])
    return c


def find_empty_positions(grid: List[List[str]]) -> Optional[Tuple[int, int]]:
    l = ()
    n = ()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '.':
                l = (i, j)
                return l
    return n


def find_possible_values(grid: List[List[str]], pos: Tuple[int, int]) -> Set[str]:
    a = list('123456789')
    b: List[str] = grid[pos[0]]
    c: List[str] = []
    for i in range(9):
        c.append(grid[i][pos[1]])
    d: List[str] = get_block(grid, pos)
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                a[i] = '.'
        for j in range(len(c)):
            if a[i] == c[j]:
                a[i] = '.'
        for j in range(len(d)):
            if a[i] == d[j]:
                a[i] = '.'
    e = []
    for i in range(len(a)):
        if a[i] != '.':
            e.append(a[i])
    f = set(e)
    return f


def sudokubool(grid):
    g = find_empty_positions(grid)
    if len(g) == 0:
        return True
    for k in find_possible_values(grid, g):
        grid[g[0]][g[1]] = k
        if sudokubool(grid):
            return True
        grid[g[0]][g[1]] = '.'
    return False


def solve(grid: List[List[str]]) -> Optional[List[List[str]]]:
    sudokubool(grid)
    return grid


def check_solution(solution: List[List[str]]) -> bool:
    res = True
    for i in range(9):
        for j in range(9):
            a = set(solution[i])
            b = []
            for k in range(9):
                b.append(solution[k][j])
            b = set(b)
            c = set(get_block(solution, (i, j)))
            if len(a) != 9 or len(b) != 9 or len(c) != 9:
                res = False
    return res


def generate_sudoku(N: int) -> List[List[str]]:
    s = list('123456789')
    a = []
    for i in range(9):
        a.append(random.choice(s))
        s.remove(a[i])
    a = a * 2
    grid = []
    for i in range(9):
        grid.append([])
    for i in range(9):
        grid[0].append(a[i])
        grid[1].append(a[i + 3])
        grid[2].append(a[i + 6])
        grid[3].append(a[i + 1])
        grid[4].append(a[i + 4])
        grid[5].append(a[i + 7])
        grid[6].append(a[i + 2])
        grid[7].append(a[i + 5])
        grid[8].append(a[i + 8])
    if N > 80:
        return grid
    if N > 41:
        i = 1
        while i < 81 - N + 1:
            m = random.randrange(0, 9)
            n = random.randrange(0, 9)
            while grid[m][n] == '.':
                m = random.randrange(0, 9)
                n = random.randrange(0, 9)
            grid[m][n] = '.'
            i = i + 1
        return grid
    else:
        grid1 = []
        for i in range(9):
            grid1.append([])
            for j in range(9):
                grid1[i].append('.')
        i = 1
        while i < N + 1:
            m = random.randrange(0, 9)
            n = random.randrange(0, 9)
            while grid1[m][n] != '.':
                m = random.randrange(0, 9)
                n = random.randrange(0, 9)
            grid1[m][n] = grid[m][n]
            i = i + 1
        return grid1


if __name__ == '__main__':
    for fname in ['puzzle1.txt', 'puzzle2.txt', 'puzzle3.txt']:
        grid = read_sudoku(fname)
        display(grid)
        solution = solve(grid)
        if not solution:
            print(f"Puzzle {fname} can't be solved")
        else:
            display(solution)
