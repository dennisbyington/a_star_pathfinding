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
from aStar_printResults import print_step   # print grid


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

    # set possible moves_list 
    if moves == 4:
        moves_list = [(-1, 0), (1, 0), (0, -1), (0, 1)]    
    else:
        moves_list = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]    
        
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

        # pop lowest f-cost off the open-list / add to closed list / mark grid with "Ø"
        current = heapq.heappop(openList)
        closedList.append(current)
        grid[current.position[0]][current.position[1]] = "Ø"

        # print step (if required)
        if step:
            print_step(grid)

        # if goal -> stop search
        if current == goal:
            path = get_path(current)  # get path
            for index, step in enumerate(path):  # loop through path & mark grid
                grid[step[0]][step[1]] = index + 1
            return grid

        # list to hold nodes to check
        nodesToCheck = []

        # check possible moves for not walkable & barrier --> if not either, append to nodesToCheck
        for move in moves_list:
            position = (current.position[0] + move[0], current.position[1] + move[1])

            # if not walkable --> ignore
            #   oob high           oob low                oob left           oob right
            if (position[0] < 0 or position[0] >= rows or position[1] < 0 or position[1] >= columns):  # noqa: E501
                continue

            # if barrier --> ignore
            if (grid[position[0]][position[1]] == "x"):
                continue

            # # if here, walkable and in bounds -> create node and append to nodesToCheck
            newNode = Node(current, position)
            nodesToCheck.append(newNode)

        # now have list of nodes to check
        # look at each node: if in closed list (ignore), if not on open list (add), if better path (update)  # noqa: E501
        for node in nodesToCheck:
            
            # if in closed list --> ignore
            if node in closedList:
                continue

            # populate node and check open list
            # check for diagonal & assign appropriate g-cost
            move_direction = (node.position[0] - current.position[0], node.position[1] - current.position[1])  # noqa: E501
            diaganols = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
            if move_direction in diaganols:
                node.g = current.g + 14
            else:  # not diag
                node.g = current.g + 10

            node.h = getH(node, goal, heuristic)
            node.f = node.g + node.h
            node.parent = current

            # if already in open list with lower g -> ignore
            #   if not ignored, will push "dupe" node with lower cost onto heap
            #   this is worth it due to saving the cost of deleting higher costs node and reshuffling the heap  # noqa: E501
            if len([n for n in openList if node.position == n.position and node.g >= n.g]) > 0:
                continue

            # if here, add to open list
            heapq.heappush(openList, node)

    # if here, while loop has broken -> openList is empty and goal is not found
    return grid
