""" Linear/sequential searching """
import tools
# uncomment the next line if you want to make some Name objects
from classes import Name


def linear_result_finder(tested_list, quarantined):
    """ The tested list contains (nhi, Name, result) tuples
        and isn't guaranteed to be in any order
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
    """
    comparisons = 0
    results = []
    # ---start student section---
    for person in quarantined:
        found = False
        for test in tested_list:
            if (test[1] == person):
                comparisons += 1
                results.append((test[1], test[0], test[2]))
                found = True
                break
            else:
                comparisons += 1
        if not found:
            results.append((person, None, None))
        
    # ===end student section===
    return results, comparisons


# Don't submit your code below or pylint will get annoyed :)
if __name__ == '__main__':
    # write your own simple tests here
    # eg
    tested = [(1,Name('Lee'), False), (2,Name('Cissiee Bednar'), True), (30,Name('Meris'),False)]
    quarantined = [Name('Cissiee Bednar'), Name('Jon Klaudt'), Name('Meris Dendi')]
    print(linear_result_finder(tested, quarantined))
