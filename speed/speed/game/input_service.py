import sys
from asciimatics.event import KeyboardEvent

class InputService:
    """Detects player input. The responsibility of the class of objects is to 
    get the player in put and then sends or returns it so that the buffer can use it.

    Stereotype: 
        Service Provider

    Attributes:
        _screen (Screen): An Asciimatics screen.
    """

    def __init__(self, screen):
        self._letters = ""
    
    def get_input(self):
        self._letters = input(isalpha())
        return self._letters

    #     """The class constructor.
        
    #     Args:
    #         self (InputService): An instance of InputService.
    #     """
    #     self._screen = screen
        
    # def get_letter(self):
    #     """Gets the letter that was typed. If the enter key was pressed returns an asterisk.

    #     Args:
    #         self (InputService): An instance of InputService.

    #     Returns:
    #         string: The letter that was typed.
    #     """
    #     result = ""
    #     event = self._screen.get_key()
    #     if not event is None:
    #         if event == 27:
    #             sys.exit()
    #         elif event == 10: 
    #             result = "*"
    #         elif event >= 97 and event <= 122: 
    #             result = chr(event)
    #     return result