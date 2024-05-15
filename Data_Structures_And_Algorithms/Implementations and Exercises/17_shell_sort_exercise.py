"""
Shell sort exercise.
"""

def shell_sort(arr, remove_duplicates=False):
    """
    Shell sort implementation.
    """
    size = len(arr)
    gap = size // 2

    while gap > 0:
        for i in range(gap, len(arr)): # Loop the whole array from gap onwards.
                                # Elements b4 the gap are already checked inisde the while.
            if i >= len(arr)-1: # When removing duplicates the size of the array changes.
                break

            anchor = arr[i]
            j = i
            # Check the gap subarray to locate where to place the anchor.
            while j >=gap and arr[j - gap] > anchor: # i.e.: arr[0] > arr[3] ?
                arr[j] = arr[j - gap]                # If true copy in gap position
                                                    # arr[3] the value of arr[0].
                j -= gap
            if remove_duplicates and arr[j - gap] == anchor:
                arr.pop(j)
            else:
                arr[j] = anchor # Copy the anchor initially in arr[3] to arr[0]. This is the swap.
        gap = gap // 2 # We reduce the gap by 2.

if __name__ == '__main__':
    tests = [[21, 38, 29, 17, 4, 25, 11, 32, 9],
             [],
             [1,5,7,8],
             [234,3,1,56,34,12,9,12,1399],
             [5]
            ]
    for test in tests:
        print(f'{test} to: ')
        shell_sort(test, True)
        print(test)
