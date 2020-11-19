#!python
from sorting_iterative import insertion_sort

def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum integer values)
    max_val = max(numbers)
    min_val = min(numbers)
    nums_range = ((max_val - min_val) + 1)

    # TODO: Create list of counts with a slot for each number in input range
    count_list = [0] * nums_range

    # TODO: Loop over given numbers and increment each number's count
    for _ in range(0, len(numbers)):
        count_list[numbers[i]-min_val] += 1

    # TODO: Loop over counts and append that many numbers into output list
    i = 0
    j = 0
    while i < len(numbers):
        while count_list < 1:
            j += 1
        numbers[i] = min_val + j
        count_list[j] -= 1
        i += 1
    # FIXME: Improve this to mutate input instead of creating new output list


def bucket_sort(numbers=[2, 3, 1, 12, 4], num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum values)
    max_val = max(numbers)
    min_val = min(numbers)

    size = max_val / len(numbers)
    
    # TODO: Create list of buckets to store numbers in subranges of input range
    buckets = [[] for _ in range(num_buckets)]

    # TODO: Loop over given numbers and place each item in appropriate bucket
    for num in numbers:
        index = num / size      # to find the index, divide the num by the size
        buckets[index].append(num)     # add the num to it's appropriate bucket
        
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    for i in range(len(buckets)):
        insertion_sort(buckets[i])

    # FIXME: Improve this to mutate input instead of creating new output list
