"""
Merge sort exercises.
"""

def merge_two_sorted_lists(a, b, arr):
    """
    Merges two already sorted lists.
    If we avoid using an auxiliar list and just modify the arr we
    reduce space complexity.
    """
    i = j = k = 0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            arr[k] = a[i]
            i += 1
        else: # a[i] >= b[j]:
            arr[k] = b[j]
            j += 1
        k += 1

    # Takes into account different len arrays:
    if i < len(a):
        for element in a[i:]:
            arr[k] = element
            k += 1
    elif j < len(b):
        for element in b[j:]:
            arr[k] = element
            k += 1

def merge_sort(arr):
    """
    Implements merge sort algorithm that sorts given array.
    """
    if len(arr) <= 1: # Stops the recursion once single element arrays have formed.

        return

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left) # Keeps dividng the array.
    merge_sort(right) # Keeps divindg the array.

    # This return is only reached once the recursion stops at single
    # element arrays, and starts going backwards.
    merge_two_sorted_lists(left, right, arr)


def merge_two_sorted_lists_by_key(a, b, arr, key, descending=False):
    """
    Merges two already sorted lists.
    If we avoid using an auxiliar list and just modify the arr we
    reduce space complexity.
    """
    i = j = k = 0

    if descending:
        while i < len(a) and j < len(b):
            if a[i][key] > b[j][key]:
                arr[k] = a[i]
                i += 1
            elif a[i][key] <= b[j][key]:
                arr[k] = b[j]
                j += 1
            k += 1

        # Takes into account different len arrays:
        if i < len(a):
            for element in a[i:]:
                arr[k] = element
                k += 1
        elif j < len(b):
            for element in b[j:]:
                arr[k] = element
                k += 1

    else:
        while i < len(a) and j < len(b):
            if a[i][key] < b[j][key]:
                arr[k] = a[i]
                i += 1
            elif a[i][key] >= b[j][key]:
                arr[k] = b[j]
                j += 1
            k += 1

        # Takes into account different len arrays:
        if i < len(a):
            for element in a[i:]:
                arr[k] = element
                k += 1
        elif j < len(b):
            for element in b[j:]:
                arr[k] = element
                k += 1

def merge_sort_by_key(arr, key, descending=False):
    """
    Sorts a list of dicts based on key.
    """
    if len(arr) <= 1: # Stops the recursion once single element arrays have formed.

        return

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort_by_key(left, key, descending) # Keeps dividng the array.
    merge_sort_by_key(right, key, descending) # Keeps divindg the array.

    # This return is only reached once the recursion stops at single
    # element arrays, and starts going backwards.
    merge_two_sorted_lists_by_key(left, right, arr, key, descending)


if __name__ == '__main__':
    f = [10, 3, 15, 7, 8, 23, 97, 29, 95]
    merge_sort(f)
    print(f)
    elements = [
                { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
                { 'name': 'rajab', 'age': 12,  'time_hours': 3},
                { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
                { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
                ]

    merge_sort_by_key(elements, 'age', True)
    print(elements)

    merge_sort_by_key(elements, 'name')
    print(elements)
