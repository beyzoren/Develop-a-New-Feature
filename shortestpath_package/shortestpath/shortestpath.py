import heapq  # For using a priority queue

def dijkstra(graph, start):
    """
    Calculates the shortest paths from a starting node to all other nodes using Dijkstra's algorithm.
    
    Parameters:
    - graph: Dictionary like {'A': [('B', 2), ('C', 5)], ...}
    - start: Starting node

    Returns:
    - distances: Dictionary with shortest distances to all nodes
    """
    distances = {node: float('inf') for node in graph}  # Initially set all distances to infinity
    distances[start] = 0  # Distance to the start node is 0
    queue = [(0, start)]  # Priority queue initialized with the start node

    while queue:
        current_distance, current_node = heapq.heappop(queue)  # Node with smallest distance is popped

        if current_distance > distances[current_node]:
            continue  # Skip if a shorter path was already found

        for neighbor, weight in graph[current_node]:  # Loop over neighbors
            distance = current_distance + weight  # Calculate distance through current node
            if distance < distances[neighbor]:  # If new distance is shorter
                distances[neighbor] = distance  # Update shortest distance
                heapq.heappush(queue, (distance, neighbor))  # Push neighbor to queue

    return distances  # Return final shortest distances
