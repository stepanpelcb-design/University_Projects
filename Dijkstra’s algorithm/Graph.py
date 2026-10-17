# ====================
# Importing
# ====================
from dataclasses import dataclass
from Edge import Edge


# ====================
# Graph Class
# ====================
@dataclass
class Graph:
    list_of_edges: list                     # First argument: List of edges - (List value)

    def add_edge(self, start_vertex: str, end_vertex: str, distance: float):
        """
        ======================================
        Adds new edge to the graph
        ======================================

        This function adds new edge to the graph. Raises an exception if the edge is already defined.
        """

        # Store the new edge (Class Edge checks the input).
        new_edge = Edge(start_vertex, end_vertex, distance)

        # Checks if the edge is already defined.
        for edge in self.list_of_edges:
            if {start_vertex, end_vertex} == {edge.start_vertex, edge.end_vertex}:
                raise ValueError(f"The edge {start_vertex} - {end_vertex} already exists.")

        # If not defined - append to the list.
        self.list_of_edges.append(new_edge)

    def list_vertices(self):
        """
        ======================================
        Lists all vertices of the graph
        ======================================
        """

        # Set to store the vertices (no duplicates).
        vertices = set()

        # For loop to go through the whole list of edges.
        for edge in self.list_of_edges:
            # Adding vertices to the set.
            vertices.add(edge.start_vertex)
            vertices.add(edge.end_vertex)
        # Returning the vertices
        if vertices:
            return list(vertices)
        else:
            return False

    def are_adjacent(self, first_vertex: str, second_vertex: str) -> bool:
        """
        ======================================
        Checks whether two vertices are adjacent
        ======================================

        Returns a boolean value (True, False).
        """

        # For loop to go through the list of edges
        for edge in self.list_of_edges:
            # Looking for a matching edge
            if {first_vertex, second_vertex} == {edge.start_vertex, edge.end_vertex}:
                return True
        # If match not found, return False
        return False

    def get_neighbours(self, vertex: str):
        """
        ================================================
        Returns a list of neighbours of the given vertex
        ================================================
        """
        # Set to store the neighbours (no duplicates)
        neighbours = set()

        # For loop to find the neighbours in the list of edges
        for edge in self.list_of_edges:
            # Checking the start and end vertex for matches
            if vertex == edge.start_vertex:
                neighbours.add(edge.end_vertex)
            elif vertex == edge.end_vertex:
                neighbours.add(edge.start_vertex)

        # Returning the neighbours
        if neighbours:
            return list(neighbours)
        else:
            return False


    def dijkstra_algorithm(self, start_vertex: str, end_vertex: str):
        """
        =====================
        Dijkstra's algorithm
        =====================

        This function takes two arguments (start_vertex, end_vertex) and it calculates the shortest path from
        start_vertex to end_vertex using Dijkstra's algorithm.
        """
        # Storing all the vertices in the graph.
        vertices = self.list_vertices()

        # Returning 0 if start vertex and end vertex is the same.
        if start_vertex == end_vertex:
            return [start_vertex], 0

        # Checking if our vertices are in the graph.
        if start_vertex not in vertices:
            raise ValueError(f"The start vertex {start_vertex} does not exist in the graph.")

        if end_vertex not in vertices:
            raise ValueError(f"The end vertex {end_vertex} does not exist in the graph.")

        # Creating a storage for the distances(dictionary).
        distances = {v: float('inf') for v in vertices}

        # Setting the distance of the start vertex
        distances[start_vertex] = 0

        # Creating the unvisited set of vertices.
        unvisited = set(vertices)

        # Storing the previous vertex for the path reconstruction(dictionary).
        previous = {v: None for v in vertices}

        # Loop to explore the nodes
        while unvisited:
            # Pick the node with the lowest travel cost as current.
            current = min(unvisited, key=lambda v: distances[v])

            # Break if the current node is the end vertex.
            if current == end_vertex:
                break

            # Remove current node from the unvisited set.
            unvisited.remove(current)

            # Loop through all the edges to find the neighbours.
            for edge in self.list_of_edges:
                if edge.start_vertex == current:
                    neighbour = edge.end_vertex
                elif edge.end_vertex == current:
                    neighbour = edge.start_vertex
                else:
                    continue

                # If the neighbour is in the unvisited set, store the new distance.
                if neighbour in unvisited:
                    new_distance = distances[current] + edge.distance

                    # Check if the new distance is less than the previous.
                    if new_distance < distances[neighbour]:
                        distances[neighbour] = new_distance
                        previous[neighbour] = current


        # If distance is infinite
        if distances[end_vertex] == float('inf'):
            return None, float('inf')       # No path found.

        # Variable to store the path.
        path = []

        # Set the current node to the end vertex.
        current = end_vertex

        # Loop to reconstruct the path.
        while current is not None:
            # Append the current node.
            path.insert(0, current)
            # Set the current node to the previous node.
            current = previous[current]

        # Return the path and its distance.
        return path, distances[end_vertex]
