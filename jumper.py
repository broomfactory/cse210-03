# cse210 Team 4 Week 5

class Jumper:
    '''
        This class represents the jumper.
    '''
    

    def __init__(self):
        '''Constructs a new Jumper.
        
        Args:
            self (Jumper): an instance of Jumper.
        '''
        self._parachute = [
            '  ___  ', 
            ' /___\ ', 
            ' \   / ', 
            '  \ /  ', 
            '   O   '
            ]

    def draw_jumper(self):
        '''
            Draws the current state of the jumper
        '''
<<<<<<< HEAD

        for i in range(0,len(self._parachute)):
            if len(self._parachute) > 1:
                print(self._parachute[i])
            else:
                print('   X   ')

        print('  /|\  ')
        print('  / \  ')
        print('')
        print('^^^^^^^')
=======
        if len(self._parachute) > 1:
            
            for i in self._parachute:
                print(i)
        else:
            print('   X   ')

        print('  /|\  ')
        print('  / \  ')

>>>>>>> 6fc25ded2a537b9ec974780c5be7bb20906ae4fa

    def register_miss(self):
        '''
            Removes the first section from the parachute
        '''
        self._parachute.pop(0)
    
    def is_alive(self):
        '''
            Reports True if
        '''
        if len(self._parachute) > 1:
            return True
        else:
            return False
