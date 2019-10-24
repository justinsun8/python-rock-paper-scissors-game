#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random
moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass
# Parent Player Class


class RandomPlayer(Player):

    def move(self):
        hand = random.choice(moves)
        return hand
# Chooses an option at random


class HumanPlayer(Player):

    def move(self):
        hand = input("What do you choose: rock, paper, or scissors? ")
        while hand not in moves:
            if hand.lower() == "quit":
                quit()
            else:
                print("Sorry, choose rock, paper, or scissors")
                hand = input("What do you choose: rock, paper, or scissors? ")
            else:
                return hand

# Human player requests input from the user
# If input is not valid, return error
# Returns input


class ReflectPlayer(Player):

    def __init__(self):
        Player.__init__(self)
        self.their_move = random.choice(moves)

    def move(self):
            hand = self.their_move
            return hand

    def learn(self, my_move, their_move):
        self.their_move = their_move
# First hand is a random selection
# Next 2 mirror the players inputs


class CyclePlayer(Player):

    def __init__(self):
        Player.__init__(self)
        self.step = -1

    def move(self):
        while self.step <= len(moves):
            self.step += 1
            return moves[self.step]
# Cycles through options in moves


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))
# Beats function used to establish scoring


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        result = Game.score(self, move1, move2)
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def score(self, move1, move2):
        if beats(move1, move2):
            print(f"Player 1: {move1}  Player 2: {move2}")
            print("Player 1 won the round!")
            self.p1_score += 1
        elif beats(move2, move1):
            print(f"Player 1: {move1}  Player 2: {move2}")
            print("Player 2 won the round!")
            self.p2_score += 1
        else:
            print(f"Player 1: {move1}  Player 2: {move2}")
            print("Tie")

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        print(f"Score: Player 1: {self.p1_score} Player 2: {self.p2_score}")
        if self.p1_score > self.p2_score:
            print("Player 1 wins the match!")
        elif self.p2_score > self.p1_score:
            print("Player 2 Wins the match!")
        else:
            print("Players Tie!")
        print("Game over!")


if __name__ == '__main__':

    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
