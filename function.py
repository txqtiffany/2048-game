# importing random package for generating random numbers.
import random


# initialize game
def start_game():
    # initiate an empty 4 x 4 matrix
    # with each empty cell represented as zero
    matrix = []
    for i in range(4):
        matrix.append([0] * 4)

    # print command as rules
    print("Commands are as follows : ")
    print("'w' : Move Up")
    print("'s' : Move Down")
    print("'a' : Move Left")
    print("'d' : Move Right")

    # initiate 2 random cells with number 2 in it
    insert_new(matrix)
    insert_new(matrix)

    # print the initial matrix to start
    print("Start : ")
    print(matrix[0])
    print(matrix[1])
    print(matrix[2])
    print(matrix[3])

    return matrix


# generate a new random 2 for an empty cell
def insert_new(matrix):
    # generate the row and column number of a random cell
    r = random.randint(0, 3)
    c = random.randint(0, 3)

    # re-choose if the cell is non-empty
    while matrix[r][c] != 0:
        r = random.randint(0, 3)
        c = random.randint(0, 3)

    # replace the empty cell as 2
    matrix[r][c] = 2


# get the current state of game
def get_current_state(matrix):
    # won if any cell contains 2048
    for i in range(4):
        for j in range(4):
            if matrix[i][j] == 2048:
                return 'YOU WON!'

    # game continues if there is still at least one empty cell
    for i in range(4):
        for j in range(4):
            if matrix[i][j] == 0:
                return 'continue'

    # or if no cell is empty now but two cells nearby could merge
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == matrix[i + 1][j] or matrix[i][j] == matrix[i][j + 1]:
                return 'continue'

    # else, lost the game
    return 'YOU LOST :('


# Build helper functions needed to operate the game

# compress the grid after every step before and after merging cells.
def compress(matrix):
    # variable indicating if there has been any changes
    changed = False

    # initiate empty grid with all cells empty
    new_mat = []
    for i in range(4):
        new_mat.append([0] * 4)

    # shift all cells to the left row by row
    for i in range(4):
        position = 0

        # traverse each column of the row
        for j in range(4):
            if matrix[i][j] != 0:

                # if the cell is not empty, shift the number to its previous
                # empty cell in that row denoted by the position variable
                new_mat[i][position] = matrix[i][j]

                if j != position:
                    changed = True
                position += 1

    # return the compressed matrix and the change variable.
    return new_mat, changed


# merge the cells in matrix after compressing
def merge(matrix):
    changed = False

    for i in range(4):
        for j in range(3):

            # if two nearby cell has the same and is both non-empty
            if matrix[i][j] == matrix[i][j + 1] and matrix[i][j] != 0:
                # double the current cell value and empty the other cell
                matrix[i][j] = matrix[i][j] * 2
                matrix[i][j + 1] = 0

                # turn changed into true
                changed = True

    return matrix, changed


# get the reverse of a matrix
def reverse(matrix):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(matrix[i][3 - j])
    return new_mat


# get the transpose of a matrix
def transpose(matrix):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(matrix[j][i])
    return new_mat


# Functions indicating each movement


# build the move left function as base
def move_left(grid):
    # compress and merge the grid
    new_grid, changed1 = compress(grid)
    new_grid, changed2 = merge(new_grid)

    # get whether anything changed
    changed = changed1 or changed2

    # compress again after merging.
    new_grid, temp = compress(new_grid)

    # return new grid and changed value
    return new_grid, changed


# to move right, we can reuse the move left function by
# putting a reserved matrix in and reverse back
def move_right(grid):
    new_grid = reverse(grid)
    new_grid, changed = move_left(new_grid)
    new_grid = reverse(new_grid)
    return new_grid, changed


# to move up, we can reuse the move left function by
# putting a transposed matrix in and transpose back
def move_up(grid):
    new_grid = transpose(grid)
    new_grid, changed = move_left(new_grid)
    new_grid = transpose(new_grid)
    return new_grid, changed


# to move down, we can reuse the move right function by
# putting a transposed matrix in and transpose back
def move_down(grid):
    new_grid = transpose(grid)
    new_grid, changed = move_right(new_grid)
    new_grid = transpose(new_grid)
    return new_grid, changed
