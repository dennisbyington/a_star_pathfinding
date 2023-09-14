#!/usr/bin/env python3
"""
Dennis Byington
dennisbyington@mac.com
CSCE 4110.001 (Algorithms)
Term Project
A-star pathfinding
Get arguments function
"""

import argparse         # parse command line args


# --------------------------------------------------
def get_args():
    """ Parses command line arguemnts & provides help description to command line

    Returns:
        args: argparse object which holds command line arguments in parsed form
    """

    parser = argparse.ArgumentParser(
        description='A* pathfinding',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # heuristic option
    parser.add_argument('-H', '--Heuristic',
                        metavar='int',
                        type=int,
                        default=1,
                        help="Heuristic --> [1]: Manhattan, [2]: Diagonal, [3]: Dijkstra's")

    # move option
    parser.add_argument('-m', '--moves',
                        metavar='int',
                        type=int,
                        default=4,
                        help="Available moves --> [4]: Up Down Left Right, [8]: adds diagonals")

    # barriers percentage option
    parser.add_argument('-b', '--barriers',
                        metavar='float',
                        type=float,
                        default=0.5,
                        help="Percentage of board to fill with randomly placed barriers: 0.00 - 1.00")  # noqa: E501

    # random seed option
    parser.add_argument('-r', '--random_seed',
                        metavar='int',
                        type=int,
                        default=None,
                        help="Random seed value") 

    # display search step-by-step flag 
    parser.add_argument('-s', '--step',                         
                        action='store_true',  # default = false
                        help='Display search step-by-step')                

    args = parser.parse_args()

    # range check & error message (Hueristic)
    if not 1 <= args.Heuristic <= 3:
        parser.error(f'-H --Heuristic "{args.Heuristic}" must be between 1 and 3')

    # range check & error message (moves)
    if (args.moves != 4) and (args.moves != 8):
        parser.error(f'-m --moves "{args.moves}" must be 4 or 8')

    # range check & error message (barriers)
    if not 0.00 <= args.barriers <= 1.00:
        parser.error(f'-b --barriers "{args.barriers}" must be between 0.00 and 1.00')

    return args
