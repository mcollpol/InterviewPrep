"""
Bubble sort exercises.
"""

def bubble_sort(elements):
    """
    Performs bubble sort. Lists and strings.
    """
    size = len(elements)

    for i in range(size - 1): # We want to do this proces n-1 times (we evaluate pairs)
                              # as the list has to be checked n-1 times for it to be all sorted.
        swapped = False
        for j in range(size - 1 - i): # Done n-1 times - i (to avoid checking already checked
                                      # elements at the end). Elements at the end are the ones
                                      # that will for sure be in the correct order already.
            if elements[j] > elements[j+1]:
                tmp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = tmp
                swapped = True
        if not swapped: # Breaks the outter loop if all items are already sorted.
            break

def bubble_sort_by_key(list_of_dicts, key):
    """
    Sorts a list of dicts based on dict key.
    """
    size = len(list_of_dicts)

    for i in range(size - 1): # We want to do this proces n-1 times (we evaluate pairs)
                              # as the list has to be checked n-1 times for it to be all sorted.
        swapped = False
        for j in range(size - 1 - i): # Done n-1 times - i (to avoid checking already checked
                                      # elements at the end). Elements at the end are the ones
                                      # that will for sure be in the correct order already.
            if list_of_dicts[j][key] > list_of_dicts[j+1][key]:
                tmp = list_of_dicts[j][key]
                list_of_dicts[j][key] = list_of_dicts[j+1][key]
                list_of_dicts[j+1][key] = tmp
                swapped = True
        if not swapped: # Breaks the outter loop if all items are already sorted.
            break

if __name__ == '__main__':
    numbers = [5,9,2,1,67,34,88,34]

    bubble_sort(numbers)
    print(numbers)

    elements = [
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
    ]

    bubble_sort_by_key(elements, 'transaction_amount')
    print(elements)

    bubble_sort_by_key(elements, 'name')
    print(elements)
