import project.board as board
import time


o = board.Board("../boards/board-1-3.txt")
while True:
    #o.loop()
    o.window.update()
    time.sleep(1 / 60)
