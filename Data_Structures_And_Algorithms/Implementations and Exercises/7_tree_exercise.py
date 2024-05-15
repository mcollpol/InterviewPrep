class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    
    # Keeping it simplem without checkig for duplicates.
    def add_child(self, child): # Child is an instance of TreeNode class.
        """
        Adds a TreeNode as a child of self.
        """
        child.parent = self # This fills the parent property of the child TreeNode.
        # Adding a child to the self object. Self will become the parent of the child.
        self.children.append(child)

    def get_level(self):
        """
        Gets the level of the tree node.
        """
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        
        return level

    def print_tree(self, print_type, level):
        """
        Prints the tree recursively.
        """
        spaces = ' ' * self.get_level() * 3 # Adds 3 spaces for each level.
        prefix = spaces + "|__" if self.parent else ""

        if print_type == 'both':
            print(f'{prefix}{self.data["name"]} ({self.data["designation"]})')
        elif print_type == 'name':
            print(f'{prefix}{self.data["name"]}')
        elif print_type == 'designation':
            print(f'{prefix}{self.data["designation"]}')
        else:
            raise ValueError("Print types: both, name, desingation")
        if self.children and self.get_level() < level: # If list is not empty.
            # We need to do a recursive print.
            for child in self.children:
                child.print_tree(print_type, level) # Here is how we apply recursivety.



def build_tree():
    """
    Builds product tree.
    """
    ceo = TreeNode({'name': 'Niupul','designation': 'CEO'})

    cto = TreeNode({'name': 'Chinmay', 'designation': 'CTO'})

    inf_head = TreeNode({'name': 'Vishwa',
                     'designation': 'Infrastructure Head'})
    inf_head.add_child(TreeNode({'name': 'Dhaval',
                     'designation': 'Cloud Manager'}))
    inf_head.add_child(TreeNode({'name': 'Abhijit',
                    'designation': 'App Manager'}))

    cto.add_child(inf_head)
    cto.add_child(TreeNode({'name': 'Aamir',
                     'designation': 'Application Head'}))

    hr_head = TreeNode({'name': 'Gels',
                     'designation': 'HR Head'})
    hr_head.add_child(TreeNode({'name': 'Peter',
                     'designation': 'Rec Manager'}))
    hr_head.add_child(TreeNode({'name': 'Waqas',
                     'designation': 'Policy Manager'}))

    ceo.add_child(cto)
    ceo.add_child(hr_head)

    return ceo

if __name__ == '__main__':
    root = build_tree()
    root.print_tree('designation', 1)
