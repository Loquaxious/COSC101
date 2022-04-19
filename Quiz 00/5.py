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
    
    def __add__(self, other):
        """Adds"""
        numer = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        denom = self.denominator * other.denominator
        
        return "{0}/{1}".format(numer, denom)
    
    def __mul__(self, other):
        """Multiplies"""
        numer = self.numerator * other.numerator
        denom = self.denominator * other.denominator
        
        return "{0}/{1}".format(numer, denom)

x = Fraction(3, 5)
y = Fraction(1, 6)
z = x * y
print(z)

x = Fraction(1, 1)
y = Fraction(7, 13)
print(type(x * y))