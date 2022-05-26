import random

class WordList: 

    "This class creates a list of words for the hide and seek game."

    def __init__(self):
        
        self._WordList = ["word", "apple", "banana", "sheep", "spade", "crisp", "chips", "cars", "orange", "shoes", "grasses", "laptop", "tables"]
       
    def get_random_word(self):

        "This definition chooses a word from the list for the puzzle class secret word attribute to grab."

        word = random.choice(self._WordList)
        return word
