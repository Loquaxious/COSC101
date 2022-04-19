def child_indices(parent, branch_factor):
    """returns a list containing the list of indices where the children 
    of the node at index parent will be stored for a heap list with 
    the given branch_factor"""
    indices = []
    
    if parent == 0 or branch_factor == 0:
        return None
    else:
        for i in range(2 - branch_factor, 2):
            indices.append(branch_factor * parent + i)
        return indices


print(child_indices(1,2))
print(child_indices(2,2))
print(child_indices(1,3))