# coding=utf-8
from core import GameTree
from game import HorseRace
from game import ChampionSolo


def main1():
    game_tree = GameTree(6, HorseRace)
    print game_tree.best_strategy(), game_tree.root.weight


def main2():
    game_tree = GameTree(10, ChampionSolo)
    print game_tree.best_strategy(), game_tree.root.weight

if __name__ == "__main__":
    main2()
