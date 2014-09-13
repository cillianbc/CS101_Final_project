example_input="John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."
def create_data_structure(string_input):
    network = {}
    user = {}
    connections = []
    games = []
    lines = string_input.split(".")
    for line in lines:
        words = line.split(" ")
        username = words[0]
        if username == "":
            break
        if username not in network:
            user = {}
            user["connections"] = []
            user["games"] = []
            network[username] = user
        else:
            user = network[username]
        info = " ".join(words[4:]).split(", ")
        if "is connected to" in line:
            user["connections"] = info
        if "likes to play" in line:
            user["games"] = info
    return network

def get_connections(network, user):
    if user in network:
        connections = network[user]["connections"]
        return connections
    else:
        return None
def get_games_liked(network, user):
    if user in network:
        games = network[user]["games"]
        return games
    else:
        return None 

def add_connection(network, user_A, user_B):
    if user_A in network and user_B in network:
        connectionsA = get_connections(network, user_A)
        connectionsA.append(user_B)
        network[user_A]["connections"] = connectionsA
        return network
    else:
        return False

def add_new_user(network, user, games):
    if user not in network:
        newuser = {}
        newuser["connections"] = []
        newuser["games"] = games
        network[user] = newuser
    else:
        oldgames = network[user]["games"]
        oldgames.append(games)
    return network

def get_secondary_connections(network, user):
    if user in network:
        primary_connections = get_connections(network, user)
        secondary_connections = []
        for primary_connection in primary_connections:
            next_connections = get_connections(network, primary_connection)
            for next_connection in next_connections:
                if next_connection != user and next_connection not in primary_connections:
                    if next_connection not in secondary_connections:
                        secondary_connections.append(next_connection)
        return secondary_connections
    else:
        return None

def connections_in_common(network, user_A, user_B):
    if user_A in network and user_B in network:
        count = 0
        connections_A = get_connections(network, user_A)
        connections_B = get_connections(network, user_B)
        for connection_A in connections_A:
            if connection_A in connections_B:
                count += 1
        return count
    else:
        return False

def path_to_friend(network, user_A, user_B):
    connections = get_connections(network, user_A)
    path = [user_A]
    for connection in connections:
        if user_B in connections:
            path.append(user_B)
            return path
        else:
            recursive_path = path_to_friend(network, connection, user_B)
            if recursive_path != None:
                path += recursive_path
            return path
    return None

def most_popular_user(network):
    connections_list = [] # create a list of all the names of connections in the network
    for user in network:
        connections_list += get_connections(network, user)
    total_connections = {} # create a dictionary of the number of connections going back to each user
    for user in network:
        count = 0
        for connection in connections_list:
            if connection == user:
                count += 1
        total_connections[user] = count
    greatest = 0 # finds the user with the greatest number of connections going back to them
    for user in total_connections:
        if total_connections[user] > greatest:
            greatest = total_connections[user]
            most_popular_user = user
    return most_popular_user

net = create_data_structure(example_input)

print net
print path_to_friend(net, "John", "Ollie")
print get_connections(net, "Debra")
print add_new_user(net, "Debra", []) 
print add_new_user(net, "Nick", ["Seven Schemers", "The Movie: The Game"]) # True
print get_connections(net, "Mercedes")
print get_games_liked(net, "John")
print add_connection(net, "John", "Freda")
print get_secondary_connections(net, "Mercedes")
print connections_in_common(net, "Mercedes", "John")