import random
import copy

#Connection occurs on the Graph level and will call the Node class's method connect.

class Node:
    def __init__(self, name, connections = []):
        self.name = name
        self.connections = copy.deepcopy(connections) #deepcopy
        
    def connect(self, node, weight):
        self.connections += [[node, weight]]


class Graph:
    
    def update_adjacencies(self):
        #Updates adjacency list, should be called after all changes to the graph.
        adjacencies = {}
        for node in self.nodes:
            adjacencies[node.name] = [n for n in node.connections]
        self.adjacencies = adjacencies
        
    def __init__(self, nodes = []):
        self.nodes = nodes
        self.adjacencies = self.update_adjacencies()
    
    def __add__ (self, node):
        #Add a node to the graph
        if type(node) is not Node:
            print('Can only add nodes to this graph, not', type(node))
        else:
            self.nodes.append(node)
        self.update_adjacencies()

    def show_adjacencies(self):
        #creates a parallel list to the adjacency list which shows connections in a way that is more easily read.
        #Instead of using a memory address, the name of the node stored at that address is shown.
        readable_adjacencies = copy.deepcopy(self.adjacencies)
        values = readable_adjacencies.values()
        for value in values:
            #Nested for loops are neccessary here because we are iterating through lists in lists that are values.
            if len(value) > 0:
                for connection in value:
                    connection[0] = connection[0].name
        for key, value in readable_adjacencies.items():
            print(key,value)
    
    def connect (self, node1, node2, weight):
        #Connect node1 to node2 (directional) and define it's weight.
        if node1 not in self.nodes or node2 not in self.nodes:
            raise Exception('Atleast one of these nodes are not in the Graph.')
        elif node2 in node1.connections:
            raise Exception('Already connected.')
        else:
            node1.connect(node2, weight)
        self.update_adjacencies()
            
    def get_new_node(self):
        #Get new num/name randomly generated that isn't in use for this graph.
        new_num = random.randint(0,999)
        if new_num in [node.name for node in self.nodes]:
            self.get_new_node()
        return Node(new_num)


paths = []

def path_length(path):
    length = 0
    if len(path) == 0:
        return length
    for segment in path:
        length += segment[-1]
    return length

def path_finder(node, path):
    global paths
    for n in node.connections:
        if len(path) == 0:
            path = [[node,0]]
        path += [n]
        path_finder(n[0], path)
        paths.append(copy.copy(path))
        del path[-1]
        
def findLongestSimplePath(graph):
    start = []# nodes already visited.
    for node in graph.nodes:
        path_finder(node, start)
    longest_simple_path = []
    for path in paths:
        if path_length(path) > path_length(longest_simple_path):
            longest_simple_path = path
    return longest_simple_path

def print_path(path):
    route = str(path[0][0].name)
    for point in range(1,len(path)):
        route += ' -> ' + str(path[point][0].name)
    print(route)
    print('Length of route:',path_length(path))

        
if __name__ == '__main__':
    #Create graph
    graph = Graph()
    
    #Make Nodes
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)

    #Add those nodes to the graph
    graph + a
    graph + b
    graph + c
    graph + d
    graph + e

    graph.connect(a,b,4)
    graph.connect(a,c,10)
    graph.connect(b,e,1)
    graph.connect(b,d,7)
    graph.connect(d,e,3)

    longest_path = findLongestSimplePath(graph)
    print_path(longest_path)
    
    


