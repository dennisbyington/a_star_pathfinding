#!/usr/bin/env python3
"""
Dennis Byington
dennisbyington@mac.com
CSCE 4110.001 (Algorithms)
Term Project
A-star pathfinding
Print results function
"""

import time
import os


# --------------------------------------------------

ansi_red_bg = '\033[48;5;196m'   # ansi code to print red background 
ansi_canx = '\033[0;0m'  # ansi code to stop color printing  


def print_grid(grid):
    """ Simply prints the grid (used by step & results print functions below)
    
    Args: 
        grid: grid from main
    """

    for row in grid:
        for val in row:
            if val == 'x':  # if barrier, print red background
                print("  " + ansi_red_bg + " " + ansi_canx, end="")  
            else:
                print(f'{val: >3}', end="")
        print()
    print()


def print_step(grid):
    """ Prints in-process steps of a-star search   

    Args:
        grid: grid from in-process a-star search
    """
    os.system('clear')

    print('Searching...\n')
    print('----- A* search steps -------')
    print('-----------------------------')
    print('Barrier:         ' + ansi_red_bg + " " + ansi_canx)   
    print('Unvisited node:  •')
    print('Visited node:    Ø\n\n')
    print_grid(grid)
    time.sleep(0.1)


def print_results(grid, goal):
    """ Prints results of a-star search

    Args:
        grid: resulting grid from a-star search
        goal: goal position
    """

    os.system('clear')

    # if no path found, display error message
    if grid[goal[0]][goal[1]] == "•":  
        print('Goal NOT found: No path available!\n')
        print('----- A* search results -----')
        print('-----------------------------')
        print('Barrier:         ' + ansi_red_bg + " " + ansi_canx)   
        print('Unvisited node:  •')
        print('Visited node:    Ø\n\n')
        
    # if path found, display success message
    else:
        print("Goal found!\n")
        print('----- A* search results -----')
        print('-----------------------------')
        print('Barrier:         ' + ansi_red_bg + " " + ansi_canx)   
        print('Unvisited node:  •')
        print('Visited node:    Ø')
        print('Path:            1 2 3...\n')
    
    print_grid(grid)
    
