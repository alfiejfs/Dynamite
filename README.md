## Dynamite Bot runner (in Python)

This repository contains a test harness for the game of Dynamite!, plus some simple example bots.

### Rules of the game

Dynamite! is an explosive variation of Rock, Paper, Scissors, with the added extras of dynamite and water bombs. Dynamite beats rock, paper and scissors. Water bombs beat dynamite, but lose to everything else. 

In a round each bot decides its move, and the winner gets a point. If both bots choose the same move, the round is a draw. The first to 1000 points wins the match.

- You only have 100 sticks of dynamite - trying to play dynamite 101 times will forfeit the match. 
- When a round is a tie, the point rolls over to the next round. E.g. Rock vs Rock in round one is a draw so no point is awarded and round two will be worth one points. If that is also a draw, round three will be worth two points! Otherwise round three will be back to a single point.
- It's unlikely to matter, but the maximum number of rounds is 2500.

### How to write your bot

1. Clone/download this repository
2. Create a new Python file in this folder
3. Define a function called `make_move`, which takes one parameter (the list of previous rounds) and returns a string saying what move you want to make (`'R'` / `'P'` / `'S'` / `'D'` / `'W'`).
> See [example_function_bot.py](example_function_bot.py) for the definition of a bot that only ever plays scissors.
4. Run `python bot_runner.py your_file` to check it works. (Put your actual filename in place of "your_file").
5. Run `python bot_runner.py your_file dynamite_bot` to see if you can beat a bot that uses dynamite.
6. Iterate and improve!

Note:
- Make sure you count your dynamite! There is nothing worse than losing a game at the last minute by attempting to use too much.
- The function parameter is a list of previous rounds (represented by dictionaries). Each round has two properties: the moves by each player. Your bot will always be "p1" (and your opponent "p2").This lets you check the results of previous rounds and what your opponent played.

```python
[
    {
        p1 : "R",
        p2 : "D"
    },
    {
        p1 : "W",
        p2 : "S"
    },
    etc
]
```

### Classes rather than functions

If you would like to practise writing a class, you can do so. See [example_class_bot.py](example_class_bot.py) for how to define your bot as a class. The "gamestate" parameter is a dictionary, containing a "rounds" property.

```python
{
    'rounds': [ {'p1': 'R', 'p2': 'P'}, etc ]
}
```