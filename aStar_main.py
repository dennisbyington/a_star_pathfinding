#!/usr/bin/env python3
"""
Dennis Byington
dennisbyington@mac.com
CSCE 4110.001 (Algorithms)
Term Project
A-star pathfinding
Main function
"""

from aStar_args import get_args                   # parse command line args
from aStar_search import aStar_search as search   # aStar search
from build_grid import build_grid as build_grid   # build grid
from aStar_printResults import print_results      # print results


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

    # print usage message
    print('\nBeginning A* search...')
    if args.Heuristic == 1: 
        print('Using Manhattan heuristic...')
    if args.Heuristic == 2:
        print('Using Diagonal heuristic...')
    if args.Heuristic == 3:
        print('Using Dijkstra heuristic...')
    if args.moves == 4:
        print('Using 4-way moves...')
    if args.moves == 8:
        print('Using 8-way moves...')
    print(f'start node: {start}')
    print(f'goal node:  {goal}\n')
    
    # call search function (returns marked grid)
    grid = search(grid, start, goal, args.Heuristic, args.moves, args.step)

    # print results of search
    print_results(grid, goal)


# --------------------------------------------------
if __name__ == '__main__':
    main()
