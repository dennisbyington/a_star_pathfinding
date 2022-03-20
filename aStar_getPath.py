#!/usr/bin/env python3
"""
Dennis Byington
CSCE 4110.001
Term Project
A-star pathfinding
get A* path
"""

# --------------------------------------------------
def path(goal):
    """
    - accepts goal node which was found in aStar_search
    - traces route from goal node to start by traversing parents
    - returns that path, but reversed
    """

    path = []
    
    # traverse path from goal -> start node (via parents) and append each node to path
    current = goal
    while current is not None:
        path.append(current.position)
        current = current.parent

    # reverse path and return
    return path[ : :-1]