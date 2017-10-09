from project.board import Board
from project.node import Node


class AStar:

    def __init__(self, board):
        """
        Constructor. Sets initial values for this A* engine.
        :param board: source for accessing the board and its nodes.
        """

        # Field init
        self.board = board
        self.initiate_start_node()
        self.open = [self.board.start_node]
        self.closed = []
        self.finished = False
        self.iter = 0

    def initiate_start_node(self):
        """
        Opens the start node
        """
        self.board.start_node.open(None, None)

    def update(self):
        """
        Checks if the program is done working or not. If not, the program
        state is updated popping an item from the list of opened nodes.
        The board class is then prompted to open the neighbouring nodes.
        Lastly, the list of opened nodes is sorted based on the nodes' f-score
        """
        if self.finished or len(self.open) < 1:
            return  # Don't update anything if done
        self.iter += 1
        node = self.open.pop()
        node.close()    # Visual change to get an indication of which nodes are considered "closed"
        self.board.open_neighbours(node, self)
        self.open.sort(key=lambda n: n.f_score, reverse=True)

    def finish(self, node):
        """
        Called when the optimal path is found.
        The nodes initiates a backtrack to reveal the optimal path,
        lastly the finished value is set to true.
        :param node:
        """
        node.backtrack()
        self.finished = True
        print(self.iter)
