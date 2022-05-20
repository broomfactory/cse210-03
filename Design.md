# Jumper Classes
## WordList - Anita
* Attributes: 
    * List of Words (private) 
* Methods: 
    * getRandomWord() return random.rand(List) 
* Encapsulation: private list of words 
    
## Jumper - Pierce
* Attributes: 
    * How much parachute left (4 Levels) 
    * List of strings to contain ascii art 
* Methods: DrawJumper()
    * RegisterMiss()
    * IsStillAlive()
* Encapsulation: how much parachute left is private / artwork private   
   
## Puzzle - Andrew
* Attributes:
    * secret word (aka puzzle) - random word from WordList 
    * _is_playing = (Jumper.IsStillAlive() and puzzle is not complete)
    * guesses[]
* Methods: makeGuess(letter) - returns True if or False  
    * _isPuzzleComplete() - secretword == displayword 
    * displayWord (correct letters + blanks)
    * checks guess
    * calls RegisterMiss() if wrong
    * calls Jumper.DrawJumper()
    * isPlaying() return _is_playing
    * getDisplayWord()
    * Encapsulation: current puzzle state (displayWord), secretWord private
## Director - Matthew
* Attributes:
    _puzzle
* Methods:
   * Start game
   * Get input
   * Loop while playing 
        * call puzzle methods
        * make guesses
        * print the puzzle word so far (with blanks)
* Encapsulation: puzzle itself 


 **Director** has a **puzzle** 
 **Puzzle** has a **WordList**, **Jumper**

# Designing Together
* Identify the objects in your program. Look for the central nouns in the game requirements. Narrow down your list to just the most essential ones. For each object, ask yourself, "is this an object, or the state in another object?"    

* Define the responsibility, behaviors and state for each object. Look for related verbs in the game requirements to help you. When you are working on an object's state, ask yourself, "what information is required to fulfill its behaviors?"

* Identify the relationships between your objects. Look at the user interface in the game requirements to help you. Try roll playing the objects as you talk through a typical game, asking other objects to perform specific behaviors, etc.

* Translate your object designs to class designs. This is not a coding task. It is simply deciding what the class name as well as method names, parameters and return types will be. It is also deciding what attribute names and data types will be.

* Document your objects and classes so that everyone can refer to them throughout the project. The graphical notation that follows is often the easiest way. It really doesn't matter how you do it though. It just matters that you do.

From CSE210 _Programming with Classes_ [Appendix: Designing Together](https://byui-cse.github.io/cse210-course-competency/appendices/designing-together.html)