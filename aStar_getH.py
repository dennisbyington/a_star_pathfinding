#!/usr/bin/env python3
"""
Dennis Byington
CSCE 4110.001
Term Project
A-star pathfinding
Heuristic function
"""

# --------------------------------------------------
def getH(current, goal):
    """
    - accepts current position and goal position
    - returns the calculated heuristic
    """

    # Manhattan
    x = abs(current.position[0] - goal.position[0])
    y = abs(current.position[1] - goal.position[1])
    return 10 * (x + y)