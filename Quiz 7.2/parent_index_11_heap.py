def parent_index_11_heap(child_index):
    """returns the index of the parent of the node at the given child_index"""
    if ((child_index + 9) // 11) == 0:
        return None
    else:
        return (child_index + 9) // 11
    
print(parent_index_11_heap(2))
print(parent_index_11_heap(15))