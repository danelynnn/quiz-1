# quiz-1

This is an enterprise ready implementation of tic tac toe, by Allie. The game is accessible through the Game class in tic_tac_toe.py, and can be used as follows:

```
from tic_tac_toe import Game, toString

game = Game(4)
```

The class has included functions for displaying the board, along with state, as follows:

```
> game.draw()

   |   |   |
---+---+---+---
   |   |   |
---+---+---+---
   |   |   |
---+---+---+---
   |   |   |

===============
game state is: pending
===============
```

Moves are made through the move function, where the class will perform state-of-the-art board analysis algorithms to detect a victory:

```
> game.move(3, 1)
> game.draw()

   |   |   |
---+---+---+---
   |   |   | X
---+---+---+---
   |   |   |
---+---+---+---
   |   |   |

===============
game state is: pending
===============
```

State can be accessed through the state variable, because I couldn't be fucked to make an accessor (sprint 2, trust):

```
> ...
> game.draw()
 X | O | X |
---+---+---+---
 X | O | O | O
---+---+---+---
   | X |   |
---+---+---+---
   |   |   |

===============
game state is: O wins
===============

> game.state
2
```

Game states are as follows:

```
0: pending
1: player 1 has won
2: player 2 has won
.
.
.
-69: you will be accepted by your parents
etc...
```
