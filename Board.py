import random


class Board(object):
    """ Class which represent playing board."""
    def __init__(self):
        # x -> 1
        # 0 -> -1
        self.cells = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def __str__(self):
        return "\n".join([" ".join([str(i) for i in lst]) for lst in self.cells])

    def has_winner(self):
        """ Returns 1 if winner is 'X'; -1 if winner is 'O'; 0 if winner is not exists."""
        for i in range(3):
            our_sum = 0
            for j in range(3):
                our_sum += self.cells[i][j]
            if our_sum == 3:
                return 1
            if our_sum == -3:
                return -1
        for j in range(3):
            our_sum = 0
            for i in range(3):
                our_sum += self.cells[i][j]
            if our_sum == 3:
                return 1
            if our_sum == -3:
                return -1
        our_sum = self.cells[0][0] + self.cells[1][1] + self.cells[2][2]
        if our_sum == 3:
            return 1
        if our_sum == -3:
            return -1
        our_sum = self.cells[0][2] + self.cells[1][1] + self.cells[2][0]
        if our_sum == 3:
            return 1
        if our_sum == -3:
            return -1
        for i in range(3):
            for j in range(3):
                if self.cells[i][j] == 0:
                    return None
        return 0

    def make_random_move(self):
        """ Returns tuple with random coordinates."""
        list_of_moves = []
        for i in range(3):
            for j in range(3):
                if self.cells[i][j] == 0:
                    list_of_moves.append((i, j))
        return random.choice(list_of_moves)

    def make_clever_random_move(self):
        """
        Returns tuple with clever coordinates.
        If computer can get victory it return those turn.
        """
        player = -1
        move_list = []
        for i in range(3):
            our_sum = 0
            for j in range(3):
                if self.cells[i][j] == player:
                    our_sum += 1
            if our_sum == 2:
                for k in range(3):
                    if self.cells[i][k] == 0:
                        move_list.append((i, k))
                        break
        for j in range(3):
            our_sum = 0
            for i in range(3):
                if self.cells[i][j] == player:
                    our_sum += 1
            if our_sum == 2:
                for k in range(3):
                    if self.cells[k][j] == 0:
                        move_list.append((k, j))
        our_sum = self.cells[0][0] + self.cells[1][1] + self.cells[2][2]
        if our_sum == -2:
            if self.cells[0][0] == 0:
                move_list.append((0, 0))
            elif self.cells[1][1] == 0:
                move_list.append((1, 1))
            elif self.cells[2][2] == 0:
                move_list.append((2, 2))
        our_sum = self.cells[0][2] + self.cells[1][1] + self.cells[2][0]
        if our_sum == -2:
            if self.cells[0][2] == 0:
                move_list.append((0, 2))
            elif self.cells[1][1] == 0:
                move_list.append((1, 1))
            elif self.cells[2][0] == 0:
                move_list.append((2, 0))
        if len(move_list) != 0:
            return random.choice(move_list)
        if len(move_list) == 0:
            return 22 # Why 22? It is a little pashalka from a future big developer. In this day is my birthday)))

    def copy_board(self):
        """ Copy original board."""
        new_board = Board()
        for i in range(3):
            for j in range(3):
                new_board.cells[i][j] = self.cells[i][j]
        return new_board

    def set_value(self, tuple, item):
        """ Gets tuple with coordinates, and sets it to the board."""
        self.cells[tuple[0]][tuple[1]] = item
