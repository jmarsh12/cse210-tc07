import random
from game.actor import Actor
#from game.point import Point


class Score(Actor):
    """Points earned. The responsibility of Score is to keep track of the player's points.

    Stereotype:
        Information Holder

    Attributes:
        _points (integer): The number of points the food is worth.
    """

    def __init__(self):
        """The class constructor. Invokes the superclass constructor, initializes points to zero, sets the position and updates the text.

        Args:
            self (Score): an instance of Score.
        """
        super().__init__()
        self._points = 0
        # position = Point(1, 0)
        # self.set_position(position)
        self.set_text(f"Score: {self._points}")

    def add_points(self, word):
        """Adds the earned points to the running total and updates the text depending on if it is a
        regular word or if it is a bonus word

        Args:
            self (Score): An instance of Score.
            word (string): The word that .
        """
        if word is "Bonus":
            self._points += 15  # adds bonus points instead of word length
        else:
            self._points += len(word)
        self.set_text(f"Score: {self._points}")