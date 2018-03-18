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

    def save_img(self, file):
        return self.maze_view.save_img(file)

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

class SmallMaze100(MazeEnv):
    def __init__(self):
        super(SmallMaze100, self).__init__(maze_file='small_mazes/100.npy', mode='plus')
class SmallMaze101(MazeEnv):
    def __init__(self):
        super(SmallMaze101, self).__init__(maze_file='small_mazes/101.npy', mode='plus')
class SmallMaze102(MazeEnv):
    def __init__(self):
        super(SmallMaze102, self).__init__(maze_file='small_mazes/102.npy', mode='plus')
class SmallMaze103(MazeEnv):
    def __init__(self):
        super(SmallMaze103, self).__init__(maze_file='small_mazes/103.npy', mode='plus')
class SmallMaze104(MazeEnv):
    def __init__(self):
        super(SmallMaze104, self).__init__(maze_file='small_mazes/104.npy', mode='plus')
class SmallMaze105(MazeEnv):
    def __init__(self):
        super(SmallMaze105, self).__init__(maze_file='small_mazes/105.npy', mode='plus')
class SmallMaze106(MazeEnv):
    def __init__(self):
        super(SmallMaze106, self).__init__(maze_file='small_mazes/106.npy', mode='plus')
class SmallMaze107(MazeEnv):
    def __init__(self):
        super(SmallMaze107, self).__init__(maze_file='small_mazes/107.npy', mode='plus')
class SmallMaze108(MazeEnv):
    def __init__(self):
        super(SmallMaze108, self).__init__(maze_file='small_mazes/108.npy', mode='plus')
class SmallMaze109(MazeEnv):
    def __init__(self):
        super(SmallMaze109, self).__init__(maze_file='small_mazes/109.npy', mode='plus')
class SmallMaze110(MazeEnv):
    def __init__(self):
        super(SmallMaze110, self).__init__(maze_file='small_mazes/110.npy', mode='plus')
class SmallMaze111(MazeEnv):
    def __init__(self):
        super(SmallMaze111, self).__init__(maze_file='small_mazes/111.npy', mode='plus')
class SmallMaze112(MazeEnv):
    def __init__(self):
        super(SmallMaze112, self).__init__(maze_file='small_mazes/112.npy', mode='plus')
class SmallMaze113(MazeEnv):
    def __init__(self):
        super(SmallMaze113, self).__init__(maze_file='small_mazes/113.npy', mode='plus')
class SmallMaze114(MazeEnv):
    def __init__(self):
        super(SmallMaze114, self).__init__(maze_file='small_mazes/114.npy', mode='plus')
class SmallMaze115(MazeEnv):
    def __init__(self):
        super(SmallMaze115, self).__init__(maze_file='small_mazes/115.npy', mode='plus')
class SmallMaze116(MazeEnv):
    def __init__(self):
        super(SmallMaze116, self).__init__(maze_file='small_mazes/116.npy', mode='plus')
class SmallMaze117(MazeEnv):
    def __init__(self):
        super(SmallMaze117, self).__init__(maze_file='small_mazes/117.npy', mode='plus')
class SmallMaze118(MazeEnv):
    def __init__(self):
        super(SmallMaze118, self).__init__(maze_file='small_mazes/118.npy', mode='plus')
class SmallMaze119(MazeEnv):
    def __init__(self):
        super(SmallMaze119, self).__init__(maze_file='small_mazes/119.npy', mode='plus')
class SmallMaze120(MazeEnv):
    def __init__(self):
        super(SmallMaze120, self).__init__(maze_file='small_mazes/120.npy', mode='plus')
class SmallMaze121(MazeEnv):
    def __init__(self):
        super(SmallMaze121, self).__init__(maze_file='small_mazes/121.npy', mode='plus')
class SmallMaze122(MazeEnv):
    def __init__(self):
        super(SmallMaze122, self).__init__(maze_file='small_mazes/122.npy', mode='plus')
class SmallMaze123(MazeEnv):
    def __init__(self):
        super(SmallMaze123, self).__init__(maze_file='small_mazes/123.npy', mode='plus')
class SmallMaze124(MazeEnv):
    def __init__(self):
        super(SmallMaze124, self).__init__(maze_file='small_mazes/124.npy', mode='plus')
class SmallMaze125(MazeEnv):
    def __init__(self):
        super(SmallMaze125, self).__init__(maze_file='small_mazes/125.npy', mode='plus')
class SmallMaze126(MazeEnv):
    def __init__(self):
        super(SmallMaze126, self).__init__(maze_file='small_mazes/126.npy', mode='plus')
