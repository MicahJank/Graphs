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
map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

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


print("len of room graph: ", len(room_graph))
print("traversal path: ", traversal_path)



# --------MY STUFF ENDS HERE------------- #




# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move[0])
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
