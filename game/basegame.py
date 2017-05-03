# coding=utf-8


class BaseGame(object):

    @classmethod
    def evaluate(cls, ind):
        raise NotImplementedError

    @classmethod
    def get_choices(cls, ind):
        raise NotImplementedError