class SmallMaze127(MazeEnv):
    def __init__(self):
        super(SmallMaze127, self).__init__(maze_file='small_mazes/127.npy', mode='plus')
class SmallMaze128(MazeEnv):
    def __init__(self):
        super(SmallMaze128, self).__init__(maze_file='small_mazes/128.npy', mode='plus')
class SmallMaze129(MazeEnv):
    def __init__(self):
        super(SmallMaze129, self).__init__(maze_file='small_mazes/129.npy', mode='plus')
class SmallMaze130(MazeEnv):
    def __init__(self):
        super(SmallMaze130, self).__init__(maze_file='small_mazes/130.npy', mode='plus')
class SmallMaze131(MazeEnv):
    def __init__(self):
        super(SmallMaze131, self).__init__(maze_file='small_mazes/131.npy', mode='plus')
class SmallMaze132(MazeEnv):
    def __init__(self):
        super(SmallMaze132, self).__init__(maze_file='small_mazes/132.npy', mode='plus')
class SmallMaze133(MazeEnv):
    def __init__(self):
        super(SmallMaze133, self).__init__(maze_file='small_mazes/133.npy', mode='plus')
class SmallMaze134(MazeEnv):
    def __init__(self):
        super(SmallMaze134, self).__init__(maze_file='small_mazes/134.npy', mode='plus')
class SmallMaze135(MazeEnv):
    def __init__(self):
        super(SmallMaze135, self).__init__(maze_file='small_mazes/135.npy', mode='plus')
class SmallMaze136(MazeEnv):
    def __init__(self):
        super(SmallMaze136, self).__init__(maze_file='small_mazes/136.npy', mode='plus')
class SmallMaze137(MazeEnv):
    def __init__(self):
        super(SmallMaze137, self).__init__(maze_file='small_mazes/137.npy', mode='plus')
class SmallMaze138(MazeEnv):
    def __init__(self):
        super(SmallMaze138, self).__init__(maze_file='small_mazes/138.npy', mode='plus')
class SmallMaze139(MazeEnv):
    def __init__(self):
        super(SmallMaze139, self).__init__(maze_file='small_mazes/139.npy', mode='plus')
class SmallMaze140(MazeEnv):
    def __init__(self):
        super(SmallMaze140, self).__init__(maze_file='small_mazes/140.npy', mode='plus')
class SmallMaze141(MazeEnv):
    def __init__(self):
        super(SmallMaze141, self).__init__(maze_file='small_mazes/141.npy', mode='plus')
class SmallMaze142(MazeEnv):
    def __init__(self):
        super(SmallMaze142, self).__init__(maze_file='small_mazes/142.npy', mode='plus')
class SmallMaze143(MazeEnv):
    def __init__(self):
        super(SmallMaze143, self).__init__(maze_file='small_mazes/143.npy', mode='plus')
class SmallMaze144(MazeEnv):
    def __init__(self):
        super(SmallMaze144, self).__init__(maze_file='small_mazes/144.npy', mode='plus')
class SmallMaze145(MazeEnv):
    def __init__(self):
        super(SmallMaze145, self).__init__(maze_file='small_mazes/145.npy', mode='plus')
class SmallMaze146(MazeEnv):
    def __init__(self):
        super(SmallMaze146, self).__init__(maze_file='small_mazes/146.npy', mode='plus')
class SmallMaze147(MazeEnv):
    def __init__(self):
        super(SmallMaze147, self).__init__(maze_file='small_mazes/147.npy', mode='plus')
class SmallMaze148(MazeEnv):
    def __init__(self):
        super(SmallMaze148, self).__init__(maze_file='small_mazes/148.npy', mode='plus')
class SmallMaze149(MazeEnv):
    def __init__(self):
        super(SmallMaze149, self).__init__(maze_file='small_mazes/149.npy', mode='plus')
class SmallMaze150(MazeEnv):
    def __init__(self):
        super(SmallMaze150, self).__init__(maze_file='small_mazes/150.npy', mode='plus')
class SmallMaze151(MazeEnv):
    def __init__(self):
        super(SmallMaze151, self).__init__(maze_file='small_mazes/151.npy', mode='plus')
class SmallMaze152(MazeEnv):
    def __init__(self):
        super(SmallMaze152, self).__init__(maze_file='small_mazes/152.npy', mode='plus')
class SmallMaze153(MazeEnv):
    def __init__(self):
        super(SmallMaze153, self).__init__(maze_file='small_mazes/153.npy', mode='plus')
class SmallMaze154(MazeEnv):
    def __init__(self):
        super(SmallMaze154, self).__init__(maze_file='small_mazes/154.npy', mode='plus')
