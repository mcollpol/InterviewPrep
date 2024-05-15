"""
Binary Search Exercise.
"""
class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_child(self, data):
        if data == self.data: # Avoids duplicates.
            return
        
        if data < self.data:
            # Add data in left subtree.
            if self.left: # If self.left is not None call add_child recursively.
                self.left.add_child(data)
            else: # If free, add the new node here.
                self.left = BinarySearchTreeNode(data)
        else: # Same for right side.
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        """
        Performs In order Traversal to the tree.
        """
        elements = []

        # Visits left tree adds to elements list.
        if self.left:
            elements += self.left.in_order_traversal() # Recursive call.

        # Visit base node and appends node when there is
        # no more depth or existing deph has already been covered.
        elements.append(self.data) # Appends node data.

        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    
    def search(self, val):
        """
        Method searches for a value in the tree.
        """
        if self.data == val:
            return True # Case value is found.

        if val < self.data: # Value might be in left side tree.
            if self.left: # If there is a left tree..
                return self.left.search(val) # RETURNing the result of the recursive search.
            # Value not in tree.
            return False

        if val > self.data: # Value might be in right side tree.
            if self.right: # If there is a right tree..
                return self.right.search(val) # Recursive search.
            # Value not in tree.
            return False

    def find_min(self):
        """
        Finds minimum element in entire binary tree.
        """
        if self.left:
            return self.left.find_min()
        return self.data

    def find_max(self):
        """
        Finds maximum element in entire binary tree.
        """
        if self.right:
            return self.right.find_max()
        return self.data        

    def calculate_sum(self):
        """
        Sums all elements from tree.
        """
        return sum(self.in_order_traversal())

    def post_order_traversal(self):
        """
        Performs post order traversal of a binary tree.
        """
        elements = []

        # Visits left tree adds to elements list.
        if self.left:
            elements += self.left.post_order_traversal() # Recursive call.
            # Each time we loop we are going one level down.

        if self.right:
            elements += self.right.post_order_traversal()

        # Visit base node:
        elements.append(self.data) # Appends base node data.

        return elements

    def pre_order_traversal(self):
        """
        Perofrms pre order traversal of a binary tree.
        """
        elements = []

        # Visit base node:
        elements.append(self.data) # Appends base node data.

        # Visits left tree adds to elements list.
        if self.left:
            elements += self.left.pre_order_traversal() # Recursive call.

        if self.right:
            elements += self.right.pre_order_traversal()

        return elements
    
    def delete(self, val):
        """
        Deletes value from tree.
        If value not found in Tree nothing will be done.
        """
        # Value could be in a left side tree.
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)

        # Value could be in a right side tree.
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)

        # At this point current node is node with value == val if found.
        else:
            # If there are no childs from current node.
            if self.left is None and self.right is None:
                return None

            if self.left is None:
                return self.right # We return right child to be the parent node so
                                # the current node gets deleted.

            if self.right is None:
                return self.left # We return the left child to the parent node so
                                  # the current node gets deleted.
            """
            # Finding the minum value from right tree delete strategy.
            min_val = self.right.find_min()
            self.right = self.right.delete(min_val) # This will delete the copied value from the tree.
                                                    # and we asign the right tree from current node
                                                    # to be the one after that value has been deleted.
            self.data = min_val # This is the copy operation.
            """
            # Finding the maximum value from left side tree delete strategy.
            max_val = self.left.find_max()
            self.left = self.left.delete(max_val)
            self.data = max_val

        return self # Tree has been modified.


def build_tree(elements):
    """
    Builds tree from given elements.
    """
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.search(4))
    print(numbers_tree.find_min())
    print(numbers_tree.find_max())
    print(numbers_tree.calculate_sum())
    print(numbers_tree.post_order_traversal())
    print(numbers_tree.pre_order_traversal())
    numbers_tree.delete(20)
    print(f'After deletion (in order): {numbers_tree.in_order_traversal()}')
    numbers_tree.delete(1)
    print(f'After deletion (in order): {numbers_tree.in_order_traversal()}')
