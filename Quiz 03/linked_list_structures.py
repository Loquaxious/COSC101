"""Data structures implemented with linked lists.

Check out the comments/code at the end of this module
for how to run the provided doctests.

You should start by implementing the __str__ method as most
tests will print out Stacks or Queues. Hint, while loops will
be handy here.

"""

import doctest
import os

os.environ['TERM'] = 'linux'  # Suppress ^[[?1034h


class Node:
    """A node for a linked list."""

    def __init__(self, item):
        self.item = item
        self.next_node = None


class Stack(object):
    """ Implements a Stack using a Linked List
    >>> s = Stack()
    >>> print(s)
    Stack: head/top -> None
    >>> result = s.pop()
    Traceback (most recent call last):
    ...
    IndexError: Can't pop from empty stack.
    >>> s.push('a')
    >>> print(s)
    Stack: head/top -> a -> None
    >>> len(s)
    1
    >>> print(s.head.item)
    a
    >>> print(s.head.next_node)
    None
    >>> s.pop()
    'a'
    >>> print(s)
    Stack: head/top -> None
    >>> s.push('b')
    >>> print(s)
    Stack: head/top -> b -> None
    >>> s.push('c')
    >>> print(s)
    Stack: head/top -> c -> b -> None
    >>> len(s)
    2
    >>> s.peek()
    'c'
    >>> print(s)
    Stack: head/top -> c -> b -> None
    >>> s.pop()
    'c'
    >>> print(s)
    Stack: head/top -> b -> None
    >>> e = Stack()
    >>> e.peek()
    Traceback (most recent call last):
    ...
    IndexError: Can't peek at empty stack.
    """

    def __init__(self):
        self.head = None
        
    def push(self, item):
        """push a new item on to the stack"""
        # ---start student section---
        new_node = Node(item)
        new_node.next_node = self.head
        self.head = new_node
        # ===end student section===

    def pop(self):
        """pop an item off the top of the stack, and return it
        If stack is empty you should raise an IndexError as per
        the comment below."""
        # use the following line to raise error when stack is empty
        # raise IndexError("Can't pop from empty stack.")
        # ---start student section---
        if self.is_empty():
            raise IndexError("Can't pop from empty stack.")
        else:
            current = self.head.item
            self.head = self.head.next_node
            return current
        # ===end student section===

    def peek(self):
        """Returns the item that is on the top of the stack, but doesn't remove it.
        If stack is empty you should an IndexError is raised.
        """
        if self.is_empty():
            raise IndexError("Can't peek at empty stack.")
        else:
            # ---start student section---
            return self.head.item
            # ===end student section===

    def is_empty(self):
        """ Returns True if stack is empty """
        return self.head is None

    def __len__(self):
        """ Returns the length --- calling len(s) will invoke this method """
        # ---start student section---
        temp = self.head
        i = 0
        
        while (temp):    
            i += 1
            temp = temp.next_node
        
        return i
        # ===end student section===

    def __str__(self):
        """Returns a string representation of the list for the stack starting
        from the beginning of the list. Items are separated by ->
        and ending with -> None
        eg, Stack: head/top -> c -> b -> None
        See doctests in class docstring
        """
        result = 'Stack: head/top'
        current = self.head
        while current is not None:
            result += ' -> ' + str(current.item)
            current = current.next_node
        result += ' -> None'
        return result


class Queue(object):
    """ Implements a Queue using a Linked List"
    >>> q = Queue()
    >>> len(q)
    0
    >>> print(q)
    Queue: head/front -> None
    >>> result = q.dequeue()
    Traceback (most recent call last):
    ...
    IndexError: Can't dequeue from empty queue.
    >>> q.enqueue('a')
    >>> print(q)
    Queue: head/front -> a -> None
    >>> len(q)
    1
    >>> q.enqueue('b')
    >>> print(q)
    Queue: head/front -> a -> b -> None
    >>> q.enqueue('c')
    >>> print(q)
    Queue: head/front -> a -> b -> c -> None
    >>> len(q)
    3
    >>> q.dequeue()
    'a'
    >>> print(q)
    Queue: head/front -> b -> c -> None
    """

    def __init__(self):
        self.head = None

    def enqueue(self, item):
        """Add an item onto the tail of the queue.
        Note: The front of the queue is stored at the head of the list
        so adding to the rear requires finding the end of the list
        """
        # ---start student section---
        new_node = Node(item)
        node = self.head
        
        if node:
            while (node.next_node):
                node = node.next_node
            
            node.next_node = new_node
        else:
            self.head = new_node

        # ===end student section===

    def dequeue(self):
        """Remove an item from the head of the queue and return it.
        If queue is empty you should raise an IndexError as per
        the comment below."""
        # use the following line to raise error when queue is empty
        #
        # ---start student section---
        if self.is_empty():
            raise IndexError("Can't dequeue from empty queue.")
        else:
            old_node = self.head
            self.head = old_node.next_node
            
        return old_node.item
        # ===end student section===

    def is_empty(self):
        """ returns True if the queue is empty """
        # ---start student section---
        return self.head is None
        # ===end student section===

    def __len__(self):
        """ Returns the length --- calling len(q) will invoke this method """
        # ---start student section---
        temp = self.head
        i = 0
        
        while (temp):    
            i += 1
            temp = temp.next_node
        
        return i        
        # ===end student section===

    def __str__(self):
        """Returns a string representation of the list for the queue starting
        from the beginning of the list. Items are separated by ->
        and ending with -> None
        eg, Queue: head/front -> a -> b -> None
        See doctests in class docstring
        """
        result = 'Queue: head/front'
        current = self.head
        while current is not None:
            result += ' -> ' + str(current.item)
            current = current.next_node
        result += ' -> None'
        return result


def run_tests():
    # change to False to get less doctest output
    with_verbose = True

    # Can enter an infinite loop if your Stack isn't implemented correctly
    #result = doctest.testmod()
    #if with_verbose:
        #print(result)

    # To check just one class you can comment out the testmod above
    # and uncomment the relevant doc test run line below
    # Be careful your can get infinite loops if done wrong... so try with Debug
    #doctest.run_docstring_examples(Stack, None, verbose=with_verbose)
    doctest.run_docstring_examples(Queue, None, verbose=with_verbose)


if __name__ == '__main__':
    run_tests()