class SmallMaze155(MazeEnv):
    def __init__(self):
        super(SmallMaze155, self).__init__(maze_file='small_mazes/155.npy', mode='plus')
class SmallMaze156(MazeEnv):
    def __init__(self):
        super(SmallMaze156, self).__init__(maze_file='small_mazes/156.npy', mode='plus')
class SmallMaze157(MazeEnv):
    def __init__(self):
        super(SmallMaze157, self).__init__(maze_file='small_mazes/157.npy', mode='plus')
class SmallMaze158(MazeEnv):
    def __init__(self):
        super(SmallMaze158, self).__init__(maze_file='small_mazes/158.npy', mode='plus')
class SmallMaze159(MazeEnv):
    def __init__(self):
        super(SmallMaze159, self).__init__(maze_file='small_mazes/159.npy', mode='plus')
class SmallMaze160(MazeEnv):
    def __init__(self):
        super(SmallMaze160, self).__init__(maze_file='small_mazes/160.npy', mode='plus')
class SmallMaze161(MazeEnv):
    def __init__(self):
        super(SmallMaze161, self).__init__(maze_file='small_mazes/161.npy', mode='plus')
class SmallMaze162(MazeEnv):
    def __init__(self):
        super(SmallMaze162, self).__init__(maze_file='small_mazes/162.npy', mode='plus')
class SmallMaze163(MazeEnv):
    def __init__(self):
        super(SmallMaze163, self).__init__(maze_file='small_mazes/163.npy', mode='plus')
class SmallMaze164(MazeEnv):
    def __init__(self):
        super(SmallMaze164, self).__init__(maze_file='small_mazes/164.npy', mode='plus')
class SmallMaze165(MazeEnv):
    def __init__(self):
        super(SmallMaze165, self).__init__(maze_file='small_mazes/165.npy', mode='plus')
class SmallMaze166(MazeEnv):
    def __init__(self):
        super(SmallMaze166, self).__init__(maze_file='small_mazes/166.npy', mode='plus')
class SmallMaze167(MazeEnv):
    def __init__(self):
        super(SmallMaze167, self).__init__(maze_file='small_mazes/167.npy', mode='plus')
class SmallMaze168(MazeEnv):
    def __init__(self):
        super(SmallMaze168, self).__init__(maze_file='small_mazes/168.npy', mode='plus')
class SmallMaze169(MazeEnv):
    def __init__(self):
        super(SmallMaze169, self).__init__(maze_file='small_mazes/169.npy', mode='plus')
class SmallMaze170(MazeEnv):
    def __init__(self):
        super(SmallMaze170, self).__init__(maze_file='small_mazes/170.npy', mode='plus')
class SmallMaze171(MazeEnv):
    def __init__(self):
        super(SmallMaze171, self).__init__(maze_file='small_mazes/171.npy', mode='plus')
class SmallMaze172(MazeEnv):
    def __init__(self):
        super(SmallMaze172, self).__init__(maze_file='small_mazes/172.npy', mode='plus')
class SmallMaze173(MazeEnv):
    def __init__(self):
        super(SmallMaze173, self).__init__(maze_file='small_mazes/173.npy', mode='plus')
class SmallMaze174(MazeEnv):
    def __init__(self):
        super(SmallMaze174, self).__init__(maze_file='small_mazes/174.npy', mode='plus')
class SmallMaze175(MazeEnv):
    def __init__(self):
        super(SmallMaze175, self).__init__(maze_file='small_mazes/175.npy', mode='plus')
class SmallMaze176(MazeEnv):
    def __init__(self):
        super(SmallMaze176, self).__init__(maze_file='small_mazes/176.npy', mode='plus')
class SmallMaze177(MazeEnv):
    def __init__(self):
        super(SmallMaze177, self).__init__(maze_file='small_mazes/177.npy', mode='plus')
class SmallMaze178(MazeEnv):
    def __init__(self):
        super(SmallMaze178, self).__init__(maze_file='small_mazes/178.npy', mode='plus')
class SmallMaze179(MazeEnv):
    def __init__(self):
        super(SmallMaze179, self).__init__(maze_file='small_mazes/179.npy', mode='plus')
class SmallMaze180(MazeEnv):
    def __init__(self):
        super(SmallMaze180, self).__init__(maze_file='small_mazes/180.npy', mode='plus')
class SmallMaze181(MazeEnv):
    def __init__(self):
        super(SmallMaze181, self).__init__(maze_file='small_mazes/181.npy', mode='plus')
class SmallMaze182(MazeEnv):
    def __init__(self):
        super(SmallMaze182, self).__init__(maze_file='small_mazes/182.npy', mode='plus')
