import numpy as np

import gym
from gym import error, spaces, utils
from gym.utils import seeding
from gym_maze.envs.maze_view_2d import MazeView2D


class MazeEnv(gym.Env):
    metadata = {
        "render.modes": ["human", "rgb_array"],
    }

    ACTION = ["N", "S", "E", "W"]

    def __init__(self, maze_file=None, maze_size=None, mode=None):

        self.viewer = None

        if maze_file:
            self.maze_view = MazeView2D(maze_name="OpenAI Gym - Maze (%s)" % maze_file,
                                        maze_file_path=maze_file,
                                        screen_size=(640, 640), has_loops=True, num_portals=3)
        elif maze_size:
            has_loops = True
            num_portals = 3
            self.maze_view = MazeView2D(maze_name="OpenAI Gym - Maze (%d x %d)" % maze_size,
                                        maze_size=maze_size, screen_size=(640, 640),
                                        has_loops=has_loops, num_portals=num_portals)
        else:
            raise AttributeError("One must supply either a maze_file path (str) or the maze_size (tuple of length 2)")

        self.maze_size = self.maze_view.maze_size

        # forward or backward in each dimension
        self.action_space = spaces.Discrete(2*len(self.maze_size))

        # observation is the x, y coordinate of the grid
        low = np.zeros(len(self.maze_size), dtype=int)
        high =  np.array(self.maze_size, dtype=int) - np.ones(len(self.maze_size), dtype=int)
        self.observation_space = spaces.Box(low, high)

        # initial condition
        self.state = None
        self.steps_beyond_done = None

        # Simulation related variables.
        self._seed()
        self.reset()

        # Just need to initialize the relevant attributes
        self._configure()

    def __del__(self):
        self.maze_view.quit_game()

    def _configure(self, display=None):
        self.display = display

    def _seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def _step(self, action):
        if isinstance(action, int):
            self.maze_view.move_robot(self.ACTION[action])
        else:
            self.maze_view.move_robot(action)

        if np.array_equal(self.maze_view.robot, self.maze_view.goal):
            reward = 1
            done = True
        else:
            reward = -0.1/(self.maze_size[0]*self.maze_size[1])
            done = False

        self.state = self.maze_view.state

        info = {}

        return self.state, reward, done, info

    def _reset(self):
        self.maze_view.reset_robot()
        self.state = self.maze_view.state
        self.steps_beyond_done = None
        self.done = False
        return self.state

    def is_game_over(self):
        return self.maze_view.game_over

    def _render(self, mode="human", close=False):
        if close:
            self.maze_view.quit_game()

        return self.maze_view.update(mode)

class MazeEnvSample5x5(MazeEnv):

    def __init__(self):
        super(MazeEnvSample5x5, self).__init__(maze_file="maze2d_5x5.npy")


class MazeEnvRandom5x5(MazeEnv):

    def __init__(self):
        super(MazeEnvRandom5x5, self).__init__(maze_size=(5, 5))


class MazeEnvSample10x10(MazeEnv):

    def __init__(self):
        super(MazeEnvSample10x10, self).__init__(maze_file="maze2d_10x10.npy")


class MazeEnvRandom10x10(MazeEnv):

    def __init__(self):
        super(MazeEnvRandom10x10, self).__init__(maze_size=(10, 10))


class MazeEnvSample3x3(MazeEnv):

    def __init__(self):
        super(MazeEnvSample3x3, self).__init__(maze_file="maze2d_3x3.npy")


class MazeEnvRandom3x3(MazeEnv):

    def __init__(self):
        super(MazeEnvRandom3x3, self).__init__(maze_size=(3, 3))


class MazeEnvSample100x100(MazeEnv):

    def __init__(self):
        super(MazeEnvSample100x100, self).__init__(maze_file="maze2d_100x100.npy")


class MazeEnvRandom100x100(MazeEnv):

    def __init__(self):
        super(MazeEnvRandom100x100, self).__init__(maze_size=(100, 100))


class MazeEnvRandom10x10Plus(MazeEnv):

    def __init__(self):
        super(MazeEnvRandom10x10Plus, self).__init__(maze_size=(10, 10), mode="plus")


class MazeEnvRandom20x20Plus(MazeEnv):

    def __init__(self):
        super(MazeEnvRandom20x20Plus, self).__init__(maze_size=(20, 20), mode="plus")


