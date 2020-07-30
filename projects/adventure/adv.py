from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

from util import Queue, Stack

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
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

    def get_random_direction(self, room_id):
        exits_list = list(self.rooms[room_id])

        # should give back directions to rooms that havent been explored
        choices = [direction for direction in exits_list if self.rooms[room_id][direction] == "?"]
        # choose a random direction from the list
        random_direction = random.choice(choices)

        return random_direction


# traversal_path = ['n', 'n']
# traversal_path is what the test code will use to walk through all the rooms
traversal_path = []


rooms_graph = Graph()
# add starting room to graph
current_room = player.current_room
rooms_graph.add_room(current_room.id)

# add the starting rooms exits
exits = player.current_room.get_exits()
for direction in exits:
    rooms_graph.add_exit(current_room.id, direction)

random_direction = random.choice(exits)

# room_stack = Stack()
while rooms_graph[current_room.id][random_direction] !== "?":





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
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
