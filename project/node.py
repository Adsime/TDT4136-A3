from tkinter import Canvas


class SymbolValues:

    def __init__(self, color, g_score):
        """
        Used to store values for easy referral in maps.
        :param color:
        :param g_score:
        """
        self.color = color
        self.g_score = g_score


class Node(Canvas):
    """
    Class node, extends tkinter.Canvas
    """

    # Globally unique fields
    HEIGHT = 30
    WIDTH = 30
    COLORS = {"A": SymbolValues("dark orange", 0), "B": SymbolValues("gold", 0), '.': SymbolValues("white", 0),
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
        self.text = None

        # Place the Canvas in the Grid.
        self.grid(column=x, row=y)

    def open(self, parent, goal):
        """
        Returns an int to indicate what was done.
        If the node is a wall, just return.
        If the node is already opened, a check is made to see if the suggested
        parent is a better alternative.
        Otherwise, object values are updated.
        A check is made to see if the node is next to the goal. If it is, a value is returned indicating this.
        :param parent: Node
        :param goal: Node
        :return: int, indicating what action to do.
        """
        if self.isWall:     # No actions are needed
            return 0
        elif self.opened:
            self.check_if_better(parent)    # Make a test on the suggested parent
            return 0
        else:
            self.update_values(parent, goal)
            return 1

    def update_values(self, parent, goal):
        """
        Will update Node metadata and display a symbol on the Canvas to indicate that the node is opened.
        :param parent: Node
        :param goal: Node
        """
        self.baseG = self.COLORS.get(self.char).g_score
        if parent and goal:     # Avoiding errors when opening the start node
            self.calc_heuristic(goal)
            self.currentG = parent.currentG + self.baseG
        self.parent = parent
        self.opened = True
        self.f_score = self.currentG + self.heuristic
        if not self.isStart and not self.isGoal:
            self.config(bg="yellow")
        self.text = self.create_text(self.WIDTH / 2, self.HEIGHT / 2, text="*", fill="black")

    def check_if_better(self, parent):
        """
        Checks if a suggested parent node is better suited to be parent than the current parent.
        :param parent: Node
        """
        calc = parent.currentG + self.baseG
        if calc < self.currentG:
            self.parent = parent
            self.currentG = calc
            self.f_score = self.currentG + self.heuristic

    def calc_heuristic(self, goal_node):
        """
        Calculates the heuristic (Mannheim heuristic) for this Node.
        :param goal_node: Node
        """
        self.heuristic = abs(self.x - goal_node.x) + abs(self.y - goal_node.y)

    def reset(self):
        self.config(bg=self.COLORS.get(self.char).color)
        pass

    def backtrack(self):
        """
        Will draw a circle on the Canvas and delete the existing text on it.
        Then it will call on the parent's backtrack method.
        This is done to mark the optimal path
        """
        dx = ((1/5)*self.WIDTH) + 3
        dy = (4/5)*self.HEIGHT
        self.delete(self.text)
        self.create_oval(dx, dx, dy, dy, fill="dark blue")
        if self.parent is not None:
            self.parent.backtrack()

    def close(self):
        if not self.isStart and not self.isGoal:
            self.config(bg="light gray")
        """
        Helper method to "mark" the nodes as closed visually.
        """
        self.delete(self.text)
        self.create_text(self.WIDTH/2, self.HEIGHT/2, text="X", fill="black")


