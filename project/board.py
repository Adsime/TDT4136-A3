from tkinter import *
from random import randint
import time


class Board:

    COLORS = ["blue", "red", "green", "black", "white", "yellow", "purple", "gold"]
    SYMBOL_MAP = {'A': "red", 'B': "green", '.': "white", '#': "gray"}
    DIM = 40

    def __init__(self, file_name):
        self.lines = None
        self.cols = 0
        self.rows = 0
        self.window = Tk()
        self.read_file(file_name)
        self.calculate_dim()
        self.board = [[None] * self.cols for i in range(self.cols)]
        self.init_board()

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
        for i, line in enumerate(self.lines):
            for j, symbol in enumerate(line):
                if symbol == "\n":
                    continue
                c = Canvas(self.window, bg=self.SYMBOL_MAP.get(symbol), height=self.DIM, width=self.DIM, border=0)
                c.grid(column=j, row=i)
                self.board[i][j] = c

    def loop(self):
        x = randint(0, self.cols-1)
        y = randint(0, self.rows-1)
        c = self.COLORS[randint(0, len(self.COLORS))-1]
        o = self.board[y][x]
        if isinstance(o, Canvas):
            o.config(bg=c)






