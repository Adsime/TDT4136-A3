from tkinter import *
from project.node import Node
from random import randint


class Board:

    def __init__(self, file_name):
        """
        Constructor. Sets the initial values of the board class.
        Will also load a given file and make a matrix based on the contents.
        :param file_name: str
        """
        # Field init
        self.lines = None
        self.goal_node = None
        self.start_node = None
        self.cols = 0
        self.rows = 0
        self.rows = 0
        self.window = Tk()

        # Read file and calculate dimensions
        self.read_file(file_name)
        self.calculate_dim()

        # Init game board
        self.board = [[None] * self.cols for i in range(self.rows)]
        self.init_board()

    def read_file(self, file_name):
        """
        Helper method to read a file and get its contents in an array.
        :param file_name: str
        """
        self.lines = open(file_name).readlines()

    def calculate_dim(self):
        for line in self.lines:
            self.rows += 1
            if self.cols == 0:
                for symbol in line:
                    if symbol == "\n":
                        break
                    self.cols += 1

    def init_board(self):
        for y, line in enumerate(self.lines):
            for x, symbol in enumerate(line):
                if symbol == "\n":
                    continue
                node = Node(self.window, x, y, symbol)
                self.check_for_special(node)
                self.board[y][x] = node

    def check_for_special(self, node):
        if node.isGoal:
            self.goal_node = node
        elif node.isStart:
            self.start_node = node

    def open_neighbours(self, node, engine):
        if isinstance(node, Node):
            nodes = []
            self.check_neighbours(node, nodes)
            for child in nodes:
                if child and isinstance(child, Node):
                    action = child.open(node, self.goal_node)
                    if action == 2:
                        self.open_neighbours(child, engine)
                        return
                    if action == 1:
                        if child.isGoal:
                            engine.finish(child)
                            return
                        engine.open.append(child)

    def check_neighbours(self, node, nodes):
        if 0 <= node.y + 1 < self.rows:
            nodes.append(self.board[node.y + 1][node.x])

        if 0 <= node.x + 1 < self.cols:
            nodes.append(self.board[node.y][node.x + 1])

        if 0 <= node.y - 1 < self.rows:
            nodes.append(self.board[node.y - 1][node.x])

        if 0 <= node.x - 1 < self.cols:
            nodes.append(self.board[node.y][node.x - 1])
