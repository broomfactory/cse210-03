import imp
from WordList import WordList
from jumper import Jumper
from director import Director

class Puzzle:

    def __init__(self):
        
        self._secret_word = WordList
        self._is_playing = Jumper.IsStillAlive()


    def makeGuess():

        user_guess = Director._get_inputs
        word = WordList.get_random_word.lower()
        hidden_word = ['_'] * len(word)
       # return hidden_word, word, []
        if user_guess ==



