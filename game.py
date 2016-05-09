from BTree import BTree
from BTNode import BNode
from Board import Board


class Game(object):
    """
    Supports prosses of the game.
    """

    def __init__(self):
        self.data = Board()
        self.root = BNode(self.data)

    def __str__(self):
        """ Show game field on screen."""
        output = ""
        output += ("-------------\n")
        for i in range(3):
            place_list = [None, None, None]
            for j in range(3):
                if self.data.cells[i][j] == 1:
                    place_list[j] = "O"
                elif self.data.cells[i][j] == - 1:
                    place_list[j] = "X"
                else:
                    place_list[j] = " "

            output +="| {0} | {1} | {2} |\n".format(place_list[0], place_list[1], place_list[2])
            output += "-------------" + "\n"
        return output

    def _user_turn(self):
        """
        Provides realization of user`s turn in a game.
        """
        while True:
            try:
                print("Your turn: ")
                i, j = (int(k) for k in input().split())
                if (0 <= i <= 2) and (0 <=j <= 2) and (self.data.cells[i][j] == 0):
                    self.data.set_value((i,j), 1)
                    print(self)
            except:
                print("Your turn is`t correct. Try again!")
            else:
                break

    def _comp_turn(self):
        """
        Provides realization of computer turn in a game.
        """
        board_copy = self.data.copy_board()
        root = BNode(board_copy)
        new_tree = BTree()
        new_tree.root = root
        new_tree.expand()
        i, j = (int(k) for k in new_tree.get_best_index())
        self.data.set_value([i, j], -1)
        print("Ей-айовий turn:")
        print(self)
    def process(self):
        """
        Provides process of the game.
        """
        inp = input("Choose your turn first(f) or second(s): ")
        while self.data.has_winner() == None:
            if inp == "f":
                self._user_turn()
            else:
                self._comp_turn()
            print()
            if self.data.has_winner() != None:
                break
            if inp == "f":
                self._comp_turn()
            else:
                self._user_turn()
        if self.data.has_winner() > 0:
            print("You have won)))")
        elif self.data.has_winner() < 0:
            print("You have lost(((")
        else:
            print("Draw!")

game = Game()
game.process()