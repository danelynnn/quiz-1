from tic_tac_toe import Game, toString

size = int(input("how big??? "))

game = Game(size)
game.draw()

while game.state == 0:
    move = input(
        f"{toString(game.turn)}'s turn, what's yer move [input format: 'x y']: "
    )
    x, y = move.split(" ")
    x, y = int(x), int(y)

    if game.board[y][x] > 0:
        print("yoouuu can't do that")
        continue

    game.move(x, y)
    game.draw()
