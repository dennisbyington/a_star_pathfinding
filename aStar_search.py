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
def aStar_search(grid, startPos, stopPos, hFlag, moveFlag):
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

    # print usage message
    print(f'Beginning A* search...')
    if hFlag == 1:
        print(f'Using Manhattan heuristic...')
    if hFlag == 2:
        print(f'Using Diagonal heuristic...')
    if hFlag == 3:
        print(f'Using Dijkstra heuristic...')
    if moveFlag == 4:
        print(f'Using 4-way moves...')
    if moveFlag == 8:
        print(f'Using 8-way moves...')

    # while open-list not empty
    while(openList):

        # set possible moves (default is 4-way)
        moves = ((-1,  0, "u"),  # up
                 ( 1,  0, "d"),  # down
                 ( 0, -1, "l"),  # left
                 ( 0,  1, "r"))  # right
        if moveFlag == 8:
            moves = [(-1,  0, "u"),   # up
                     ( 1,  0, "d"),   # down
                     ( 0, -1, "l"),   # left
                     ( 0,  1, "r"),   # right
                     (-1, -1, "ul"),  # up left
                     (-1,  1, "ur"),  # up right
                     ( 1, -1, "dl"),  # down left
                     ( 1,  1, "dr")]  # down right

        diaganols = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

        # pop lowest f-cost off the open-list / add to closed list
        current = heapq.heappop(openList)
        closedList.append(current)

        # if goal -> stop search
        if current == goal:
            return closedList, path(current)

        # list to hold nodes to check
        nodesToCheck = []

        # check possible moves for barrier & inbounds --> if not, append to nodesToCheck
        for move in moves:
            position = (current.position[0] + move[0], current.position[1] + move[1])

            # if not walkable --> ignore
            if (position[0] < 0 or      # oob high
            position[0] >= rows or      # oob low
            position[1] < 0 or          # oob l
            position[1] >= columns):    # oob r
                continue

            # if barrier --> ignore
            if (grid[position[0]][position[1]] == "x"):
                # if up, remove upleft & upright
                if move[2] == "u":
                    if (-1, -1, "ul") in moves:
                        moves.remove((-1, -1, "ul"))
                    if (-1, 1, "ur") in moves:
                        moves.remove((-1, 1, "ur"))

                # if down, remove downleft & downright
                if move[2] == "d":
                    if (1, -1, "dl") in moves:
                        moves.remove((1, -1, "dl"))
                    if (1, 1, "dr") in moves:
                        moves.remove((1, 1, "dr"))

                # if left, remove upleft & downleft
                if move[2] == "l":
                    if (-1, -1, "ul") in moves:
                        moves.remove((-1, -1, "ul"))
                        # print(f'removing ul...')
                    if (1, -1, "dl") in moves:
                        moves.remove((1, -1, "dl"))
                        # print(f'removing dl...')

                # if right, remove upright & downright
                if move[2] == "r":
                    if (-1, 1, "ur") in moves:
                        moves.remove((-1, 1, "ur"))
                    if (1, 1, "dr") in moves:
                        moves.remove((1, 1, "dr"))

                # ignore the original barrier node above
                continue

            # # if here, walkable and in bounds -> create node and append to nodesToCheck
            newNode = Node(current, position)
            nodesToCheck.append(newNode)

        # look at each node for closed list (ignore), not on open list (add), better path (update)
        for node in nodesToCheck:
            # if in closed list --> ignore
            if node in closedList:
                continue

            # populate node and check open list
            node.parent = current

            # check for diagonal & assign appropriate g-cost
            diag = (node.position[0] - current.position[0], node.position[1] - current.position[1])
            if diag in diaganols:
                node.g = current.g + 14
            else: # not diag
                node.g = current.g + 10

            node.h = getH(node, goal, hFlag)
            node.f = node.g + node.h

            # if already in open list & current g is higher, ignore
            if len([n for n in openList if node.position == n.position and node.g >= n.g]) > 0:
                continue

            # if here, add to open list
            heapq.heappush(openList, node)

    # if here while loop has broken -> openList is empty and goal is not found
    return closedList, -1




