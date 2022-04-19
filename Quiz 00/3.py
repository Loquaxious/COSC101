class Fraction(object):
    '''Defines a Fraction type that has an integer numerator and a non-zero integer denominator'''

    def __init__(self, num=0, denom=1):
        ''' Creates a new Fraction with numberator num and denominator denom'''
        self.numerator = num
        if denom != 0:
            self.denominator = denom
        else:
            raise ZeroDivisionError
        
    def __str__(self):
        """Shows the numerator and the denominator"""
        template = "{0}/{1}"
        return template.format(self.numerator, self.denominator)

f = Fraction(12, 3)
print(f)   