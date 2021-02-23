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
        #self._word = ""
        #self.set_word()
        #self.array_seg = []
        self._reset()
        
        
    def display(self):
        print(self._words)
        print(len(self._words))

    def set_words(self):
        index = []
        for i in range(5):
            number = random.randint(0,9885)
            index.append(number)
            self._new_words.append(self._words[number])

    def set_word(self):
        number = random.randint(0, 9885)
        self._word = self._words[number]
    
    def get_word(self):
        return self._segments

    def get_segments(self):
        return self._segments

    def get_words(self):
        return self._new_words

    def move_words(self, direction):
        count = 0
        for i in range(len(self._new_words)):
            count += len(self._new_words[i])
        count -= 1
        for n in range(count, -1, -1):
            segment = self._segments[n]   
            if n > 0:
                leader = self._segments[n - 1]
                velocity = leader.get_velocity()
                segment.set_velocity(velocity)
            else:
                segment.set_velocity(direction)
            segment.move_next()     
        
        # count = len(self._new_words[i]) - 1
        # for n in range(count, -1 , -1):
        #     segment = self._segments[n]
        #     if n > 0:
        #         leader = self._segments[n - 1]
        #         velocity = leader.get_velocity()
        #         segment.set_velocity(velocity)
        #     else:
        #         segment.set_velocity(direction)


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
        #self.array_seg.append(segment.get_text())
        self._segments.append(segment)


    def _reset(self):
        x = 1
        
        for n in range(len(self._new_words)):
            y = random.randint(2, constants.MAX_Y - 2)
            w_reverse = ""
            for char in self._new_words[n]:
                w_reverse = char + w_reverse
            self._new_words[n] = w_reverse
            for i in range(len(self._new_words[n])):
                text = self._new_words[n][i:i+1]
                position = Location(x - i, y)
                velocity = Location(1, 0)
                self._add_segment(text, position, velocity)
        # for n in range(len(self._new_words[i])):
        #     text = self._new_words[i][n:n+1]
        #     position = Location(x, y)
        #     velocity = Location(1, 0)
        #     self._add_segment(text, position, velocity)

