# cse210 Team 4 Week 5

class Jumper:
    '''
    
    '''
    

    def __init__(self):
        '''Constructs a new Jumper.
        
        Args:
            self (Jumper): an instance of Jumper.
        '''
        self._parachute = [
            '  ___  ', 
            ' /   \ ', 
            ' \   / ', 
            '  \ /  ', 
            '   O   '
            ]

    def draw_jumper(self):
        '''
        '''
        for i in self._parachute:
            if len(self._parachute) > 0:
                print(i)
            else:
                print('   X   ')

            print('  /|\  ')
            print('  / \  ')

    def register_miss(self):
        '''
            Removes the first section from the parachute
        '''
        self._parachute.pop()
    
    def is_alive(self):
        '''
        '''
        if len(self._parachute) == 0:
            return True
        else:
            return False
