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
                    
    def dft_recursive(self, starting_vertex, visited=set()):
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
        current_node = starting_vertex
        neighbors = self.get_neighbors(current_node)


        if current_node in visited:
            # print(starting_vertex)
            return
        else:
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
          # make a queue
        q = Queue()
        # enqueue our start node
        q.enqueue(starting_vertex)
        
        # make a set to track visited nodes
        visited = set()
        path = []
        shortest_path = []
        
        current_node = starting_vertex
        # while queue still has things in it
        while current_node != destination_vertex:
        ## dq from front of the line, this is our current node
        ## check if we've visited, if not:
            if current_node not in visited:
        ### mark it as visited
                visited.add(current_node)
                path.append(current_node)
        ### get its neighbors
                neighbors = self.get_neighbors(current_node)
        ### iterate over neighbors,
                for neighbor in neighbors:
        #### add to queue
                    q.enqueue(neighbor)

                current_node = q.dequeue()

        for i in reversed(path):


    
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO
    
    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        
        This should be done using recursion.
        """
        pass  # TODO

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
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))