from tkinter import Canvas


class Node(Canvas):

    def __init__(self, root, bg, height, width, border, x, y):
        super().__init__(root, bg=bg, height=height, width=width, border=border)
        self.grid(column=x, row=y)
        self.x = x
        self.y = y
        self.parent = None
        self.heuristic = 0
        self.G = 0
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
            return self.check_if_better(parent)
        self.parent = parent

        self.isOpened = True
        self.config(bg="yellow")
        return True

    def check_if_better(self, node):
        return False

    def set_heuristic(self, goal_node):
        self.heuristic = abs(self.x - goal_node.x) + abs(self.y - goal_node.y)
        self.create_text(20, 20, fill="black", text=self.heuristic)

    def backtrack(self):
        self.config(bg="blue")
        if self.parent:
            self.parent.backtrack()
