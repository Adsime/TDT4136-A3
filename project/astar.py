from project.board import Board
from project.node import Node


class AStar:

    def __init__(self, board):
        self.board = board
        self.board.start_node.open(None)
        self.open = [self.board.start_node]
        self.closed = []
        self.finished = False

    def update(self):
        if self.finished:
            return
        node = self.open.pop()
        if isinstance(node, Node):
            self.board.open_neighbours(node, self)
            self.open.sort(key=lambda n: n.heuristic, reverse=True)

    def finish(self, node):
        node.backtrack()
        self.finished = True
