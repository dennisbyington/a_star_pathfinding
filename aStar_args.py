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

    # Add options/flags:
    # option to restrict movement to 4 or 8
    # option to set heuristic: Dijkstra’s algo, Manhattan distance, or Diagonal distance
    # option to adjust barrier % (this wasn't part of my proposal...)

    return parser.parse_args()