class MazeEnvRandom30x30Plus(MazeEnv):
    def __init__(self):
        super(MazeEnvRandom30x30Plus, self).__init__(maze_size=(30, 30), mode="plus")

class MilestoneMaze(MazeEnv):
    def __init__(self):
        super(MilestoneMaze, self).__init__(maze_file='milestone_maze.npy', mode='plus')

class SmallMaze0(MazeEnv):
    def __init__(self):
        super(SmallMaze0, self).__init__(maze_file='small_mazes/0.npy', mode='plus')
class SmallMaze1(MazeEnv):
    def __init__(self):
        super(SmallMaze1, self).__init__(maze_file='small_mazes/1.npy', mode='plus')
class SmallMaze2(MazeEnv):
    def __init__(self):
        super(SmallMaze2, self).__init__(maze_file='small_mazes/2.npy', mode='plus')
class SmallMaze3(MazeEnv):
    def __init__(self):
        super(SmallMaze3, self).__init__(maze_file='small_mazes/3.npy', mode='plus')
class SmallMaze4(MazeEnv):
    def __init__(self):
        super(SmallMaze4, self).__init__(maze_file='small_mazes/4.npy', mode='plus')
class SmallMaze5(MazeEnv):
    def __init__(self):
        super(SmallMaze5, self).__init__(maze_file='small_mazes/5.npy', mode='plus')
class SmallMaze6(MazeEnv):
    def __init__(self):
        super(SmallMaze6, self).__init__(maze_file='small_mazes/6.npy', mode='plus')
class SmallMaze7(MazeEnv):
    def __init__(self):
        super(SmallMaze7, self).__init__(maze_file='small_mazes/7.npy', mode='plus')
class SmallMaze8(MazeEnv):
    def __init__(self):
        super(SmallMaze8, self).__init__(maze_file='small_mazes/8.npy', mode='plus')
class SmallMaze9(MazeEnv):
    def __init__(self):
        super(SmallMaze9, self).__init__(maze_file='small_mazes/9.npy', mode='plus')
class SmallMaze10(MazeEnv):
    def __init__(self):
        super(SmallMaze10, self).__init__(maze_file='small_mazes/10.npy', mode='plus')
class SmallMaze11(MazeEnv):
    def __init__(self):
        super(SmallMaze11, self).__init__(maze_file='small_mazes/11.npy', mode='plus')
class SmallMaze12(MazeEnv):
    def __init__(self):
        super(SmallMaze12, self).__init__(maze_file='small_mazes/12.npy', mode='plus')
class SmallMaze13(MazeEnv):
    def __init__(self):
        super(SmallMaze13, self).__init__(maze_file='small_mazes/13.npy', mode='plus')
class SmallMaze14(MazeEnv):
    def __init__(self):
        super(SmallMaze14, self).__init__(maze_file='small_mazes/14.npy', mode='plus')
class SmallMaze15(MazeEnv):
    def __init__(self):
        super(SmallMaze15, self).__init__(maze_file='small_mazes/15.npy', mode='plus')
class SmallMaze16(MazeEnv):
    def __init__(self):
        super(SmallMaze16, self).__init__(maze_file='small_mazes/16.npy', mode='plus')
class SmallMaze17(MazeEnv):
    def __init__(self):
        super(SmallMaze17, self).__init__(maze_file='small_mazes/17.npy', mode='plus')
class SmallMaze18(MazeEnv):
    def __init__(self):
        super(SmallMaze18, self).__init__(maze_file='small_mazes/18.npy', mode='plus')
class SmallMaze19(MazeEnv):
    def __init__(self):
        super(SmallMaze19, self).__init__(maze_file='small_mazes/19.npy', mode='plus')
class SmallMaze20(MazeEnv):
    def __init__(self):
        super(SmallMaze20, self).__init__(maze_file='small_mazes/20.npy', mode='plus')
class SmallMaze21(MazeEnv):
    def __init__(self):
        super(SmallMaze21, self).__init__(maze_file='small_mazes/21.npy', mode='plus')
class SmallMaze22(MazeEnv):
    def __init__(self):
        super(SmallMaze22, self).__init__(maze_file='small_mazes/22.npy', mode='plus')
