from project.board import Board
import time
from project.astar import AStar
# Field init
task = 1
board = 5



files = {
    1: "../boards/board-1-1.txt",
    2: "../boards/board-1-2.txt",
    3: "../boards/board-1-3.txt",
    4: "../boards/board-1-4.txt",
    5: "../boards/board-2-1.txt",
    6: "../boards/board-2-2.txt",
    7: "../boards/board-2-3.txt",
    8: "../boards/board-2-4.txt",
}


active_boards = []
active_engines = []


def assign_task(x):
    Board.style = x
    if x == 1 or x == 2:
        b = Board(files[board])
        active_boards.append(b)
        active_engines.append(AStar(b))
    elif x == 2:
        pass
    elif x == 3:
        pass


assign_task(task)

"""
Game loop. Will trigger and engine update and refresh the window.
Refresh rate can be edited in the time.sleep method.
"""
while True:
    for engine in active_engines:
        engine.update()
    for board in active_boards:
        board.window.update()
    #engine.update()
    #board.window.update()
    #time.sleep(0.01)
