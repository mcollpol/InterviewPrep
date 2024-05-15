class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}

        for start, end in self.edges:
            # Case start already in dict.
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            # Case start not in dict.
            else:
                self.graph_dict[start] = [end]

        print(f"Graph dict {self.graph_dict}")

    def get_paths(self, start, end, path=None):
        """
        Returns possible paths in graph given start and end points.
        """
        if path is None:
            path = [start] # This is to avoid using empty list
                           # as default path value (not pylint complient.)
        else:
            path = path + [start] # Path initialization.

        if start == end: # Case start and end are the same.
            return [path] # Important []: Returns/closes the path found.

        if start not in self.graph_dict:
            return []

        paths = [] # List to store all possible paths.
        for node in self.graph_dict[start]: # Search for end in all start connections.
            if node not in path: # Avoids node duplication in path.
                # Reursive call to find a possible connexion from node to end.
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)

        return paths

    def get_shortest_path(self, start, end, path=None):
        """
        Gets shortest path.
        """
        if path is None: # This is to avoid using empty list
                         # as default path value (not pylint complient.)
            path = [start]
        else:
            path = path + [start]

        if start == end:
            return path

        if start not in self.graph_dict:
            return None

        # Case start != end.
        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp: # Aims for shortest path available. sp can be None.
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp

        return shortest_path


if __name__ == '__main__':
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto")
    ]
    g = Graph(routes)

    start = "Mumbai"
    end = "New York"

    print(f'Paths between {start} and {end}: ', g.get_paths(start, end))
    print(f'Paths between {start} and {end}: ', g.get_shortest_path(start, end))
