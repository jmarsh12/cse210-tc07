import random
from game.actor import Actor
from game.location import Location

class Buffer(Actor):

    def __init__(self):
        
        super().__init__()
        position = Location(1, 20)
        self.set_position(position)
        self.set_text(f"Buffer: ")

    def check_match(self, word):
        """
        check if word is anywhere in the buffer if so, return True; if not, return False
        Params:
            word (word class object)

        returns:
            Boolean:
                True if it's a match
                False if it's not a match
        """
        pass

    def add_points(self, word):
        """
        Adds points based on the given word.
        1 point per letter.

        Params:
            word (word class object)

        Returns:
            ???
        """
        # if word is "Bonus":
        #     self._points += 15  # adds bonus points instead of word length
        # else:
        #     self._points += len(word)
        self.set_text(f"Buffer: ")

    def add_letter(self, letter):
        """
        Adds the given letter to the buffer.

        Params:
            letter (A string with a single letter in it)

        returns:
            None
        """
        self.set_text(self.get_text() + letter)