class SmallMaze183(MazeEnv):
    def __init__(self):
        super(SmallMaze183, self).__init__(maze_file='small_mazes/183.npy', mode='plus')
class SmallMaze184(MazeEnv):
    def __init__(self):
        super(SmallMaze184, self).__init__(maze_file='small_mazes/184.npy', mode='plus')
class SmallMaze185(MazeEnv):
    def __init__(self):
        super(SmallMaze185, self).__init__(maze_file='small_mazes/185.npy', mode='plus')
class SmallMaze186(MazeEnv):
    def __init__(self):
        super(SmallMaze186, self).__init__(maze_file='small_mazes/186.npy', mode='plus')
class SmallMaze187(MazeEnv):
    def __init__(self):
        super(SmallMaze187, self).__init__(maze_file='small_mazes/187.npy', mode='plus')
class SmallMaze188(MazeEnv):
    def __init__(self):
        super(SmallMaze188, self).__init__(maze_file='small_mazes/188.npy', mode='plus')
class SmallMaze189(MazeEnv):
    def __init__(self):
        super(SmallMaze189, self).__init__(maze_file='small_mazes/189.npy', mode='plus')
class SmallMaze190(MazeEnv):
    def __init__(self):
        super(SmallMaze190, self).__init__(maze_file='small_mazes/190.npy', mode='plus')
class SmallMaze191(MazeEnv):
    def __init__(self):
        super(SmallMaze191, self).__init__(maze_file='small_mazes/191.npy', mode='plus')
class SmallMaze192(MazeEnv):
    def __init__(self):
        super(SmallMaze192, self).__init__(maze_file='small_mazes/192.npy', mode='plus')
class SmallMaze193(MazeEnv):
    def __init__(self):
        super(SmallMaze193, self).__init__(maze_file='small_mazes/193.npy', mode='plus')
class SmallMaze194(MazeEnv):
    def __init__(self):
        super(SmallMaze194, self).__init__(maze_file='small_mazes/194.npy', mode='plus')
class SmallMaze195(MazeEnv):
    def __init__(self):
        super(SmallMaze195, self).__init__(maze_file='small_mazes/195.npy', mode='plus')
class SmallMaze196(MazeEnv):
    def __init__(self):
        super(SmallMaze196, self).__init__(maze_file='small_mazes/196.npy', mode='plus')
class SmallMaze197(MazeEnv):
    def __init__(self):
        super(SmallMaze197, self).__init__(maze_file='small_mazes/197.npy', mode='plus')
class SmallMaze198(MazeEnv):
    def __init__(self):
        super(SmallMaze198, self).__init__(maze_file='small_mazes/198.npy', mode='plus')
class SmallMaze199(MazeEnv):
    def __init__(self):
        super(SmallMaze199, self).__init__(maze_file='small_mazes/199.npy', mode='plus')




class MediumMaze0(MazeEnv):
    def __init__(self):
        super(MediumMaze0, self).__init__(maze_file='medium_mazes/0.npy', mode='plus')
class MediumMaze1(MazeEnv):
    def __init__(self):
        super(MediumMaze1, self).__init__(maze_file='medium_mazes/1.npy', mode='plus')
class MediumMaze2(MazeEnv):
    def __init__(self):
        super(MediumMaze2, self).__init__(maze_file='medium_mazes/2.npy', mode='plus')
class MediumMaze3(MazeEnv):
    def __init__(self):
        super(MediumMaze3, self).__init__(maze_file='medium_mazes/3.npy', mode='plus')
class MediumMaze4(MazeEnv):
    def __init__(self):
        super(MediumMaze4, self).__init__(maze_file='medium_mazes/4.npy', mode='plus')
class MediumMaze5(MazeEnv):
    def __init__(self):
        super(MediumMaze5, self).__init__(maze_file='medium_mazes/5.npy', mode='plus')
class MediumMaze6(MazeEnv):
    def __init__(self):
        super(MediumMaze6, self).__init__(maze_file='medium_mazes/6.npy', mode='plus')
class MediumMaze7(MazeEnv):
    def __init__(self):
        super(MediumMaze7, self).__init__(maze_file='medium_mazes/7.npy', mode='plus')
class MediumMaze8(MazeEnv):
    def __init__(self):
        super(MediumMaze8, self).__init__(maze_file='medium_mazes/8.npy', mode='plus')
class MediumMaze9(MazeEnv):
    def __init__(self):
        super(MediumMaze9, self).__init__(maze_file='medium_mazes/9.npy', mode='plus')
class MediumMaze10(MazeEnv):
    def __init__(self):
        super(MediumMaze10, self).__init__(maze_file='medium_mazes/10.npy', mode='plus')
