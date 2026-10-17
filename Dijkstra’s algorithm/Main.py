# ====================
# Importing the graph class
# ====================
from JSON_to_graph import json_to_graph
from pathlib import Path


# =============================================
# Testing with JSON files
# =============================================

# Defining pathways

BASE_DIR = Path(__file__).parent

paths = [
    BASE_DIR / "JSON files/graph_1.jsn",
    BASE_DIR / "JSON files/graph_2.jsn",
    BASE_DIR / "JSON files/graph_3.jsn",
    BASE_DIR / "JSON files/graph_4.jsn",
    BASE_DIR / "JSON files/graph_5.jsn",
    BASE_DIR / "JSON files/created_graph.jsn"
]

# Loop for the graphs
for n, path in enumerate(paths):
    print(25 * "=")
    print(f"\nGraph {n + 1}:\n")

    try:
        # Converting to the graph class.
        graph = json_to_graph(path)

        # Storing vertices
        vertices = graph.list_vertices()
        print(f"Vertices: {vertices}\n")

        # Storing the path and distance using dijkstra's algorithm.
        result_path, distance = graph.dijkstra_algorithm("A", "Z")

        if result_path is None:
            print(f'No path found from "A" to "Z".')

        else:
            print(f"Shortest path: {result_path}\n")
            print(f"Total distance: {distance}\n")

    # Printing the exceptions
    except Exception as e:
        print(f"❌Error❌")
        print(e)

    print(25 * "=")




