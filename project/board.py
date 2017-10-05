from tkinter import *
from project.node import Node
from random import randint


class Board:

    GOAL = "B"
    START = "A"
    WALL = "#"
    COLORS = ["blue", "red", "green", "black", "white", "yellow", "purple", "gold"]
    SYMBOL_MAP = {START: "red", GOAL: "green", '.': "white", WALL: "gray"}
    DIM = 40

    def __init__(self, file_name):
        self.lines = None
        self.cols = 0
        self.rows = 0
        self.window = Tk()
        self.read_file(file_name)
        self.calculate_dim()
        self.goal_node = None
        self.start_node = None
        self.board = [[None] * self.cols for i in range(self.cols)]
        self.init_board()
        self.init_heuristic()

    def read_file(self, file_name):
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
                node = Node(self.window, self.SYMBOL_MAP.get(symbol), self.DIM, self.DIM, 0, x, y)
                self.check_for_special(symbol, node)
                self.board[y][x] = node

    def check_for_special(self, symbol, node):
        if isinstance(node, Node):
            if symbol == self.START:
                node.isStart = True
                self.start_node = node
            elif symbol == self.GOAL:
                node.isGoal = True
                self.goal_node = node
            elif symbol == self.WALL:
                node.isWall = True

    def init_heuristic(self):
        for y in range(self.rows):
            for x in range(self.cols):
                node = self.board[y][x]
                if isinstance(node, Node):
                    if node.isGoal or node.isStart:
                        continue
                    node.set_heuristic(self.goal_node)

    def loop(self):
        x = randint(0, self.cols-1)
        y = randint(0, self.rows-1)
        c = self.COLORS[randint(0, len(self.COLORS))-1]
        o = self.board[y][x]
        if isinstance(o, Canvas):
            o.config(bg=c)

    def open_neighbours(self, node, engine):
        if isinstance(node, Node):
            nodes = []
            if 0 <= node.y + 1 < self.rows:
                nodes.append(self.board[node.y + 1][node.x])

            if 0 <= node.x + 1 < self.cols:
                nodes.append(self.board[node.y][node.x + 1])

            if 0 <= node.y - 1 < self.rows:
                nodes.append(self.board[node.y - 1][node.x])

            if 0 <= node.x - 1 < self.cols:
                nodes.append(self.board[node.y][node.x-1])

            for child in nodes:
                if child and isinstance(child, Node):
                    if child.open(node):
                        if child.isGoal:
                            engine.finish(child)
                            return
                        engine.open.append(child)





