import pygame
import random
import numpy as np
import os


class MazeView2D:

    def __init__(self, maze_name="Maze2D", maze_file_path=None,
                 maze_size=(30, 30), screen_size=(600, 600),
                 has_loops=False, num_portals=3):

        # PyGame configurations
        pygame.init()
        pygame.display.set_caption(maze_name)
        self.clock = pygame.time.Clock()
        self.__game_over = False

        # Load a maze
        if maze_file_path is None:
            self.__entrance = np.array((np.random.randint(maze_size[0]),
                np.random.randint(maze_size[1])))
            self.__goal = np.array((np.random.randint(maze_size[0]),
                np.random.randint(maze_size[1])))
            while MazeView2D.is_adjacent(self.__entrance, self.__goal):
                self.__goal = np.array((np.random.randint(maze_size[0]),
                np.random.randint(maze_size[1])))

            self.__maze = Maze(maze_size=maze_size, has_loops=has_loops, num_portals=num_portals,
                entrance=self.__entrance, goal=self.__goal)
        else:
            if 'milestone-maze' in maze_file_path:
                if not os.path.exists(maze_file_path):
                    dir_path = os.path.dirname(os.path.abspath(__file__))
                    rel_path = os.path.join(dir_path, "maze_samples", maze_file_path)
                    if os.path.exists(rel_path):
                        maze_file_path = rel_path
                    else:
                        raise RuntimeError("Cannot find %s." % maze_file_path)
                cells = Maze.load_maze(maze_file_path)
                maze_size = cells.shape
                self.__entrance = np.array((np.random.randint(maze_size[0]),
                    np.random.randint(maze_size[1])))
    
                self.__goal = np.array((np.random.randint(maze_size[0]),
                    np.random.randint(maze_size[1])))
    
                self.__maze = Maze(maze_cells=cells, has_loops=has_loops, num_portals=num_portals,
                    entrance=self.__entrance, goal=self.__goal)
            else:
                if not os.path.exists(maze_file_path):
                    dir_path = os.path.dirname(os.path.abspath(__file__))
                    rel_path = os.path.join(dir_path, "maze_samples", maze_file_path)
                    print(rel_path)
                    if os.path.exists(rel_path):
                        maze_file_path = rel_path
                    else:
                        raise RuntimeError("Cannot find %s." % maze_file_path)
                stack = Maze.load_maze(maze_file_path)
                cells = stack[:,:,0]
                entrancemap = stack[:,:,1]
                goalmap = stack[:,:,2]
                portalmaps = stack[:,:,3:] # we assume three portals

                portal_locations = []
                for i in range(portalmaps.shape[2]):
                    portal_locations.append(np.squeeze(np.where(portalmaps[:,:,i] == 1)).T)

                self.__entrance = np.squeeze(np.where(entrancemap == 1))
                self.__goal = np.squeeze(np.where(goalmap == 1))

                maze_size = cells.shape
                self.__maze = Maze(maze_cells=cells, has_loops=has_loops, num_portals=num_portals,
                    entrance=self.__entrance, goal=self.__goal, portal_locations=portal_locations)

        self.maze_size = self.__maze.maze_size
        # to show the right and bottom border
        self.screen = pygame.display.set_mode(screen_size)
        self.__screen_size = tuple(map(sum, zip(screen_size, (-1, -1))))




        # Create the Robot
        self.__robot = np.copy(self.entrance)

        # Create a background
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.background.fill((255, 255, 255))

        # Create a layer for the maze
        self.maze_layer = pygame.Surface(self.screen.get_size()).convert_alpha()
        self.maze_layer.fill((0, 0, 0, 0,))

        # show the maze
        self.__draw_maze()

        # show the portals
        self.__draw_portals()

        # show the robot
        self.__draw_robot()

        # show the entrance
        self.__draw_entrance()

        # show the goal
        self.__draw_goal()

        # this is where the state is initialized
        self.reset_robot()

        # to render
        # if maze_file_path:
        #     self.update()
        #     import time
        #     time.sleep(20)

    @staticmethod
    def is_adjacent(cell1, cell2):
        return np.abs(cell1[0] - cell2[0]) + np.abs(cell1[1] - cell2[1]) < 1.5

    def update(self, mode="human"):
        try:
            img_output = self.__view_update(mode)
            self.__controller_update()
        except Exception as e:
            self.__game_over = True
            self.quit_game()
            raise e
        else:
            return img_output

    def quit_game(self):
        try:
            self.__game_over = True
            pygame.display.quit()
            pygame.quit()
        except Exception:
            pass

    def move_robot(self, dir):
        if dir not in self.__maze.COMPASS.keys():
            raise ValueError("dir cannot be %s. The only valid dirs are %s."
                             % (str(dir), str(self.__maze.COMPASS.keys())))

        self.__state[self.__robot[0], self.__robot[1],0] = 0 # robotmap
        # self.__state[self.__robot[0], self.__robot[1]] = 0 # robotmap


        if self.__maze.is_open(self.__robot, dir):

            # update the drawing
            self.__draw_robot(transparency=0)

            # move the robot
            self.__robot += np.array(self.__maze.COMPASS[dir])

            # if it's in a portal afterward
            if self.maze.is_portal(self.robot):
                self.__robot = np.array(self.maze.get_portal(tuple(self.robot)).teleport(tuple(self.robot)))
            self.__draw_robot(transparency=255)

        else:
            self.walk_into_wall += 1

        # self.__state[self.__robot[0], self.__robot[1]] = 1# robotmap

        self.__state[self.__robot[0], self.__robot[1], 0] = 1 # robotmap
        # self.__state[self.__robot[0], self.__robot[1], 1] = 1 # visitedmap

    def save_img(self, file):
        return pygame.image.save(self.screen, file)

    def reset_robot(self):
        # Added for DQN
        shape = self.__maze.maze_size
        robotmap = np.zeros(shape) # gets updated every step
        visitedmap = np.zeros(shape) # gets updated on steps
        robotmap[self.entrance[0], self.entrance[1]] = 1
        visitedmap[self.entrance[0], self.entrance[1]] = 1
        mazemap = np.zeros(shape + (4,)) # only need to make once
        for x in range(shape[0]):
            for y in range(shape[1]):
                for d,v in {'N':0,'E':1,'S':2,'W':3}.items():
                    xprime = x + self.__maze.COMPASS[d][0]
                    yprime = y + self.__maze.COMPASS[d][1]
                    mazemap[x,y,v] = self.__maze.is_open((x,y), d) and self.__maze.is_within_bound(xprime, yprime)

        portalmap = np.zeros(shape + (3,))
        for i,portal in enumerate(self.maze.portals):
            for location in portal.locations:
                x,y = location
                portalmap[x,y,i] = 1

        self.__state = np.dstack((robotmap, mazemap, portalmap)) #np.dstack((robotmap, visitedmap, mazemap, portalmap))
        self.__draw_robot(transparency=0)
        self.__robot = np.copy(self.entrance)
        self.__draw_robot(transparency=255)
        self.walk_into_wall = 0

    def __controller_update(self):
        if not self.__game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__game_over = True
                    self.quit_game()

    def __view_update(self, mode="human"):
        if not self.__game_over:
            # update the robot's position
            self.__draw_entrance()
            self.__draw_goal()
            self.__draw_portals()
            self.__draw_robot()


            # update the screen
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.maze_layer,(0, 0))

            if mode == "human":
                pygame.display.flip()

            return np.flipud(np.rot90(pygame.surfarray.array3d(pygame.display.get_surface())))

    def __draw_maze(self):

        line_colour = (0, 0, 0, 255)

        # drawing the horizontal lines
        for y in range(self.maze.MAZE_H + 1):
            pygame.draw.line(self.maze_layer, line_colour, (0, y * self.CELL_H),
                             (self.SCREEN_W, y * self.CELL_H), 2)

        # drawing the vertical lines
        for x in range(self.maze.MAZE_W + 1):
            pygame.draw.line(self.maze_layer, line_colour, (x * self.CELL_W, 0),
                             (x * self.CELL_W, self.SCREEN_H), 2)

        # breaking the walls
        for x in range(len(self.maze.maze_cells)):
            for y in range (len(self.maze.maze_cells[x])):
                # check the which walls are open in each cell
                walls_status = self.maze.get_walls_status(self.maze.maze_cells[x, y])
                dirs = ""
                for dir, open in walls_status.items():
                    if open:
                        dirs += dir
                self.__cover_walls(x, y, dirs)

    def __cover_walls(self, x, y, dirs, colour=(0, 0, 255, 15)):

        dx = x * self.CELL_W
        dy = y * self.CELL_H

        if not isinstance(dirs, str):
            raise TypeError("dirs must be a str.")

        for dir in dirs:
            if dir == "S":
                line_head = (dx + 1, dy + self.CELL_H)
                line_tail = (dx + self.CELL_W - 1, dy + self.CELL_H)
            elif dir == "N":
                line_head = (dx + 1, dy)
                line_tail = (dx + self.CELL_W - 1, dy)
            elif dir == "W":
                line_head = (dx, dy + 1)
                line_tail = (dx, dy + self.CELL_H - 1)
            elif dir == "E":
                line_head = (dx + self.CELL_W, dy + 1)
                line_tail = (dx + self.CELL_W, dy + self.CELL_H - 1)
            else:
                raise ValueError("The only valid directions are (N, S, E, W).")

            pygame.draw.line(self.maze_layer, colour, line_head, line_tail, 2)

    def __draw_robot(self, colour=(0, 0, 0), transparency=255):

        x = int(self.__robot[0] * self.CELL_W + self.CELL_W * 0.5 + 0.5)
        y = int(self.__robot[1] * self.CELL_H + self.CELL_H * 0.5 + 0.5)
        r = int(min(self.CELL_W, self.CELL_H)/5 + 0.5)

        colour = (255,167,0)

        pygame.draw.circle(self.maze_layer, colour + (transparency,), (x, y), r)

    def __draw_entrance(self, colour=(0, 0, 150), transparency=245):
        colour = (128, 128, 128)
        
        self.__colour_cell(self.entrance, colour=colour, transparency=transparency)

    def __draw_goal(self, colour=(150, 0, 0), transparency=245):
        colour = (128, 128, 128)
        
        self.__colour_cell(self.goal, colour=colour, transparency=transparency)

    def __draw_portals(self, transparency=245):

        google_colors = [(52,152,219), (231,76,60), (46,204,113)]
        colour_i = 0
        for portal in self.maze.portals:
            colour = google_colors[colour_i]
            colour_i += 1
            for location in portal.locations:
                self.__colour_cell(location, colour=colour, transparency=transparency)

    def __colour_cell(self, cell, colour, transparency):

        if not (isinstance(cell, (list, tuple, np.ndarray)) and len(cell) == 2):
            raise TypeError("cell must a be a tuple, list, or numpy array of size 2")

        x = int(cell[0] * self.CELL_W + 0.5 + 1)
        y = int(cell[1] * self.CELL_H + 0.5 + 1)
        w = int(self.CELL_W + 0.5 - 1)
        h = int(self.CELL_H + 0.5 - 1)
        pygame.draw.rect(self.maze_layer, colour + (transparency,), (x, y, w, h))

    @property
    def state(self):
        return self.__state

    @property
    def maze(self):
        return self.__maze

    @property
    def robot(self):
        return self.__robot

    @property
    def entrance(self):
        return self.__entrance

    @property
    def goal(self):
        return self.__goal

    @property
    def game_over(self):
        return self.__game_over

    @property
    def SCREEN_SIZE(self):
        return tuple(self.__screen_size)

    @property
    def SCREEN_W(self):
        return int(self.SCREEN_SIZE[0])

    @property
    def SCREEN_H(self):
        return int(self.SCREEN_SIZE[1])

    @property
    def CELL_W(self):
        return float(self.SCREEN_W) / float(self.maze.MAZE_W)

    @property
    def CELL_H(self):
        return float(self.SCREEN_H) / float(self.maze.MAZE_H)


