"""
Implement hash table where collisions are handled using linear probing. 
"""
# Keys are unique.
class HashTable:
    """
    HashTable simple implementation using Linear Probing for collision handling.
    """
    def __init__(self):
        self.max = 10 # MAX size of list of the values array.
        self.arr = [() for i in range(self.max)] # List of tuples initialization.
        # The key value pairs will be stored as tuples.

    # Hash function allows to get an element by key with O(1) aprox.
    # In this specific case it would be O(n) where 'n' is the number of chars in
    # the string key assumed to be small.
    def get_hash(self, key):
        """
        Hash function to obtain the index that corresponds to the string key.
        """
        h = 0
        for char in key:
            h +=ord(char)# SUM of ASCII values for each char.
        return h % self.max  # Mode operation to limit it to 100 positions max.

    # Overrides the set operator so we can set the value like t[key] = value.
    def __setitem__(self,key, value):
        """
        Adds key, value pair into the hashmap.
        """
        h =self.get_hash(key) # Get index using hash function.

        # If key already present, override value:
        key_index = self.find_key(key)
        if key_index is not None:
            self.arr[key_index] = (key, value)
            return

        value_setted = False
        for index in self.get_search_range(h):
            if not self.arr[index]: # Index is free/ tuple in h is empty.
                self.arr[index] = (key, value)
                value_setted = True
                break

        if not value_setted:
            raise BufferError("Hashmap is full.")

    # Overrides the get operator so we can get a value like: t[key].
    def __getitem__(self,key):
        """
        Gets the value for given key.
        """
        index = self.find_key(key)
        if index is not None:
            return self.arr[index][1]

        return None # Python returns None by default if no return operation is found.
                    # But adding it adds clarity and aligns with PEP8.

    def __delitem__(self,key):
        """
        Deletes item given a key.
        """
        h = self.find_key(key)
        if h is not None:
            self.arr[h] = ()
        else:
            raise KeyError(f'{key} not in Hashmap.')

    def get_search_range(self, h):
        """
        Create range that starts with 'h' for an efficient search.
        """
        # * In Python, the asterisk (*) is used for unpacking iterable objects like lists,
        # tuples, or ranges into individual elements. It has to be used in a way where
        # unpacked values can be stored, like using a list like here.
        return [*range(h, self.max)] + [*range(0, h)]

    def find_key(self, key):
        """
        Finds key index if it is already stored in array.
        """
        h =self.get_hash(key)

        for index in self.get_search_range(h):
            if self.arr[index] and self.arr[index][0] == key:
                return index

        return None

if __name__ == '__main__':
    hh = HashTable()
    hh['march 6'] = 310
    hh['march 7'] = 340
    hh['march 8'] = 380
    hh['march 17'] = 459
    hh['march 17'] = 45
    print(hh.arr)
    print(hh['march 17'])
    del hh['march 7']
    print(hh.arr)
    hh['march 18'] = 45
    hh['march 19'] = 45
    hh['march 20'] = 45
    hh['march 21'] = 45
    hh['march 22'] = 45
    hh['march 23'] = 45
    hh['march 24'] = 45
    print(hh.arr)
    hh['march 25'] = 45
