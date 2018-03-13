import os
from gym_maze.envs.maze_view_2d import Maze, MazeView2D
import numpy as np

if __name__ == "__main__":

    # check if the folder "maze_samples" exists in the current working directory
    dir_name = os.path.join(os.getcwd(), "maze_samples", "very_big_mazes")
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    
    np.random.seed(10)
    for i in range(10):
        maze_name = "{}.npy".format(i)
        maze_path = os.path.join(dir_name, maze_name)
        
        mazeview = MazeView2D(maze_size=(40, 40), screen_size=(600, 600), has_loops=True, num_portals=3)
        mazeview.maze.save_maze(maze_path)
        print("New maze generated and saved at %s." %  maze_path)

    maze_path = os.path.join(dir_name, '8.npy')
        
    mazeview = MazeView2D(maze_file_path=maze_path)
    mazeview.update()
    import time
    time.sleep(20)
    print("New maze generated and saved at %s." %  maze_path)
 # note: might also need to change setup.py