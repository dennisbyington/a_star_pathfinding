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

aStar_main.py
    TODO: still need to update instructions, readme, and final report
    TODO: pretty print resulting maze (*and visited nodes*)

aStar_args.py
    TODO: add argparse options/flags       
        # option to restrict movement to 4 or 8
        # option to adjust barrier % (this wasn't part of my proposal...)
        
aStar_search.py
    TODO: update moves to allow for diagonal moves (ties into options/flags && will require refactoring algo)
    
aStar_getH.py
    TODO: update heuristic function to allow to alternate h-functions (ties into options/flags)
    
aStar_getPath.py
    none

Node.py
    none

misc
    don't forget to cite tiny python projects...

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
    hFlag = args.Heuristic

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
    goal =  (9, 9)

    # call search function (returns path or error message)
    path = search(grid, start, goal, hFlag)

    # ---------------------------------------------------------
    # print(f'aStar path = {path}')
    # ---------------------------------------------------------

    # if no path found, display error message
    if path == -1:
        print(f'Error.  Goal not found.  No path available.')
    # if path found, create path in grid and print
    else:
        # loop through each position in path & assign that grid position a numerical path (1, 2, 3...goal)
        for index, p in enumerate(path):
            grid[p[0]][p[1]] = index + 1

        # print maze
        print(f'A* search results:')
        print(f'   X indicates a barrier / 0 indicates an open node')
        print(f'   Path begins at 1 and continues increasing until goal reached\n')
        print(str(grid).replace(' [', '').replace('[', '').replace(']', '').replace('-1', ' X'))


# --------------------------------------------------
if __name__ == '__main__':
    main()

# ---------------------------------------------------------------
