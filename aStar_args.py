#!/usr/bin/env python3
"""
Dennis Byington
CSCE 4110.001
Term Project
A-star pathfinding
main function
"""

import argparse         # parse command line args


# --------------------------------------------------
def get_args():
    """
    - accepts nothing and returns command line arguments in parsed form
    - provides help description to command line
    """

    parser = argparse.ArgumentParser(
        description = 'A* pathfinding',
        formatter_class = argparse.ArgumentDefaultsHelpFormatter)

    # heuristic option
    parser.add_argument('-H', '--Heuristic',
                        metavar = 'int',
                        type = int,
                        default = 1,
                        help = "Heuristic --> [1]: Manhattan, [2]: Diagonal, [3]: Dijkstra's")

    # move option
    parser.add_argument('-m', '--moves',
                        metavar = 'int',
                        type = int,
                        default = 4,
                        help = "Available moves --> [4]: Up Down Left Right, [8]: adds diagonals")

    # barriers option
    # FIXME: not implemented 
    # parser.add_argument('-b', '--barrier',
    #                     metavar='float',
    #                     type=float,
    #                     default=0,
    #                     help="%% of random barriers.  Must be between (0 - 0.5).  If 0, the standard maze will be used.")

    args = parser.parse_args()

    # range check & error message (Hueristic)
    if not 1 <= args.Heuristic <= 3:
        parser.error(f'-H --Heuristic "{args.Heuristic}" must be between 1 and 3')

    # range check & error message (moves)
    if (args.moves != 4) and (args.moves != 8):
        parser.error(f'-m --moves "{args.moves}" must be 4 or 8')

    # range check & error message (barriers)
    # FIXME: not implemented
    # if not 0 <= args.barrier <= 0.5:
    #     parser.error(f'-b --barrier "{args.barrier}" must be between 0 and 0.5')

    return args