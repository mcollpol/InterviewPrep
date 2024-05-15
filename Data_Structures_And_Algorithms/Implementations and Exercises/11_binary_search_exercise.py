"""
Implementation of binary search.

Binary search exercise 1:
When I try to find number 5 in below list using binary search, it doesn't work and returns me -1 index. Why is that?

numbers = [1,4,6,9,10,5,7]

Answer: List is not sorted.
"""
import time
from util import time_it


@time_it # decorator
def linear_search(number_list, number_to_find):
    """
    Performs linear search.
    """
    for index, element in enumerate(number_list):
        if element == number_to_find:
            return index
    return -1

@time_it
def binary_search(numbers_list, number_to_find):
    """
    Performs binary search. Returns index of found number or -1 otherwise.
    Expects sorted list.
    """
    left_index = 0
    right_index = len(numbers_list) - 1
    mid_index = 0

    while left_index <= right_index:

        mid_index = (left_index + right_index)  // 2  # // ensures result will be the intiger
                                                      # portion of the division 2.5 = 2.
        mid_number = numbers_list[mid_index]

        # Case found.
        if mid_number == number_to_find:
            return mid_index

        # Case mid_number is lower than number_to_find.
        if mid_number < number_to_find:
            left_index = mid_index + 1 # + 1 ensures previous mid index is not checked again.
        # Case mid_number is greater than the number_to_find.
        else:
            right_index = mid_index - 1 # - 1 ensures previous mid index is not checked again.

    return -1 # Case number not in list.


def binary_search_recursive(numbers_list, number_to_find, left_index, right_index):
    """
    Performs binary search using a recursive algorithm. Expects sorted list.
    """
    if right_index < left_index:
        return -1 # Not found.

    mid_index = (left_index + right_index)  // 2  # // ensures result will be the intiger
                                                    # portion of the division 2.5 = 2.
    mid_number = numbers_list[mid_index]

    # Case found.
    if mid_number == number_to_find:
        return mid_index

    # Case mid_number is lower than number_to_find.
    if mid_number < number_to_find:
        left_index = mid_index + 1 # + 1 ensures previous mid index is not checked again.
    # Case mid_number is greater than the number_to_find.
    else:
        right_index = mid_index - 1 # - 1 ensures previous mid index is not checked again.

    # Recursive function. This avoids the while loop.
    return binary_search_recursive(numbers_list, number_to_find, left_index, right_index)


def find_all_occurances(numbers_list, number_to_find):
    """
    Case where repeated values are accepted. Expects sorted list.
    """

    index = binary_search_recursive(numbers_list,
                                    number_to_find,
                                    0,
                                    len(numbers_list) - 1)
    indices = [index]
    
    # Finds the indices on the left hand side.
    i = index - 1
    while i >= 0:
        if numbers_list[i] == number_to_find:
            indices.append(i)

        else:
            break

        i -= 1

    i = index + 1
    # Finds the indices on the right hand side.
    while i < len(numbers_list):
        if numbers_list[i] == number_to_find:
            indices.append(i)

        else:
            break

        i += 1

    return sorted(indices)


if __name__ == '__main__':
    n_list = list(range(0, 1000001))

    print(f"Number found at index {linear_search(n_list, 1000000)} using linear search.")
    print(f"Number found at index {binary_search(n_list, 1000000)} using binary search.")

    start = time.time()
    recursive_search = binary_search_recursive(n_list,
                                               1000000,
                                               0,
                                               len(n_list) - 1)
    end = time.time()
    print(f"Number found at index {recursive_search} using binary search recursive.")
    print(f"Binary search recursive took {round((end-start) * 1000, 2)} miliseconds.")
    n_list.append(1000000)
    n_list.append(1000000)
    print(n_list[-3:])
    start = time.time()
    more_finings = find_all_occurances(n_list, 1000000)
    end = time.time()
    print(f"Number found at index {more_finings} using binary search recursive.")
    print(f"find all ocurrances took {round((end-start) * 1000, 2)} miliseconds.")

