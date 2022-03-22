#!/usr/bin/env python3
"""
Dennis Byington
CSCE 4110.001
Term Project
A-star pathfinding
Heuristic function
"""


# --------------------------------------------------
def getH(current, goal, hFlag):
    """
    - accepts current position, goal position, and heuristic option
    - returns the calculated heuristic
    """

    # used for Manhattan and Diagonal
    x = abs(current.position[0] - goal.position[0])
    y = abs(current.position[1] - goal.position[1])

    # Manhattan: best for square grids, 4 way moves
    if hFlag == 1:
        return 10 * (x + y)

    # Diagonal: best for square grid, 8 way moves
    if hFlag == 2:
        return 10 * (x + y) + (14 - 2 * 10) * min(x, y)

    # Dijkstra
    if hFlag == 3:
        return 0

    # if here, error due to invalid hFlag
    return -1