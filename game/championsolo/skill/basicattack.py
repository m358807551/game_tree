# coding=utf-8


class BasicAttack(object):

    def __init__(self, value):
        # 攻击力
        self.value = value

    def do(self, champion):
        champion.hp -= self.value
