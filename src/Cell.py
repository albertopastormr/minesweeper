from enum import Enum


class State(Enum):
    HIDDEN = 0
    FLAG = 1


class Cell(object):
    """
    Represents a unique cell which can hold bombs

    Atributtes:
        - bomb_distance: An integer which represents the distance to the nearest bomb
    """

    def __init__(self, value, def_state):
        self.bomb_distance = value
        self.state = def_state

    def __str__(self):
        if self.state == State.FLAG:
            return "F"
        elif self.state == State.HIDDEN:
            return "#"
        else:
            if self.bomb_distance == 0:
                return "*"
            elif self.bomb_distance <= 4:
                    return str(self.bomb_distance)
            else:
                return " "

    def is_bomb(self):
        return self.bomb_distance == 0


