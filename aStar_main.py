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

CURRENT NOTES: right now it's assigning g=14 to everything
                    trying to figure out why...

CURRENT IW: updating moves to allow 8
    - update arg parse ------------------------------------------------- DONE
    - pass into search ------------------------------------------------- DONE
        - if == 8 --> add diagonals into moves[] ----------------------- DONE
        - print move # usage message ----------------------------------- DONE
        - update barrier check ( ** do this "safely" ** ) -------------- DONE
            - if directly l/r, this removes ul/dl (or ur/dr) ----------- DONE
            - if directly u/d, this removes ul/dr (or dl/dr) ----------- DONE
            - if in corners, only affects itself ----------------------- DONe
        - update g-cost ------------------------------------------------ DONE
            - check if diagonal and use 14 ----------------------------- DONE

all files
    TODO: run through linter and formatter
    TODO: remove all debugging statements

aStar_main.py
    TODO: still need to update instructions, readme, and final report

aStar_args.py
    TODO: add argparse options/flags       
        # option to adjust barrier % (this wasn't part of my proposal...)
        
aStar_search.py
    none
    
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
    moveFlag = args.moves

    # define the grid
    # ---------------------------------------------------------
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
    # ---------------------------------------------------------
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

    # grid = ([["-", "x", "-", "-", "-"],
    #          ["-", "x", "-", "-", "-"],
    #          ["-", "-", "-", "-", "-"],
    #          ["-", "-", "-", "-", "-"],
    #          ["-", "-", "-", "-", "-"]])

    # set start and goal
    start = (0, 0)
    goal =  (9, 9)
    #goal = (4, 4)

    # call search function (returns path or error message)
    closedList, path = search(grid, start, goal, hFlag, moveFlag)

    # ---------------------------------------------------------
    # for n in closedList:
    #     print(f'closedList: {n.position}')
    #     print(f'{n.position[0]}, {n.position[1]}')
    # ---------------------------------------------------------
    # print(f'aStar path = {path}')
    # ---------------------------------------------------------

    # print results of search
    printResults(grid, path, closedList)


# --------------------------------------------------
if __name__ == '__main__':
    main()

# ---------------------------------------------------------------
