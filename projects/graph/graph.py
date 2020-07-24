"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        try:
            self.vertices[v1].add(v2)
        except:
            print("One of the vertices you tried adding dont exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]
        # if self.vertices[vertex_id]:
        # else:
        #     return None

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # make a queue
        q = Queue()
        # enqueue our start node
        q.enqueue(starting_vertex)
        
        # make a set to track visited nodes
        visited = set()
        
        # while queue still has things in it
        while q.size() > 0:
        ## dq from front of the line, this is our current node
            current_node = q.dequeue()
        ## check if we've visited, if not:
            if current_node not in visited:
        ### mark it as visited
                visited.add(current_node)
                print(current_node)
        ### get its neighbors
                neighbors = self.get_neighbors(current_node)
        ### iterate over neighbors,
                for neighbor in neighbors:
        #### add to queue
                    q.enqueue(neighbor)
                    
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # make a stack
        s = Stack()
        # push our starting node onto the stack
        s.push(starting_vertex)
        # make a set to track the nodes we've visited
        visited = set()
        
        # as long as our stack isn't empty
        while s.size() > 0:
        ## pop off the top, this is our current node
            current_node = s.pop()
            
        ## check if we have visited this before, and if not:
            if current_node not in visited:
        ### mark it as visited
                visited.add(current_node)
        ### print it (in this case)
                print(current_node)
        ### get its neighbors
                neighbors = self.get_neighbors(current_node)
        ### iterate over neighbors
                for neighbor in neighbors:
        #### and add them to our stack
                    s.push(neighbor)
                    
    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        
        This should be done using recursion.
        """
        # get a base case
        # work toward base case
        # call itself

        # the base case is when the current node is in the visited set
        # work toward the base case by getting the current nodes neighbors and performing the dft_recursive function
        # on all of them while also passing it the updated visited list
        if visited == None:
            visited = set()

        current_node = starting_vertex
        neighbors = self.get_neighbors(current_node)

        if current_node not in visited:
            print(current_node)
            visited.add(current_node)

            for neighbor in neighbors:
                self.dft_recursive(neighbor, visited)
        return
    
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # instead of a queue of verticies, make it a queue of paths TO a specific vertex
        q = Queue()
        path = [starting_vertex]
        q.enqueue(path)
        visited = set()
        
        while q.size() > 0:
            current_path = q.dequeue()
            # still need the current node to check if its been visited or not - can get it by grabbing the last item out of the current path
            current_node = current_path[-1]

            if current_node not in visited:
                # since i am building up a path as a traverse the graph - once i find the destination vertex - getting the path is as simple as returning what ive built up so far
                if current_node == destination_vertex:
                    return current_path

                visited.add(current_node)
                neighbors = self.get_neighbors(current_node)

                # this is what builds up the path each time we go to another vertex - i copy the old path and then append the new neighbor to it. Then i can enqueue the new path
                for neighbor in neighbors:
                    next_path = current_path.copy()
                    next_path.append(neighbor)
                    q.enqueue(next_path)


    
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
         # make a stack
        s = Stack()
        # create a path to store the nodes to the current vertext
        path = [starting_vertex]
        # push the path onto the stack
        s.push(path)
        # make a set to track the nodes we've visited
        visited = set()
        
        # as long as our stack isn't empty
        while s.size() > 0:
        ## pop off the top of the stack - this is our list of nodes i.e our path
            current_path = s.pop()
            # current node can be grabbed off the last item in the list
            current_node = current_path[-1]
            
        ## check if we have visited this before, and if not:
            if current_node not in visited:
        ### mark it as visited
                visited.add(current_node)
            
                # whenever we find the destination node we can just return our current path at that point
                if current_node == destination_vertex:
                    return current_path

        ### get its neighbors
                neighbors = self.get_neighbors(current_node)
        ### iterate over neighbors
                for neighbor in neighbors:
                    # we need to create the next path that will be added to our stack
                    next_path = current_path.copy()
                    next_path.append(neighbor)
                    s.push(next_path)
    
    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        
        This should be done using recursion.
        """

        if visited == None:
            visited = set()

        current_node = starting_vertex
        neighbors = self.get_neighbors(current_node)
        path.append(current_node)

        if current_node == destination_vertex:
            visited.add(current_node)
            return path
        else:
            if current_node not in visited:
                visited.add(current_node)

                for neighbor in neighbors:
                    path = self.dfs_recursive(neighbor, destination_vertex, visited, path)
                    if destination_vertex in visited:
                        return path
                    else:
                        path.pop()

        return path
        
        

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)


    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    graph.add_edge('0', '4')

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    print("### BFT ###")
    graph.bft(1)


    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("### DFT ###")
    graph.dft(1)
    print("### DFT with RECURSION ###")
    graph.dft_recursive(1)


    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("### BFS ###")
    print("Should return [1, 2, 4, 6]")
    print(graph.bfs(1, 6))


    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print("### DFS ITERATIVE ###")
    print(graph.dfs(1, 6))
    print("### DFS RECURSIVE ###")
    print(graph.dfs_recursive(1, 6))