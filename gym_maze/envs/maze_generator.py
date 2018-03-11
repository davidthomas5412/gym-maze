import os
from gym_maze.envs.maze_view_2d import Maze, MazeView2D
import numpy as np

if __name__ == "__main__":

    # check if the folder "maze_samples" exists in the current working directory
    dir_name = os.path.join(os.getcwd(), "maze_samples", "small_mazes")
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    
    np.random.seed(10)
    for i in range(100):
        maze_name = "{}.npy".format(i)
        maze_path = os.path.join(dir_name, maze_name)
        
        mazeview = MazeView2D(maze_size=(5, 5), screen_size=(600, 600), has_loops=True, num_portals=3)
        mazeview.maze.save_maze(maze_path)
        print("New maze generated and saved at %s." %  maze_path)

 # note: might also need to change setup.py