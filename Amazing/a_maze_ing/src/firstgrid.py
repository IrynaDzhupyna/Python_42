import random
import sys


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y  # x and y are the position of the cell in the maze
        self.visited = False
        self.walls = {
            "N": True,
            "S": True,
            "E": True,
            "W": True
        }


class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height  # width and height define the size of the grid
        self.grid = [
            [Cell(x, y) for x in range(width)]
            for y in range(height)
            ]
        
        config_data = read_config()

        entry_coordinates = config_data["ENTRY"].split(",")
        exit_coordinates = config_data["EXIT"].split(",")

        entry_x, entry_y = map(int, entry_coordinates)
        exit_x, exit_y = map(int, exit_coordinates)

        self.entry = self.grid[entry_y][entry_x]
        self.exit = self.grid[exit_y][exit_x]

    def get_neighbors(self, cell):  # get the neighbor cell of the current cell
        neighbors = []
        directions = [  # pick one of the 4 directions
            (0, -1, "N"),
            (0, 1, "S"),
            (-1, 0, "W"),
            (1, 0, "E")
        ]

        for dx, dy, direction in directions:
            nx = cell.x + dx
            ny = cell.y + dy

            if 0 <= nx < self.width and 0 <= ny < self.height:
                neighbor = self.grid[ny][nx]
                if not neighbor.visited:
                    neighbors.append((neighbor, direction))

        return neighbors

    def generate(self):
        stack = []
        current = self.grid[0][0]  # start at the (0,0) coordinate (top left corner)
        current.visited = True

        while True:
            neighbors = self.get_neighbors(current)

            if neighbors:
                next_cell, direction = random.choice(neighbors)
                stack.append(current)

                self.remove_wall(current, next_cell, direction)

                next_cell.visited = True  # set the next cell as 'visited'
                current = next_cell  # set the next cell as the current one

            elif stack:
                current = stack.pop()

            else:
                break

        self.entry.walls["N"] = False
        self.exit.walls["S"] = False

    def remove_wall(self, current, next_cell, direction):  # remove a wall from a cell
        # and the wall from the other (opposite) cell
        opposite = {"N": "S", "S": "N", "W": "E", "E": "W"}

        current.walls[direction] = False  # destroys one wall of the current cell
        next_cell.walls[opposite[direction]] = False  # destroys the opposite wall of the next cell


def display(maze):  # display 2 lines for every row of the grid : top one ( horizontal walls)
    # and middle one (vertical wall and cell)
    for row in maze.grid:
        top = ""
        middle = ""

        for cell in row:
            if cell.walls["N"]:
                top += "+---"
            elif cell == maze.entry:
                top += "+---"
            else:
                top += "+   "

            if cell.walls["W"]:
                middle += "|"
            else:
                middle += " "

            if cell == maze.entry:
                middle += " A "
            elif cell == maze.exit:
                middle += " B "
            else:
                middle += "   "
            # middle += "|   " if cell.walls["W"] else "    "

        print(top + "+")  # print the end of the top line
        print(middle + "|")  # print the end of the middle line

    print("+---" * maze.width + "+")  # print the very last row of the grid (the sourthmost walls)


def read_config():
    with open('config.txt', 'r') as f:
        content = f.read()
    
    parts = []
    parts = content.split("\n")

    config_dict = {}

    for line in parts:
        if line.strip():
            key, value = line.split("=")
            config_dict[key.strip()] = value.strip()

    # print(config_dict)
    return config_dict


def main():
    config_data = read_config()
    print(config_data)
    maze = Maze(int(config_data["WIDTH"]), int(config_data["HEIGHT"]))  # create a width x height grid with the class Maze
    maze.generate()  # generate a unique path throught all the cells with DFS
    display(maze)  # display the grid on the terminal


if __name__ == "__main__":
    main()
