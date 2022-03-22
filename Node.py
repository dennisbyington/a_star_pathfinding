#!/usr/bin/env python3
"""
Dennis Byington
CSCE 4110.001
Term Project
A-star pathfinding
node class
"""


# --------------------------------------------------
class Node:
    """
    Node class for A* pathfinding
    equality is checked by position
    less/greater than/equal is checked by f-value
    """

    # constructor
    def __init__(self, parent = None, position = None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0

    # equality check (operator overload)
    def __eq__(self, other):
        return self.position == other.position

    # less than check (operator overload)
    def __lt__(self, other):
        return self.f < other.f

    # less than equal check (operator overload)
    def __le__(self, other):
        return self.f <= other.f

    # greater than check (operator overload)
    def __gt__(self, other):
        return self.f > other.f

    # greater than equal check (operator overload)
    def __ge__(self, other):
        return self.f >= other.f

    # representation
    def __repr__(self):
        return f'Node({self.parent}, {self.position})'
