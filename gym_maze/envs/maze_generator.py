import os
from gym_maze.envs.maze_view_2d import Maze
import numpy as np

if __name__ == "__main__":

    # check if the folder "maze_samples" exists in the current working directory
    dir_name = os.path.join(os.getcwd(), "maze_samples")
    if not os.path.exists(dir_name):
        # create it if it doesn't
        os.mkdir(dir_name)

    # increment number until it finds a name that is not being used already (max maze_999)
    maze_path = None
    maze_name = "milestone_maze.npy"
    maze_path = os.path.join(dir_name, maze_name)
    np.random.seed(10)
    maze = Maze(maze_size=(10, 10), num_portals=3)
    maze.save_maze(maze_path)
    print("New maze generated and saved at %s." %  maze_path)

