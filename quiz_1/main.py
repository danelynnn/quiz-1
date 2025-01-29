from tic_tac_toe import Game, toString
from datetime import datetime

game_count = 0

with open("logbook.txt", "a") as file:
    file.write("======================================\n")

    choice = True
    while choice:
        game_count += 1
        size = int(input("how big??? "))

        game = Game(size)
        game.draw()

        while game.state == 0:
            move = input(
                f"{toString(game.next)}'s turn, what's yer move [input format: 'x y']: "
            )
            x, y = move.split(" ")
            x, y = int(x), int(y)

            if game.board[y][x] > 0:
                print("yoouuu can't do that")
                continue

            game.move(x, y)
            game.draw()

        file.write("-----------------------------------\n")
        file.write(datetime.now().strftime("%B %d, %Y %H:%M:%S"))
        file.write("\n")
        file.write(f"Game of size {size} played\n")
        file.write(f"Winner was {toString(game.state)}\n")
        file.write("-----------------------------------\n")

        choice = input("do you want to play agane? ") in [
            "y",
            "yes",
            "sure",
            "uhuh",
            "fuck it why not",
        ]

    file.write(f'{game_count} game{("s" if game_count > 1 else "")} played\n')
    file.write("======================================\n")
