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
def printResults(grid, path, closedList):
    """
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
        print(f'Goal NOT found: No path available!\n')
        print(f'----- A* search results -----')
        print(f'-----------------------------')
        print(f'Unvisited node:  "-"')
        print(f'Visited node:    "*"')
        print(f'Barrier:         "x"\n')
        for row in grid:
            for val in row:
                print(f'{val :>4}', end="")
            print()
        print()
    # if path found, create path in grid, display success message and grid
    else:
        # loop through path & mark grid
        for index, p in enumerate(path):
            grid[p[0]][p[1]] = index + 1

        print("Goal found!\n")
        print(f'----- A* search results -----')
        print(f'-----------------------------')
        print(f'Unvisited node:  "-"')
        print(f'Visited node:    "*"')
        print(f'Barrier:         "x"')
        print(f'Path:            "1 2 3 ..."\n')
        # ---------------------------------------------------------
        # print(str(grid).replace(' [', '').replace('[', '').replace(']', '').replace('-1', ' X'))
        # ---------------------------------------------------------
        for row in grid:
            for val in row:
                print(f'{val: >4}', end="")
            print()
        print()
