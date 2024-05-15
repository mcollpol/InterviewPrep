"""
Queue excercise with multithreading.
"""
import time
import threading

from collections import deque

class Queue:
    """
    Class Queue.
    """
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        """
        Adds element to buffer.
        """
        self.buffer.appendleft(val)

    def dequeue(self):
        """
        Removes element from buffer.
        """
        return self.buffer.pop()

    def is_empty(self):
        """
        Checks if queue is empty.
        """
        return len(self.buffer)==0

    def size(self):
        """
        Returns queue size.
        """
        return len(self.buffer)

    def front(self):
        """
        Returns front element from the queue. 
        """
        return self.buffer[-1]

# Global variables
FOOD_ORDER_QUEUE = Queue() # Exercise 1 queue

# Exercise 1

def place_order(orders):
    """
    Adds an order from orders into the queue every 0.5 seconds.
    """
    for order in orders:
        FOOD_ORDER_QUEUE.enqueue(order)
        print(f'{order} queued.')
        time.sleep(0.5)

def serve_order():
    """
    Serves an order from the FOOD_ORDER_QUEUE every 2 seconds.
    """
    while FOOD_ORDER_QUEUE.size() > 0:
        order = FOOD_ORDER_QUEUE.dequeue()
        print(f'{order} served.')
        time.sleep(2)

# Exercise 2

def create_binary_count_queue(max_num):
    """
    Fills BINARY_QUEUE with consecutive binary numbers
    till max_num is reached and prints them/
    """
    queue = Queue() # Exercise 2 queue
    queue.enqueue('1')

    for _ in range(0, max_num):
        front = queue.front()
        print("   ", front)
        queue.enqueue(front + "0")
        queue.enqueue(front + "1")

        queue.dequeue()


if __name__ == '__main__':
    # Exercise 1
    food_orders =[{'banana': 2}, {'apple': 1},
                  {'t': 10}, {'ds': 12}, {'12312': 12312}]
    t1 = threading.Thread(target=place_order,
                          args=(food_orders,))
    t2 = threading.Thread(target=serve_order)

    t1.start()
    time.sleep(1)
    t2.start()

    t1.join()
    t2.join()

    print('done')

    # Exercise 2

    create_binary_count_queue(10)

