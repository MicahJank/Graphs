from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

from util import Queue, Stack

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)


# --------MY STUFF STARTS HERE------------- #

class Graph:
    def __init__(self):
        self.rooms = {}
    
    # nodes
    def add_room(self, room_id):
        self.rooms[room_id] = {}
    
    # edges
    def add_exit(self, current_room, exit):
        self.rooms[current_room][exit] = '?'

    # finds the exits for whatever room id is entered
    def get_room_exits(self, room_id):
        return self.rooms[room_id]

    # useful for when i need to fill in the graph with the previous room information
    # i.e if i go to a north room then my current room needs to know the previous
    # room is to the south
    def get_opposite_direction(self, direction):
        if direction == "n":
            return "s"
        elif direction == "s":
            return "n"
        elif direction == "w":
            return "e"
        elif direction == "e":
            return "w"

    def get_random_direction(self, room_id):
        exits_list = list(self.rooms[room_id])

        # should give back directions to rooms that havent been explored
        choices = [direction for direction in exits_list if self.rooms[room_id][direction] == "?"]

        # if the player tries to get a random direction in a room where there are no
        # unexplored paths - then i should return None
        if len(choices) > 0:
            # choose a random direction from the list
            random_direction = random.choice(choices)
            return random_direction
        else:
            return None


# traversal_path = ['n', 'n']
# traversal_path is what the test code will use to walk through all the rooms
traversal_path = []


rooms_graph = Graph()
# keep track of the previous room so that i can update its rooms as i move onto the next
prev_room = None
# add starting room to graph
current_room = player.current_room
rooms_graph.add_room(current_room.id)

# add the starting rooms exits
exits = player.current_room.get_exits()
for direction in exits:
    rooms_graph.add_exit(current_room.id, direction)

random_direction = rooms_graph.get_random_direction(current_room.id)


while random_direction is not None:
    prev_room = current_room
    # add the direction we are travelling into our traversal path
    traversal_path.append(random_direction)
    # travel in the random direction
    player.travel(random_direction)
    # re-assign the current room to the room we travelled to
    current_room = player.current_room
    # fill in previous room with the updated direction since i now have that
    # rooms info
    rooms_graph.rooms[prev_room.id][random_direction] = current_room.id


    # add the new room to the graph
    rooms_graph.add_room(current_room.id)

    # get all of the current rooms exits and fill in the graph
    exits = player.current_room.get_exits()
    for direction in exits:
        rooms_graph.add_exit(current_room.id, direction)

    # i also need to update the current room with the prev room information
    # get the opposite direction to fill in the prev room information for the current room
    opposite_direction = rooms_graph.get_opposite_direction(random_direction)
    rooms_graph.rooms[current_room.id][opposite_direction] = prev_room.id

    # update random direction to continue the loop until there are no explored rooms
    random_direction = rooms_graph.get_random_direction(current_room.id)




# --------MY STUFF ENDS HERE------------- #

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

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
