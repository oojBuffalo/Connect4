import grid
import player
import traceback


# noinspection PyBroadException
class Connect4:
    """This class shall keep track of the game state and manage game control.  A single instance of the class behaves
    as a single game of Connect Four. """

    def __init__(self):
        """Constructor. Class/member variables for playing board and current player's turn."""
        self.grid = grid.Grid()
        self.player1 = player.ManualPlayer(1)
        self.player2 = player.ManualPlayer(2)
        self.players = [self.player1, self.player2]
        self.pid_turn = 1

    def play(self):
        """This method will simulate a game between two players by alternating asking each to make a move,
        until either one of them wins or the game board is full. """
        num_turn = 0
        print(self.grid.to_string())
        while not self.grid.exists_win():
            pid_turn = num_turn % 2 + 1
            self.take_turn(pid_turn)
            print(self.grid.to_string())
            num_turn += 1
        if self.grid.exists_win():
            print('Player ' + str(self.pid_turn) + ' wins!')
        else:
            print('Alas, it is a draw.')

    def take_turn(self, pid):
        """Method used trigger the choose_move() method of the appropriate player in the game."""
        plyr = self.players[pid-1]
        try:
            chosen_col_idx = plyr.choose_move()
            self.grid.place_token(plyr.pid, chosen_col_idx)
        except Exception as e:
            print(str(e))
            self.take_turn(pid)
