import random

class Graph:
    def __init__(self):
        self.rooms = {}
    
    # nodes
    def add_room(self, room_id):
        if room_id not in self.rooms:
            self.rooms[room_id] = {}
    
    # edges
    def add_exit(self, current_room, exit):
        # if self.rooms[current_room][exit] != "?"
        if exit not in self.rooms[current_room]:
            # print("adding exit: ", exit, "to room: ", current_room)
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

        # print("THE EXITS FOR THIS ROOM ARE: ", self.rooms[room_id])
        # should give back directions to rooms that havent been explored
        choices = [direction for direction in exits_list if self.rooms[room_id][direction] == "?"]
        # print("THE CURRENT PLAYER ROOM IS: ", room_id)
        # print("THE RANDOM CHOICES TO MOVE ARE: ", choices)
        # if the player tries to get a random direction in a room where there are no
        # unexplored paths - then i should return None
        if len(choices) > 0:
            # choose a random direction from the list
            random_direction = random.choice(choices)
            # print("the random direction to move in is: ", random_direction)
            # print("random direction: ", random_direction)
            return random_direction
        else:
            # print("there are no directions to move in OOOH NOOOOO!")
            return None
