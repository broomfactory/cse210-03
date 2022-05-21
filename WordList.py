import random

class WordList: 

    def __init__(self) -> None:
        
        self._WordList = ["word", "apple", "banana", "sheep", "spade", "crisp", "chips", "cars", "orange", "shoes", "grasses", "laptop", "tables"]

    def getRandomWord(word):

        word = random.choice(WordList)
        return word