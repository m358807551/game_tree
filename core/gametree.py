# coding=utf-8
from gamenode import GameNode
from parentchildrenlinker import ParentChildrenLinker


class GameTree(object):
    def __init__(self, deep, game):
        """
        @evaluate: 计算一个节点的权重的函数
        """
        self.deep = deep
        self.root = GameNode()
        self._generate(self.root, self.deep, game.get_choices)
        self._set_weights(game.evaluate)

    @staticmethod
    def _generate(root, deep, get_choices):
        """
        生成深度为 self.deep 的博弈树。
        """
        if not deep:
            return
        # 已经选择的动作序列
        children = []
        for action in get_choices(root.get_actions()):
            child = GameNode()
            child.action = action
            children.append(child)
        ParentChildrenLinker(root, children).do()

        for child in children:
            GameTree._generate(child, deep - 1, get_choices)

    def get_leaves(self):
        leaves = []

        def get_leaves(root):
            for child in root.children:
                if not child.children:
                    leaves.append(child)
                else:
                    get_leaves(child)

        get_leaves(self.root)

        return leaves

    def get_traces(self):
        return map(lambda x: x.get_trace(), self.get_leaves())

    def get_strategies(self):
        return map(lambda x: x.get_actions(), self.get_leaves())

    def _set_weights(self, evaluate):
        """
        设置博弈树中每个节点的权重。
        """
        def set_weight(node, deep):
            """
            计算并设置一个节点和其子孙节点的权重。
            @deep: 当前层数。
            """
            # 叶子节点
            if not node.children:
                node.weight = evaluate(node.get_actions())
                return node.weight
            else:
                child_weights = map(lambda x: set_weight(x, deep + 1), node.children)
                node.weight = max(child_weights) if deep % 2 else min(child_weights)
                return node.weight

        set_weight(self.root, 1)

    def best_strategy(self):
        def best_node(node, deep):
            if not node.children:
                return node
            children = sorted(node.children, key=lambda x: x.weight)
            best_child = children[-1] if deep % 2 else children[0]
            return best_node(best_child, deep+1)

        best_leaf = best_node(self.root, 1)
        return best_leaf.get_actions()
