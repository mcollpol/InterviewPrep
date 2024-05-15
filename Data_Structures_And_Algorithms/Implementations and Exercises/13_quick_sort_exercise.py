"""
Quick sort exercises.
"""
def swap(a, b, arr):
    """
    Swaps two elements of an array.
    """
    arr[a], arr[b] = arr[b], arr[a]

def partition_hoare(elements, start, end):
    """
    Partitionin Hoare scheme implementation.
    """
    pivot_index = start
    pivot = elements[pivot_index]

    while start < end: # Stops when pointers cross.
        while start < len(elements) and elements[start] <= pivot: # Start condition.
                                        # Equal is to take care of duplicates.
            start += 1

        while elements[end] > pivot: # End condition.
            end -= 1

        if start < end: # Swapping end and start elements.
            swap(start, end, elements)

    swap(pivot_index, end, elements) # Swapping end pointer with pivot to sort it.

    return end # Position of the sorted pivot that splits the list.

def partition_lomuto(elements, start, end):
    """
    Partitionin Lomuto scheme implementation. 
    p_index is start.
    pivot_index is the end of the array.
    """
    pivot = elements[end]
    p_index = start

    for i in range(start, end):
        if elements[i] <= pivot:
            swap(i, p_index, elements)
            p_index += 1

    swap(p_index, end, elements)
    return p_index

def quick_sort(elements, start, end, p_scheme='hoare'):
    """
    Implements quick sort.
    """
    if len(elements) == 1:
        return
    if start < end: # Terminates the recursion process proceeds only when there
                    # are two or more elements in the subarray being sorted.
        if p_scheme == 'hoare':
            partition_index = partition_hoare(elements, start, end)
        elif p_scheme == 'lomuto':
            partition_index = partition_lomuto(elements, start, end)
        else:
            raise ValueError('Partition scheme is not implemented. Options = [hoare, lomuto]')
        quick_sort(elements, start, partition_index - 1)     # Left partition.
        quick_sort(elements, partition_index + 1, end)       # Right partition.



if __name__ == '__main__':
    numbers = [11,9,2,1,67,34,88,34]

    quick_sort(numbers, 0, len(numbers) - 1, 'hoare')
    print(numbers)
    
    quick_sort(numbers, 0, len(numbers) - 1, 'lomuto')
    print(numbers)
