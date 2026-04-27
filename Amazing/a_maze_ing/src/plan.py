# 1. how to define the structure of the maze :

# the maze is a table of cell, and every cell has 4 wall/entry :
# west, east, north, south
# so we could vizualize a cell like this :

# and define the problem and different questions :
# - size of the maze : width and height
# - should it be always solvable ?
# - do we want one unique solution ?


# 2. pick  a simple algorithm :

# the easiest one in python is : recursive backtracking (DFS)
#   1. leave from the start cell
#   2. mark it as 'visited'
#   3. pick a random 'non-visited' neighbour
#   4. break the wall between these two
#   5. keep going
#   6. go back if blocked


# 3. split the code in classes :

# recommended squeletton :

maze/
 |--main.py 
 |--maze.py 
 |--cell.py 
 |--renderer.py 

# ideas and examples for these files :

# maze.py

import random
from cell import Cell

class Maze:
   def __init__(self, width, height):
      self.width = width
      self.height = height
      self.grid = [[Cell(x,y) for x in range(width)] for y in range len(height)]

    def get_neighbors(self, cell):
      neightbors = []
      directions = [
         (0, -1, "N"),
         (0, 1, "S"),
         (-1, 0, "W"),
         (1, 0, "E")
      ]

    for dx, dy, direction in directions:
      nx = cell.x + dx
      ny = cell.y + dy

      if 0 <= nx < self.width and 0 <= ny < self.height:
         neighbor = self.grid[nx][ny]
         if not neighbor.visited:
            neighbors.append((neightbor, direction))

    return neighbors

    def generate(self):
      stack = []
      current = self.grid[0][0]
      current.visited = True

      while True:
         neighbors = self.get_neighbors(current)

        if neghbors:
            next_cell, direction = random.choice(neighbors)
            stack.append(current)

            self.remove_wall(current, next_cell, direction)

            next_cell.visited = True
            current = next_cell

        elif stack:
            current = stackk.pop

        else:
            break
      
    def remove_wall(self, current, next_cell, direction):
        opposite = {"N": "S", "S": "N", "E": "W", "W": "E"}

        current.walls[direction] = False
        next_cell.walls[opposite[direction]] = False


# renderer.py:

???

def display(maze):
    for row in maze.grid:
        top = ""
        middle = ""

        for cell in row:
            top += "+---" if cell.walls["N"] else "+   "
            middle += "|   " if cell.walls["W"] else "    "

        print(top + "+")
        print(middle + "|")

    print("+---" * maze.width + "+")


# main.py:

from maze import Maze
from renderer import display

maze = Maze(10, 10)
maze.generate()
display(maze)


# recommended order to build this code 

# 1. create a simple grid (4,4) and verify it exists
# 2. code get_neighbors() and test that the neighbor is well detected
# 3. code remove_wall()
# 4. code genreate()
# 5. code the output