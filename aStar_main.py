#!/usr/bin/env python3
"""
Dennis Byington
CSCE 4110.001
Term Project
A-star pathfinding
main function
"""
"""
TODO: ------------------------------------------------------------

all files
    TODO: run through linter and formatter
    TODO: update all block quotes below function defs
    TODO: remove all debugging statements
    TODO: smooth variables names and flow -> make readable and my own

aStar_main.py
    TODO: still need to update instructions, readme, and final report
    TODO: eventually randomize the barriers
    TODO: move argparse into separate .py file
    TODO: add argparse options/flags
    TODO: pretty print resulting maze (and visited nodes)

astar_search.py
    TODO: update hueristic function to allow to alternate h-functions (ties into options/flags)
    TODO: update moves to allow for diagonal moves (ties into options/flags && will require refactoring algo)

Node.py
    none...

TODO: ------------------------------------------------------------
"""

import argparse
import numpy as np
from aStar_search import aStar_search as search

# --------------------------------------------------
def get_args():
    """parse command line args"""

    parser = argparse.ArgumentParser(
        description='A* pathfinding',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # Add options/flags:
    # option to resrict movement to 4 or 8
    # option to set hueristic: Dijkstra’s algo, Manhattan distance, or Diagonal distance
    # option to adjust barrier % (this wasn't part of my proposal...)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """main funct"""

    args = get_args()

    # define the maze
    grid = np.array([[0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                     [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 1, 0, 1, 1, 1, 0, 0],
                     [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                     [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                     [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]])

    # print maze to verify
    # print(str(grid).replace(' [', '').replace('[', '').replace(']', ''))

    # set start and end
    start = (0, 0)
    stop = (9, 9)

   # print(grid[start])

    path = search(grid, start, stop)
    print(f'aStar path = {path}')


# --------------------------------------------------
if __name__ == '__main__':
    main()

# ---------------------------------------------------------------
