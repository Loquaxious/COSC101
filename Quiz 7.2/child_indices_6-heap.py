def child_indices_6_heap(parent):
    """Returns a list containing all the indexes of the children from the 
    given parent"""
    if parent == 0:
        return None
    else:
        return [6 * parent - 4, 6 * parent - 3, 6 * parent - 2, 6 * parent - 1, \
                6 * parent, 6 * parent + 1]
    

hello = child_indices_6_heap(3)
print(hello)