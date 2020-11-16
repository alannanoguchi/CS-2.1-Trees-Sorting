#!python


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    sorted_list = []    # append items to new list in sorted order

    left_index = 0
    right_index = 0

    # TODO: Repeat until one list is empty
    while left_index < len(items1) and right_index < len(items2):    # while the indexes are less than the length of the lists

    # TODO: Find minimum item in both lists and append it to new list
        if items1[left_index] < items2[right_index]:    # if item1 is less than its compared item2
            sorted_list.append(items1[left_index])    # add the smaller value to sorted_list
            left_index += 1      # increase the index to check next item
        else:
            sorted_list.append(items2[right_index])
            right_index += 1

    # TODO: Append remaining items in non-empty list to new list
    if left_index < len(items1):
        sorted_list.append(items1[left_index])
        left_index += 1

    if right_index < len(items2):
        sorted_list.append(items2[right_index])
        right_index += 1

    return sorted_list

items1 = [2, 9, 12]
items2 = [1, 3, 7, 11]
print(merge(items1, items2))


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half using any other sorting algorithm
    # TODO: Merge sorted halves into one list in sorted order


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    # TODO: Check if list is so small it's already sorted (base case)
    if len(items) <= 1:
        return items

    # TODO: Split items list into approximately equal halves
    middle = len(items) // 2
    left_side = items[:middle]    # :middle begins at index 0 to the middle index
    right_side = items[middle:]    # middle: begins at the middle index to the end

    # TODO: Sort each half by recursively calling merge sort
    merge_sort(left_side)
    merge_sort(right_side)

    # TODO: Merge sorted halves into one list in sorted order
    merged = merge(left_side, right_side)
    return merged

list1 = [3, 55, 34, 63, 65, 12]
merge_sort(list1)
print(list1)



def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    pivot = items[high]     # last item is the pivot

    left = low
    right = high - 1     # the pivot is the high so this will be one before the pivot

    # TODO: Loop through all items in range [low...high]
    while left < right:
    # TODO: Move items less than pivot into front of range [low...p-1]
        if items[right] >= pivot:     # if the value of the right pointer is greater than the pivot
            right -= 1      # move the right pointer to the left (subtract 1)
        
    # TODO: Move items greater than pivot into back of range [p+1...high]
        if items[left] < pivot:    # if the value of th left pointer is less than the pivot
            left += 1     # move the left pointer to the right (add 1)

        if items[left] >= pivot and items[right] < pivot:   # if the left pointer is less than or equal to the right pointer then
            items[left], items[right] = items[right], items[left]   # swap the values at these locations
            left += 1    # move the left pointer to the right (add 1)
            right -= 1   # move the right pointer to the left (subtract 1)

    # TODO: Move pivot item into final position [p] and return index p
    if items[left] < pivot:
        left += 1
    items[left], items[high] = items[high], items[left]
    return left


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    if low is None and high is None:
        low = 0
        high = len(items) - 1

    # TODO: Check if list or range is so small it's already sorted (base case)
    if len(items[low:high + 1]) == 1:
        return items

    # TODO: Partition items in-place around a pivot and get index of pivot
    if low < high:
        p = partition(items, low, high)

    # TODO: Sort each sublist range by recursively calling quick sort
        quick_sort(items, low, p-1)
        quick_sort(items, p+1, high)



# items = [3, 55, 34, 63, 65, 99, 75, 33, 100, 140, 66]
# merge_sort(items)
# print(items)

# middle = len(items) // 2

# print(items[:middle])   # left side [3, 55, 34, 63, 65]
# print(items[middle:])   # right side [99, 75, 33, 100, 140, 66]