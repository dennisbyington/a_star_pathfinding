#!/usr/bin/env python3
"""
Dennis Byington
dennisbyington@mac.com
CSCE 4110.001 (Algorithms)
Term Project
A-star pathfinding
A* search function
"""

import heapq                                # binary heap (priority queue) for open list
import numpy as np                          # used to get rows & columns from grid
from aStar_Node import Node                 # node class for grid
from aStar_getH import getH                 # heuristic function
from aStar_getPath import get_path          # return A* path
from aStar_printResults import print_grid   # print grid
import time
import os


# --------------------------------------------------

def aStar_search(grid, start_pos, stop_pos, heuristic, moves, step):
    """ Performs A* search (steps are described in comments)
    
    Args:
        grid:       grid with barriers installed
        start_pos:  starting position of the search
        stop_pos:   goal to reach 
        heuristic:  which hueristic used to calculate h-value
        moves:      number of moves_list allowed (cardinal or diagonal as well)
        step:       flag to indincate if step-by-step search should be shown

    Returns:
        grid:       grid with visited nodes marked and path shown (if found)
    """

    # get # of rows & columns in grid
    rows, columns = np.shape(grid)

    # create start/stop nodes
    start = Node(None, start_pos)
    start.f = start.g = start.h = 0
    goal = Node(None, stop_pos)
    goal.f = goal.g = goal.h = 0

    # create open list (heapq) and closed list
    openList = []
    heapq.heapify(openList)
    closedList = []

    # add start node to open list
    heapq.heappush(openList, start)

    # while open-list not empty
    while(openList):

        # set possible moves_list (default is 4-way)
        moves_list = [(-1,  0, "u"),  # up                 # noqa: E241
                      ( 1,  0, "d"),  # down               # noqa: E201, E241
                      ( 0, -1, "l"),  # left               # noqa: E201
                      ( 0,  1, "r")]  # right              # noqa: E201, E241
        if moves == 8:
            moves_list = [(-1,  0, "u"),   # up            # noqa: E241
                          ( 1,  0, "d"),   # down          # noqa: E201, E241
                          ( 0, -1, "l"),   # left          # noqa: E201
                          ( 0,  1, "r"),   # right         # noqa: E201, E241
                          (-1, -1, "ul"),  # up left
                          (-1,  1, "ur"),  # up right      # noqa: E241
                          ( 1, -1, "dl"),  # down left     # noqa: E201
                          ( 1,  1, "dr")]  # down right    # noqa: E201, E241

        # pop lowest f-cost off the open-list / add to closed list
        current = heapq.heappop(openList)
        closedList.append(current)

        # update grid with "*" as node added to closed list
        grid[current.position[0]][current.position[1]] = "*"

        # print step (if required)
        if step:
            os.system('clear')
            print('\n\n\nSearching...\n\n\n\n\n')
            print_grid(grid)
            time.sleep(0.1)

        # if goal -> stop search
        if current == goal:
            path = get_path(current)          # get path
            for index, p in enumerate(path):  # loop through path & mark grid
                grid[p[0]][p[1]] = index + 1
            return grid

        # list to hold nodes to check
        nodesToCheck = []

        # check possible moves for walkable & barrier --> if not either, append to nodesToCheck
        # TODO make this a function call? (pass in grid and move flag? -- return nodesToCheck)
        for move in moves_list:
            position = (current.position[0] + move[0], current.position[1] + move[1])

            # if not walkable --> ignore
            if (position[0] < 0 or      # oob high    # noqa: W504
            position[0] >= rows or      # oob low     # noqa: W504
            position[1] < 0 or          # oob l       # noqa: W504
            position[1] >= columns):    # oob r
                continue

            # if barrier --> ignore (also remove diagonals if 8-way moves selected)
            if (grid[position[0]][position[1]] == "x"):
                # if up, remove upleft & upright
                if move[2] == "u":
                    if (-1, -1, "ul") in moves_list:
                        moves_list.remove((-1, -1, "ul"))
                    if (-1, 1, "ur") in moves_list:
                        moves_list.remove((-1, 1, "ur"))

                # if down, remove downleft & downright
                if move[2] == "d":
                    if (1, -1, "dl") in moves_list:
                        moves_list.remove((1, -1, "dl"))
                    if (1, 1, "dr") in moves_list:
                        moves_list.remove((1, 1, "dr"))

                # if left, remove upleft & downleft
                if move[2] == "l":
                    if (-1, -1, "ul") in moves_list:
                        moves_list.remove((-1, -1, "ul"))
                        # print(f'removing ul...')
                    if (1, -1, "dl") in moves_list:
                        moves_list.remove((1, -1, "dl"))
                        # print(f'removing dl...')

                # if right, remove upright & downright
                if move[2] == "r":
                    if (-1, 1, "ur") in moves_list:
                        moves_list.remove((-1, 1, "ur"))
                    if (1, 1, "dr") in moves_list:
                        moves_list.remove((1, 1, "dr"))

                # ignore the original barrier node above
                continue

            # # if here, walkable and in bounds -> create node and append to nodesToCheck
            newNode = Node(current, position)
            nodesToCheck.append(newNode)

        # now have list of nodes to check
        # look at each node: if in closed list (ignore), if not on open list (add), if better path (update)
        # TODO double check that I am doing the 3 things above correctly (ignore if closed, add if not in open, update if in open but better path)
        for node in nodesToCheck:
            # if in closed list --> ignore
            if node in closedList:
                continue

            # populate node and check open list
            # check for diagonal & assign appropriate g-cost
            diag = (node.position[0] - current.position[0], node.position[1] - current.position[1])
            diaganols = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
            if diag in diaganols:
                node.g = current.g + 14
            else:  # not diag
                node.g = current.g + 10

            node.h = getH(node, goal, heuristic)
            node.f = node.g + node.h
            node.parent = current

            # if already in open list with lower g -> ignore
            if len([n for n in openList if node.position == n.position and node.g >= n.g]) > 0:
                continue

            # if here, add to open list
            heapq.heappush(openList, node)

    # if here, while loop has broken -> openList is empty and goal is not found
    # TODO only return grid (do not update path first)
    # TODO figure out how to mark grid when "no path found"
    return grid
