import random
from game import constants
from game.location import Location

class Actor:
    """A visible, moveable thing that participates in the game. The responsibility of Actor is to keep track of its appearance, position
    and velocity in 2d space.

    Stereotype:
        Information Holder

    Attributes:
        _text (string): The textual representation of the actor.
        _position (Location): The actor's position in 2d space.
        _velocity (Location): The actor's speed and direction.
    """

    def __init__(self):
        """The class constructor.

        Args:
            self (Actor): an instance of Actor.
        """
        self._text = []
        #self._lines = [Point(0, 0), Point(0, 0), Point(0, 0), Point(0, 0), Point(0, 0)]
        # TODO find better way to space out lines
        self._velocity = Location(0, 0)
        self._position = Location(0,0)

    def get_position(self):

        """Gets the actor's position in 2d space.
        
        Args:
            self (Actor): an instance of Actor.

        Returns:
            Location: The actor's position in 2d space.
        """
        return self._position

    def get_text(self):
        """Gets the actor's textual representation.

        Args:
            self (Actor): an instance of Actor.

        Returns:
            string: The actor's textual representation.
        """
        return self._text

    def get_velocity(self):
        """Gets the actor's speed and direction.

        Args:
            self (Actor): an instance of Actor.

        Returns:
            Location: The actor's speed and direction.
        """
        return self._velocity

    def move_next(self):
        """Moves the actor to its next position according to its velocity. Will
        wrap the position from one side of the screen to the other when it
        reaches the boundary in either direction.

        Args:
            self (Actor): an instance of Actor.
        """

        x1 = self._position.get_x()
        y1 = self._position.get_y()
        x2 = self._velocity.get_x()
        y2 = self._velocity.get_y()
        x = 1 + (x1 + x2 - 1)
        if x == (constants.MAX_X):
            x = -10
        y = 1 + (y1 + y2 - 1)
        position = Location(x, y)
        self._position = position
       

    def set_location(self, location):
        """Updates the actor's position to the given one.

        Args:
            self (Actor): An instance of Actor.
            position (Location): The given position.
        """
        self._position = position

    def set_text(self, text):
        """Updates the actor's text to the given value.

        Args:
            self (Actor): An instance of Actor.
            text (string): The given value.
        """
        self._text = text

    # def move_next(self):
    #     """Moves the actor to its next position according to its velocity. Will 
    #     wrap the position from one side of the screen to the other when it 
    #     reaches the boundary in either direction.
        
    #     Args:
    #         self (Actor): an instance of Actor.
    #     """
    #     x1 = self._position.get_x()
    #     y1 = self._position.get_y()
    #     x2 = self._velocity.get_x()
    #     y2 = self._velocity.get_y()
    #     x = 1 + (x1 + x2 - 1) % (constants.MAX_X - 1)
    #     y = 1 + (y1 + y2 - 1) % (constants.MAX_Y - 1)
    #     position = Location(x, y)
    #     self._position = position
    

    def set_velocity(self, velocity):
        """Updates the actor's velocity to the given one.

        Args:
            self (Actor): An instance of Actor.
            velocity (Location): The given velocity.
        """
        self._velocity = velocity