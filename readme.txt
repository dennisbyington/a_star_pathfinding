# Background

This was a term project for my Computer Science Algorithms II course at the University of North Texas, Denton.


# ---------------------------------------------------------------------------
# Description

A-Star Pathfinding (A*) implemented in python

  1) Parses command line arguments (if any)
    - default values are 4-way moves with the Manhattan heuristic

  2) Creates a grid with barriers

  3) Performs A* on default grid with assigned allowed moves and heuristic

  3) Displays result


# ---------------------------------------------------------------------------
# Dependencies

- Requires Python3+
- Install required libraries via 'pip3 install -r requirements.txt'


# ---------------------------------------------------------------------------
# Executing program

  - Invoke the A* program by calling: ./aStar_main.py
    - The default [m] value is 4
    - The default [H] value is 1 (Manhattan)
        - You may override these by providing alternate values to the -m/--moves or -H/--Heuristic options


# ---------------------------------------------------------------------------
# Help

Help can be obtained by including the [-h] option to the program:

  ./aStar_main.py -h


# ---------------------------------------------------------------------------
# Author

Dennis Byington
dennisbyington@mac.com


# ---------------------------------------------------------------------------
# Version history & release notes

0.1 - Initial release


# ---------------------------------------------------------------------------
# Bugs

- No known bugs.  However, I am seeking inputs and constructive criticism on areas I can improve.


# ---------------------------------------------------------------------------
# License

This software is licensed under the MIT license.  See license.txt for details.


# ---------------------------------------------------------------------------
# Acknowledgments

The sites below were instrumental in helping me complete this project:

https://www.javatpoint.com/ai-informed-search-algorithms
https://brilliant.org/wiki/a-star-search/
https://www.baeldung.com/cs/dijkstra-time-complexity
https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2
https://towardsdatascience.com/a-star-a-search-algorithm-eb495fb156bb
http://csis.pace.edu/~benjamin/teaching/cs627/webfiles/Astar.pdf
https://tinypythonprojects.com
https://www.redblobgames.com/pathfinding/
