#!/usr/bin/python3
'''N Queens Problem'''


def validation(chessboard, row, column):
    '''validates current position to see if its available
       vs the queens already set on the columns to the left.
    Args:
        chessboard: actual state of the game.
        row: row to validate.
        column: column to validate.
    '''
    for col in range(column):
        # checks if there is no queen in the row or diagonal
        if (chessboard[col] == row or
                # checks the slope:
                abs(col - column) == abs(chessboard[col] - row)):
            return False
    return True


def backtracking(chessboard, column):
    '''backtracking application.
    Args:
        chessboard: actual state of the game.
        column: the colum to backtrack,
    '''
    q = len(chessboard)
    # when all the queens are set and the validation is True,
    # prints the solution
    if column == q:
        solution = []
        for col in range(q):
            solution.append([col, chessboard[col]])
        print(solution)
        return

    for row in range(q):
        # if validation is True, a new queen is set and start to test a new one
        if validation(chessboard, row, column):
            chessboard[column] = row
            backtracking(chessboard, column + 1)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    q = 0
    try:
        q = int(sys.argv[1])
    except:
        print("N must be a number")
        sys.exit(1)
    if q < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Creation of the chessboard
    chessboard = []
    for col in range(q):
        chessboard.append(col)
    # starts the seeking of the solution in the first column
    backtracking(chessboard, 0)
