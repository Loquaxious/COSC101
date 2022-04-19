""" Binary search is trickier than you think.
Remember your binary search should only use one comparison
per while loop, ie, one comparison per halving.
"""
from stats import StatCounter, NAME_COMPS
import tools
# uncomment the next line if you want to make some Name objects
from classes import Name

# We recomment using a helper function that does a binary search
# for a Name in a given tested list. This will let you test your
# binary search by itself.




def binary_result_finder(tested, quarantined):
    """ The tested list contains (nhi, Name, result) tuples and
        will be sorted by Name
        quarantined is a list of Name objects
        and isn't guaranteed to be in any order
        This function should return a list of (Name, nhi, result)
        tuples and the number of comparisons made
        The result list must be in the same order
        as the  quarantined list.
        The nhi and result should both be set to None if
        the Name isn't found in tested_list
        You must keep track of all the comparisons
        made between Name objects.
        Your function must not alter the tested_list or
        the quarantined list in any way.
        Note: You shouldn't sort the tested_list, it is already sorted. Sorting it
        will use lots of extra comparisons!
    """
    total_comparisons = 0
    results = []
    # ---start student section---
    for person in quarantined:
        first_index = 0
        last_index = len(tested) - 1
        middle = (last_index + first_index) // 2
        while first_index < last_index:
            middle = (last_index + first_index) // 2
            
            total_comparisons += 1
            if person > tested[middle][1]:
                first_index = middle + 1
            else:
                last_index = middle
        
        print('-'*30)
        total_comparisons += 1
        if tested[first_index][1] == person:
            results.append((tested[first_index][1], tested[first_index][0], \
                            tested[first_index][2]))     
        else:
            results.append((person, None, None))
    # ===end student section===
    return results, total_comparisons


# Don't submit your code below or pylint will get annoyed :)
if __name__ == '__main__':
    # feel free to do some of your simple tests here
    # eg,
    quarantined = tools.make_name_list(['b'])
    tested = tools.make_tested_list(
        ['b','Boomer'], sort_order='name')
    print(quarantined)
    print(tested)
    results, comparisons = binary_result_finder(tested, quarantined)
    print(results) 
    print(comparisons)
    print(StatCounter.get_count(NAME_COMPS))
