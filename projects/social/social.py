import random
from util import Queue
class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}

        # this is your adjacency list representation of a graph
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship

        Therefore creates an undirected graph

        Makes TWO friendships
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set() # like an adjacency list the user at friendship[last_id] will contain a set of users that are their friends

    def fisher_yates_shuffle(self, l):
        for i in range(0, len(l)):
            random_index = random.randint(i, len(l) - 1)
            l[random_index], l[i] = l[i], l[random_index]

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        
        # Add users
        for user in range(num_users):
            self.add_user(user)
            # starts at 1, up to and including num_users

        # * Hint 1: To create N random friendships, 
        # you could create a list with all possible friendship combinations of user ids, 

        friendship_combinations = []
        # O(n^2)
        # there is no 0 user so we start the range at 1 ---- the self.last_id is dependent on how many users we added since that increments each time we did self.add_user above
        for user in range(1, self.last_id + 1):
            for friend in range(user + 1, self.last_id + 1):
                friendship_combinations.append((user, friend))
        
        # print("friendship_combinations:", friendship_combinations)

        # shuffle the list
        self.fisher_yates_shuffle(friendship_combinations)

        # then grab the first N elements from the list. 
        total_friendships = num_users * avg_friendships

        friends_to_make = friendship_combinations[:(total_friendships // 2)]

        # Create friendships
        for friendship in friends_to_make:
            self.add_friendship(friendship[0], friendship[1])

    # takes a user and should return all the friends for that user
    def get_friends(self, user):
        # i need to check that the len of the set is more than 0 because of the edge case where there is a user who has no friends
        if len(self.friendships[user]) > 0:
            return self.friendships[user]
        else:
            return None

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # if the user we are searching its connections - has no friends then we can just return and print a message
        if self.get_friends(user_id) is None:
            print("You have no friends!")
            return

        visited = {}  # Note that this is a dictionary, not a set
        # since i am trying to find a shortest path i will use a BFT
        # visited is a dict that will have the visited user as the key
        # what would the value of the visited user be? - the friends of that user?


        q = Queue()
        path = [user_id]
        q.enqueue(path)
        
        while q.size() > 0:
            current_path = q.dequeue()
            current_node = current_path[-1]

            if current_node not in visited:
                visited[current_node] = current_path

                if self.get_friends(current_node) is not None:  
                    friends = self.get_friends(current_node)

                    for friend in friends:
                        new_path = current_path.copy()
                        new_path.append(friend)
                        q.enqueue(new_path)


        return visited

if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print("friendships:", sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)