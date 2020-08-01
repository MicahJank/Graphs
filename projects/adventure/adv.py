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

    # finds the exits directions for whatever room id is entered
    def get_room_exits(self, room_id):
        return list(self.rooms[room_id])

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

traversal_path.append("Room 0")

# if random direction ever returns None its because the room we are in has had all its exits explored
random_direction = rooms_graph.get_random_direction(current_room.id)

print("current room: ", player.current_room.id)
# since traversal path will contain the number of rooms i have visited - i can keep track of it
# and know i have searched all the rooms when its length has reached the number of rooms there are
while len(rooms_graph.rooms) < 9:        

    while random_direction is not None:
        # print("looped")
        # prev_room = current_room
        # add the direction we are travelling into our traversal path
        traversal_path.append(random_direction)
        # before moving the player to the new room i need to update the graph for the current room
        # i can use the current rooms built in method to find out which room is in the direction the player is travelling and update accordingly
        # print(random_direction)
        room_in_direction = player.current_room.get_room_in_direction(random_direction)
        rooms_graph.rooms[player.current_room.id][random_direction] = room_in_direction

        # add the new room in that direction to the graph
        rooms_graph.add_room(room_in_direction.id)

        # get all of the rooms exits and fill in the graph
        exits = room_in_direction.get_exits()
        for direction in exits:
            rooms_graph.add_exit(room_in_direction.id, direction)

        # after adding the next room and its exits to the graph i need to update its exit in the graph that i already know about (the current player room)
        opposite_direction = rooms_graph.get_opposite_direction(random_direction)
        rooms_graph.rooms[room_in_direction.id][opposite_direction] = player.current_room

        # re-assign the current room to the room we travelled to
        # current_room = player.current_room


        # i also need to update the current room with the prev room information
        # get the opposite direction to fill in the prev room information for the current room
        # rooms_graph.rooms[current_room.id][opposite_direction] = prev_room.id
        # travel in the random direction
        player.travel(random_direction)

        # update random direction to continue the loop until there are no explored rooms
        random_direction = rooms_graph.get_random_direction(player.current_room.id)
        print("current room: ", player.current_room.id)
    else:
        # print("currentroom id: ", current_room.id)
        # print(rooms_graph.rooms)
        # BFS if we reach the end of a DFT - need to find the shortest path to the next ? room and then begin the DFT again
        q = Queue()
        rooms_exits = rooms_graph.get_room_exits(player.current_room.id)
        for direction in rooms_exits:
            path = [rooms_graph.rooms[player.current_room.id][direction]] # should give me the room of the exit
            q.enqueue(path)

        # path = [(prev_room, opposite_direction)]
        # q.enqueue(path)
        visited = set()

        while q.size() > 0:
            current_path = q.dequeue()
            current_room = current_path[-1]
            # print(current_path)
            if current_room not in visited:
                # i can use get_random_direction to check
                # and see if the current room has an unexplored room or not
                # print("currentroom id: ", current_room.id)
                random_direction = rooms_graph.get_random_direction(current_room.id)
                # print("randomdir: ", random_direction)
                if random_direction is not None:
                    player.current_room = current_room
                    break
                
                visited.add(current_room)
                room_exit_directions = rooms_graph.get_room_exits(current_room.id)

                for direction in room_exit_directions:
                    next_room = current_room.get_room_in_direction(direction)
                    next_path = current_path.copy()
                    next_path.append(next_room)
                    q.enqueue(next_path)

print("len of room graph: ", len(room_graph))
print("traversal path: ", traversal_path)



# --------MY STUFF ENDS HERE------------- #

# MY TRAVERSAL TEST
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



# TRAVERSAL TEST
# visited_rooms = set()
# player.current_room = world.starting_room
# visited_rooms.add(player.current_room)

# for move in traversal_path:
#     player.travel(move)
#     visited_rooms.add(player.current_room)

# if len(visited_rooms) == len(room_graph):
#     print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
# else:
#     print("TESTS FAILED: INCOMPLETE TRAVERSAL")
#     print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



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
