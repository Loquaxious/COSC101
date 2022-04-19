class Rectangle(object):
    """ Rectangle class """

    def __init__(self, width=1, height=2):
        self.width = width
        self.height = height
        self.area()
        self.perimeter()
    
    def area(self):
        """Calculates the area"""
        return (self.width * self.height)
    
    def perimeter(self):
        """Calculates the perimeter"""
        return (2*self.width + 2*self.height)
    
  