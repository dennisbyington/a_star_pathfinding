#!/usr/bin/env python3
"""
Dennis Byington
dennisbyington@mac.com
CSCE 4110.001 (Algorithms)
Term Project
A-star pathfinding
Print results function
"""


# --------------------------------------------------

# TODO add in colors (grids: red, visited: ?, path: ?)

def print_grid(grid):
    """ Simply prints the grid 
    
    Args: 
        grid: grid from main
    """
    for row in grid:
        for val in row:
            print(f'{val: >4}', end="")
        print()
    print()


def print_results(grid, goal):
    """ Prints results of a-star search

    Args:
        grid: resulting grid from a-star search
        goal: goal position
    """

    # if no path found, display error message
    if grid[goal[0]][goal[1]] == "-":  
        print('Goal NOT found: No path available!\n')
        print('----- A* search results -----')
        print('-----------------------------')
        print('Unvisited node:  "-"')
        print('Visited node:    "*"')
        print('Barrier:         "x"\n')
        
    # if path found, display success message
    else:
        print("Goal found!\n")
        print('----- A* search results -----')
        print('-----------------------------')
        print('Unvisited node:  "-"')
        print('Visited node:    "*"')
        print('Barrier:         "x"')
        print('Path:            "1 2 3 ..."\n')
    
    # print grid
    print_grid(grid)
    
