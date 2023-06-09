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
    """ Main function for a-star search program
    
    Parses any command line args
    Designate start and goal locations
    Build the grid with random barriers
    Call search function - returns grid with visited nodes marked and path shown (if found)
    Calls print function to print out grid and resulting path
    """

    # get command line arguments & save heuristic option
    args = get_args()
    
    # set start and goal
    start = (0, 0)
    goal =  (9, 9)  # noqa: E222

    # build grid
    grid = build_grid(args.barriers, start, goal)

    # call search function (returns marked grid)
    grid = search(grid, start, goal, args.Heuristic, args.moves, args.step)

    # TODO need to convert to print_results (figure out how to print if not path found)
    # print results of search
    print_grid(grid)


# --------------------------------------------------
if __name__ == '__main__':
    main()
