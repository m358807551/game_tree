# coding=utf-8
from game.basegame import BaseGame


class ChampionSolo(BaseGame):

    @classmethod
    def evaluate(cls, ind):
        human1_actions = ind[::2]
        human2_actions = ind[1::2]
        human1_hp = 300
        human2_hp = 400

        for act1, act2 in zip(human1_actions, human2_actions):
            human2_hp -= act1
            human1_hp -= act2
        return human1_hp - human2_hp

    @classmethod
    def get_choices(cls, ind):
        # A turn
        if not (len(ind) % 2):
            return [50]
        else:
            return [40]