class MediumMaze11(MazeEnv):
    def __init__(self):
        super(MediumMaze11, self).__init__(maze_file='medium_mazes/11.npy', mode='plus')
class MediumMaze12(MazeEnv):
    def __init__(self):
        super(MediumMaze12, self).__init__(maze_file='medium_mazes/12.npy', mode='plus')
class MediumMaze13(MazeEnv):
    def __init__(self):
        super(MediumMaze13, self).__init__(maze_file='medium_mazes/13.npy', mode='plus')
class MediumMaze14(MazeEnv):
    def __init__(self):
        super(MediumMaze14, self).__init__(maze_file='medium_mazes/14.npy', mode='plus')
class MediumMaze15(MazeEnv):
    def __init__(self):
        super(MediumMaze15, self).__init__(maze_file='medium_mazes/15.npy', mode='plus')
class MediumMaze16(MazeEnv):
    def __init__(self):
        super(MediumMaze16, self).__init__(maze_file='medium_mazes/16.npy', mode='plus')
class MediumMaze17(MazeEnv):
    def __init__(self):
        super(MediumMaze17, self).__init__(maze_file='medium_mazes/17.npy', mode='plus')
class MediumMaze18(MazeEnv):
    def __init__(self):
        super(MediumMaze18, self).__init__(maze_file='medium_mazes/18.npy', mode='plus')
class MediumMaze19(MazeEnv):
    def __init__(self):
        super(MediumMaze19, self).__init__(maze_file='medium_mazes/19.npy', mode='plus')
class MediumMaze20(MazeEnv):
    def __init__(self):
        super(MediumMaze20, self).__init__(maze_file='medium_mazes/20.npy', mode='plus')
class MediumMaze21(MazeEnv):
    def __init__(self):
        super(MediumMaze21, self).__init__(maze_file='medium_mazes/21.npy', mode='plus')
class MediumMaze22(MazeEnv):
    def __init__(self):
        super(MediumMaze22, self).__init__(maze_file='medium_mazes/22.npy', mode='plus')
class MediumMaze23(MazeEnv):
    def __init__(self):
        super(MediumMaze23, self).__init__(maze_file='medium_mazes/23.npy', mode='plus')
class MediumMaze24(MazeEnv):
    def __init__(self):
        super(MediumMaze24, self).__init__(maze_file='medium_mazes/24.npy', mode='plus')
class MediumMaze25(MazeEnv):
    def __init__(self):
        super(MediumMaze25, self).__init__(maze_file='medium_mazes/25.npy', mode='plus')
class MediumMaze26(MazeEnv):
    def __init__(self):
        super(MediumMaze26, self).__init__(maze_file='medium_mazes/26.npy', mode='plus')
class MediumMaze27(MazeEnv):
    def __init__(self):
        super(MediumMaze27, self).__init__(maze_file='medium_mazes/27.npy', mode='plus')
class MediumMaze28(MazeEnv):
    def __init__(self):
        super(MediumMaze28, self).__init__(maze_file='medium_mazes/28.npy', mode='plus')
class MediumMaze29(MazeEnv):
    def __init__(self):
        super(MediumMaze29, self).__init__(maze_file='medium_mazes/29.npy', mode='plus')
class MediumMaze30(MazeEnv):
    def __init__(self):
        super(MediumMaze30, self).__init__(maze_file='medium_mazes/30.npy', mode='plus')
class MediumMaze31(MazeEnv):
    def __init__(self):
        super(MediumMaze31, self).__init__(maze_file='medium_mazes/31.npy', mode='plus')
class MediumMaze32(MazeEnv):
    def __init__(self):
        super(MediumMaze32, self).__init__(maze_file='medium_mazes/32.npy', mode='plus')
class MediumMaze33(MazeEnv):
    def __init__(self):
        super(MediumMaze33, self).__init__(maze_file='medium_mazes/33.npy', mode='plus')
class MediumMaze34(MazeEnv):
    def __init__(self):
        super(MediumMaze34, self).__init__(maze_file='medium_mazes/34.npy', mode='plus')
class MediumMaze35(MazeEnv):
    def __init__(self):
        super(MediumMaze35, self).__init__(maze_file='medium_mazes/35.npy', mode='plus')
class MediumMaze36(MazeEnv):
    def __init__(self):
        super(MediumMaze36, self).__init__(maze_file='medium_mazes/36.npy', mode='plus')
class MediumMaze37(MazeEnv):
    def __init__(self):
        super(MediumMaze37, self).__init__(maze_file='medium_mazes/37.npy', mode='plus')
