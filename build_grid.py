#!/usr/bin/env python3
"""
Dennis Byington
dennisbyington@mac.com
A-star pathfinding
Build grid function
"""

import random


def build_grid(barriers, start, stop):
    """ inserts barriers randomly into grid at given percentage
    
    Args:
        barriers: percentage of grid to place barriers
        start:    start position
        stop:     stop position
    
    Returns:
        grid:     grid with barriers
    """
    
    # default grid
    # grid = ([["•", "x", "•", "•", "•", "•", "•", "•", "•", "•"],
    #          ["•", "x", "•", "•", "•", "•", "•", "•", "•", "•"],
    #          ["•", "x", "•", "x", "•", "•", "•", "•", "•", "•"],
    #          ["•", "x", "•", "x", "•", "•", "•", "•", "•", "•"],
    #          ["•", "•", "•", "x", "•", "•", "•", "•", "•", "•"],
    #          ["•", "•", "•", "x", "•", "x", "x", "x", "•", "•"],
    #          ["•", "•", "•", "x", "•", "x", "•", "•", "•", "•"],
    #          ["•", "•", "•", "x", "•", "x", "•", "•", "•", "•"],
    #          ["•", "•", "•", "x", "•", "•", "•", "•", "•", "•"],
    #          ["•", "•", "•", "x", "•", "•", "•", "•", "•", "•"]])

    # start with barrier-less grid
    grid = ([["•", "•", "•", "•", "•", "•", "•", "•", "•", "•"],
             ["•", "•", "•", "•", "•", "•", "•", "•", "•", "•"],
             ["•", "•", "•", "•", "•", "•", "•", "•", "•", "•"],
             ["•", "•", "•", "•", "•", "•", "•", "•", "•", "•"],
             ["•", "•", "•", "•", "•", "•", "•", "•", "•", "•"],
             ["•", "•", "•", "•", "•", "•", "•", "•", "•", "•"],
             ["•", "•", "•", "•", "•", "•", "•", "•", "•", "•"],
             ["•", "•", "•", "•", "•", "•", "•", "•", "•", "•"],
             ["•", "•", "•", "•", "•", "•", "•", "•", "•", "•"],
             ["•", "•", "•", "•", "•", "•", "•", "•", "•", "•"]])

    # loop over each elelent in grid and replace (at given probability)
    for row_index, row in enumerate(grid):
        for column_index, element in enumerate(row):
            # skip start and goal 
            if (row_index, column_index) == start or (row_index, column_index) == stop:
                continue
            if random.random() < barriers:
                grid[row_index][column_index] = "x"
    
    return grid
