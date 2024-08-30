
# Odd Even Cricket Game

Odd Even Cricket is a fun and simple Python game where you play a virtual game of cricket against the computer. The game involves choosing between "Odd" or "Even" and then picking a number between 1 and 10. The computer also picks a number, and the game progresses based on the outcome.

## Features

- Toss simulation with odd/even choice.
- Batting and bowling phases for both player and computer.
- Dynamic scoring with random number generation.
- Immediate game end when the target is reached.
- Option to replay the game after it ends.

## Installation

To install the Odd Even Cricket Game, simply use pip:

```sh
pip install OddEvenGame
```

## How to Use

After installation, you can start playing the game by importing the package and calling the `start()` function.

### Example

```python
import oddevengame
oddevengame.start()
```

## Game Flow

1. **Toss**: Choose "Odd" or "Even" and pick a number between 1 and 10. The computer does the same, and the sum determines the winner of the toss.
2. **Batting/Bowling**: Depending on the toss result, either you or the computer will bat first. The game will then simulate each inning, with the goal being to outscore the opponent.
3. **Winning**: The game automatically ends when one player surpasses the other's score, and a winner is declared.
4. **Replay Option**: After the game ends, you will be asked if you want to play again.

## Requirements

- Python 3.8 or higher

## License

This project is licensed under the MIT License.

## Author

Developed by Siddharth Yadav.

## Links

- [GitHub Repository](https://github.com/siddharthdis/OddEvenGame)
- [PyPI Package](https://pypi.org/project/OddEvenGame/)