class MediumMaze38(MazeEnv):
    def __init__(self):
        super(MediumMaze38, self).__init__(maze_file='medium_mazes/38.npy', mode='plus')
class MediumMaze39(MazeEnv):
    def __init__(self):
        super(MediumMaze39, self).__init__(maze_file='medium_mazes/39.npy', mode='plus')
class MediumMaze40(MazeEnv):
    def __init__(self):
        super(MediumMaze40, self).__init__(maze_file='medium_mazes/40.npy', mode='plus')
class MediumMaze41(MazeEnv):
    def __init__(self):
        super(MediumMaze41, self).__init__(maze_file='medium_mazes/41.npy', mode='plus')
class MediumMaze42(MazeEnv):
    def __init__(self):
        super(MediumMaze42, self).__init__(maze_file='medium_mazes/42.npy', mode='plus')
class MediumMaze43(MazeEnv):
    def __init__(self):
        super(MediumMaze43, self).__init__(maze_file='medium_mazes/43.npy', mode='plus')
class MediumMaze44(MazeEnv):
    def __init__(self):
        super(MediumMaze44, self).__init__(maze_file='medium_mazes/44.npy', mode='plus')
class MediumMaze45(MazeEnv):
    def __init__(self):
        super(MediumMaze45, self).__init__(maze_file='medium_mazes/45.npy', mode='plus')
class MediumMaze46(MazeEnv):
    def __init__(self):
        super(MediumMaze46, self).__init__(maze_file='medium_mazes/46.npy', mode='plus')
class MediumMaze47(MazeEnv):
    def __init__(self):
        super(MediumMaze47, self).__init__(maze_file='medium_mazes/47.npy', mode='plus')
class MediumMaze48(MazeEnv):
    def __init__(self):
        super(MediumMaze48, self).__init__(maze_file='medium_mazes/48.npy', mode='plus')
class MediumMaze49(MazeEnv):
    def __init__(self):
        super(MediumMaze49, self).__init__(maze_file='medium_mazes/49.npy', mode='plus')
class MediumMaze50(MazeEnv):
    def __init__(self):
        super(MediumMaze50, self).__init__(maze_file='medium_mazes/50.npy', mode='plus')
class MediumMaze51(MazeEnv):
    def __init__(self):
        super(MediumMaze51, self).__init__(maze_file='medium_mazes/51.npy', mode='plus')
class MediumMaze52(MazeEnv):
    def __init__(self):
        super(MediumMaze52, self).__init__(maze_file='medium_mazes/52.npy', mode='plus')
class MediumMaze53(MazeEnv):
    def __init__(self):
        super(MediumMaze53, self).__init__(maze_file='medium_mazes/53.npy', mode='plus')
class MediumMaze54(MazeEnv):
    def __init__(self):
        super(MediumMaze54, self).__init__(maze_file='medium_mazes/54.npy', mode='plus')
class MediumMaze55(MazeEnv):
    def __init__(self):
        super(MediumMaze55, self).__init__(maze_file='medium_mazes/55.npy', mode='plus')
class MediumMaze56(MazeEnv):
    def __init__(self):
        super(MediumMaze56, self).__init__(maze_file='medium_mazes/56.npy', mode='plus')
class MediumMaze57(MazeEnv):
    def __init__(self):
        super(MediumMaze57, self).__init__(maze_file='medium_mazes/57.npy', mode='plus')
class MediumMaze58(MazeEnv):
    def __init__(self):
        super(MediumMaze58, self).__init__(maze_file='medium_mazes/58.npy', mode='plus')
class MediumMaze59(MazeEnv):
    def __init__(self):
        super(MediumMaze59, self).__init__(maze_file='medium_mazes/59.npy', mode='plus')
class MediumMaze60(MazeEnv):
    def __init__(self):
        super(MediumMaze60, self).__init__(maze_file='medium_mazes/60.npy', mode='plus')
class MediumMaze61(MazeEnv):
    def __init__(self):
        super(MediumMaze61, self).__init__(maze_file='medium_mazes/61.npy', mode='plus')
class MediumMaze62(MazeEnv):
    def __init__(self):
        super(MediumMaze62, self).__init__(maze_file='medium_mazes/62.npy', mode='plus')
class MediumMaze63(MazeEnv):
    def __init__(self):
        super(MediumMaze63, self).__init__(maze_file='medium_mazes/63.npy', mode='plus')
class MediumMaze64(MazeEnv):
    def __init__(self):
        super(MediumMaze64, self).__init__(maze_file='medium_mazes/64.npy', mode='plus')
