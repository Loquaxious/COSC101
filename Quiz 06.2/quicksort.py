import time
import random
import doctest

DATA_DIR = './data/'


def load_file(file_name):
    """ Returns the numbers in the file assuming the file has one number per line.
    Remember to prefix the file name with ./data/
    eg, './data/list1.txt'
    """
    with open(file_name) as infile:
        values = [int(line.strip()) for line in infile]
    return values


def quicksort(values, style='left-pivot'):
    """Starts the quicksort algorithm for sorting a list of values in-place.
    >>> quicksort([1, 4, 10, 8, 2, 6, 7, 0, 5, 9, 3])
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """

    copy_of_list = list(values)

    if len(copy_of_list) == 1:
        # return the copy of the 1 item list
        return copy_of_list
    else:
        # Quicksort the copy of the list
        quicksort_helper(copy_of_list, 0, len(copy_of_list) - 1, style)
        return copy_of_list


def quicksort_helper(values, left, right, style):
    """
    Recursive quicksort helper.
    Sorts, in place, the portion of values between left and right.
    """
    # Stop when the left and right indices cross
    if left >= right:
        return

    # Partition the list
    split = partition(values, left, right, style)

    # Sort the left part
    quicksort_helper(values, left, split - 1, style)

    # Sort the right part
    quicksort_helper(values, split + 1, right, style)


def partition(values, left, right, style):
    """
    Partitions the values between left and right.
    Returns the index of the split.
    if style='left-pivot' then left item used as pivot
    if sytle='mo3-pivot' then index of median of three
     used as pivot
    if sytle is unknown then left-pivot is used.

    """

    # Figure out which index to use as the pivot
    if style == 'left-pivot':
        pivot_i = left
    elif style == 'mo3-pivot':
        pivot_i = pivot_index_mo3(values, left, right)
    else:
        print('I am unfamiliar with your funky styles.')
        print('Default left-pivot used...')
        pivot_i = left

    # Swap the pivot with the left item so we can keep the pivot
    # out of the way
    values[left], values[pivot_i] = values[pivot_i], values[left]

    # the pivot value is now the value in the left slot
    pivot = values[left]

    # move leftmark to first item after the pivot
    leftmark = left + 1
    rightmark = right

    # Move the left and right marks
    while True:
        # Find an item larger or equal to the pivot
        while leftmark <= rightmark and values[leftmark] < pivot:
            leftmark += 1
        # Find an item smaller than the pivot
        while leftmark <= rightmark and values[rightmark] >= pivot:
            rightmark -= 1

        # If the pointers cross, we're done
        if leftmark > rightmark:
            break
        else:
            # Otherwise... swap the items and keep going
            values[leftmark], values[rightmark] = values[
                rightmark], values[leftmark]

    # Put the pivot in its correct place
    values[left], values[rightmark] = values[rightmark], values[left]

    # Return the location of the split
    # values to right of rightmark are >= pivot value
    # values to left of rightmark are < pivot value
    return rightmark


def quicksort_range(values, start, end, style='left-pivot'):
    """Starts a quicksort that only guarantees that values between
       the start and end index (inclusive) are sorted.
    >>> x = quicksort_range([2, 10, 5, 1, 0, 8, 3, 6, 9, 4, 7],0,1)
    >>> x[0]
    0
    >>> x[1]
    1
    >>> x = quicksort_range([2, 10, 5, 1, 0, 8, 3, 6, 9, 4, 7], 9, 10)
    >>> x[9]
    9
    >>> x[10]
    10
    >>> x = quicksort_range([2, 10, 5, 1, 0, 8, 3, 6, 9, 4, 7], 2, 3)
    >>> x[2]
    2
    >>> x[3]
    3
    >>> quicksort_range([2, 10, 5, 1, 0, 8, 3, 6, 9, 4, 7], 0, 10)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    """
    copy_of_list = list(values)
    if len(copy_of_list) == 1:
        # return the copy of the only item in list
        return copy_of_list
    else:
        # Quicksort the copy of the list
        quicksort_range_helper(copy_of_list,
                               0,
                               len(copy_of_list) - 1,
                               start,
                               end,
                               style)
        return copy_of_list


def quicksort_range_helper(values, left, right, start, end, style):
    """
    Recursive quicksort range helper.
    Sorts, in place, the portion of values between left and right (inclusive)
    but only if the left-right range has any overlap with the start-end range.
    """
    # ---start student section---
    # Stop when the left and right indices cross
    if start >= right or left >= right:
        return
    elif end <= left or left >= right:
        return

    # Partition the list
    split = partition(values, left, right, style)

    # Sort the left part
    quicksort_helper(values, left, split - 1, style)

    # Sort the right part
    quicksort_helper(values, split + 1, right, style)    
    # ===end student section===


def pivot_index_mo3(values, left, right):
    """
    Returns the index of the item that is the median of the left, right and
    middle value in the list. The return value should normally be
    either left, right or middle.
    If there are only two items in the range, ie, if right==left+1
    then return the index of the first item as there are only two items
    to find the median of, so we can't get a middle index...
    If there is only one item in the range then also simply
    return the left index, ie, if left==right then return left.

    >>> print(pivot_index_mo3([0,1,2],0,2))
    1
    >>> pivot_index_mo3([2,1,0],0,2)
    1
    >>> pivot_index_mo3([1,2,3],0,2)
    1
    >>> pivot_index_mo3([3,2,1],0,2)
    1
    >>> pivot_index_mo3([3,5,1],0,2)
    0
    >>> pivot_index_mo3([1,5,3],0,2)
    2
    >>> pivot_index_mo3([1,2],0,1)
    0
    >>> pivot_index_mo3([3,1],0,1)
    0
    >>> pivot_index_mo3([1,2],1,1)
    1
    >>> x = [1,1,3]
    >>> i = pivot_index_mo3(x,0,2)
    >>> x[i]
    1
    >>> y = [1,3,1]
    >>> i = pivot_index_mo3(y,0,2)
    >>> y[i]
    1
    >>> z = [3,1,1]
    >>> i = pivot_index_mo3(z,0,2)
    >>> z[i]
    1
    >>> xx = [1,3]
    >>> i = pivot_index_mo3(xx,0,1)
    >>> xx[i]
    1
    >>> pivot_index_mo3([1,2,2,5,2,8,10],0,6)
    3
    >>> pivot_index_mo3([1,6,0,5,9,8,10],0,4)
    0
    """

    middle = (left + right) // 2
    # ---start student section---
    if right == left+ 1 or left == right:
        return left
    else:
        if values[left] <= values[middle] and values[middle] <= values[right]:
            return middle
        if values[right] <= values[middle] and values[middle] <= values[left]:
            return middle
        if values[left] <= values[right] and values[right] <= values[middle]:
            return right
        if values[middle] <= values[right] and values[right] <= values[left]:
            return right
        return left
    # ===end student section===


if __name__ == "__main__":
    doctest.testmod()
