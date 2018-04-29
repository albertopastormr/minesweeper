import InputParser


class Controller(object):
    """
    Represents the main controller of the application serving as a
    input receiver and output server
    """

    def __init__(self, game):
        self.actual_game = game

    def execute(self):
        option_input = input("command (use 'exit' to stop; type 'help' for info) --> ")
        while option_input != "exit" and not self.actual_game.is_finish():
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
                print(self.actual_game.surrender())
            elif option_input == "reset":
                self.actual_game.reset()
            elif option_input == "help":
                print("available commands: <show{'x coord','y_coord'}> <flag{'x coord','y_coord'}> <surrender> <reset> <help>")
            else:
                print("unknown command")
                print("available commands: <show{'x coord','y_coord'}> <flag{'x coord','y_coord'}> <surrender> <reset> <help>")

            option_input = input("command (use 'exit' to stop; type 'help' for info) --> ")
