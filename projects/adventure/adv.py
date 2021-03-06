from room import Room
from player import Player
from world import World

from ast import literal_eval

from util import Queue, Stack

from Graph import Graph

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)


# --------MY STUFF STARTS HERE------------- #

# traversal_path = ['n', 'n']
# traversal_path is what the test code will use to walk through all the rooms
traversal_path = []
rooms_graph = Graph()
# add starting room to graph
rooms_graph.add_room(player.current_room.id)

# add the starting rooms exits
exits = player.current_room.get_exits()
for direction in exits:
    rooms_graph.add_exit(player.current_room.id, direction)

# if random direction ever returns None its because the room we are in has had all its exits explored
random_direction = rooms_graph.get_random_direction(player.current_room.id)

# i know i know my taversal graph is full once my rooms graphs rooms have all been filled out
while len(rooms_graph.rooms) != 500:
    # for the DFT - i check the room on each loop - if random direction ever returns None -that means ive 
    # reached a dead end and can begin the BFS 
    while random_direction is not None:
        # add the direction we are travelling into our traversal path
        traversal_path.append(random_direction)
        # before moving the player to the new room i need to update the graph for the current room
        # i can use the current rooms built in method to find out which room is in the direction the player is travelling and update accordingly
        room_in_direction = player.current_room.get_room_in_direction(random_direction)
        rooms_graph.rooms[player.current_room.id][random_direction] = room_in_direction.id                                                                                                                                                                     

        # add the new room in that direction to the graph
        rooms_graph.add_room(room_in_direction.id)

        # get all of the rooms exits and fill in the graph
        exits = room_in_direction.get_exits()
        for direction in exits:
            rooms_graph.add_exit(room_in_direction.id, direction)

        # after adding the next room and its exits to the graph i need to update its exit in the graph that i already know about (the current player room)
        opposite_direction = rooms_graph.get_opposite_direction(random_direction)
        rooms_graph.rooms[room_in_direction.id][opposite_direction] = player.current_room.id

        # travel in the direction
        player.travel(random_direction)
        # update random direction to continue the loop until there are no explored rooms
        random_direction = rooms_graph.get_random_direction(player.current_room.id)
    else:
        # if DFT ends we should recheck the len of the rooms graph to see if we are done
        if len(rooms_graph.rooms) == 500:
            break
        # BFS if we reach the end of a DFT - need to find the shortest path to the next ? room and then begin the DFT again
        visited = set()
        q = Queue()
        next_room = player.current_room
        rooms_exits = rooms_graph.get_room_exits(player.current_room.id)
        visited.add(player.current_room)
        # store the direction AND the next room in a tuple so i can use later
        for direction in rooms_exits:
            next_room = player.current_room.get_room_in_direction(direction)
            path = [(next_room, direction)] # should give me the room of the exit
            q.enqueue(path)

        while q.size() > 0:
            current_path = q.dequeue()
            current_room = current_path[-1][0] # last item in the path but first item in the tuple
            if current_room not in visited:
                visited.add(current_room)
                
                room_exit_directions = rooms_graph.get_room_exits(current_room.id)
                random_direction = rooms_graph.get_random_direction(current_room.id)
                # if random direction ever returns a value its because we have found an unexplored room
                # in which case go to the else statement
                if random_direction is None:
                    # should get the rooms exits and create new paths to enqueue
                    for direction in room_exit_directions:
                        next_path = current_path.copy()
                        next_path.append((current_room.get_room_in_direction(direction), direction))
                        q.enqueue(next_path)

                else:
                    # we have found an unexplored room and we should search it using DFT
                    player.current_room = current_room
                    for path in current_path:
                        # append the direction to the traversal path
                        traversal_path.append(path[1])
                    break

# print("len of room graph: ", len(room_graph))
# print("traversal path: ", traversal_path)



# --------MY STUFF ENDS HERE------------- #

# MY TRAVERSAL TEST
# visited_rooms = set()
# player.current_room = world.starting_room
# visited_rooms.add(player.current_room)

# for pair in traversal_path:
#     player.travel(pair[0])
#     visited_rooms.add(player.current_room)

# if len(visited_rooms) == len(room_graph):
#     print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
# else:
#     print("TESTS FAILED: INCOMPLETE TRAVERSAL")
#     print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)
# print("TRAVERSAL LENGTH: ", len(traversal_path))
# print("TRAVERSAL: ", traversal_path)
for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
