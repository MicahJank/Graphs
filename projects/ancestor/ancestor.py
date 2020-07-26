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

# will return the target nodes parent/s node/s
def get_neighbors(adjaceny_list, target_node):
    return adjaceny_list[target_node]

def earliest_ancestor(ancestors, starting_node):
    # take the ancestors and put them in an adjacency list where the connected neighbors are each nodes parent/s
    # creates the adjacency list that will create a list of the nodes and all their parents for quick access - can use this to find neighbors quick
    adjaceny_list = {}
    for pair in ancestors:
        parent = pair[0]
        child = pair[1]

        if child not in adjaceny_list:
            adjaceny_list[child] = set()
            adjaceny_list[child].add(parent)
        else:
            adjaceny_list[child].add(parent)

    # create stack
    stack = Stack()

    print(adjaceny_list)