from time import sleep
from game import constants
from game.score import Score
from game.words import Words
from game.buffer import Buffer


class Director:
    """A code template for a person who directs the game. The responsibility of
    this class of objects is to control the sequence of play.

    Stereotype:
        Controller

    Attributes:
        food (Food): The snake's target.
        input_service (InputService): The input mechanism.
        keep_playing (boolean): Whether or not the game can continue.
        output_service (OutputService): The output mechanism.
        score (Score): The current score.
        snake (Snake): The player or snake.
    """

    def __init__(self, input_service, output_service):
        """The class constructor.

        Args:
            self (Director): an instance of Director.
        """
        self._buffer = Buffer()
        self._input_service = input_service
        self._keep_playing = True
        self._output_service = output_service
        self._score = Score()
        self._words = []

    def start_game(self):
        """Starts the game loop to control the sequence of play.

        Args:
            self (Director): an instance of Director.
        """
        self._setup()

        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            sleep(constants.FRAME_LENGTH)

    def _setup(self):
        # TODO create 5 words and add them to the list
        pass

    def _check_offscreen(self):
        # TODO go through each word and see if it's off the screen
        # TODO if the word is off the screen, remove from list and create a new one
        pass

    def _check_matches(self):
        # TODO check if the buffer matches any of the words
        for word in self._words:
            if self._buffer.check_match(word):
                # TODO pull out of list and update score
                score = word.get_score()
                # TODO add to words class
        # TODO if so, pull it off and update the score accordingly

        pass

    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the desired direction and moving the snake.

        Args:
            self (Director): An instance of Director.
        """
        # input_service.get_letter()
        # TODO add letter to buffer
        # if the letter is not a letter or not pushed, don't add it to buffer
        direction = self._input_service.get_direction()
        self._snake.move_head(direction)

    def _do_updates(self):
        """Updates the important game information for each round of play. In
        this case, that means checking for a collision and updating the score.

        Args:
            self (Director): An instance of Director.
        """
        # TODO check_offscreen(), check_matches()
        # self._handle_body_collision()
        # self._handle_food_collision()

    def _do_outputs(self):
        """Outputs the important game information for each round of play. In
        this case, that means checking if there are stones left and declaring
        the winner.

        Args:
            self (Director): An instance of Director.
        """
        # TODO draw actor: buffer
        # TODO go through each word and call draw_actor()
        self._output_service.clear_screen()
        # self._output_service.draw_actor(self._food)
        # self._output_service.draw_actors(self._snake.get_all())
        self._output_service.draw_actor(self._score)
        self._output_service.flush_buffer()

    # def _handle_body_collision(self):
    #     """Handles collisions between the snake's head and body. Stops the game
    #     if there is one.
    #
    #     Args:
    #         self (Director): An instance of Director.
    #     """
    #     head = self._snake.get_head()
    #     body = self._snake.get_body()
    #     for segment in body:
    #         if head.get_position().equals(segment.get_position()):
    #             self._keep_playing = False
    #             break

    # def _handle_food_collision(self):
    #     """Handles collisions between the snake's head and the food. Grows the
    #     snake, updates the score and moves the food if there is one.
    #
    #     Args:
    #         self (Director): An instance of Director.
    #     """
    #     head = self._snake.get_head()
    #     if head.get_position().equals(self._food.get_position()):
    #         points = self._food.get_points()
    #         for n in range(points):
    #             self._snake.grow_tail()
    #         self._score.add_points(points)
    #         self._food.reset()