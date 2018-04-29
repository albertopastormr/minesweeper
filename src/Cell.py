from enum import Enum


class Status(Enum):
    HIDDEN = 0
    FLAG = 1
    SHOW = 2


class Position(object):
    """
    Represents the position (x,y) of a single cell in a board
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Cell(object):
    """
    Represents a unique cell which can hold bombs

    Atributtes:
        - bomb_distance: An integer which represents the distance to the nearest bomb
    """

    def __init__(self, value, def_state):
        self.bomb_distance = value
        self.status = def_state

    def __str__(self):
        if self.status == Status.FLAG:
            return "F"
        elif self.status == Status.HIDDEN:
            return "#"
        elif self.status == Status.SHOW:
            if self.bomb_distance == 0:
                return "*"
            elif self.bomb_distance <= 4:
                    return str(self.bomb_distance)
            else:
                return " "

    def is_bomb(self):
        return self.bomb_distance == 0

    def reset(self):
        self.bomb_distance = -1
        self.status = Status.HIDDEN

    def surrender(self):
        self.status = Status.SHOW

    def set_status(self, new_status):
        if new_status == Status.FLAG:
            if self.status == Status.HIDDEN:
                self.status = Status.FLAG
        else:
            self.status = new_status

    def check_finish(self):
        if (self.status == Status.SHOW or self.status == Status.FLAG) and self.bomb_distance == 0:
            return True
        else:
            return False


