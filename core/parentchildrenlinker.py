# coding=utf-8


class ParentChildrenLinker(object):
    def __init__(self, parent, children):
        self._parent = parent
        self._children = children

    def do(self):
        for child in self._children:
            child.parent = self._parent
            self._parent.children.append(child)
