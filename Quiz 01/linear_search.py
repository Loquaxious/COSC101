""" Array classes for Lab 1.
NOTE: the LinearArray doctests will fail until your implement the find_index method"""
import doctest


#------------------------------------------------------------------------
class LinearArray():
    """Implements an array using an un-ordered Python list.

    >>> straighty = LinearArray()
    >>> straighty.insert(12)
    >>> straighty.insert(82)
    >>> straighty.insert(45)
    >>> straighty.insert(11)
    >>> print(straighty)
    0 , 12
    1 , 82
    2 , 45
    3 , 11
    <BLANKLINE>
    >>> print(straighty.find_index(45))
    2
    >>> print(straighty.comparisons)
    3
    >>> print(straighty.find_index(7))
    None
    >>> print(straighty.comparisons)
    4
    >>> print(straighty.find_index(2))
    None
    >>> print(straighty.comparisons)
    4
    >>> print(straighty.find_index(12))
    0
    >>> print(straighty.comparisons)
    1
    >>> straighty.remove(45)
    >>> print(straighty.comparisons)
    3
    """

    def __init__(self):
        self.data = list()  # Create the list to store the data
        self.comparisons = 0  # Reset comparison counter

    def insert(self, value):
        """Adds an item to the end of the array"""
        # Add the item to the end of the data list
        self.data.append(value)
        # obviously this didn't use any comparisons
        self.comparisons = 0

    def remove(self, value):
        """Removes the first occurrence of value in the array."""
        # Look for the index in the list that
        # contains the element to delete
        index = self.find_index(value)

        # If we've found the item...
        if index is not None:
            # Delete it from the list
            del self.data[index]
        # otherwise do nothing as it wasn't in the list...

    def contains(self, value):
        """Returns True if the array contains the value, else returns False."""
        return self.find_index(value) is not None

    def find_index(self, value):
        """
        Finds the index of the given value in the data list.
        Returns either the index of the item in the list, or None if
        the item doesn't exist.
        """
        # Counter for how many comparisons are done is set to zero
        self.comparisons = 0
        # Loop through each item in the data list
        for item in self.data:
            # Add one to comparisons for each comparison
            self.comparisons += 1
            # involving a list element
            # If the item is equal to our search value
            if item == value:
                # return the index this item is at
                return self.data.index(value)
            # If we loop through everything and haven't found
            # the item, return None
        return None


    def __str__(self):
        """
        Prints out all the values in the array
        """
        string = ''
        for i, value in enumerate(self.data):
            string += '{} , {}\n'.format(i, value)
        return string