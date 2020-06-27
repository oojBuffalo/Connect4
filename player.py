"""Player Module containing player classes."""


class Player(object):
    """This class will serve as the parent class for all other players"""
    pid: int

    def __init__(self, pid):
        """Base Player Constructor."""
        self.pid = pid

    @property
    def get_pid(self):
        """Return the integer value of player's pid."""
        return self.pid

    def choose_move(self):
        """Method returns integer reflecting the index of the column in which the player wishes to place a token."""
        pass


class ManualPlayer(Player):
    """This class extends the base player class by manually prompting a user to make a move."""
    def choose_move(self):
        try:
            col_num = int(input('Player ' + str(self.pid) + ': Your turn. In which column do you wish to play?\n')) - 1
        except ValueError:
            raise
        return col_num
