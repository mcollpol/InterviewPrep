import time


def time_it(func):
    """
    Times the execution of a function.
    """
    def wrapper(*args, **kwargs):
        """
        Valid for non recursive funcs.
        """
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        #wrapper.__total_execution_time__ = round((end-start) * 1000, 2)
        print(f'{func.__name__} took {round((end-start) * 1000, 2)} mil sec')
        return result

    return wrapper
