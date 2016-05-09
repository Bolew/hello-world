from BTNode import BNode
from BTNode import BNode

class BTree(object):
    def __init__(self, data=None):
        self.root = BNode(data)

    def expand(self):
        # Get grid, and make precisions of our turns.
        # Got the best choice, which give maximal probability of win!
        self._expand_node(self.root, -1)

    def _expand_node(self, node, item):
        if node != None:
            brd = node.data
            brd_1 = brd.copy_board()
            brd_2 = brd.copy_board()
            trial = brd.make_clever_random_move()
            if trial == 22:
                i_1, j_1 = brd.make_random_move()
                i_2, j_2 = brd.make_random_move()
            else:
                i_1, j_1 = brd.make_clever_random_move()
                i_2, j_2 = brd.make_clever_random_move()

            brd_1.set_value((i_1, j_1), item)
            brd_2.set_value((i_2, j_2), item)
            nd_1 = BNode(brd_1)
            nd_2 = BNode(brd_2)
            node.left = nd_1
            node.right = nd_2
            item = -item
            if brd_1.has_winner() == None:
                self._expand_node(nd_1, item)
            if brd_2.has_winner() == None:
                self._expand_node(nd_2, item)

    def get_best_move(self):
        val_1 = self.compute(self.root.left)
        val_2 = self.compute(self.root.right)
        if val_1 <= val_2:
            return self.root.left.data
        else:
            return self.root.right.data

    def get_best_index(self):
        best_board = self.get_best_move()
        for j in range(3):
            for i in range(3):
                if best_board.cells[j][i] == -1 and self.root.data.cells[j][i] == 0:
                    return [j, i]

    def _compute_value(self, node):
        if node.data.has_winner() == None:
            return self._compute_value(node.left) + self._compute_value(node.right)
        else:
            return node.data.has_winner()

    def compute(self, node):
        return self._compute_value(node)