"""Grid Module containing the grid class."""
import numpy as np


class Grid(object):
    """The Grid class stores the game state data for a game of Connect Four."""
    """
    #       col_idx
    #    0|1|2|3|4|5|6
    #  ----------------- row_idx
    #  | O O O O O O O |   0
    #  | O O X O O O O |   1  --> X is self.grid[1,2] (type:numpy.ndarray)
    #  | O O O O O O O |   2
    #  | O O O O O O O |   3
    #  | O O O O O O O |   4
    #  | O O O O O O O |   5
    #  -----------------
    #
    """
    def __init__(self, size=(6, 7)):
        """Grid constructor.
        :param size: tuple specifying dimensions of grid in (#rows, #columns) format
        """
        self._num_rows, self._num_cols = size
        self._matrix = np.zeros(size)

    def place_token(self, pid, col):
        """Modifies values in the grid's underlying data structure to reflect the state of the grid after a player
        takes a single turn.
        :param pid: Unique player identifier (int)
        :param col: Specified column index to place player's game token (int)
        """
        if 0 not in self._matrix[:, col]:
            raise Exception("Invalid move: column number {} is already full.".format(col))
        elif col < 0 or col > self._num_cols-1:
            raise Exception("Invalid move: Column number {} doesn't exist".format(col))
        else:
            row_idx = 5 - list(np.flip(self._matrix[:, col])).index(0)
            self._matrix[row_idx, col] = pid

    def get_grid(self):
        """Returns the grid's underlying data structure in its current state."""
        return self._matrix

    def set_grid(self, mat):
        """Sets the grid's underlying (ndarray) data structure to the specified (ndarray) mat."""
        self._matrix = mat

    def exists_win(self):
        """Returns a a boolean reflecting if there exists a win on the grid in its current state."""
        return self._check_h() or self._check_v() or self._check_d()

    def _check_h(self):
        for row in range(self._num_rows):
            for col_start in range(self._num_cols-3):
                if np.unique(self._matrix[row, col_start:col_start + 4]).size == 1 and self._matrix[row, col_start] != 0:
                    return True
        return False

    def _check_v(self):
        for col in range(self._num_cols):
            for row_start in range(self._num_rows-3):
                if np.unique(self._matrix[row_start:row_start + 4, col]).size == 1 and self._matrix[row_start, col] != 0:
                    return True
        return False

    def _check_d(self):
        grid_d0 = self._matrix
        grid_d1 = np.fliplr(self._matrix)

        # helper function
        def _check_d_helper(mat):
            for offset in range(-2, 4):
                d = mat.diagonal(offset)
                for startIdx in range(d.size - 3):
                    if np.unique(d[startIdx:startIdx + 4]).size == 1 and d[startIdx] != 0:
                        return True
            return False

        return _check_d_helper(grid_d0) or _check_d_helper(grid_d1)

    def to_string(self):
        """Return string representation of underlying ndarray data structure"""
        s = ''
        hrzt_sz = 7
        vert_sz = 6
        f = lambda n: 'O' if n == 0 else ('X' if n == 1 else '+')
        for i in range(hrzt_sz * vert_sz):
            if i == 0: s += '-' * (hrzt_sz * 2 + 3) + '\n'
            if i % hrzt_sz == 0: s += '| '
            if i == 0:
                s += str(f(int(self._matrix[0][0]))) + ' '
            else:
                s += str(f(int(self._matrix[i // hrzt_sz][i % hrzt_sz]))) + ' '
            if i % hrzt_sz == hrzt_sz - 1: s += '|\n'
            if i == hrzt_sz * vert_sz - 1: s += '-' * (hrzt_sz * 2 + 3) + '\n'
        s += '--1-2-3-4-5-6-7--\n'
        s += '-----------------\n'
        return s
