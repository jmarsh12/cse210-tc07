from game import constants
from game.actor import Actor
from game.location import Location
import random

class Words(Actor):
    def __init__(self):
        super().__init__()
        self._words = constants.LIBRARY
        self._new_words = []
        self.set_words()
        self._segments = []
        
    def display(self):
        print(self._words)
        print(len(self._words))

    def set_words(self):
        index = []
        for i in range(5):
            number = random.randint(0,9885)
            index.append(number)
            self._new_words.append(self._words[number])
            print(number)

    def get_words(self):
        return self._segments

    def move_words(self, direction, i):
        self._reset(i)
        count = len(self._new_words[i]) - 1
        for n in range(count, -1 , -1):
            segment = self._segments[n]
            if n > 0:
                leader = self._segments[n - 1]
                velocity = leader.get_velocity()
                segment.set_velocity(velocity)
            else:
                segment.set_velocity(direction)
            # word = self._new_words[i][n:n+1]
            # if n > 0:
            #     leader = self._new_words[i][n-1:n]
            #     velocity = leader.get_velocity()
            #     word.set_velocity(velocity)
            # else:
            #     word.set_velocity(direction)

            segment.move_next()       
    
    def _add_segment(self, text, position, velocity):
        """Adds a new segment to the snake using the given text, position and velocity.

        Args:
            self (Snake): An instance of snake.
            text (string): The segment's text.
            position (Point): The segment's position.
            velocity (Point): The segment's velocity.
        """
        segment = Actor()
        segment.set_text(text)
        segment.set_position(position)
        segment.set_velocity(velocity)
        self._segments.append(segment)


    def _reset(self, i):
        x = 1
        y = random.randint(1, constants.MAX_Y - 2)
        position = Location(x, y)
        for n in range(len(self._new_words[i])):
            text = self._new_words[i][n:n+1]
            position = Location(x, y)
            velocity = Location(1, 0)
            self._add_segment(text, position, velocity)

