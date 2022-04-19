class Fraction(object):
    '''Defines a Fraction type that has an integer numerator and a non-zero integer denominator'''

    def __init__(self, num=0, denom=1):
        ''' Creates a new Fraction with numberator num and denominator denom'''
        self.numerator = num
        if denom != 0:
            self.denominator = denom
        else:
            raise ZeroDivisionError

class ReducedFraction(Fraction):   # is a sub-class of the Fraction class

    def __init__(self, numerator, denominator=1):
        super().__init__(numerator, denominator)  # explicitly use parent/super class __init__()
        self.__reduce__()


    def __reduce__(self):
        """Reduces"""
        #find greatest common divisor for numerator and denominator, except 1:
        common_factor = 1
        for i in xrange(min(abs(numer), abs(denom)), 1, -1):
            if numer % i == 0 and denom % i == 0:
                common_factor = i
                break

    def __add__(self, other):
        """Adds"""
        result = Fraction.__add__(self, other)
        # make a new ReducedFraction, called reduced_result, that is the reduced version of the Fraction
        return reduced_result