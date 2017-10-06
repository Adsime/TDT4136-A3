from project.board import Board
import time
from project.astar import AStar

# Field init
board = Board("../boards/board-2-1.txt")
engine = AStar(board)

"""
Game loop. Will trigger and engine update and refresh the window.
Refresh rate can be edited in the time.sleep method.
"""
while True:
    engine.update()
    board.window.update()
    time.sleep(0.01)
