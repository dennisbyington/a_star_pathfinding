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

    # set heuristic options
    parser.add_argument('-H', '--Heuristic',
                        metavar = 'int',
                        type = int,
                        default = 1,
                        help = "Heuristic: 1: Manhattan, 2: Diagonal, 3: Dijkstra's")

    # TODO:
    # movement
    # numeric flag
        # 4 = 4 way (default)
        # 8 = 8 way

    args = parser.parse_args()

    # range check & error message (Hueristic)
    if not 1 <= args.Heuristic <= 3:
        parser.error(f'-H --Heuristic "{args.Heuristic}" must be between 1 and 3')

    # TODO: add range check & error message (moves)

    # TODO: option to adjust barrier % (this wasn't part of my proposal...)



    return args