from project.board import Board
import time
from project.astar import AStar


board = Board("../boards/board-2-1.txt")
engine = AStar(board)
while True:
    engine.update()
    board.window.update()
    time.sleep(0.01)