class Maze:

    COMPASS = {
        "N": (0, -1),
        "E": (1, 0),
        "S": (0, 1),
        "W": (-1, 0)
    }

    def __init__(self, maze_cells=None, maze_size=(10,10), has_loops=True, num_portals=0, entrance=(0,0), goal=(9,9), portal_locations=None):

        # maze member variables
        self.maze_cells = maze_cells
        self.has_loops = has_loops
        self.__portals_dict = dict()
        self.__portals = []
        self.num_portals = num_portals
        self.goal = goal
        self.entrance = entrance

        # Use existing one if exists
        if self.maze_cells is not None:
            if isinstance(self.maze_cells, (np.ndarray, np.generic)) and len(self.maze_cells.shape) == 2:
                self.maze_size = tuple(maze_cells.shape)
            else:
                raise ValueError("maze_cells must be a 2D NumPy array.")
            self.__set_portals(portal_locations=portal_locations)
        # Otherwise, generate a random one
        else:
            # maze's configuration parameters
            if not (isinstance(maze_size, (list, tuple)) and len(maze_size) == 2):
                raise ValueError("maze_size must be a tuple: (width, height).")
            self.maze_size = maze_size

            self._generate_maze()

    def save_maze(self, file_path):

        if not isinstance(file_path, str):
            raise TypeError("Invalid file_path. It must be a str.")

        if not os.path.exists(os.path.dirname(file_path)):
            raise ValueError("Cannot find the directory for %s." % file_path)

        else:
            entrancemap = np.zeros(self.maze_size)
            entrancemap[self.entrance[0], self.entrance[1]] = 1
            goalmap = np.zeros((self.maze_size))
            goalmap[self.goal[0], self.goal[1]] = 1
            portalmaps = np.zeros((self.maze_size[0], self.maze_size[1], self.num_portals))
            for i, portal in enumerate(self.__portals):
                for loc in portal.locations:
                    portalmaps[loc[0], loc[1], i] = 1
            to_save = np.dstack((self.maze_cells, entrancemap, goalmap, portalmaps)).astype('int64')
            np.save(file_path, to_save)

    @classmethod
    def load_maze(cls, file_path):

        if not isinstance(file_path, str):
            raise TypeError("Invalid file_path. It must be a str.")

        if not os.path.exists(file_path):
            raise ValueError("Cannot find %s." % file_path)

        else:
            return np.load(file_path, allow_pickle=False, fix_imports=True)

    def _generate_maze(self):

        # list of all cell locations
        self.maze_cells = np.zeros(self.maze_size, dtype=int)

        # Initializing constants and variables needed for maze generation
        current_cell = (random.randint(0, self.MAZE_W-1), random.randint(0, self.MAZE_H-1))
        num_cells_visited = 1
        cell_stack = [current_cell]

        # Continue until all cells are visited
        while cell_stack:

            # restart from a cell from the cell stack
            current_cell = cell_stack.pop()
            x0, y0 = current_cell

            # find neighbours of the current cells that actually exist
            neighbours = dict()
            for dir_key, dir_val in self.COMPASS.items():
                x1 = x0 + dir_val[0]
                y1 = y0 + dir_val[1]
                # if cell is within bounds
                if 0 <= x1 < self.MAZE_W and 0 <= y1 < self.MAZE_H:
                    # if all four walls still exist
                    if self.all_walls_intact(self.maze_cells[x1, y1]):
                    #if self.num_walls_broken(self.maze_cells[x1, y1]) <= 1:
                        neighbours[dir_key] = (x1, y1)

            # if there is a neighbour
            if neighbours:
                # select a random neighbour
                dir = random.choice(tuple(neighbours.keys()))
                x1, y1 = neighbours[dir]

                # knock down the wall between the current cell and the selected neighbour
                self.maze_cells[x1, y1] = self.__break_walls(self.maze_cells[x1, y1], self.__get_opposite_wall(dir))

                # push the current cell location to the stack
                cell_stack.append(current_cell)

                # make the this neighbour cell the current cell
                cell_stack.append((x1, y1))

                # increment the visited cell count
                num_cells_visited += 1

        if self.has_loops:
            self.__break_random_walls(0.2)

        if self.num_portals > 0:
            self.__set_random_portals(num_portal_sets=self.num_portals)

    def __set_portals(self, portal_locations=None):
        if not portal_locations:
            portal_locations = [[(3, 4), (5, 3)], [(8, 4), (3, 6)], [(1, 6), (9, 0)]]
        for portal_location_pair in portal_locations:
            portal = Portal(*portal_location_pair)
            self.__portals.append(portal)

            # create a dictionary of portals
            for portal_location in portal_location_pair:
                self.__portals_dict[tuple(portal_location.tolist())] = portal

    def __break_random_walls(self, percent):
        # find some random cells to break
        num_cells = int(round(self.MAZE_H*self.MAZE_W*percent))
        cell_ids = random.sample(range(self.MAZE_W*self.MAZE_H), num_cells)

        # for each of those walls
        for cell_id in cell_ids:
            x = cell_id % self.MAZE_H
            y = int(cell_id/self.MAZE_H)

            # randomize the compass order
            dirs = random.sample(list(self.COMPASS.keys()), len(self.COMPASS))
            for dir in dirs:
                # break the wall if it's not already open
                if self.is_breakable((x, y), dir):
                    self.maze_cells[x, y] = self.__break_walls(self.maze_cells[x, y], dir)
                    break

    def __set_random_portals(self, num_portal_sets):
        taken_locations = set()
        for i in range(num_portal_sets):
            portal_locations = []
            while len(portal_locations) < 2:
                x = np.random.randint(self.maze_size[0])
                y = np.random.randint(self.maze_size[1])
                is_goal = (x == self.goal[0]) and (y == self.goal[1])
                is_entrance = (x == self.entrance[0]) and (y == self.entrance[1])
                if (x,y) not in taken_locations and not is_goal and not is_entrance:
                    portal_locations.append((x,y))
                    taken_locations.add((x,y))
            # append the new portal to the maze
            portal = Portal(*portal_locations)
            self.__portals.append(portal)

            # create a dictionary of portals
            for portal_location in portal_locations:
                self.__portals_dict[portal_location] = portal

    def is_open(self, cell_id, dir):
        # check if it would be out-of-bound
        x1 = cell_id[0] + self.COMPASS[dir][0]
        y1 = cell_id[1] + self.COMPASS[dir][1]

        # if cell is still within bounds after the move
        if self.is_within_bound(x1, y1):
            # check if the wall is opened
            this_wall = bool(self.get_walls_status(self.maze_cells[cell_id[0], cell_id[1]])[dir])
            other_wall = bool(self.get_walls_status(self.maze_cells[x1, y1])[self.__get_opposite_wall(dir)])
            return this_wall or other_wall
        return False

    def is_breakable(self, cell_id, dir):
        # check if it would be out-of-bound
        x1 = cell_id[0] + self.COMPASS[dir][0]
        y1 = cell_id[1] + self.COMPASS[dir][1]

        return not self.is_open(cell_id, dir) and self.is_within_bound(x1, y1)

    def is_within_bound(self, x, y):
        # true if cell is still within bounds after the move
        return 0 <= x < self.MAZE_W and 0 <= y < self.MAZE_H

    def is_portal(self, cell):
        return tuple(cell) in self.__portals_dict

    @property
    def portals(self):
        return tuple(self.__portals)

    def get_portal(self, cell):
        if cell in self.__portals_dict:
            return self.__portals_dict[cell]
        return None

    @property
    def MAZE_W(self):
        return int(self.maze_size[0])

    @property
    def MAZE_H(self):
        return int(self.maze_size[1])

    @classmethod
    def get_walls_status(cls, cell):
        walls = {
            "N" : (cell & 0x1) >> 0,
            "E" : (cell & 0x2) >> 1,
            "S" : (cell & 0x4) >> 2,
            "W" : (cell & 0x8) >> 3,
        }
        return walls

    @classmethod
    def all_walls_intact(cls, cell):
        return cell & 0xF == 0

    @classmethod
    def num_walls_broken(cls, cell):
        walls = cls.get_walls_status(cell)
        num_broken = 0
        for wall_broken in walls.values():
            num_broken += wall_broken
        return num_broken

    @classmethod
    def __break_walls(cls, cell, dirs):
        if "N" in dirs:
            cell |= 0x1
        if "E" in dirs:
            cell |= 0x2
        if "S" in dirs:
            cell |= 0x4
        if "W" in dirs:
            cell |= 0x8
        return cell

    @classmethod
    def __get_opposite_wall(cls, dirs):

        if not isinstance(dirs, str):
            raise TypeError("dirs must be a str.")

        opposite_dirs = ""

        for dir in dirs:
            if dir == "N":
                opposite_dir = "S"
            elif dir == "S":
                opposite_dir = "N"
            elif dir == "E":
                opposite_dir = "W"
            elif dir == "W":
                opposite_dir = "E"
            else:
                raise ValueError("The only valid directions are (N, S, E, W).")

            opposite_dirs += opposite_dir

        return opposite_dirs

class Portal:

    def __init__(self, *locations):

        self.__locations = []
        for location in locations:
            if isinstance(location, (tuple, list)):
                self.__locations.append(tuple(location))
            elif isinstance(location, np.ndarray):
                self.__locations.append(tuple(location.tolist()))
            else:
                raise ValueError("location must be a list or a tuple.")

    def teleport(self, cell):
        if cell in self.locations:
            return self.locations[(self.locations.index(cell) + 1) % len(self.locations)]
        return cell

    def get_index(self, cell):
        return self.locations.index(cell)

    @property
    def locations(self):
        return self.__locations


if __name__ == "__main__":

    maze = MazeView2D(screen_size= (500, 500), maze_size=(10,10))
    maze.update()
    input("Enter any key to quit.")


