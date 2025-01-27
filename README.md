# Tic-Tac-Toe Perfected

This is an enterprise ready implementation of tic tac toe, by Allie. The game can be run simply as follows:

```
> python main.py

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

X's turn, what's yer move [input format: 'x y']:
```

Moves will be prompted with the given format until a player has won. The R&D department has unfortunately run out of budget to do input validation, or bounds checking, so the program is and forever will be crash-prone.

```
X's turn, what's yer move [input format: 'x y']: 3 1

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

O's turn, what's yer move [input format: 'x y']:
```

If a player has won, the program will terminate very abruptly and robotically, with the minimum required congratulations specified in the rubric:

```
O's turn, what's yer move [input format: 'x, y']: 3 1

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
```

## Documentation

The game logic is accessible through the Game class in tic_tac_toe.py, and can be used as follows:

```
from tic_tac_toe import Game

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
