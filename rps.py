#!/usr/bin/env python3
import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""


"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    moves = ['rock', 'paper', 'scissors']

    def __init__(self):
        self.my_move = self.moves
        self.their_move = random.choice(self.moves)

    def learn(self, my_move, their_move):  # storing player moves
        self.my_move = my_move
        self.their_move = their_move


class HumanPlayer(Player):  # human user
    def move(self):
        while True:
            move_human = input("Rock, paper, scissors? > ")
            if move_human.lower() in self.moves:
                return move_human.lower()
            elif move_human.lower() == 'exit':
                exit()


class RandomPlayer(Player):  # chooses move at random
    def move(self):
        return random.choice(self.moves)


class RepeatPlayer(Player):
    def move(self):
        return 'rock'


class ReflectPlayer(Player):  # remembers opponents last move
    def move(self):
        return self.their_move


class CyclePlayer(Player):  # remembers last round move
    def move(self):
        if self.my_move == self.moves[0]:
            return self.moves[1]
        elif self.my_move == self.moves[1]:
            return self.moves[2]
        else:
            return self.moves[0]


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score_p1 = 0
        self.score_p2 = 0

    def beats(self, one, two):
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        if self.beats(move1, move2):
            self.score_p1 += 1
            winner = '** PLAYER ONE WINS **'
        elif move1 == move2:
            self.score_p1 = self.score_p1
            self.score_p2 = self.score_p2
            winner = '** TIE **'
        else:
            self.score_p2 += 1
            winner = '** PLAYER TWO WINS **'
        print(
            f"> You played {move1}."
            f"\n> Opponent played {move2}."
            f"\n{winner}"
            f"\nScore: Player One ( {self.score_p1} ),"
            f"Player Two ( {self.score_p2} )"
        )
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Rock Paper Scissors, Go!")
        print("This game is for 3 rounds")
        for round in range(int(3)):
            print(f"\nRound {round + 1} --")
            self.play_round()
        if self.score_p1 == self.score_p2:
            print(
                f"\n-- The game ended in a tie! --"
                f"\nScore: Player one ( {self.score_p1} ),"
                f"Player two ( {self.score_p2} )"
            )
        elif self.score_p1 > self.score_p2:
            print(
                f"\n-- Player ONE has won! --"
                f"\nScore: Player one ( {self.score_p1} ),"
                f"Player two ( {self.score_p2} )"
            )
        else:
            print(
                f"\n-- Player TWO has won! --"
                f"\nScore: Player one ( {self.score_p1} ),"
                f"Player two ( {self.score_p2} )*"
            )


if __name__ == '__main__':
    game = Game(HumanPlayer(), random.choice(
        [RandomPlayer(), RepeatPlayer(), ReflectPlayer(), CyclePlayer()]))
    game.play_game()
