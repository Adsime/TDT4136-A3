from project.board import Board
import time
from project.astar import AStar


board = Board("../boards/board-1-3.txt")
engine = AStar(board)
while True:
    engine.update()
    board.window.update()
    time.sleep(0.2)
