from vertex import Vertex


class Graph:
    def __init__(self):
        self.graph_dict = {}

    def add_vertex(self, node):
        self.graph_dict[node.value] = node

    def add_edge(self, from_node, to_node, weight=0):
        self.graph_dict[from_node.value].add_edge(to_node.value, weight)
        self.graph_dict[to_node.value].add_edge(from_node.value, weight)

    # method for playing the game
    def explore(self):
        print("Exploring the graph....\n")
        current_room = 'entrance'
        path_total = 0
        print("\nStarting off at the {0}\n".format(current_room))
        # active loop until end room is found
        while current_room != 'treasure room':
            node = self.graph_dict[current_room]
            # prints options for players
            for connected_room, weight in node.edges.items():
                # takes first letter from room names
                key = connected_room[0]
                print("enter {0} for {1}: {2} steps".format(key, connected_room, weight))
            valid_choices = [room[0] for room in node.edges.keys()]
            valid_choices_str = ''
            # converts valid choices list into readable string
            for letter in valid_choices:
                if (len(valid_choices) - 1) == valid_choices.index(letter):
                    valid_choices_str += letter + "."
                    break
                elif (len(valid_choices) - 2) == valid_choices.index(letter):
                    valid_choices_str += letter + " or "
                else:
                    valid_choices_str += letter + ", "
            print("\nYou have accumulated: {0} steps".format(path_total))
            # listens for user input
            choice = input("\nWhich room do you move to?")
            if choice not in valid_choices:
                print("\nplease select from these letters: {0}\n".format(valid_choices_str))
            else:
                for room in node.edges.keys():
                    if room.startswith(choice):
                        # moves player to selected room
                        current_room = room
                        # updates path total
                        path_total += node.edges[room]
                print("\n*** You have chosen: {0} ***\n".format(current_room))
        print("Made it to the treasure room with {0} steps".format(path_total))

    def print_map(self):
        print("\nMAZE LAYOUT\n")
        for node_key in self.graph_dict:
            print("{0} connected to...".format(node_key))
            node = self.graph_dict[node_key]
            for adjacent_node, weight in node.edges.items():
                print("=> {0}: cost is {1}".format(adjacent_node, weight))
            print("")
        print("")


def build_graph():
    graph = Graph()

    # MAKE ROOMS INTO VERTICES BELOW...
    entrance = Vertex("entrance")
    ante_chamber = Vertex("ante-chamber")
    kings_room = Vertex("king's room")
    grand_gallery = Vertex("grand gallery")
    treasure_room = Vertex("treasure room")

    # ADD ROOMS TO GRAPH BELOW...
    graph.add_vertex(entrance)
    graph.add_vertex(ante_chamber)
    graph.add_vertex(kings_room)
    graph.add_vertex(grand_gallery)
    graph.add_vertex(treasure_room)

    # ADD EDGES BETWEEN ROOMS BELOW...
    graph.add_edge(entrance, ante_chamber, 28)
    graph.add_edge(entrance, kings_room, 12)
    graph.add_edge(kings_room, ante_chamber, 4)
    graph.add_edge(grand_gallery, ante_chamber, 8)
    graph.add_edge(kings_room, grand_gallery, 8)
    graph.add_edge(treasure_room, grand_gallery, 16)
    graph.add_edge(treasure_room, ante_chamber, 24)

    graph.print_map()
    return graph
