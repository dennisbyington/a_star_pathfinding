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

CURRENT IW: updating moves to allow 8
    - update arg parse 
    - pass into search
        - if == 8 --> add diagonals into moves[]
        - print move # usage message 
        - IN SEARCH:
            - update barrier check
                - if directly l/r, this removes ul/dl (or ur/dr)
                - if directly u/d, this removes ul/dr (or dl/dr)
                - if in corners, only affects itself 
            - update g-cost
                - check if diagonal and use 14
                - will also need to update getH (check all functions)

all files
    TODO: run through linter and formatter
    TODO: remove all debugging statements

aStar_main.py
    TODO: still need to update instructions, readme, and final report

aStar_args.py
    TODO: add argparse options/flags       
        # option to restrict movement to 4 or 8
        # option to adjust barrier % (this wasn't part of my proposal...)
        
aStar_search.py
    TODO: update moves to allow for diagonal moves (ties into options/flags && will require refactoring algo)
    
aStar_getH.py
    none
    
aStar_getPath.py
    none

Node.py
    none

misc
    don't forget to cite tiny python projects...

TODO: ------------------------------------------------------------
"""

from aStar_args import get_args                                 # parse command line args
import numpy as np                                              # array
from aStar_search import aStar_search as search                 # aStar search
from aStar_printResults import printResults as printResults     # aStar print
# --------------------------------------------------
def main():
    """
    - parses any command line args
    - build the grid (including barriers)
    - designate start and goal locations
    - call search function (returns A* path or error message if no path)
    - calls print function to print out grid and resulting path
    """

    # get command line arguments & save heuristic option
    args = get_args()
    hFlag = args.Heuristic

    # define the grid
    # grid = np.array([[0, -1, 0,  0, 0,  0,  0,  0, 0, 0],
    #                  [0, -1, 0,  0, 0,  0,  0,  0, 0, 0],
    #                  [0, -1, 0, -1, 0,  0,  0,  0, 0, 0],
    #                  [0, -1, 0, -1, 0,  0,  0,  0, 0, 0],
    #                  [0,  0, 0, -1, 0,  0,  0,  0, 0, 0],
    #                  [0,  0, 0, -1, 0, -1, -1, -1, 0, 0],
    #                  [0,  0, 0, -1, 0, -1,  0,  0, 0, 0],
    #                  [0,  0, 0, -1, 0, -1,  0,  0, 0, 0],
    #                  [0,  0, 0, -1, 0,  0,  0,  0, 0, 0],
    #                  [0,  0, 0, -1, 0,  0,  0,  0, 0, 0]])

    grid = ([["-", "x", "-", "-", "-", "-", "-", "-", "-", "-"],
             ["-", "x", "-", "-", "-", "-", "-", "-", "-", "-"],
             ["-", "x", "-", "x", "-", "-", "-", "-", "-", "-"],
             ["-", "x", "-", "x", "-", "-", "-", "-", "-", "-"],
             ["-", "-", "-", "x", "-", "-", "-", "-", "-", "-"],
             ["-", "-", "-", "x", "-", "x", "x", "x", "-", "-"],
             ["-", "-", "-", "x", "-", "x", "-", "-", "-", "-"],
             ["-", "-", "-", "x", "-", "x", "-", "-", "-", "-"],
             ["-", "-", "-", "x", "-", "-", "-", "-", "-", "-"],
             ["-", "-", "-", "x", "-", "-", "-", "-", "-", "-"]])

    # set start and goal
    start = (0, 0)
    goal =  (9, 9)

    # call search function (returns path or error message)
    closedList, path = search(grid, start, goal, hFlag)

    # ---------------------------------------------------------
    # for n in closedList:
    #     print(f'closedList: {n.position}')
    #     print(f'{n.position[0]}, {n.position[1]}')
    # ---------------------------------------------------------
    # print(f'aStar path = {path}')
    # ---------------------------------------------------------

    # print results of search
    printResults(grid, path, closedList)

    # # mark visited nodes
    # for index, n in enumerate(closedList):
    #     grid[n.position[0]][n.position[1]] = "*"
    #
    # # if no path found, display error message and grid
    # if path == -1:
    #     print(f'Goal NOT found: No path available!\n')
    #     print(f'----- A* search results -----')
    #     print(f'-----------------------------')
    #     print(f'Unvisited node:  "-"')
    #     print(f'Visited node:    "*"')
    #     print(f'Barrier:         "x"\n')
    #     for row in grid:
    #         for val in row:
    #             print(f'{val :>4}', end = "")
    #         print()
    #     print()
    # # if path found, create path in grid, display success message and grid
    # else:
    #     # loop through path & mark grid
    #     for index, p in enumerate(path):
    #         grid[p[0]][p[1]] = index + 1
    #
    #     print("Goal found!\n")
    #     print(f'----- A* search results -----')
    #     print(f'-----------------------------')
    #     print(f'Unvisited node:  "-"')
    #     print(f'Visited node:    "*"')
    #     print(f'Barrier:         "x"')
    #     print(f'Path:            "1 2 3 ..."\n')
    #     # ---------------------------------------------------------
    #     # print(str(grid).replace(' [', '').replace('[', '').replace(']', '').replace('-1', ' X'))
    #     # ---------------------------------------------------------
    #     for row in grid:
    #         for val in row:
    #             print(f'{val: >4}', end = "")
    #         print()
    #     print()


# --------------------------------------------------
if __name__ == '__main__':
    main()

# ---------------------------------------------------------------
