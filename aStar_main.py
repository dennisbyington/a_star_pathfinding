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
    TODO: remove all debugging statements
    TODO: smooth variables names and flow -> make readable and my own

aStar_main.py
    TODO: still need to update instructions, readme, and final report
    TODO: pretty print resulting maze (*and visited nodes*)
    TODO: update all block quotes below function defs

aStar_args.py
    TODO: add argparse options/flags
    TODO: eventually randomize the barriers
    
aStar_search.py
    TODO: update moves to allow for diagonal moves (ties into options/flags && will require refactoring algo)
    TODO: update block quotes below function def
    TODO: fix error message not being reached if no path available...
    
aStar_getH.py
    TODO: update heuristic function to allow to alternate h-functions (ties into options/flags)
    
aStar_getPath.py
    none

Node.py
    none

TODO: ------------------------------------------------------------
"""

from aStar_args import get_args                     # parse command line args
import numpy as np                                  # array
from aStar_search import aStar_search as search     # aStar search function

# --------------------------------------------------
def main():
    """
    - parses any command line args
    - build the grid (including barriers)
    - designate start and goal locations
    - call search function (returns A* path or error message if no path)
    - print out grid and resulting path
    """

    # get command line arguments
    args = get_args()

    # define the maze
    grid = np.array([[0, -1, 0,  0, 0,  0,  0,  0, 0, 0],
                     [0, -1, 0,  0, 0,  0,  0,  0, 0, 0],
                     [0, -1, 0, -1, 0,  0,  0,  0, 0, 0],
                     [0, -1, 0, -1, 0,  0,  0,  0, 0, 0],
                     [0,  0, 0, -1, 0,  0,  0,  0, 0, 0],
                     [0,  0, 0, -1, 0, -1, -1, -1, 0, 0],
                     [0,  0, 0, -1, 0, -1,  0,  0, 0, 0],
                     [0,  0, 0, -1, 0, -1,  0,  0, 0, 0],
                     [0,  0, 0, -1, 0,  0,  0,  0, 0, 0],
                     [0,  0, 0, -1, 0,  0,  0,  0, 0, 0]])

    # set start and goal
    start = (0, 0)
    goal = (9, 9)

    # call search function (returns path or error message)
    path = search(grid, start, goal)

    # print(f'aStar path = {path}')

    # loop through each position in path & assign that grid position a numerical path (1, 2, 3...goal)
    for i, p in enumerate(path):
        grid[p[0]][p[1]] = i + 1

    # print maze
    print(f'A* search results:')
    print(f'   X indicates a barrier / 0 indicates an open node')
    print(f'   Path begins at 1 and continues increasing until goal reached\n')
    print(str(grid).replace(' [', '').replace('[', '').replace(']', '').replace('-1', ' X'))


# --------------------------------------------------
if __name__ == '__main__':
    main()

# ---------------------------------------------------------------