class SmallMaze23(MazeEnv):
    def __init__(self):
        super(SmallMaze23, self).__init__(maze_file='small_mazes/23.npy', mode='plus')
class SmallMaze24(MazeEnv):
    def __init__(self):
        super(SmallMaze24, self).__init__(maze_file='small_mazes/24.npy', mode='plus')
class SmallMaze25(MazeEnv):
    def __init__(self):
        super(SmallMaze25, self).__init__(maze_file='small_mazes/25.npy', mode='plus')
class SmallMaze26(MazeEnv):
    def __init__(self):
        super(SmallMaze26, self).__init__(maze_file='small_mazes/26.npy', mode='plus')
class SmallMaze27(MazeEnv):
    def __init__(self):
        super(SmallMaze27, self).__init__(maze_file='small_mazes/27.npy', mode='plus')
class SmallMaze28(MazeEnv):
    def __init__(self):
        super(SmallMaze28, self).__init__(maze_file='small_mazes/28.npy', mode='plus')
class SmallMaze29(MazeEnv):
    def __init__(self):
        super(SmallMaze29, self).__init__(maze_file='small_mazes/29.npy', mode='plus')
class SmallMaze30(MazeEnv):
    def __init__(self):
        super(SmallMaze30, self).__init__(maze_file='small_mazes/30.npy', mode='plus')
class SmallMaze31(MazeEnv):
    def __init__(self):
        super(SmallMaze31, self).__init__(maze_file='small_mazes/31.npy', mode='plus')
class SmallMaze32(MazeEnv):
    def __init__(self):
        super(SmallMaze32, self).__init__(maze_file='small_mazes/32.npy', mode='plus')
class SmallMaze33(MazeEnv):
    def __init__(self):
        super(SmallMaze33, self).__init__(maze_file='small_mazes/33.npy', mode='plus')
class SmallMaze34(MazeEnv):
    def __init__(self):
        super(SmallMaze34, self).__init__(maze_file='small_mazes/34.npy', mode='plus')
class SmallMaze35(MazeEnv):
    def __init__(self):
        super(SmallMaze35, self).__init__(maze_file='small_mazes/35.npy', mode='plus')
class SmallMaze36(MazeEnv):
    def __init__(self):
        super(SmallMaze36, self).__init__(maze_file='small_mazes/36.npy', mode='plus')
class SmallMaze37(MazeEnv):
    def __init__(self):
        super(SmallMaze37, self).__init__(maze_file='small_mazes/37.npy', mode='plus')
class SmallMaze38(MazeEnv):
    def __init__(self):
        super(SmallMaze38, self).__init__(maze_file='small_mazes/38.npy', mode='plus')
class SmallMaze39(MazeEnv):
    def __init__(self):
        super(SmallMaze39, self).__init__(maze_file='small_mazes/39.npy', mode='plus')
class SmallMaze40(MazeEnv):
    def __init__(self):
        super(SmallMaze40, self).__init__(maze_file='small_mazes/40.npy', mode='plus')
class SmallMaze41(MazeEnv):
    def __init__(self):
        super(SmallMaze41, self).__init__(maze_file='small_mazes/41.npy', mode='plus')
class SmallMaze42(MazeEnv):
    def __init__(self):
        super(SmallMaze42, self).__init__(maze_file='small_mazes/42.npy', mode='plus')
class SmallMaze43(MazeEnv):
    def __init__(self):
        super(SmallMaze43, self).__init__(maze_file='small_mazes/43.npy', mode='plus')
class SmallMaze44(MazeEnv):
    def __init__(self):
        super(SmallMaze44, self).__init__(maze_file='small_mazes/44.npy', mode='plus')
class SmallMaze45(MazeEnv):
    def __init__(self):
        super(SmallMaze45, self).__init__(maze_file='small_mazes/45.npy', mode='plus')
class SmallMaze46(MazeEnv):
    def __init__(self):
        super(SmallMaze46, self).__init__(maze_file='small_mazes/46.npy', mode='plus')
class SmallMaze47(MazeEnv):
    def __init__(self):
        super(SmallMaze47, self).__init__(maze_file='small_mazes/47.npy', mode='plus')
class SmallMaze48(MazeEnv):
    def __init__(self):
        super(SmallMaze48, self).__init__(maze_file='small_mazes/48.npy', mode='plus')
