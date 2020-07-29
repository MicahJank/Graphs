from util import Stack 
'''
Suppose we have some input data describing a graph of relationships between parents and children over multiple 
generations. The data is formatted as a list of (parent, child) pairs, 
where each individual is assigned a unique integer identifier.

For example, in this diagram and the sample input, 3 is a child of 1 and 2, and 5 is a child of 4:
                                             10
                                            /
                                           1   2   4  11
                                            \ /   / \ /
                                             3   5   8
                                              \ / \   \ 
                                               6   7   9


Write a function that, given the dataset and the ID of an individual in the dataset, 
returns their earliest known ancestor – the one at the farthest distance from the input individual. 
If there is more than one ancestor tied for "earliest", return the one with the lowest numeric ID. 
If the input individual has no parents, the function should return -1.

Clarifications:

The input will not be empty.
There are no cycles in the input.
There are no "repeated" ancestors – if two individuals are connected, it is by exactly one path.
IDs will always be positive integers.
A parent may have any number of children.

'''
# what are the nodes?
# -  the ids of an individual

# what are the edges?
# - the children


# PLAN
# DFS seems the way to go since we want to reach the farthest thing away the quickest
# need a get neighbors function

# get neighbors sudo code
# - will need to take in a node to get the neighbors of
# - get neighbors can also take in the adjacency list and use it to find the neighbors
#  { 1: {5, 4, 3 }, 2: { 1, 5 } } -- eg

adjaceny_list = {}

# create adjacency list
def create_adjacency_list(nodes):
    for pair in nodes:
        parent = pair[0]
        child = pair[1]

        if child not in adjaceny_list:
            adjaceny_list[child] = set()
            adjaceny_list[child].add(parent)
        else:
            adjaceny_list[child].add(parent)


# will return the target nodes parent/s node/s
def get_neighbors(adjaceny_list, target_node):
    if target_node in adjaceny_list:
        return adjaceny_list[target_node]
    else:
        return

def dfs_iterative(starting_node):
    s = Stack()
    path = [starting_node]
    s.push(path)

    visited = set()

    possible_paths = []
        
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
            # if current_node == destination_vertex:
            #     return current_path

            neighbors = get_neighbors(adjaceny_list, current_node)
            if neighbors is not None:
                for neighbor in neighbors:
                    # we need to create the next path that will be added to our stack
                    next_path = current_path.copy()
                    next_path.append(neighbor)
                    s.push(next_path)
            # if neighbors is None its because we have reached the end of a path - at this point i can add the path to the possible paths array
            else:
                # the initial path should be added regardless and i know that its the initial path when the len of the possible paths array is 0
                if len(possible_paths) == 0:
                    possible_paths.append(current_path)
                # after the inital path has been added though - i need to check subsequent paths with the length of the path in possible paths
                # if its greater then that means i want to override whatever is the paths are that are in possible paths
                elif len(current_path) > len(possible_paths[0]):
                    possible_paths.clear()
                    possible_paths.append(current_path)
                # also whenever i get a current path that has the same number of layers as what is in the possible paths - then i should simply add them to the possible paths
                elif len(current_path) == len(possible_paths[0]):
                    possible_paths.append(current_path)

    print(possible_paths)
    return possible_paths

def earliest_ancestor(ancestors, starting_node):
    # take the ancestors and put them in an adjacency list where the connected neighbors are each nodes parent/s
    # creates the adjacency list that will create a list of the nodes and all their parents for quick access - can use this to find neighbors quick
    create_adjacency_list(ancestors)

    if get_neighbors(adjaceny_list, starting_node) is None:
        return -1

    paths = dfs_iterative(starting_node)

    # paths can either have 1 path in which case i will just need to get the last item in that path to get the earliest ancestory
    # if paths has multiple paths in it though - i will need to check and compare the last items in the list to see which has the lower id number and return that one

    if len(paths) > 1:
        lowest_id = paths[0][-1]
        for path in paths:
            if path[-1] < lowest_id:
                lowest_id = path[-1]
        print(lowest_id)
        return lowest_id

    print("final answer", paths[0][-1])
    return paths[0][-1]



# test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

# earliest_ancestor(test_ancestors, 9)