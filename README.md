# Ultimate Tic-Tac-Toe

Ultimate Tic-Tac-Toe is an extension of Tic-Tac-Toe that offers a big increase in complexity and strategy.

This project is written in Python. You can find a JavaScript version here:\
https://j-freddy.github.io/projects/ultimate-tictactoe/

## Prerequisites

### Install Python

Python 3.7.7 or greater is recommended. Check with:

```console
$ python3 --version
```

Download: https://www.python.org/downloads/

### Install Pygame

```console
$ python3 -m pip install -U pygame --user
```

## Playing the game

### Player options

This program is currently set to "Player vs AI". You can change the settings by editing `player_x` and `player_o` in `game.py`.

### Running the game

```console
$ python3 main.py
```

Alternatively, if you have Visual Studio Code, you can open the folder. Then, open `main.py` and click the triangle on the top right.

## Game instructions

- Each small 3×3 board is a local board, and the larger 3×3 board is the global board.
- When a player plays a move, it sends their opponent to its relative location on the global board.
- If a player wins on a local board, that board gets captured by the player.
- If a player is sent to a local board that is full or captured, then that player may choose any other board.
- A player wins by winning on the global board.

## Programming notes

### Board result

Stored in `winner` attribute:

- `None` - In progress
- `CellValue.O` - O wins
- `CellValue.X` - X wins
- `CellValue.Empty` - Draw<sup>[1](#f1)</sup>

<a name="f1"><sup>[1]</sup></a> If a local board ends in a draw, it has an empty value in the global board.

### Next steps

Currently, the AI makes random moves.

I plan to implement an AI that uses MCTS.\
https://www.geeksforgeeks.org/ml-monte-carlo-tree-search-mcts/
