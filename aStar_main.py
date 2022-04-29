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

--> add option to adjust barrier % (this wasn't part of my proposal...)
    1 - add arg parse -------------------------------------- DONE
        0 = default ---------------------------------------- DONE
        check 0 <= x <= 0.5  ------------------------------- DONE
    2 - create the maze in main
            if 0: use standard maze (default)
            if 0.1 - 0.5: use randomly generate barriers
                
misc:
    remove all debugging statements
    check on cse machines
    update instructions, readme, and final report (2500 words double spaced)
        don't forget to cite tiny python projects...
        cite all websites..
    
TODO: ------------------------------------------------------------
"""

from aStar_args import get_args                                 # parse command line args
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
    # barrier = args.barrier


    # TODO: if 0: use standard maze (default)
    # TODO: if 0.1 - 0.5: use randomly generate barriers

    # define the grid
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
    closedList, path = search(grid, start, goal, hFlag, moveFlag)

    # print results of search
    printResults(grid, path, closedList)


# --------------------------------------------------
if __name__ == '__main__':
    main()
