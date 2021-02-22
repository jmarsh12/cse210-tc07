from game.buffer import Buffer
from game.score import Score


class Location:

    def __init__(self, x, y):
        """
        The constructor method.
        """
        self._x = x
        self._y = y
        self._buffer_pos = (0, 0)
        self._score_pos = (0, 0)
        self._word_x = x
        self._word_y = y

    def buffer_position(self):
        """
        Defines the buffer position on the screen.
        """
        self._buffer_pos = (55, 15)
        return self._buffer_pos

        pass

    def score_position(self):
        """
        Defines the score position on the screen.
        """
        self._score_pos = (5, 0)
        return self._score_pos

        pass

    def word_position(self, other):
        """
        Defines the position for the words and moves them across the screen.
        """
        x = self._word_x + other.get_x()
        y = self._word_y
        return Location(x, y)

        pass

    def get_x(self):
        """
        Returns the x value.
        """
        return self._x

    def get_y(self):
        """
        Returns the y value.
        """
        return self._y

    pass
