from project.board import Board
import time
from project.engine import Engine

"""
HOW TO:

There are two variables which can be modified to show the assignment in question. 

task: can either be 1 or 2. Option 1 covers task 1 and 2, where option 2 covers task 3
board: index [numbers 1 through 8] indicating which board to evaluate.

The program is designed so that only these variables should be changed. Little to no
actions are made to prevent wrong input, so use the suggested input.
"""

# Field init
task = 2    # Here you can choose which task to look at. Options are 1 and 2.
board = 8   # Here you can choose which board to run through the program.


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
    """
    Will generate boards and engines.
    :param x: int
    """
    Board.style = x
    if x == 1:
        b = Board(files[board], Engine.DIJKSTRA)
        active_boards.append(b)
        active_engines.append(Engine(b, Engine.DIJKSTRA))
    elif x == 2:
        active_boards.append(Board(files[board], Engine.A_STAR))
        active_boards.append(Board(files[board], Engine.BFS))
        active_boards.append(Board(files[board], Engine.DIJKSTRA))
        active_engines.append(Engine(active_boards[0], Engine.A_STAR))
        active_engines.append(Engine(active_boards[1], Engine.BFS))
        active_engines.append(Engine(active_boards[2], Engine.DIJKSTRA))



assign_task(task)

"""
Game loop. Will trigger updates in any active engines. Will also update 
and refresh the window. Refresh rate can be edited in the time.sleep method.
"""
while True:
    for engine in active_engines:
        engine.update()
    for board in active_boards:
        board.window.update()
    time.sleep(0.01)
