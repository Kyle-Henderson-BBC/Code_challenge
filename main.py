import numpy as np


# take top row, rotate, take top row
def solutionRecursive(grid, result):
    grid2 = grid[::]
    if len(grid2) == 0:
        return result
    result.extend(grid[0])
    grid2 = np.delete(grid2, 0, axis=0)
    grid2 = np.rot90(grid2)

    return solutionRecursive(grid2, result)


def solutionIteration(grid):
    result = []
    grid2 = grid[::]
    while len(grid2) > 0:
        result.extend(grid2[0])
        grid2 = np.delete(grid2, 0, axis=0)
        grid2 = np.rot90(grid2)
    return result


def outOfBounds(arr, n):
    return n < 0 or n >= len(arr)


def solutionSim(grid):
    m = len(grid)
    n = len(grid[0])
    result = []
    direc = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    x = 0
    y = 0
    seen = [[False for _ in range(n)] for _ in range(m)]
    for i in range(0, m * n):
        item = grid[x][y]
        new_x = x + dx[direc]
        new_y = y + dy[direc]
        print(item)
        print(f"x: {x}, y: {y}")
        if outOfBounds(seen, new_x) or outOfBounds(seen[0], new_y) or seen[new_x][new_y] is True:
            direc = (direc + 1) % 4
        result.append(item)
        seen[x][y] = True

        x += dx[direc]
        y += dy[direc]
    return result


test = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

test2 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    array = np.array(test)
    array2 = np.array(test2)

    print("      Sim:", solutionSim(test))

    print("recursive:", solutionRecursive(array, []))
    print("Iteration:", solutionIteration(array))
