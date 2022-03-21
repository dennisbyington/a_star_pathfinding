#!/usr/bin/env python3
"""
Dennis Byington
CSCE 4110.001
Term Project
A* pathfinding
A* search function
"""


import heapq                    # binary heap (priority queue) for open list
import numpy as np              # used to get rows & columns from grid
from Node import Node           # node class for grid
from aStar_getH import getH     # heuristic function
from aStar_getPath import path  # return A* path


# --------------------------------------------------
def aStar_search(grid, startPos, stopPos, hFlag):
    """
    - accepts grid, start position, and goal position
    - performs A* search (steps are described in comments)
    - returns path (start -> goal) if found
        - returns error message if not
    """

    # get # of rows & columns in grid
    rows, columns = np.shape(grid)

    # create start/stop nodes
    start = Node(None, startPos)
    start.f = start.g = start.h = 0
    goal = Node(None, stopPos)
    goal.f = goal.g = goal.h = 0

    # create open list (heapq) and closed list
    openList = []
    heapq.heapify(openList)
    closedList = []

    # add start node to open list
    heapq.heappush(openList, start)

    # set possible moves
    # TODO: if flag set, add the four diagonal moves
    moves = ((-1,  0),   # up
             ( 1,  0),   # down
             ( 0, -1),   # left
             ( 0,  1))   # right

    print(f'Beginning A* search...')
    if hFlag == 1:
        print(f'Using Manhattan heuristic...')
    if hFlag == 2:
        print(f'Using Diagonal heuristic...')
    if hFlag == 3:
        print(f'Using Dijkstra heuristic...')


    # while open-list not empty
    while(openList):
        # ----------------------------------------------------------------------
        # # print current openList
        # print(f'-----------------------------------------')
        # print(f'openList: ', end="")
        # for n in openList:
        #     print(f'{n.position}', end=", ")
        # print("")
        # #input("press enter to continue")
        # ----------------------------------------------------------------------

        # pop lowest f-cost off the open-list / add to closed list
        current = heapq.heappop(openList)
        closedList.append(current)

        # ----------------------------------------------------------------------
        # print(f'\ncurrent: {current.position}')
        # ----------------------------------------------------------------------

        # if goal -> stop search
        if current == goal:
            print("Goal found, returning...\n")
            return path(current)

        # list to hold nodes to check
        nodesToCheck = []

        # check possible moves for barrier & inbounds --> if not, append to nodesToCheck
        for move in moves:
            # get adjacent node to check (U, D, L, R)
            position = (current.position[0] + move[0], current.position[1] + move[1])

            # if not walkable --> ignore
            if (position[0] < 0 or      # oob high
            position[0] >= rows or      # oob low
            position[1] < 0 or          # oob l
            position[1] >= columns):    # oob r
                # ----------------------------------------------------------------------
                # print(f'{position[0]:2} {position[1]:2} : not walkable')
                # ----------------------------------------------------------------------
                continue

            # if barrier --> ignore
            if (grid[position] != 0):
                # ----------------------------------------------------------------------
                # print(f'{position[0]:2} {position[1]:2} : barrier')
                # ----------------------------------------------------------------------
                continue

            # # if here, walkable and in bounds -> create node and append to nodesToCheck
            # ----------------------------------------------------------------------
            # print(f'{position[0]:2} {position[1]:2} : adding to nodesToCheck')
            # ----------------------------------------------------------------------
            newNode = Node(current, position)
            nodesToCheck.append(newNode)

        # ----------------------------------------------------------------------
        # print(f'\nnodesToCheck: ', end = "")
        # for n in nodesToCheck:
        #     print(f'{n.position}', end = ", ")
        # print("")
        # ----------------------------------------------------------------------

        # look at each node for closed list (ignore), not on open list (add), better path (update)
        for node in nodesToCheck:
            # ----------------------------------------------------------------------
            # print(f'\ncurrent: node: {node.position}')
            # ----------------------------------------------------------------------
            # if in closed list --> ignore
            if node in closedList:
                # ----------------------------------------------------------------------
                # print(f'{node.position[0]:2} {node.position[1]:2} : in closed list')
                # ----------------------------------------------------------------------
                continue

            # populate node and check open list
            node.parent = current
            # TODO: update this to account for diag moves @ 14 cost
            node.g = current.g + 10
            node.h = getH(node, goal, hFlag)
            node.f = node.g + node.h
            # ----------------------------------------------------------------------
            # print(f'{node.position}: f = g + h: {node.f} = {node.g} + {node.h}')
            # ----------------------------------------------------------------------

            # if already in open list & current g is higher, ignore
            if len([n for n in openList if node.position == n.position and node.g >= n.g]) > 0:
                # ----------------------------------------------------------------------
                # print(f'{node.position[0]:2} {node.position[1]:2} : in open list with lower g-cost')
                # ----------------------------------------------------------------------
                continue

            # if here, add to open list
            heapq.heappush(openList, node)
            # ----------------------------------------------------------------------
            # print(f'{node.position[0]:2} {node.position[1]:2} : adding to open list')
            # ----------------------------------------------------------------------

        # ----------------------------------------------------------------------
        # print(f'\nclosedList: ', end = "")
        # for n in closedList:
        #     print(f'{n.position}', end = ", ")
        # print("")
        # ----------------------------------------------------------------------

    # if here while loop has broken -> openList is empty and goal is not found
    return -1




