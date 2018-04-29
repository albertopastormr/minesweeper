import InputParser
from Board import Board
from random import randint
from Controller import Controller
import sys


class Game(object):
    """
    Represents the abstraction of the whole minesweeper game containing a playable board
    """

    def __init__(self, size):
        self.board = Board(size, randint(1, (size*size)/2))
        self.num_bombs = self.board.get_num_bombs()
        self.available_flags = self.num_bombs
        self.finish = False

    def is_finish(self):
        return self.finish

    def play_show(self, position_to_show):
        self.board.add_show(position_to_show)
        self.check_finish()

    def play_flag(self, position_to_flag):
        if self.available_flags > 0:
            self.board.add_flag(position_to_flag)
            self.available_flags -= 1
            self.check_finish()

    def show_game(self):
        print("/////////- MINESWEEPER GAME -///////// ")
        print(self.board.show_board())

    def surrender(self):
        self.finish = True
        self.board.surrender()

    def reset(self):
        self.board.reset()

    def check_finish(self):
        self.finish = self.board.check_finish()


def main():
    size_input = input("choose a size for the minesweeper board -- > ")
    size_selected = InputParser.parse_int(size_input)
    new_game = Game(size_selected)
    controller = Controller(new_game)
    controller.execute()
    sys.exit(0)


if __name__ == '__main__':
    main()