class SmallMaze49(MazeEnv):
    def __init__(self):
        super(SmallMaze49, self).__init__(maze_file='small_mazes/49.npy', mode='plus')
class SmallMaze50(MazeEnv):
    def __init__(self):
        super(SmallMaze50, self).__init__(maze_file='small_mazes/50.npy', mode='plus')
class SmallMaze51(MazeEnv):
    def __init__(self):
        super(SmallMaze51, self).__init__(maze_file='small_mazes/51.npy', mode='plus')
class SmallMaze52(MazeEnv):
    def __init__(self):
        super(SmallMaze52, self).__init__(maze_file='small_mazes/52.npy', mode='plus')
class SmallMaze53(MazeEnv):
    def __init__(self):
        super(SmallMaze53, self).__init__(maze_file='small_mazes/53.npy', mode='plus')
class SmallMaze54(MazeEnv):
    def __init__(self):
        super(SmallMaze54, self).__init__(maze_file='small_mazes/54.npy', mode='plus')
class SmallMaze55(MazeEnv):
    def __init__(self):
        super(SmallMaze55, self).__init__(maze_file='small_mazes/55.npy', mode='plus')
class SmallMaze56(MazeEnv):
    def __init__(self):
        super(SmallMaze56, self).__init__(maze_file='small_mazes/56.npy', mode='plus')
class SmallMaze57(MazeEnv):
    def __init__(self):
        super(SmallMaze57, self).__init__(maze_file='small_mazes/57.npy', mode='plus')
class SmallMaze58(MazeEnv):
    def __init__(self):
        super(SmallMaze58, self).__init__(maze_file='small_mazes/58.npy', mode='plus')
class SmallMaze59(MazeEnv):
    def __init__(self):
        super(SmallMaze59, self).__init__(maze_file='small_mazes/59.npy', mode='plus')
class SmallMaze60(MazeEnv):
    def __init__(self):
        super(SmallMaze60, self).__init__(maze_file='small_mazes/60.npy', mode='plus')
class SmallMaze61(MazeEnv):
    def __init__(self):
        super(SmallMaze61, self).__init__(maze_file='small_mazes/61.npy', mode='plus')
class SmallMaze62(MazeEnv):
    def __init__(self):
        super(SmallMaze62, self).__init__(maze_file='small_mazes/62.npy', mode='plus')
class SmallMaze63(MazeEnv):
    def __init__(self):
        super(SmallMaze63, self).__init__(maze_file='small_mazes/63.npy', mode='plus')
class SmallMaze64(MazeEnv):
    def __init__(self):
        super(SmallMaze64, self).__init__(maze_file='small_mazes/64.npy', mode='plus')
class SmallMaze65(MazeEnv):
    def __init__(self):
        super(SmallMaze65, self).__init__(maze_file='small_mazes/65.npy', mode='plus')
class SmallMaze66(MazeEnv):
    def __init__(self):
        super(SmallMaze66, self).__init__(maze_file='small_mazes/66.npy', mode='plus')
class SmallMaze67(MazeEnv):
    def __init__(self):
        super(SmallMaze67, self).__init__(maze_file='small_mazes/67.npy', mode='plus')
class SmallMaze68(MazeEnv):
    def __init__(self):
        super(SmallMaze68, self).__init__(maze_file='small_mazes/68.npy', mode='plus')
class SmallMaze69(MazeEnv):
    def __init__(self):
        super(SmallMaze69, self).__init__(maze_file='small_mazes/69.npy', mode='plus')
class SmallMaze70(MazeEnv):
    def __init__(self):
        super(SmallMaze70, self).__init__(maze_file='small_mazes/70.npy', mode='plus')
class SmallMaze71(MazeEnv):
    def __init__(self):
        super(SmallMaze71, self).__init__(maze_file='small_mazes/71.npy', mode='plus')
class SmallMaze72(MazeEnv):
    def __init__(self):
        super(SmallMaze72, self).__init__(maze_file='small_mazes/72.npy', mode='plus')
class SmallMaze73(MazeEnv):
    def __init__(self):
        super(SmallMaze73, self).__init__(maze_file='small_mazes/73.npy', mode='plus')
