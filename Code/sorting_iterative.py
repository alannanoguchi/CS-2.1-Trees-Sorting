#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions? O(n) because it runs through an array/list once
    TODO: Memory usage: ??? Why and under what conditions? O(1) because the items are checked in their index """
    # TODO: Check that all adjacent items are in order, return early if so
    for i in range(len(items) - 1):  # we need to stop the loop one index before or else we get IndexError: list index out of range
        current = items[i]
        next_item = items[i+1]
        
    # assume checking for ascending order
        if next_item <= current:
            return False # list is not ordered so return False
        
    # if we checked all the things and there are no problems, 
    return True

# print(is_sorted([19,61,77,1,3]))    # False
# print(is_sorted([13, 45, 60, 74]))   # True



def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?  O(n^2) the entire array needs to be iterated for every element
    TODO: Memory usage: ??? Why and under what conditions? O(1) the items are checked in their index"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order
    
    for i in range(len(items)):
        for j in range(len(items) - 1):
            if items[j] > items[j+1]:

                # swap, create a temp variable to hold the item
                temp = items[j]
                items[j] = items[j+1]
                items[j+1] = temp

# items = [19,61,77,1,3]
# bubble_sort(items)
# print(items)

def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions? O(n^2) because items are compared and swapped
    TODO: Memory usage: ??? Why and under what conditions? O(1)"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item

    for i in range(len(items)): # iterate through all of the items
        smallest = i      # create a variable that holds the first item in the list of items
        
        for j in range(i+1, len(items)):     # iterate through the rest of the items in the list
            if items[smallest] > items[j]: 
                smallest = j 
        
        items[i], items[smallest] = items[smallest], items[i]    # swap the smallest item in the unsorted list with the first element

# items = [139, 6, 15, 99, 75, 18]
# selection_sort(items)
# print(items)

def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions? O(n^2) each element is compared with all the other elements in the sorted array
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items

    # we start from 1 because range() requires a (start, end)
    for i in range(1, len(items)):
        current_val = items[i]
        current_pos = i

        # As long as we haven't reached the beginning and there is an element
        # in our sorted array larger than the one we're trying to insert
        # move that element to the right
        while current_pos and items[current_pos - 1] > current_val:
            items[current_pos] = items[current_pos - 1]
            current_pos = current_pos - 1


        # We have either reached the beginning of the array or we have found
        # an element of the sorted array that is smaller than the element
        # we're trying to insert at index currentPosition - 1.
        # Either way - we insert the element at currentPosition
        items[current_pos] = current_val
        
items = [3, 55, 34, 63, 65, 99, 75, 33, 100, 140, 66]
insertion_sort(items)
print(items)

