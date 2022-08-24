#!/usr/bin/env python3
"""
Dennis Byington
dennisbyington@mac.com
CSCE 4110.001 (Algorithms)
Term Project
A-star pathfinding
Main function
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