class SmallMaze74(MazeEnv):
    def __init__(self):
        super(SmallMaze74, self).__init__(maze_file='small_mazes/74.npy', mode='plus')
class SmallMaze75(MazeEnv):
    def __init__(self):
        super(SmallMaze75, self).__init__(maze_file='small_mazes/75.npy', mode='plus')
class SmallMaze76(MazeEnv):
    def __init__(self):
        super(SmallMaze76, self).__init__(maze_file='small_mazes/76.npy', mode='plus')
class SmallMaze77(MazeEnv):
    def __init__(self):
        super(SmallMaze77, self).__init__(maze_file='small_mazes/77.npy', mode='plus')
class SmallMaze78(MazeEnv):
    def __init__(self):
        super(SmallMaze78, self).__init__(maze_file='small_mazes/78.npy', mode='plus')
class SmallMaze79(MazeEnv):
    def __init__(self):
        super(SmallMaze79, self).__init__(maze_file='small_mazes/79.npy', mode='plus')
class SmallMaze80(MazeEnv):
    def __init__(self):
        super(SmallMaze80, self).__init__(maze_file='small_mazes/80.npy', mode='plus')
class SmallMaze81(MazeEnv):
    def __init__(self):
        super(SmallMaze81, self).__init__(maze_file='small_mazes/81.npy', mode='plus')
class SmallMaze82(MazeEnv):
    def __init__(self):
        super(SmallMaze82, self).__init__(maze_file='small_mazes/82.npy', mode='plus')
class SmallMaze83(MazeEnv):
    def __init__(self):
        super(SmallMaze83, self).__init__(maze_file='small_mazes/83.npy', mode='plus')
class SmallMaze84(MazeEnv):
    def __init__(self):
        super(SmallMaze84, self).__init__(maze_file='small_mazes/84.npy', mode='plus')
class SmallMaze85(MazeEnv):
    def __init__(self):
        super(SmallMaze85, self).__init__(maze_file='small_mazes/85.npy', mode='plus')
class SmallMaze86(MazeEnv):
    def __init__(self):
        super(SmallMaze86, self).__init__(maze_file='small_mazes/86.npy', mode='plus')
class SmallMaze87(MazeEnv):
    def __init__(self):
        super(SmallMaze87, self).__init__(maze_file='small_mazes/87.npy', mode='plus')
class SmallMaze88(MazeEnv):
    def __init__(self):
        super(SmallMaze88, self).__init__(maze_file='small_mazes/88.npy', mode='plus')
class SmallMaze89(MazeEnv):
    def __init__(self):
        super(SmallMaze89, self).__init__(maze_file='small_mazes/89.npy', mode='plus')
class SmallMaze90(MazeEnv):
    def __init__(self):
        super(SmallMaze90, self).__init__(maze_file='small_mazes/90.npy', mode='plus')
class SmallMaze91(MazeEnv):
    def __init__(self):
        super(SmallMaze91, self).__init__(maze_file='small_mazes/91.npy', mode='plus')
class SmallMaze92(MazeEnv):
    def __init__(self):
        super(SmallMaze92, self).__init__(maze_file='small_mazes/92.npy', mode='plus')
class SmallMaze93(MazeEnv):
    def __init__(self):
        super(SmallMaze93, self).__init__(maze_file='small_mazes/93.npy', mode='plus')
class SmallMaze94(MazeEnv):
    def __init__(self):
        super(SmallMaze94, self).__init__(maze_file='small_mazes/94.npy', mode='plus')
class SmallMaze95(MazeEnv):
    def __init__(self):
        super(SmallMaze95, self).__init__(maze_file='small_mazes/95.npy', mode='plus')
class SmallMaze96(MazeEnv):
    def __init__(self):
        super(SmallMaze96, self).__init__(maze_file='small_mazes/96.npy', mode='plus')
class SmallMaze97(MazeEnv):
    def __init__(self):
        super(SmallMaze97, self).__init__(maze_file='small_mazes/97.npy', mode='plus')
class SmallMaze98(MazeEnv):
    def __init__(self):
        super(SmallMaze98, self).__init__(maze_file='small_mazes/98.npy', mode='plus')
class SmallMaze99(MazeEnv):
    def __init__(self):
        super(SmallMaze99, self).__init__(maze_file='small_mazes/99.npy', mode='plus')
