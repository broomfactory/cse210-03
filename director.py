# Matthew Scoville
# cse210 Team 4 Week 5
from puzzle import Puzzle

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _puzzle: A puzzle instance
        is_playing (boolean): Whether or not the game is being played.        
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._puzzle = Puzzle()
        self._is_playing = True    
        self._guess = None
        self._is_guess_correct = True            

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
       
        #Display initial puzzle and jumper
        self._show_puzzle()

        while self.is_playing:            
            self._get_inputs()
            self._make_guess()
            self._show_puzzle()

    def _show_puzzle(self):
        """Displays the current puzzle and jumper state"""
        print(f"{_puzzle.getDisplayWord()}")
        _puzzle.draw_jumper()

    def _get_inputs(self):
        """Ask the player for a guess

        Args:
            self (Director): An instance of Director.
        """

        guess = None

        while guess not in "abcdefghijklmnopqrstuvwxyz":
            guess = input("Guess a letter [a-z]: ").lower()

        return guess

    def _make_guess(self):
        """Submits the guess to the puzzle
            and deals with the response

        Args:
            self (Director): An instance of Director.
        """
        if not self._is_playing:
            return 

        _puzzle.makeGuess(self._get_inputs())
        self.is_playing = _puzzle.isPlaying()
 