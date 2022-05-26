# Matthew Scoville
# cse210 Team 4 Week 5
from puzzle import Puzzle

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _puzzle: A puzzle instance
        _is_playing (boolean): Whether or not the game is being played.        
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._puzzle = Puzzle()
        self._is_playing = True            

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
       
        #Display initial puzzle and jumper
        self._show_puzzle()

        while self._is_playing:
            self._make_guess(self._get_inputs())
            self._show_puzzle()

    def _show_puzzle(self):
        """Displays the current puzzle and jumper state"""
        print(f"{self._puzzle.getDisplayWord()}")
        self._puzzle.drawJumper()

    def _get_inputs(self):
        """Ask the player for a guess

        Args:
            self (Director): An instance of Director.
        """

        guess = " "

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

        self._puzzle.makeGuess(self._get_inputs())
        self._is_playing = self._puzzle.isPlaying()
 