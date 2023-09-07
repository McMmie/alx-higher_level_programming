#!/usr/bin/python3
import sys


def is_safe(board, row, col, N):
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True


def utility(board, row, N, solutions):
    if row == N:
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            utility(board, row + 1, N, solutions)
            board[row][col] = 0


def solve_queens(N):
    board = [[0 for x in range(N)] for x in range(N)]
    solutions = []
    utility(board, 0, N, solutions)
    return solutions


def _print(solutions):
    for column in solutions:
        lst = []
        for row in column:
            lst.append(row)
        print(lst)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)

    except ValueError:
        print("N must be a Number")
        sys.exit(1)

    solutions = solve_queens(N)
    _print(solutions)
