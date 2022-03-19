#!/usr/bin/env python3
"""
Dennis Byington
CSCE 4110.001
Term Project
A-star pathfinding
search function
"""


import heapq
import numpy as np
from Node import Node

# --------------------------------------------------
def getH(currentNode, goalNode):
    """Manhatten distance"""

    x = abs(currentNode.position[0] - goalNode.position[0])
    y = abs(currentNode.position[1] - goalNode.position[1])
    return 10 * (x + y)

# --------------------------------------------------
#FIXME: update this to my own...
def path(currentNode):
    path = []
    current = currentNode
    while current is not None:
        path.append(current.position)
        current = current.parent

    return path[::-1]


# --------------------------------------------------
def aStar_search(grid, start, stop):
    """update..."""

    # get # of rows & columns in grid
    rows, columns = np.shape(grid)

    # create start/stop nodes
    startNode = Node(None, start)
    startNode.f = startNode.g = startNode.h = 0
    stopNode = Node(None, stop)
    stopNode.f = stopNode.g = stopNode.h = 0

    # create open (heapq) and closed lists
    openList = []
    heapq.heapify(openList)
    closedList = []

    # add startNode to open list
    heapq.heappush(openList, startNode)

    # set possible moves
    # TODO: if flag set, add the four diagonal moves
    moves = ((-1, 0), (1, 0), (0, -1), (0, 1))

    # while open-list not empty
    while(openList):
        # print current openList
        print(f'-----------------------------------------')
        print(f'openList: ', end="")
        for n in openList:
            print(f'{n.position}', end=", ")
        print("")
        #input("press enter to continue")

        # pop lowest f-cost off the open-list / add to closed list
        currentNode = heapq.heappop(openList)
        closedList.append(currentNode)
        print(f'\ncurrentNode: {currentNode.position}')

        # if target -> stop search
        if currentNode == stopNode:
             print("stop found.  returning...")
             return path(currentNode)

        # list to hold nodes to check
        nodesToCheck = []

        # check possible moves for barrier & inbounds --> if not, append to nodesToCheck
        for move in moves:
            # get adjacent node to check
            position = (currentNode.position[0] + move[0], currentNode.position[1] + move[1])

            # if not walkable --> ignore
            if (position[0] < 0 or
            position[0] >= rows or
            position[1] < 0 or
            position[1] >= columns):
                print(f'{position[0]:2} {position[1]:2} : not walkable')
                continue

            # if barrier --> ignore
            if (grid[position] != 0):
                print(f'{position[0]:2} {position[1]:2} : barrier')
                continue

            # # if here, walkable and in bounds -> create node and append to nodesToCheck
            print(f'{position[0]:2} {position[1]:2} : adding to nodesToCheck')
            newNode = Node(currentNode, position)
            nodesToCheck.append(newNode)

        print(f'\nnodesToCheck: ', end = "")
        for n in nodesToCheck:
            print(f'{n.position}', end = ", ")
        print("")

        # look at each nodeToCheck for closed list (ignore), not on open list (add), better path (update)
        for nodeToCheck in nodesToCheck:
            print(f'\ncurrent: nodeToCheck: {nodeToCheck.position}')
            # if in closed list --> ignore
            if nodeToCheck in closedList:
                print(f'{nodeToCheck.position[0]:2} {nodeToCheck.position[1]:2} : in closed list')
                continue

            # populate node and check open list
            nodeToCheck.parent = currentNode
            # TODO: update this to account for diag moves @ 14 cost
            nodeToCheck.g = currentNode.g + 10
            nodeToCheck.h = getH(nodeToCheck, stopNode)
            nodeToCheck.f = nodeToCheck.g + nodeToCheck.h
            print(f'{nodeToCheck.position}: f = g + h: {nodeToCheck.f} = {nodeToCheck.g} + {nodeToCheck.h}')

            # if already in open list & current g is higher, ignore
            if len([n for n in openList if nodeToCheck.position == n.position and nodeToCheck.g >= n.g]) > 0:
                print(f'{nodeToCheck.position[0]:2} {nodeToCheck.position[1]:2} : in open list with lower g-cost')
                continue

            # if here, add to open list
            heapq.heappush(openList, nodeToCheck)
            print(f'{nodeToCheck.position[0]:2} {nodeToCheck.position[1]:2} : adding to open list')

        print(f'\nclosedList: ', end = "")
        for n in closedList:
            print(f'{n.position}', end = ", ")
        print("")

    # if here while loop has broken -> openList is empty and goal is not found
    print(f'Error.  Goal not found.  No path available.')



