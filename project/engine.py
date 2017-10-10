from project.board import Board
from project.node import Node


class Engine:

    A_STAR = "A*"
    BFS = "BFS"
    DIJKSTRA = "DIJKSTRA"

    def __init__(self, board, t):
        """
        Constructor. Sets initial values for this A* engine.
        :param board: source for accessing the board and its nodes.
        """

        # Field init
        self.board = board
        self.type = t
        self.initiate_start_node()
        self.opened_nodes = [self.board.start_node]
        self.closed_nodes = []
        self.finished = False
        self.iter = 0
        self.combined_g_value = 0

    def initiate_start_node(self):
        """
        Opens the start node
        """
        self.board.start_node.open(None, None, self.type)

    def update(self):
        """
        Checks if the program is done working or not. If not, the program
        state is updated popping an item from the list of opened nodes.
        The board class is then prompted to open the neighbouring nodes.
        Lastly, the list of opened nodes is sorted based on the nodes' f-score,
        unless the type is defined as BFS. If the type is Dijkstra, the
        f_score will simply represent the g_score
        """
        if self.finished or len(self.opened_nodes) < 1:
            return  # Don't update anything if done
        self.iter += 1
        node = self.opened_nodes.pop()
        node.close()    # Visual change to get an indication of which nodes are considered "closed"
        self.board.open_neighbours(node, self)
        self.closed_nodes.append(node)
        if self.type == self.A_STAR or self.type == self.DIJKSTRA:
            self.opened_nodes.sort(key=lambda n: n.f_score, reverse=True)

    def finish(self, node):
        """
        Called when the optimal path is found.
        The nodes initiates a backtrack to reveal the optimal path,
        lastly the finished value is set to true.
        :param node:
        """
        node.backtrack(self)
        self.finished = True
        self.print_stats()

    def print_stats(self):
        print(self.type)
        print("Sum total G-value: " + self.combined_g_value.__str__())
        print("# of updates run: " + self.iter.__str__())
        print("# of open nodes when done: " + len(self.opened_nodes).__str__())
        print("# of closed (or checked) nodes when done: " + len(self.closed_nodes).__str__())
        print("# of nodes interacted with: " + (len(self.opened_nodes) + len(self.closed_nodes)).__str__())
        print("")
