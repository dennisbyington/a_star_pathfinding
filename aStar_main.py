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
from build_grid import build_grid as build_grid                 # build grid
from aStar_printResults import print_grid as print_grid         # print grid
from aStar_printResults import printResults as printResults     # print results


# --------------------------------------------------

def main():
    """
    - parses any command line args
    - designate start and goal locations
    - build the grid with random barriers
    - call search function (returns A* path or error message if no path)
    - calls print function to print out grid and resulting path
    """

    # get command line arguments & save heuristic option
    args = get_args()
    hFlag = args.Heuristic  # TODO just add args.Hueristic to the function call below
    moveFlag = args.moves   # TODO just add args.moves to function call below

    # set start and goal
    start = (0, 0)
    goal =  (9, 9)  # noqa: E222

    # build grid
    grid = build_grid(args.barriers, start, goal)

    # TODO add display flag option to arguments
    #         only return the grid
    # call search function (returns path or error message)
    closedList, path = search(grid, start, goal, hFlag, moveFlag)

    # TODO only pass in grid & stop position
    # print results of search
    printResults(grid, path, closedList)


# --------------------------------------------------
if __name__ == '__main__':
    main()
