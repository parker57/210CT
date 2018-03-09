import random
import copy

#Connection occurs on the Graph level and will call the Node class's method connect.


class Node:
    def __init__(self, name, connections = []):
        self.name = name
        self.connections = copy.deepcopy(connections) #deepcopy
        
    def connect(self, node):
        self.connections += [node]


class Graph:
    
    def update_adjacencies(self):
        #Updates adjacency list, should be called after all changes to the graph.
        adjacencies = {}
        for node in self.nodes:
            adjacencies[node.name] = [node.name for node in node.connections]
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

    def __sub__ (self, node):
        #Remove a node from the graph
        if type(node) is not Node:
            print('Can only remove nodes to this graph, not', type(node))
        else:
            self.nodes.remove(node)
        for n in self.nodes:
            #Remove lingering references to the removed node.
            if node in n.connections:
                n.connections.remove(node)
        self.update_adjacencies()
    
    def connect (self, node1, node2):
        #Connect two nodes that are in this graph.
        if node1 not in self.nodes or node2 not in self.nodes:
            raise Exception('Atleast one of these nodes are not in the Graph.')
        elif node2 in node1.connections:
            raise Exception('Already connected.')
        else:
            node1.connect(node2)
            node2.connect(node1)
        self.update_adjacencies()
            
    def get_new_node(self):
        #Get new num/name randomly generated that isn't in use for this graph.
        new_num = random.randint(0,999)
        if new_num in [node.name for node in self.nodes]:
            get_new_name(self)
        return Node(new_num)

    
def reachable(node, connected = []):
    #Recursive function that gives the list of all nodes reachable from the argumen node.
    for n in node.connections:
        if n not in connected:
            connected += [n]
            reachable(n, connected)
    return connected

def isConnected(graph):
    if type(graph) != Graph:
        raise TypeError('Argument',type(graph),' is not a graph.')
        return False
    nodes = graph.nodes
    #node = random.choice(nodes)
    node = nodes[0]
    if len(reachable(node,[])) == len(nodes):
        return True
    else:
        return False
    

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
    
    #Partially connect graph.
    graph.connect(a,b)
    graph.connect(c,d)
    print('Connected:',isConnected(graph))
    print(graph.adjacencies,'\n')

    #Fully connect graph.
    graph.connect(a,d)
    print('Connected:',isConnected(graph))
    print(graph.adjacencies,'\n')
    
    #Sever graph.
    graph - d
    print('Connected:',isConnected(graph))
    print(graph.adjacencies,'\n')

