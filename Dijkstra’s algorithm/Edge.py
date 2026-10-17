# ====================
# Importing dataclass
# ====================
from dataclasses import dataclass


# ====================
# Edge Class
# ====================
@dataclass
class Edge:
    start_vertex: str              # First argument: Start vertex - (String value)
    end_vertex: str                # Second argument: End vertex - (String value)
    distance: float = None         # Third argument: Distance between vertices - (Float, or None - undefined)

    def __post_init__(self):
        """
        ======================================
        Initializes the Edge class
        ======================================

        This function takes care of all the types of the user input. Raises an error if the user tries to set both
        of the vertices as the same value. If the user enters a negative value, it will consider it as an
        absolute value.
        """

        # Checking the vertex type
        if not isinstance(self.start_vertex, str) or not isinstance(self.end_vertex, str):
            raise TypeError("start_vertex and end_vertex must be strings.")

        # Raises an exception if the user tries to define an edge with the same start and finish vertices.
        if self.start_vertex == self.end_vertex:
            raise ValueError('An edge class cannot connect two same vertices.')

        # Raises an exception if the distance is not integer or float.
        if self.distance is not None and not isinstance(self.distance, (int, float)):
            raise TypeError("The distance must be a number.")

        # Condition if the user enters a negative value, absolute value will be taken.
        if self.distance is not None and self.distance < 0:
            self.distance = abs(self.distance)