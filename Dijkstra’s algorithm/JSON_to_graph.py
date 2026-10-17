# ====================
# Importing the graph class
# ====================
from Graph import Graph
import json

# =======================
# List to Graph Function
# =======================

def list_to_graph(triplets: list) -> Graph:
    """
    ========================================
    Coverts a list of triplets into a graph
    ========================================

    This function takes a list of triplets and checks if it is in the right format. Using the Graph and the Edge
    classes, the function converts the triplets into a graph and returns it.
    """

    # Creating an empty instance of the Graph class.
    graph = Graph([])

    # Looping through all the triplets.
    for lst in triplets:
        # Checking the length of a triplet.
        if len(lst) != 3:
            raise TypeError(f"Expected 3 elements, got {len(lst)}.")
        # Storing distance and each end in a variable.
        start, end, distance = lst
        # Checking the data structure type for the ends.
        if not isinstance(start, str) or not isinstance(end, str):
            raise TypeError(f"Expected a string vertices, got {type(lst)}.")
        # Checking the data structure type for distance.
        if not isinstance(distance, (int, float)):
            raise TypeError(f"Expected an integer, or float distance, got {type(lst)}.")

        # Adding the checked edge to the Graph instance.
        graph.add_edge(start, end, distance)

    # Returning the Graph instance.
    return graph



# =======================
# JSON to Graph Function
# =======================

def json_to_graph(file_path: str) -> Graph:
    """
    ==============================================================
    Coverts a list of triplets, stored in JSON file, into a graph
    ==============================================================

    This function reads a JSON file containing a list of triplets and uses the "list_to_graph" function to convert the
    triplets into the Graph class.
    """

    # Reading the JSON file data
    with open(file_path, "r") as file:
        # Storing the data
        data = json.load(file)

    # Checking if the data is stored as a list
    if not isinstance(data, list):
        raise TypeError(f"Expected a list, got {type(data)}.")

    # Returning the data as a Graph
    return list_to_graph(data)