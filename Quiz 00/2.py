class Rectangle(object):
    """ Implements a simple rectangle class '"""
    
    def __init__(self, width=1, height=2):
        self.width = width
        self.height = height
        
    def __str__(self):
        """ """
        string = self.height *('#' * self.width + '\n')
        return string.strip()
            
recker = Rectangle(20,5)
print(recker)