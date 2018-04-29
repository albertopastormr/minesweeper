from Cell import *
from random import randint


class Board(object):
    """
    Represents a matrix of cells

    Attributes:
        - _board: matrix of Cell (using lists)
        - _size: size of _board (int)
        - _num_bombs: number of the bombs that _board has
    """

    def __init__(self, _size, _num_bombs):
        self._size = _size
        self._num_bombs = _num_bombs
        self._board = []
        for i in range(_size):
            x = []
            for j in range(_size):
                x.append(Cell(-1, Status.HIDDEN))
            self._board.append(x)
        self._init_bombs_board()

    def _init_bombs_board(self):
        rand_bomb_positions = [(randint(0, self._size - 1), randint(0, self._size - 1)) for i in range(self._num_bombs)]
        for x in rand_bomb_positions:
            self._set_bomb_at_pos(x[0], x[1])

    def _get_cell_at_pos(self, x_coord, y_coord):
        return self._board[x_coord][y_coord]

    def get_num_bombs(self):
        return self._num_bombs

    def get_size(self):
        return self._size

    def _set_bomb_at_pos(self, x_coord, y_coord):
        self.__set_cell_value_at_pos(0, x_coord, y_coord)
        self._notify_board_new_bomb(x_coord, y_coord)

    def __set_cell_value_at_pos(self, value, x_coord, y_coord):
        self._board[x_coord][y_coord].bomb_distance = value

    def _notify_board_new_bomb(self, x_bomb, y_bomb):
        for i in range(self._size):
            for j in range(self._size):
                new_distance_value = max(abs(x_bomb - i), abs(y_bomb - j))
                if self._get_cell_at_pos(i, j).bomb_distance == -1 or self._get_cell_at_pos(i, j).bomb_distance > new_distance_value:
                    self.__set_cell_value_at_pos(new_distance_value, i, j)

    def show_board(self):
        board_str = ""
        pprint_str = " "
        for i in range(self._size):
            board_str += "|"
            pprint_str += "---"
            for j in range(self._size):
                board_str += " " + str(self._get_cell_at_pos(i, j)) + " "
            board_str += "|\n"
        pprint_str += "\n"
        return pprint_str + board_str + pprint_str

    def reset(self):
        for i in range(self._size):
            for j in range(self._size):
                self._board[i][j].reset()
        self._init_bombs_board()

    def surrender(self):
        for i in range(self._size):
            for j in range(self._size):
                self._board[i][j].surrender()

    def add_flag(self, position_flag):
        self._board[position_flag.x][position_flag.y].set_status(Status.FLAG)

    def add_show(self, position_show):
        self._board[position_show.x][position_show.y].set_status(Status.SHOW)

    def check_finish(self):
        is_finish = True
        i = j = 0
        while i in range(self._size) and is_finish:
            while j in range(self._size) and is_finish:
                if self._board[i][j].check_finish:
                    is_finish = False
        return is_finish
