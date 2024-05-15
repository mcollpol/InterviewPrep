""""
2. Double Linked lists implementation.
"""

class Node:
    """
    Node class.
    """
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoubleLinkedList:
    """
    Double Linked list class.
    """
    def __init__(self):
        self.head = None

    def print_forward(self):
        """
        This method prints list in forward direction.
        """
        # This method prints list in forward direction. Use node.next
        if self.head is None:
            print("List is empty.")
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr += f"{str(itr.data)} --> "
            itr = itr.next

        print(llstr)

    def print_backward(self):
        """
        Print linked list in reverse direction.
        """
        # Print linked list in reverse direction. Use node.prev for this.
        if self.head is None:
            print("List is empty.")
            return

        itr = self.get_last_node()

        llstr = ''
        while itr: # Stops when node is None.
            llstr += f"{str(itr.data)} --> "
            itr = itr.prev

        print(llstr)

    def get_last_node(self):
        """
        Returns last node.
        """
        itr = self.head
        while itr.next: # Stops when next element is None.
            itr = itr.next

        return itr

    def insert_at_begining(self, data):
        """
        Inserts at begining of the list.
        """
        # Case list is empty.
        if self.head is None:
            node = Node(data, self.head, None)
            self.head = node
        # Case list is not empty. Prev link needs an update.
        else:
            node = Node(data, self.head, None)
            self.head.prev = node # Updating current first element prev link.
            self.head = node # Adding the new first element.


    def insert_at_end(self, data):
        """
        Inserts at the end of the list.
        """
        if self.head is None:
            self.head = Node(data, None, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None, itr)

    def insert_values(self, data_list):
        """
        Empties previous linkedlist and creates new one with the given normal list.
        """
        if not isinstance(data_list, list):
            raise ValueError("data_list is not of type List.")

        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        """
        Returns the lenght of the list.
        """
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    def remove_at(self, index):
        """
        Removes element at the given index.
        """
        # For python we do not need to cleanup the memory asociated
        # with the element removed.
        if index < 0 or index >= self.get_length():
            raise KeyError("Invalid index")

        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return

        count = 0
        itr = self.head
        while itr:
            if count == index: # Stoping on previous element to modify link.
                itr.prev.next = itr.next
                # Link now points to the elemen after the one being removed.
                if itr.next: # Stoping at the element after the one being removed.
                    itr.next.prev = itr.prev # Updating previous link.
                break

            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        """
        Inserts element at provided index.
        """
        if index < 0 or index > self.get_length():
            raise KeyError("Invalid Index")

        if index == 0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1: # Stoping on previous element to modify link.
                node = Node(data, itr.next, itr) # Creating new element node.
                if node.next:
                    node.next.prev = node # Updating prev link for next node.
                itr.next = node # Modifying link for the node we are stopped at.
                # Therefore, adding the new node to the linked list.
                break

            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        """
        Searches for first occurance of data_after value in linked list
        and inserts data_to_insert after data_after node.
        """
        if self.head is None:
            print("List is empty.")
            return

        itr = self.head
        index = 0
        while itr:
            if itr.data == data_after:
                self.insert_at(index + 1, data_to_insert)
                break

            itr = itr.next
            index += 1

    def remove_by_value(self, data):
        """
        Removes first node that contains data.
        """
        if self.head is None: # Checks if list is empty.
            print("List is empty.")
            return # To avoid executing following code.

        itr = self.head
        index = 0
        found = False
        while itr:
            if itr.data == data:
                self.remove_at(index)
                found = True
                break

            itr = itr.next
            index += 1

        if not found:
            print("Value is not present in the linked list.")

if __name__ == '__main__':
    ll = DoubleLinkedList()
    ll.insert_at_begining(5)
    ll.insert_at_begining(89)
    ll.insert_at_end(79)
    ll.print_forward()
    ll.insert_values(["a", "b", "c"])
    print(f'lenght: {ll.get_length()}')
    ll.remove_at(2)
    ll.print_forward()
    ll.insert_at(1, "f")
    ll.print_forward()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print_forward()
    ll.print_backward()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print_forward()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print_forward()
    ll.remove_by_value("figs")
    ll.print_forward()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_at(1)
    ll.print_forward()
