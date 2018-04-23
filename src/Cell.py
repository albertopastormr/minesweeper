class Cell(object):
    """
    Represents a unique cell which can hold bombs

    Atributtes:
        - bomb_distance: An integer which represents the distance to the nearest bomb
    """
    def __init__(self, value):
        self.bomb_distance = value

    def __str__(self):
        if self.bomb_distance == 0:
            return "*"
        else:
            if self.bomb_distance <= 4:
                return str(self.bomb_distance)
            else:
                return ""

    def is_bomb(self):
        return self.bomb_distance == 0


