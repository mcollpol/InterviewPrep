"""
Selection sort exercise.
"""
def selection_sort(arr):
    """
    Selection sort implementation.
    """
    size = len(arr)
    for i in range(size-1): # Last item will be indirectly checked.
        min_index = i
        for j in range(min_index+1, size): # Checks for min value in unsorted arr.
            if arr[j] < arr[min_index]:
                min_index = j
        if i != min_index: # If i index already has the min element no need for a swap.
            arr[i], arr[min_index] = arr[min_index], arr[i] # Swap.

def multi_level_sort(arr, key_preference):
    """
    Multi level Selection sort implementation based on dict key preference.
    """
    # [-1::-1] flips the list.
    for key in key_preference[-1::-1]: # Sorting first by least important key.
        size = len(arr)
        for i in range(size-1): # Last item will be indirectly checked.
            min_index = i
            for j in range(min_index+1, size): # Checks for min value in unsorted arr.
                if arr[j][key] < arr[min_index][key]:
                    min_index = j
            if i != min_index: # If i index already has the min element no need for a swap.
                arr[i], arr[min_index] = arr[min_index], arr[i] # Swap.



if __name__ == '__main__':
    tests = [[21, 38, 29, 17, 4, 25, 11, 32, 9],
             [],
             [1,5,7,8],
             [234,3,1,56,34,12,9,12,1399],
             [5]
            ]
    for test in tests:
        print(f'{test} to: ')
        selection_sort(test)
        print(test)

    a = [
        {'First Name': 'Raj', 'Last Name': 'Nayyar'},
        {'First Name': 'Suraj', 'Last Name': 'Sharma'},
        {'First Name': 'Karan', 'Last Name': 'Kumar'},
        {'First Name': 'Jade', 'Last Name': 'Canary'},
        {'First Name': 'Raj', 'Last Name': 'Thakur'},
        {'First Name': 'Raj', 'Last Name': 'Sharma'},
        {'First Name': 'Kiran', 'Last Name': 'Kamla'},
        {'First Name': 'Armaan', 'Last Name': 'Kumar'},
        {'First Name': 'Jaya', 'Last Name': 'Sharma'},
        {'First Name': 'Ingrid', 'Last Name': 'Galore'},
        {'First Name': 'Jaya', 'Last Name': 'Seth'},
        {'First Name': 'Armaan', 'Last Name': 'Dadra'},
        {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
        {'First Name': 'Aahana', 'Last Name': 'Arora'}
        ]
    multi_level_sort(a, ['First Name', 'Last Name'])
    print(a)
