# Representing social network graph
class SocialNetwork:
    def __init__(self):
        self.graph = {}  # adjacency list {user: [friends]}
    
    def add_user(self, user):
        if user not in self.graph:
            self.graph[user] = []
    
    def add_association(self, user1, user2):
        # Undirected edge (mutual friendship)
        self.add_user(user1)
        self.add_user(user2)
        self.graph[user1].append(user2)
        self.graph[user2].append(user1)
    
    def show_associations(self):
        for user in self.graph:
            print(f"User {user} has {len(self.graph[user])} associations: {self.graph[user]}")

# Example usage
network = SocialNetwork()

# Adding associations
network.add_association("A", "B")
network.add_association("A", "C")
network.add_association("B", "D")

# Show associations
network.show_associations()
