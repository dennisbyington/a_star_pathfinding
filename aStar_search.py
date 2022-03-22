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

    # FIXME: debug, moved this below for now..
    # # set possible moves (default is 4-way)
    # moves = ((-1,  0, "u"),   # up
    #          ( 1,  0, "d"),   # down
    #          ( 0, -1, "l"),   # left
    #          ( 0,  1, "r"))   # right
    # if moveFlag == 8:
    #     moves = [(-1,  0, "u"),   # up
    #              ( 1,  0, "d"),   # down
    #              ( 0, -1, "l"),   # left
    #              ( 0,  1, "r"),   # right
    #              (-1, -1, "ul"),  # up left
    #              (-1,  1, "ur"),  # up right
    #              ( 1, -1, "dl"),  # down left
    #              ( 1,  1, "dr")]  # down right

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
        # FIXME: debug -> moved this here from above...
        # set possible moves (default is 4-way)
        moves = ((-1, 0, "u"),  # up
                 (1, 0, "d"),  # down
                 (0, -1, "l"),  # left
                 (0, 1, "r"))  # right
        if moveFlag == 8:
            moves = [(-1, 0, "u"),  # up
                     (1, 0, "d"),  # down
                     (0, -1, "l"),  # left
                     (0, 1, "r"),  # right
                     (-1, -1, "ul"),  # up left
                     (-1, 1, "ur"),  # up right
                     (1, -1, "dl"),  # down left
                     (1, 1, "dr")]  # down right

        # db ----------------------------------------------------------------------
        # -----------------               debug                 ----------------
        # ----------------------------------------------------------------------
        #input("press enter to continue")
        # print current openList
        # print(f'-----------------------------------------')
        # print(f'openList: ', end="")
        # for n in openList:
        #     print(f'{n.position}', end=", ")
        # print("")
        # ----------------------------------------------------------------------

        # pop lowest f-cost off the open-list / add to closed list
        current = heapq.heappop(openList)
        closedList.append(current)
        # db ----------------------------------------------------------------------
        # -----------------               debug                 ----------------
        # print(f'\ncurrent: {current.position}')
        # ----------------------------------------------------------------------

        # FIXME: IW debugging: moved this lower for now...
        # if goal -> stop search
        if current == goal:
            return closedList, path(current)

        # list to hold nodes to check
        nodesToCheck = []

        # check possible moves for barrier & inbounds --> if not, append to nodesToCheck
        for move in moves:
           # print(f'current moves = {moves}')
            # get adjacent node to check (U, D, L, R)
            position = (current.position[0] + move[0], current.position[1] + move[1])

            # if not walkable --> ignore
            if (position[0] < 0 or      # oob high
            position[0] >= rows or      # oob low
            position[1] < 0 or          # oob l
            position[1] >= columns):    # oob r
                # db ----------------------------------------------------------------------
                # -----------------               debug                 ----------------
                # print(f'{position[0]:2} {position[1]:2} : not walkable')
                # ----------------------------------------------------------------------
                # ignore the non-walkable node
                continue

            # TODO: IW: need to check for diagonal barrier
            # if barrier --> ignore
            if (grid[position[0]][position[1]] == "x"):
                # db ----------------------------------------------------------------------
                # -----------------               debug                 ----------------
                # print(f'{position[0]:2} {position[1]:2} : barrier')
                # ----------------------------------------------------------------------
                # **********************************************************************
                # -------------             In Work                        -------------
                # **********************************************************************
                # TODO: if up, remove upleft & upright (add debug print)
                # FIXME: THIS IS THE ISSUE!!!   DON'T REMOVE FROM MOVES[]...
                # FIXME: NEED TO FIND A DIFFERENT WAY
                if move[2] == "u":
                    # print(f'barrier = u')
                    if (-1, -1, "ul") in moves:
                        moves.remove((-1, -1, "ul"))
                        # print(f'removing ul...')
                    if (-1, 1, "ur") in moves:
                        moves.remove((-1, 1, "ur"))
                        # print(f'removing ur...')

                # TODO: if down, remove downleft & downright (add debug print)
                if move[2] == "d":
                    # print(f'barrier = d')
                    if (1, -1, "dl") in moves:
                        moves.remove((1, -1, "dl"))
                        # print(f'removing dl...')
                    if (1, 1, "dr") in moves:
                        moves.remove((1, 1, "dr"))
                        # print(f'removing dr...')

                # TODO: if left, remove upleft & downleft (add debug print)
                if move[2] == "l":
                    # print(f'barrier = l')
                    if (-1, -1, "ul") in moves:
                        moves.remove((-1, -1, "ul"))
                        # print(f'removing ul...')
                    if (1, -1, "dl") in moves:
                        moves.remove((1, -1, "dl"))
                        # print(f'removing dl...')

                # TODO: if right, remove upright & downright (add debug print)
                if move[2] == "r":
                    # print(f'barrier = r')
                    if (-1, 1, "ur") in moves:
                        moves.remove((-1, 1, "ur"))
                        # print(f'removing ur...')
                    if (1, 1, "dr") in moves:
                        moves.remove((1, 1, "dr"))
                        # print(f'removing dr...')
                # **********************************************************************
                # -------------             In Work                        -------------
                # **********************************************************************


                # ignore the barrier node
                continue

            # # if here, walkable and in bounds -> create node and append to nodesToCheck
            newNode = Node(current, position)
            nodesToCheck.append(newNode)
            # db ----------------------------------------------------------------------
            # -----------------               debug                 ----------------
            # print(f'{position[0]:2} {position[1]:2} : adding to nodesToCheck')
            # ----------------------------------------------------------------------

        # db ----------------------------------------------------------------------
        # -----------------               debug                 ----------------
        # print(f'\nnodesToCheck: ', end = "")
        # for n in nodesToCheck:
        #     print(f'{n.position}', end = ", ")
        # print("")
        # ----------------------------------------------------------------------

        # look at each node for closed list (ignore), not on open list (add), better path (update)
        for node in nodesToCheck:
            # db ----------------------------------------------------------------------
            # -----------------               debug                 ----------------
            # print(f'\ncurrent: node: {node.position}')
            # ----------------------------------------------------------------------
            # if in closed list --> ignore
            if node in closedList:
                # db ----------------------------------------------------------------------
                # -----------------               debug                 ----------------
                # print(f'{node.position[0]:2} {node.position[1]:2} : in closed list')
                # ----------------------------------------------------------------------
                continue

            # populate node and check open list
            node.parent = current

            # FIXME: IW update this to account for diag moves @ 14 cost
            # ----------------------------------------------------------------------
            # -----------------               debug                 ----------------
            # print(f'node.position[0] = {node.position[0]}')
            # print(f'node.position[1] = {node.position[1]}')
            # print(f'current.position[0] = {current.position[0]}')
            # print(f'current.position[1] = {current.position[1]}')
            # ----------------------------------------------------------------------

            diaganols = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

            diag = (node.position[0] - current.position[0], node.position[1] - current.position[1])

            # print(f'diag = {diag}')

            # FIXME: this is broken.  Always diag...
            #if (diag == ((-1, -1)) or ((-1, 1)) or ((1, -1)) or ((1, 1))):
            if diag in diaganols:
                node.g = current.g + 14
                # (print(f"diag! = {diag}"))
            else: # not diag
                node.g = current.g + 10
                # (print('NOT diag g'))

            node.h = getH(node, goal, hFlag)
            node.f = node.g + node.h
            # db ----------------------------------------------------------------------
            # -----------------               debug                 ----------------
            # print(f'{node.position}: f = g + h: {node.f} = {node.g} + {node.h}')
            # ----------------------------------------------------------------------

            # if already in open list & current g is higher, ignore
            if len([n for n in openList if node.position == n.position and node.g >= n.g]) > 0:
                # db ----------------------------------------------------------------------
                # -----------------               debug                 ----------------
                # print(f'{node.position[0]:2} {node.position[1]:2} : in open list with lower g-cost')
                # ----------------------------------------------------------------------

                continue

            # if here, add to open list
            heapq.heappush(openList, node)
            # db ----------------------------------------------------------------------
            # -----------------               debug                 ----------------
            # print(f'{node.position[0]:2} {node.position[1]:2} : adding to open list')
            # ----------------------------------------------------------------------

            # if current == goal -> stop search
            # if node == goal:
            #     return closedList, path(node)


        # db ----------------------------------------------------------------------
        # -----------------               debug                 ----------------
        # print(f'\nclosedList: ', end = "")
        # for n in closedList:
        #     print(f'{n.position}', end = ", ")
        # print("")
        # ----------------------------------------------------------------------

    # if here while loop has broken -> openList is empty and goal is not found
    return closedList, -1




