"""
​
NOTE TO SELF UPDATE DEFINITION
​
Write a function that takes a 2D binary array and returns the number of 1 islands. 
An island consists of 1s that are connected to the north, south, east or west, or a 1 by itself. 
For example:
​
islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]
​
islands[0][1]
islands[1][1]
​
1. Describe in graphs terminology
- What are our nodes? 1s
- When do we have an edge to another node? if one step away, to NSEW
​
What do we call a group of 1s/nodes? Connected components
​
2. Build your graph or define getNeighbors()
​
3. Choose your algorithm
"""
islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]
# 4 islands
big_islands = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
               [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
               [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
               [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
               [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
               [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
               [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
               [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
               [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
               [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]
​
# 13
​
# check if we can take a step in a direction
# take that step, and see if it's a 1
def getNeighbors(node, islands):
    row, col = node

    stepNorth = stepSouth = stepWest = stepEast = None

    neighbors = []
    
    if row > 0:
        stepNorth = row - 1
        ​
    if row < len(islands) - 1:
        stepSouth = row + 1

    if col < len(islands) - 1:
        stepEast = col + 1
        ​
    if col > 0:
        stepWest = col - 1

    if stepNorth is not None and islands[stepNorth][col] == 1:
        neighbors.append((stepNorth, col))
        ​
    if stepSouth is not None and islands[stepSouth][col] == 1:
        neighbors.append((stepSouth, col))

    if stepWest is not None and islands[row][stepWest] == 1:
        neighbors.append((row, stepWest))
        ​
    if stepEast is not None and islands[row][stepEast] == 1:
        neighbors.append((row, stepEast))

    return neighbors
    ​
    ​
def dft_recursive(node, visited, islands):
    if node not in visited:
        visited.add(node)

        neighbors = getNeighbors(node, islands)
        ​
        for neighbor in neighbors:
            dft_recursive(neighbor, visited, islands)
            
def islands_counter(islands):
    total_islands = 0
    visited = set()
    # iterate over the matrix
    for row in range(len(islands)):
        for col in range(len(islands)):
            node = (row, col)
            # when we hit a 1 that hasn't been visited
            if islands[row][col] == 1 and node not in visited:
                ## increment our islands counter
                total_islands += 1
                ## run DFT on it, and mark them all as visited
                dft_recursive(node, visited, islands)
    return total_islands
​
# then continue iterating
​
print(islands_counter(islands))
print(islands_counter(big_islands))