class MediumMaze65(MazeEnv):
    def __init__(self):
        super(MediumMaze65, self).__init__(maze_file='medium_mazes/65.npy', mode='plus')
class MediumMaze66(MazeEnv):
    def __init__(self):
        super(MediumMaze66, self).__init__(maze_file='medium_mazes/66.npy', mode='plus')
class MediumMaze67(MazeEnv):
    def __init__(self):
        super(MediumMaze67, self).__init__(maze_file='medium_mazes/67.npy', mode='plus')
class MediumMaze68(MazeEnv):
    def __init__(self):
        super(MediumMaze68, self).__init__(maze_file='medium_mazes/68.npy', mode='plus')
class MediumMaze69(MazeEnv):
    def __init__(self):
        super(MediumMaze69, self).__init__(maze_file='medium_mazes/69.npy', mode='plus')
class MediumMaze70(MazeEnv):
    def __init__(self):
        super(MediumMaze70, self).__init__(maze_file='medium_mazes/70.npy', mode='plus')
class MediumMaze71(MazeEnv):
    def __init__(self):
        super(MediumMaze71, self).__init__(maze_file='medium_mazes/71.npy', mode='plus')
class MediumMaze72(MazeEnv):
    def __init__(self):
        super(MediumMaze72, self).__init__(maze_file='medium_mazes/72.npy', mode='plus')
class MediumMaze73(MazeEnv):
    def __init__(self):
        super(MediumMaze73, self).__init__(maze_file='medium_mazes/73.npy', mode='plus')
class MediumMaze74(MazeEnv):
    def __init__(self):
        super(MediumMaze74, self).__init__(maze_file='medium_mazes/74.npy', mode='plus')
class MediumMaze75(MazeEnv):
    def __init__(self):
        super(MediumMaze75, self).__init__(maze_file='medium_mazes/75.npy', mode='plus')
class MediumMaze76(MazeEnv):
    def __init__(self):
        super(MediumMaze76, self).__init__(maze_file='medium_mazes/76.npy', mode='plus')
class MediumMaze77(MazeEnv):
    def __init__(self):
        super(MediumMaze77, self).__init__(maze_file='medium_mazes/77.npy', mode='plus')
class MediumMaze78(MazeEnv):
    def __init__(self):
        super(MediumMaze78, self).__init__(maze_file='medium_mazes/78.npy', mode='plus')
class MediumMaze79(MazeEnv):
    def __init__(self):
        super(MediumMaze79, self).__init__(maze_file='medium_mazes/79.npy', mode='plus')
class MediumMaze80(MazeEnv):
    def __init__(self):
        super(MediumMaze80, self).__init__(maze_file='medium_mazes/80.npy', mode='plus')
class MediumMaze81(MazeEnv):
    def __init__(self):
        super(MediumMaze81, self).__init__(maze_file='medium_mazes/81.npy', mode='plus')
class MediumMaze82(MazeEnv):
    def __init__(self):
        super(MediumMaze82, self).__init__(maze_file='medium_mazes/82.npy', mode='plus')
class MediumMaze83(MazeEnv):
    def __init__(self):
        super(MediumMaze83, self).__init__(maze_file='medium_mazes/83.npy', mode='plus')
class MediumMaze84(MazeEnv):
    def __init__(self):
        super(MediumMaze84, self).__init__(maze_file='medium_mazes/84.npy', mode='plus')
class MediumMaze85(MazeEnv):
    def __init__(self):
        super(MediumMaze85, self).__init__(maze_file='medium_mazes/85.npy', mode='plus')
class MediumMaze86(MazeEnv):
    def __init__(self):
        super(MediumMaze86, self).__init__(maze_file='medium_mazes/86.npy', mode='plus')
class MediumMaze87(MazeEnv):
    def __init__(self):
        super(MediumMaze87, self).__init__(maze_file='medium_mazes/87.npy', mode='plus')
class MediumMaze88(MazeEnv):
    def __init__(self):
        super(MediumMaze88, self).__init__(maze_file='medium_mazes/88.npy', mode='plus')
class MediumMaze89(MazeEnv):
    def __init__(self):
        super(MediumMaze89, self).__init__(maze_file='medium_mazes/89.npy', mode='plus')
class MediumMaze90(MazeEnv):
    def __init__(self):
        super(MediumMaze90, self).__init__(maze_file='medium_mazes/90.npy', mode='plus')
class MediumMaze91(MazeEnv):
    def __init__(self):
        super(MediumMaze91, self).__init__(maze_file='medium_mazes/91.npy', mode='plus')
class MediumMaze92(MazeEnv):
    def __init__(self):
        super(MediumMaze92, self).__init__(maze_file='medium_mazes/92.npy', mode='plus')
