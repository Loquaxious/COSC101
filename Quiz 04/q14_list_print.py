def recursive_list_print(alist, start_index=0):
    """Takes a list and prints the elements one by one"""
    if len(alist) <= start_index:
        return 
    else:
        print(alist[start_index])
        recursive_list_print(alist, start_index +1)

letters = list('ab')
recursive_list_print(letters)
recursive_list_print([1])
recursive_list_print([1,2,3,4,5], 2)