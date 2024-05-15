"""
Implements insertion sort exercises.
"""

def median(elements):
    """ 
    Calculates the median of an array.
    """
    size = len(elements)
    # Array is even:
    if size % 2 == 0:
        return (elements[size//2 - 1] + elements[size//2]) / 2

    return elements[size//2]



def insertion_sort(elements):
    """
    Implements insertion sort.
    """
    for i in range(1, len(elements)): # Start at second element.
        anchor = elements[i] # Where pointer is placed.
        j = i - 1
        # Check where to place the anchor in the sorted list moving from right to left.
        while j >= 0 and anchor < elements[j]:
            elements[j+1] = elements[j] # We move current inspected element to the right.
            j -= 1
        # Once an element lower than the anchor value has been found we place anchor next to it.
        elements[j+1] = anchor
        print(median(elements[:i]))

if __name__ == '__main__':
    numbers = [11,9,29,7,2,15,28]
    insertion_sort(numbers)
    print(numbers)
