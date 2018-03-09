##    (Graph related) A connected undirected graph G = (V, E) is given by its cost matrix, where all costs are
##    positive. Determine a simple cycle passing through all nodes (a Hamiltonian cycle) of minimal cost. The
##    output should be the minimal cost found and the actual cycle found.

import random

def total_costs(matrix):
    #sums an integer matrix
    #actually double because of symmetry in matrix, still a suitable function used for UB.
    return sum([sum(lst) for lst in matrix])

def random_cost_matrix(nodes, max_weight, chance_of_connection = 0.5):
    #Amount of nodes in qraph, maximum weight of connection and chance of any two given nodes being connected.
    cost_matrix = [[0 for col in range(nodes)] for row in range(nodes)]
    for i in range(nodes):
        for j in range(i+1, nodes):
            if random.uniform(0,1) < chance_of_connection:
                #If chance of connection succeeds create the connection
                cost = random.randint(1,max_weight)
                #Nodes reflected diagonally for symmetry
                cost_matrix[i][j] = cost
                cost_matrix[j][i] = cost
    return cost_matrix


def connection_dictionary(cost_row):
    #Turn a list into a dictionary, key being name of node connected to, value being weight.
    costs = {}
    for i in range(len(cost_row)):
        if cost_row[i] > 0:
            costs[i] = cost_row[i]
    return costs


class Node:
    def __init__ (self,name,connections):
        self.name = name
        self.connections = connection_dictionary(connections)

        
class Graph:
    
    def __init__(self, cost_matrix):
        self.matrix = cost_matrix
        self.nodes = [Node(cost_matrix.index(row), row) for row in cost_matrix] #Create a node for every row in the matrix
        self.shortest_hamiltonian = []
        self.shortest_hamiltonian_cost = total_costs(cost_matrix)
        
    def __str__(self):
        graph_string = '\n'
        for node in self.nodes:
            graph_string += (str(node.name) + ' : ' + str(node.connections) + '\n')
        return graph_string
    
    def print_matrix(self):
        for row in self.matrix:
            print(row)
            
    def reachable(self, node, connected):
        #Recursive function which returns largest connected graph possible from starting arguments
        for n in [self.nodes[i] for i in list(node.connections)]:
            if n not in connected:
                connected += [n]
                self.reachable(n, connected)
        return connected

    def connected(self):
        #Uses reachable and compares the size to the amount of nodes in the graph to return a boolean, True means fully connected.
        node = self.nodes[0]
        if len(self.reachable(node,[])) == len(self.nodes):
            return True
        return False

    def node_by_name(self, name):
        for n in self.nodes:
            if n.name == name:
                return n
        raise Exception('Node not found!')
    
    def find_cycle(self, vertex, path, total = 0):
        #Find a cycle recursivley keeping track of path so far and cost.
        if len(path) == len(self.nodes):
            neighbor_nodes = [self.node_by_name(node) for node in vertex.connections]
            if path[0] in neighbor_nodes:
                #If hamiltonian can be created by connecting last to first.
                final_cost = self.matrix[path[0].name][path[-1].name]
                path.append(path[0])
                #final_cost is found by checking the cost to travel between the first and last vertex.
                total += final_cost
                if total < self.shortest_hamiltonian_cost:
                    #If a new minimal cost circuit has been found then make it a graph attribute.
                    self.shortest_hamiltonian = path
                    self.shortest_hamiltonian_cost = total
                
        for v in vertex.connections:
            #Connections are stored not as nodes but as the names of there nodes
            #This is why node_by_name is neccessary
            #While it is not the most efficient, it makes the connections more human readable
            value = v
            v = self.node_by_name(v)
            if v not in path:
                total += vertex.connections.get(value)
                path.append(v)
                self.find_cycle(v, path, total) 
        

    def hamiltonian_cycles(self):
        if not self.connected():
            raise Exception('Graph is not connected so features no Hamiltonian cycles')
        cycles = []
        for node in self.nodes:
            self.find_cycle(node, [node], 0)

    def show_shortest_cycle(self):
        for i in range(len(self.shortest_hamiltonian)):
            print(self.shortest_hamiltonian[i].name,end=' ')
            if i < len(self.shortest_hamiltonian)-1:
                print('->', end=' ')
            


Hamiltonian =[
    [0,5,5,4],
    [5,0,6,5],
    [5,6,0,5],
    [4,5,5,0]]

NotConnected =[
    [0,0],
    [0,0]]

test = [
    [0,1,0,0],
    [1,0,0,0],
    [0,0,0,0],
    [0,0,0,0]]

if __name__ == '__main__':
    g = Graph(random_cost_matrix(9,9,0.5))
    #g = Graph(Hamiltonian)
    print(g)
    print(g.connected())
    g.hamiltonian_cycles()
    print('Minimal cost: ',g.shortest_hamiltonian_cost)
    g.show_shortest_cycle()

    
