from tkinter import Canvas


class SymbolValues:

    def __init__(self, color, g_score):
        self.color = color
        self.g_score = g_score


class Node(Canvas):

    HEIGHT = 60
    WIDTH = 35
    COLORS = {"A": SymbolValues("red", 0), "B": SymbolValues("gold", 0), '.': SymbolValues("white", 0),
              "#": SymbolValues("black", 0), "w": SymbolValues("blue", 100), "m": SymbolValues("gray", 50),
              "f": SymbolValues("dark green", 10), "g": SymbolValues("light green", 5), "r": SymbolValues("brown", 1)}

    def __init__(self, root, bg, height, width, border, x, y, char):
        super().__init__(root, bg=self.COLORS.get(char).color, height=self.HEIGHT, width=self.WIDTH, border=border)
        self.grid(column=x, row=y)
        self.x = x
        self.y = y
        self.char = char
        self.parent = None
        self.heuristic = 0
        self.currentG = 0
        self.baseG = 0
        self.F = 0
        self.isGoal = False
        self.isStart = False
        self.isOpened = False
        self.isWall = False

    def set_parent(self, parent):
        self.parent = parent

    def open(self, parent):
        if self.isWall:
            return False
        elif self.isOpened:
            self.check_if_better(parent)
            return False
        self.parent = parent
        self.baseG = self.COLORS.get(self.char).g_score
        if parent:
            self.currentG = parent.currentG + self.baseG
        self.F = self.currentG + self.heuristic
        self.isOpened = True
        self.config(bg="yellow")
        return True

    def check_if_better(self, node):
        calc = node.currentG + self.baseG
        if calc < self.currentG:
            self.parent = node
            self.currentG = calc
            self.F = self.currentG + self.heuristic

    def set_heuristic(self, goal_node):
        self.heuristic = abs(self.x - goal_node.x) + abs(self.y - goal_node.y)

    def reset(self):
        self.config(bg=self.COLORS.get(self.char).color)

    def backtrack(self):
        dx = ((1/4)*self.WIDTH) + 3
        dy = (3/4)*self.HEIGHT
        self.create_oval(dx,dx,dy,dy, fill="dark blue")
        if self.parent:
            self.parent.backtrack()



