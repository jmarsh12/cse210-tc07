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
        # TODO check if word is anywhere in the buffer
        # TODO if so, return True; if not, return False
        pass
    def add_points(self, word):
        # if word is "Bonus":
        #     self._points += 15  # adds bonus points instead of word length
        # else:
        #     self._points += len(word)
        self.set_text(f"Buffer: ")
