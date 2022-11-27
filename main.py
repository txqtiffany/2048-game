# import the function.py file to access all functions
import function

# Driver code
if __name__ == '__main__':
    # start game
    matrix = function.start_game()

while True:

    # taking user input
    x = input("Press the command: ")

    # move up
    if x == 'w':

        # generate the move
        mat, flag = function.move_up(matrix)

        # get the current game status
        status = function.get_current_state(matrix)

        # if game not over, then add a new cell
        if status == 'continue':
            function.insert_new(matrix)

        # else break the loop
        else:
            break

    # move down
    elif x == 's':
        mat, flag = function.move_down(matrix)
        status = function.get_current_state(matrix)
        if status == 'continue':
            function.insert_new(matrix)
        else:
            break

    # move left
    elif x == 'a':
        mat, flag = function.move_left(matrix)
        status = function.get_current_state(matrix)
        if status == 'continue':
            function.insert_new(matrix)
        else:
            break

    # move right
    elif x == 'd':
        mat, flag = function.move_right(matrix)
        status = function.get_current_state(matrix)
        if status == 'continue':
            function.insert_new(matrix)
        else:
            break
    else:
        print("Invalid Key")

    # print the matrix after each move
    print(matrix[0])
    print(matrix[1])
    print(matrix[2])
    print(matrix[3])
