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
# TODO need to check if successful search (how to check if path has been dran on grid)
#       may need to pass in stop position to check if path found
#       if stop position == '-', then no path found?

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


def printResults(grid, path, closedList):
    """ Print results of a-star search
    
    - accepts grid, path (or error), and visited nodes
    - marks visited nodes in grid
    - if successful path, also marks path
    - prints resultant grid with legend
    """

    # mark visited nodes
    for index, n in enumerate(closedList):
        grid[n.position[0]][n.position[1]] = "*"

    # if no path found, display error message and grid
    if path == -1:
        print('Goal NOT found: No path available!\n')
        print('----- A* search results -----')
        print('-----------------------------')
        print('Unvisited node:  "-"')
        print('Visited node:    "*"')
        print('Barrier:         "x"\n')
        for row in grid:
            for val in row:
                print(f'{val :>4}', end="")
            print()
        print()
    # if path found, create path in grid, display success message and grid
    else:
        # # loop through path & mark grid
        # for index, p in enumerate(path):
        #     grid[p[0]][p[1]] = index + 1

        print("Goal found!\n")
        print('----- A* search results -----')
        print('-----------------------------')
        print('Unvisited node:  "-"')
        print('Visited node:    "*"')
        print('Barrier:         "x"')
        print('Path:            "1 2 3 ..."\n')
        # ---------------------------------------------------------
        # print(str(grid).replace(' [', '').replace('[', '').replace(']', '').replace('-1', ' X'))
        # ---------------------------------------------------------
        for row in grid:
            for val in row:
                print(f'{val: >4}', end="")
            print()
        print()
