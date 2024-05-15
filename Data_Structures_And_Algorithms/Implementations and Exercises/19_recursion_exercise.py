"""
Recursion exercises.
"""

def find_sum(n):
    """
    Find the sum of all the elements from 1 up to n.
    """
    if n==1: # 2. Base condition to terminate the recursion.
        return 1 # 3. Return base condition with simple answer.

    return n + find_sum(n-1) # 1. Divide big problem into small and simple problem.

if __name__ =='__main__':
    print(find_sum(5))
