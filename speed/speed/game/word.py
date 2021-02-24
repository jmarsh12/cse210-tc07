from game.actor import Actor
from game.location import Location
from random import randint
from game import constants

class Word(Actor):

    def __init__(self, text):

        super().__init__()
        self.set_velocity(Location(1, 0))
        self.set_text(text)

        x = 0
        y = randint(1, constants.MAX_Y)
        self.set_position(Location(x, y))


    def get_points(self):
        """
        Returns the number of points associate with this word. 1 per letter.

        Params:
            None

        Returns:
            Point value as an integer.
        """
        pass
