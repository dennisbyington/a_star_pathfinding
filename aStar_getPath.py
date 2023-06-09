#!/usr/bin/env python3
"""
Dennis Byington
dennisbyington@mac.com
CSCE 4110.001 (Algorithms)
Term Project
A-star pathfinding
get A* path
"""


# --------------------------------------------------
def get_path(goal):
    """ Traces route from goal node to start by traversing parents 
    
    Args:
        goal: node which was found in aStar_search
    
    Returns:
        path from goal node to start node
    """

    path = []
    
    # traverse path from goal -> start node (via parents) and append each node to path
    current = goal
    while current is not None:
        path.append(current.position)
        current = current.parent

    # reverse path and return
    return path[ : :-1]         # noqa: E201
