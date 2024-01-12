#!/usr/bin/python3
"""
Solves the N-Queens problem and prints every possible solution.
"""
import sys


def is_valid(board, row, col):
    """
    Checks if a position of the queen is valid

    Args:
        board: 2D array representing the board
        row: row of the queen
        col: column of the queen

    Returns:
        Boolean: True if the position is valid, False otherwise
    """
    # Check this row on left side
    if 1 in board[row]:
        return False

    upper_diag = zip(range(row, -1, -1), range(col, -1, -1))
    for i, j in upper_diag:
        if board[i][j] == 1:
            return False

    lower_diag = zip(range(row, len(board), 1), range(col, -1, -1))
    for i, j in lower_diag:
        if board[i][j] == 1:
            return False

    return True


def nqueens_helper(board, col, solutions):
    """
    Helper function for nqueens

    Args:
        board: 2D array representing the board
        col: column to start from
        solutions: List to store found solutions

    Returns:
        None
    """
    if col >= len(board):
        solutions.append([row, col] for row, col in enumerate(board))
    for i in range(len(board)):
        if is_valid(board, i, col):
            board[i][col] = 1
            nqueens_helper(board, col + 1, solutions)
            board[i][col] = 0


def print_solutions(n):
    """
    Prints every possible solution to the N-Queens problem.

    Args:
        n: size of the board

    Returns:
        None
    """
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    elif n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * n for _ in range(n)]
    solutions = []
    nqueens_helper(board, 0, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    queens = sys.argv[1]
    if not queens.isnumeric():
        print("N must be a number")
        sys.exit(1)
    else:
        n = int(queens)
        print_solutions(n)

