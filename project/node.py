from tkinter import Canvas


class SymbolValues:

    def __init__(self, color, g_score):
        self.color = color
        self.g_score = g_score


class Node(Canvas):
    """
    Class node, extends tkinter.Canvas
    """

    # Globally unique fields
    HEIGHT = 30
    WIDTH = 30
    COLORS = {"A": SymbolValues("red", 0), "B": SymbolValues("gold", 0), '.': SymbolValues("white", 0),
              "#": SymbolValues("black", 0), "w": SymbolValues("blue", 100), "m": SymbolValues("gray", 50),
              "f": SymbolValues("dark green", 10), "g": SymbolValues("light green", 5), "r": SymbolValues("brown", 1)}

    # Special chars
    GOAL = "B"
    START = "A"
    WALL = "#"

    def __init__(self, root, x, y, char):
        """
        Constructor. Sets the initial values for a Node and places in in the parent grid.
        :param root: Grid of which to display the Canvas.
        :param x: x-value of the Canvas in the Grid
        :param y: y-value of the Canvas in the Grid
        :param char: Special character used to define node properties
        """

        # Init super
        super().__init__(root, bg=self.COLORS.get(char).color, height=self.HEIGHT, width=self.WIDTH)

        # Field init
        self.x = x
        self.y = y
        self.char = char
        self.parent = None
        self.heuristic = 0
        self.currentG = 0
        self.baseG = 0
        self.f_score = 0
        self.isGoal = char == self.GOAL
        self.isStart = char == self.START
        self.isWall = char == self.WALL
        self.opened = False

        # Place the Canvas in the Grid.
        self.grid(column=x, row=y)

    def open(self, parent, goal):
        """

        :param parent: Node
        :param goal: Node
        :return: int, indicating what action to do.
        """
        if self.isWall:
            return 0
        elif self.opened:
            self.check_if_better(parent)
            return 0
        else:
            self.update_values(parent, goal)
            # This check will often reduce number of iterations needed to find the optimal route.
            if self.heuristic == 1:
                return 2
            return 1

    def update_values(self, parent, goal):
        self.baseG = self.COLORS.get(self.char).g_score
        if parent and goal:
            self.calc_heuristic(goal)
            self.currentG = parent.currentG + self.baseG
        self.parent = parent
        self.opened = True
        self.f_score = self.currentG + self.heuristic
        self.config(bg="yellow")

    def check_if_better(self, node):
        calc = node.currentG + self.baseG
        if calc < self.currentG:
            self.parent = node
            self.currentG = calc
            self.f_score = self.currentG + self.heuristic

    def calc_heuristic(self, goal_node):
        self.heuristic = abs(self.x - goal_node.x) + abs(self.y - goal_node.y)

    def reset(self):
        self.config(bg=self.COLORS.get(self.char).color)

    def backtrack(self):
        dx = ((1/4)*self.WIDTH) + 3
        dy = (3/4)*self.HEIGHT
        self.create_oval(dx, dx, dy, dy, fill="dark blue")
        if self.parent is not None:
            self.parent.backtrack()

    def close(self):
        self.config(bg="light gray")


