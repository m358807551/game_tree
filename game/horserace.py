# coding=utf-8
# 田忌赛马

from basegame import BaseGame


class HorseRace(BaseGame):

    @classmethod
    def evaluate(cls, ind):
        human1_actions = ind[::2]
        human2_actions = ind[1::2]
        value = 0
        for a1, a2 in zip(human1_actions, human2_actions):
            if a1 > a2:
                value += 1
            elif a1 < a2:
                value -= 1
        return value

    @classmethod
    def get_choices(cls, ind):
        # A turn
        if not(len(ind) % 2):
            choices = {2, 4, 6} - set(ind[::2])
        else:
            choices = {1, 3, 5} - set(ind[1::2])
        return choices
