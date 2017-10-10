from tkinter import *
from project.node import Node


class Board:

    A_STAR = "A*"
    BFS = "BFS"
    DIJKSTRA = "DIJKSTRA"

    def __init__(self, file_name, t):
        """
        Constructor. Sets the initial values of the board class.
        Will also load a given file and make a matrix based on the contents.
        :param file_name: str
        :param t: str
        """
        # Field init
        self.lines = None
        self.goal_node = None
        self.start_node = None
        self.cols = 0
        self.rows = 0
        self.rows = 0
        self.window = Tk()
        self.algorithm_type = t
        self.window.wm_title(self.algorithm_type)

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
        """
        Calculates the rows and columns for the board
        """
        for line in self.lines:
            self.rows += 1
            if self.cols == 0:
                for symbol in line:
                    if symbol == "\n":
                        break
                    self.cols += 1

    def init_board(self):
        """
        Generates a unique node for every index in the matrix (board)
        """
        for y, line in enumerate(self.lines):
            for x, symbol in enumerate(line):
                if symbol == "\n":
                    continue
                node = Node(self.window, x, y, symbol)
                self.check_for_special(node)    # Needed to set start and goal node
                self.board[y][x] = node

    def check_for_special(self, node):
        """
        Determines if a node is either a start or a goal node.
        The appropriate pointers are assigned in case.
        :param node: Node
        """
        if node.isGoal:
            self.goal_node = node
        elif node.isStart:
            self.start_node = node

    def open_neighbours(self, node, engine):
        """
        Opens all the neighbouring nodes to a given node. Will do
        certain actions based on the node type and algorithm type.
        :param node: Node
        :param engine: Engine
        """
        for child in self.check_neighbours(node):
            if child.open(node, self.goal_node, self.algorithm_type):
                if child.isGoal:
                    engine.finish(child)
                    return
                if self.algorithm_type == self.BFS:
                    engine.opened_nodes.insert(0, child)
                else:
                        engine.opened_nodes.append(child)

    def check_neighbours(self, node):
        """
        Checks if there are Node objects present to the north,
        east, south and west of a given Node.
        :param node: Node
        :return: array of Node objects
        """
        nodes = []
        if 0 <= node.y + 1 < self.rows:
            nodes.append(self.board[node.y + 1][node.x])

        if 0 <= node.x + 1 < self.cols:
            nodes.append(self.board[node.y][node.x + 1])

        if 0 <= node.y - 1 < self.rows:
            nodes.append(self.board[node.y - 1][node.x])

        if 0 <= node.x - 1 < self.cols:
            nodes.append(self.board[node.y][node.x - 1])
        return nodes
