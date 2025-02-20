# 2048 Game

This is a simple implementation of the popular game 2048 using Python and Pygame.

## Project Structure

```
2048-game
├── src
│   ├── main.py        # Entry point of the game
│   ├── game.py        # Contains the Game class for managing game state
│   ├── grid.py        # Defines the Grid class for the game grid
│   └── utils.py       # Utility functions for the game
├── requirements.txt    # Lists dependencies
└── README.md           # Project documentation
```

## Installation

To run this project, you need to have Python and Pygame installed. You can install the required dependencies using pip:

```
pip install -r requirements.txt
```

## Running the Game

After installing the dependencies, you can run the game by executing the following command:

```
python src/main.py
```

## Gameplay

The objective of the game is to slide numbered tiles on a grid to combine them and create a tile with the number 2048. Use the arrow keys to move the tiles in the desired direction. When two tiles with the same number touch, they merge into one!

## License

This project is open-source and available under the MIT License.