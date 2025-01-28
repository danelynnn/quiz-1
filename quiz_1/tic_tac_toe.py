from enum import Enum

WIN = 3


def toString(player):
    if player == 0:
        return " "
    elif player == 1:
        return "X"
    elif player == 2:
        return "O"


def countDirection(board, x, y, xd, yd, player):
    # count how many same marks are in the direction, then
    # count how many marks are in the opposite direction and add them up (if not finished yet)
    count = 1
    xtest, ytest = x, y
    while (
        xtest + xd >= 0
        and xtest + xd <= len(board) - 1
        and ytest + yd >= 0
        and ytest + yd <= len(board) - 1
    ):
        xtest += xd
        ytest += yd

        if board[ytest][xtest] == player:
            count += 1
            if count == WIN:
                return count
        else:
            break

    xtest, ytest = x, y
    while (
        xtest - xd >= 0
        and xtest - xd <= len(board) - 1
        and ytest - yd >= 0
        and ytest - yd <= len(board) - 1
    ):
        xtest -= xd
        ytest -= yd

        if board[ytest][xtest] == player:
            count += 1
            if count == WIN:
                return count
        else:
            break

    return count


class Game:
    def __init__(self, size):
        self.board = [[0 for i in range(size)] for j in range(size)]
        self.turn = 1
        self.state = 0

    def move(self, x, y):
        self.board[y][x] = self.turn

        # check for a win
        # for each direction, count how many same marks
        # if ever reach 3, win
        if countDirection(self.board, x, y, -1, 0, self.turn) == WIN:  # west
            self.state = self.turn
        elif countDirection(self.board, x, y, -1, -1, self.turn) == WIN:  # northwest
            self.state = self.turn
        elif countDirection(self.board, x, y, 0, -1, self.turn) == WIN:  # north
            self.state = self.turn
        elif countDirection(self.board, x, y, -1, 1, self.turn) == WIN:  # southwest
            self.state = self.turn

        # switch players
        self.turn = (self.turn % 2) + 1

    def draw(self):
        print()
        for r in range(len(self.board)):
            line = []
            line.append(" ")
            for c in range(len(self.board[r])):
                line.append(toString(self.board[r][c]))
                if c < len(self.board[r]) - 1:
                    line.append(" | ")
            line.append(" ")
            print("".join(line))

            separator_str = ["-+-" if s == " | " else ("-" * len(s)) for s in line]
            if r < len(self.board[r]) - 1:
                # TODO: add plusses for crosses
                print("".join(separator_str))

        print()
        print("=" * 69)
        status = "pending"
        if self.state == 1:
            status = "X wins"
        elif self.state == 2:
            status = "O wins"
        print(f"game state is: {status}")
        print("=" * 69)
        print()
