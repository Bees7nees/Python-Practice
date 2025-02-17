my_graph = {
    'A': [('B', 3), ('D', 1)],  # A is connected to B and D with weights 3 and 1 respectively
    'B': [('A', 3), ('C', 4)],  # B is connected to A and C with weights 3 and 4 respectively
    'C': [('B', 4), ('D', 7)],  # C is connected to B and D with weights 4 and 7 respectively
    'D': [('A', 1), ('C', 7)]  # D is connected to A and C with weights 1 and 7 respectively
}

def shortest_path(graph, start):
    """
    This function takes a graph and a start node as input and returns the shortest path from the start node to all other nodes in the graph.
    The graph is represented as a dictionary where each key is a node and the value is a list of tuples. 
    Each tuple contains a node and the weight of the edge between the two nodes.
    """
    unvisited = list(graph)  # Create a list of all nodes in the graph that are yet to be visited
    distances = {node: 0 if node == start else float('inf') for node in graph}  # Create a dictionary to store the shortest distance from the start node to each node in the graph. The distance to the start node is 0 and the distance to all other nodes is infinity.
    paths = {node: [] for node in graph}  # Create a dictionary to store the shortest path from the start node to each node in the graph. The path to the start node is an empty list and the path to all other nodes is an empty list.
    paths[start].append(start)  # Add the start node to the path of the start node
    
    while unvisited:  # While there are still nodes that are yet to be visited
        current = min(unvisited, key=distances.get)  # Get the node with the shortest distance
        for node, distance in graph[current]:  # For each neighbor of the current node
            if distances[current] + distance < distances[node]:  # If the distance to the neighbor is shorter than the current shortest distance
                distances[node] = distances[current] + distance  # Update the shortest distance
                paths[node] = paths[current] + [node]  # Update the shortest path
        unvisited.remove(current)  # Remove the current node from the list of unvisited nodes
    
    print(f'Unvisited: {unvisited}\nDistances: {distances}\nPaths: {paths}')
    
#shortest_path(my_graph, 'A')