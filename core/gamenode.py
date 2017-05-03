# coding=utf-8


class GameNode(object):
    def __init__(self):
        self.parent = None
        self.children = []
        self.action = None
        self.weight = 0

    def get_trace(self):
        """
        按序得到从根节点到本节点这条路径上的节点。
        """
        trace = []
        node = self
        while node.parent:
            trace.append(node)
            node = node.parent
        trace.reverse()
        return trace

    def get_actions(self):
        trace = self.get_trace()
        return map(lambda x: x.action, trace)
