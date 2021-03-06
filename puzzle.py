from wordlist import WordList
from jumper import Jumper

class Puzzle:
    """
        Class to represent the puzzle
    """
    def __init__(self):
        """
          Called on creation of Puzzle instance
          arg: self - an instance of Puzzle
        """


        word_list = WordList()
        self._secret_word = word_list.get_random_word() 
        hidden = ['_'] * len(self._secret_word)
        self._hidden_word = list(hidden)
        
        self._jumper = Jumper()

        #Start with _is_playing set to True
        self._is_playing = True 
 
    def makeGuess(self, guess):
        """
            checks guess
            if correct, update _display_word by placing the guess in the appropriate location
            calls _jumper.RegisterMiss() if wrong
            sets _is_playing to false if _isPuzzleComplete() or not _jumper.IsStillAlive() 
        """
        
        # Check to see if the guess is found in the word
        is_guess_correct = (guess in self._secret_word)
        if is_guess_correct:
            self._updateHiddenWord(guess)
        else:
            self._jumper.register_miss()

        #Update self._is_playing
        self._is_playing = (self._jumper.is_alive() and not self._isPuzzleComplete())
        
        #Report result of guess
        return is_guess_correct
        
    def _updateHiddenWord(self, guess):
        """
            Updates _hidden_word based on correct guess
        """
        #Loop through self._secret_word
        for i in range(0, len(self._secret_word)):
            if self._secret_word[i] == guess:
                self._hidden_word[i] = guess
        #If self._secret_word[i] == guess
        # Set self._hidden_word[i] = guess

    def _isPuzzleComplete(self):
        """        
            non public method to check if the puzzle is
            complete
        """
        return (self._secret_word == ''.join(self._hidden_word))

    def getDisplayWord(self):
        """
            Returns the puzzle word in progress
            _hidden_word = blanks + correct guesses
        """
        return ''.join(self._hidden_word)
        
    def drawJumper(self):
        """
             calls Jumper.draw_jumper() so the director
             can request the current jumper be drawn
        """
        self._jumper.draw_jumper()

    def isPlaying(self):
        """
            Returns True if the game is going
        """ 
        return self._is_playing    
