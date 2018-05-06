import InputParser


class GameEndException(Exception):
    """
        Represents an exception which occurs when the program ends because of a win or a lose
    """

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class Controller(object):
    """
    Represents the main controller of the application serving as a
    input receiver and output server
    """

    def __init__(self, game):
        self.actual_game = game

    def execute(self):
        self.actual_game.show_game()
        option_input = input("command (use 'exit' to stop; type 'help' for info) --> ")
        while option_input != "exit" and not self.actual_game.is_finish():
            try:
                if option_input == "show":
                    coord_input = input("show {x_coord, y_coord} --> ")
                    coord_input = InputParser.parse_coordinates(coord_input)
                    self.actual_game.play_show(coord_input)
                    self.actual_game.show_game()
                elif option_input == "flag":
                    coord_input = input("flag {x_coord, y_coord} --> ")
                    coord_input = InputParser.parse_coordinates(coord_input)
                    self.actual_game.play_flag(coord_input)
                    self.actual_game.show_game()
                elif option_input == "surrender":
                    self.actual_game.surrender()
                    self.actual_game.show_game()
                elif option_input == "reset":
                    self.actual_game.reset()
                    self.actual_game.show_game()
                elif option_input == "help":
                    print("available commands: <show{'x coord','y_coord'}> <flag{'x coord','y_coord'}> <surrender> <reset> <help>")
                elif option_input == "save":
                    self.actual_game.save_file()
                else:
                    print("unknown command")
                    print("available commands: <show{'x coord','y_coord'}> <flag{'x coord','y_coord'}> <surrender> <reset> <help>")
            except (InputParser.ParseException, GameEndException) as ex:
                self.actual_game.show_game()
                print(ex.message)

            if option_input != "exit" and not self.actual_game.is_finish():
                option_input = input("command (use 'exit' to stop; type 'help' for info) --> ")
        print("Game finished! Thanks for playing!")
