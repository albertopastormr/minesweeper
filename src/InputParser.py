from Cell import Position


class ParseException(Exception):
    """
    Represents an exception which occurs when the program finds a problem parsing an input
    """
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


def parse_coordinates(str_input):
    input_numbers = str_input.split(" ")
    if len(input_numbers) == 2:
        if input_numbers[0].isdigit() and input_numbers[1].isdigit():
            return Position(int(input_numbers[0]), int(input_numbers[1]))
        else:
            raise ParseException("ERROR: coordinates must be represented by two positive integers")
    else:
        raise ParseException("ERROR: needed only 2 coordinates <x,y>")


def parse_int(str_int):
    if str_int.isdigit():
        return int(str_int)
    else:
        raise ParseException("ERROR: needed a integer as input")