class MediumMaze93(MazeEnv):
    def __init__(self):
        super(MediumMaze93, self).__init__(maze_file='medium_mazes/93.npy', mode='plus')
class MediumMaze94(MazeEnv):
    def __init__(self):
        super(MediumMaze94, self).__init__(maze_file='medium_mazes/94.npy', mode='plus')
class MediumMaze95(MazeEnv):
    def __init__(self):
        super(MediumMaze95, self).__init__(maze_file='medium_mazes/95.npy', mode='plus')
class MediumMaze96(MazeEnv):
    def __init__(self):
        super(MediumMaze96, self).__init__(maze_file='medium_mazes/96.npy', mode='plus')
class MediumMaze97(MazeEnv):
    def __init__(self):
        super(MediumMaze97, self).__init__(maze_file='medium_mazes/97.npy', mode='plus')
class MediumMaze98(MazeEnv):
    def __init__(self):
        super(MediumMaze98, self).__init__(maze_file='medium_mazes/98.npy', mode='plus')
class MediumMaze99(MazeEnv):
    def __init__(self):
        super(MediumMaze99, self).__init__(maze_file='medium_mazes/99.npy', mode='plus')
class BigMaze0(MazeEnv):
    def __init__(self):
        super(BigMaze0, self).__init__(maze_file='big_mazes/0.npy', mode='plus')
class BigMaze1(MazeEnv):
    def __init__(self):
        super(BigMaze1, self).__init__(maze_file='big_mazes/1.npy', mode='plus')
class BigMaze2(MazeEnv):
    def __init__(self):
        super(BigMaze2, self).__init__(maze_file='big_mazes/2.npy', mode='plus')
class BigMaze3(MazeEnv):
    def __init__(self):
        super(BigMaze3, self).__init__(maze_file='big_mazes/3.npy', mode='plus')
class BigMaze4(MazeEnv):
    def __init__(self):
        super(BigMaze4, self).__init__(maze_file='big_mazes/4.npy', mode='plus')
class BigMaze5(MazeEnv):
    def __init__(self):
        super(BigMaze5, self).__init__(maze_file='big_mazes/5.npy', mode='plus')
class BigMaze6(MazeEnv):
    def __init__(self):
        super(BigMaze6, self).__init__(maze_file='big_mazes/6.npy', mode='plus')
class BigMaze7(MazeEnv):
    def __init__(self):
        super(BigMaze7, self).__init__(maze_file='big_mazes/7.npy', mode='plus')
class BigMaze8(MazeEnv):
    def __init__(self):
        super(BigMaze8, self).__init__(maze_file='big_mazes/8.npy', mode='plus')
class BigMaze9(MazeEnv):
    def __init__(self):
        super(BigMaze9, self).__init__(maze_file='big_mazes/9.npy', mode='plus')
class VeryBigMaze0(MazeEnv):
    def __init__(self):
        super(VeryBigMaze0, self).__init__(maze_file='very_big_mazes/0.npy', mode='plus')
class VeryBigMaze1(MazeEnv):
    def __init__(self):
        super(VeryBigMaze1, self).__init__(maze_file='very_big_mazes/1.npy', mode='plus')
class VeryBigMaze2(MazeEnv):
    def __init__(self):
        super(VeryBigMaze2, self).__init__(maze_file='very_big_mazes/2.npy', mode='plus')
class VeryBigMaze3(MazeEnv):
    def __init__(self):
        super(VeryBigMaze3, self).__init__(maze_file='very_big_mazes/3.npy', mode='plus')
class VeryBigMaze4(MazeEnv):
    def __init__(self):
        super(VeryBigMaze4, self).__init__(maze_file='very_big_mazes/4.npy', mode='plus')
class VeryBigMaze5(MazeEnv):
    def __init__(self):
        super(VeryBigMaze5, self).__init__(maze_file='very_big_mazes/5.npy', mode='plus')
class VeryBigMaze6(MazeEnv):
    def __init__(self):
        super(VeryBigMaze6, self).__init__(maze_file='very_big_mazes/6.npy', mode='plus')
class VeryBigMaze7(MazeEnv):
    def __init__(self):
        super(VeryBigMaze7, self).__init__(maze_file='very_big_mazes/7.npy', mode='plus')
class VeryBigMaze8(MazeEnv):
    def __init__(self):
        super(VeryBigMaze8, self).__init__(maze_file='very_big_mazes/8.npy', mode='plus')
class VeryBigMaze9(MazeEnv):
    def __init__(self):
        super(VeryBigMaze9, self).__init__(maze_file='very_big_mazes/9.npy', mode='plus')