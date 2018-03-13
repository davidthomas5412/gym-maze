from gym.envs.registration import register


register(
    id='maze-v0',
    entry_point='gym_maze.envs:MazeEnvSample5x5',
    timestep_limit=2000,
)

register(
    id='maze-sample-5x5-v0',
    entry_point='gym_maze.envs:MazeEnvSample5x5',
    timestep_limit=2000,
)

register(
    id='maze-random-5x5-v0',
    entry_point='gym_maze.envs:MazeEnvRandom5x5',
    timestep_limit=2000,
    nondeterministic=True,
)

register(
    id='maze-sample-10x10-v0',
    entry_point='gym_maze.envs:MazeEnvSample10x10',
    timestep_limit=10000,
)

register(
    id='maze-random-10x10-v0',
    entry_point='gym_maze.envs:MazeEnvRandom10x10',
    timestep_limit=10000,
    nondeterministic=True,
)

register(
    id='maze-sample-3x3-v0',
    entry_point='gym_maze.envs:MazeEnvSample3x3',
    timestep_limit=1000,
)

register(
    id='maze-random-3x3-v0',
    entry_point='gym_maze.envs:MazeEnvRandom3x3',
    timestep_limit=1000,
    nondeterministic=True,
)


register(
    id='maze-sample-100x100-v0',
    entry_point='gym_maze.envs:MazeEnvSample100x100',
    timestep_limit=1000000,
)

register(
    id='maze-random-100x100-v0',
    entry_point='gym_maze.envs:MazeEnvRandom100x100',
    timestep_limit=1000000,
    nondeterministic=True,
)

register(
    id='maze-random-10x10-plus-v0',
    entry_point='gym_maze.envs:MazeEnvRandom10x10Plus',
    timestep_limit=1000000,
    nondeterministic=True,
)

register(
    id='maze-random-20x20-plus-v0',
    entry_point='gym_maze.envs:MazeEnvRandom20x20Plus',
    timestep_limit=1000000,
    nondeterministic=True,
)

register(
    id='maze-random-30x30-plus-v0',
    entry_point='gym_maze.envs:MazeEnvRandom30x30Plus',
    timestep_limit=1000000,
    nondeterministic=True,
)

register(
    id='milestone-maze-v0',
    entry_point='gym_maze.envs:MilestoneMaze',
    timestep_limit=1000000
)

register(id='small-maze-0-v0', entry_point='gym_maze.envs:SmallMaze0', timestep_limit=1000000)
register(id='small-maze-1-v0', entry_point='gym_maze.envs:SmallMaze1', timestep_limit=1000000)
register(id='small-maze-2-v0', entry_point='gym_maze.envs:SmallMaze2', timestep_limit=1000000)
register(id='small-maze-3-v0', entry_point='gym_maze.envs:SmallMaze3', timestep_limit=1000000)
register(id='small-maze-4-v0', entry_point='gym_maze.envs:SmallMaze4', timestep_limit=1000000)
register(id='small-maze-5-v0', entry_point='gym_maze.envs:SmallMaze5', timestep_limit=1000000)
register(id='small-maze-6-v0', entry_point='gym_maze.envs:SmallMaze6', timestep_limit=1000000)
register(id='small-maze-7-v0', entry_point='gym_maze.envs:SmallMaze7', timestep_limit=1000000)
register(id='small-maze-8-v0', entry_point='gym_maze.envs:SmallMaze8', timestep_limit=1000000)
register(id='small-maze-9-v0', entry_point='gym_maze.envs:SmallMaze9', timestep_limit=1000000)
register(id='small-maze-10-v0', entry_point='gym_maze.envs:SmallMaze10', timestep_limit=1000000)
register(id='small-maze-11-v0', entry_point='gym_maze.envs:SmallMaze11', timestep_limit=1000000)
register(id='small-maze-12-v0', entry_point='gym_maze.envs:SmallMaze12', timestep_limit=1000000)
register(id='small-maze-13-v0', entry_point='gym_maze.envs:SmallMaze13', timestep_limit=1000000)
register(id='small-maze-14-v0', entry_point='gym_maze.envs:SmallMaze14', timestep_limit=1000000)
register(id='small-maze-15-v0', entry_point='gym_maze.envs:SmallMaze15', timestep_limit=1000000)
register(id='small-maze-16-v0', entry_point='gym_maze.envs:SmallMaze16', timestep_limit=1000000)
register(id='small-maze-17-v0', entry_point='gym_maze.envs:SmallMaze17', timestep_limit=1000000)
register(id='small-maze-18-v0', entry_point='gym_maze.envs:SmallMaze18', timestep_limit=1000000)
register(id='small-maze-19-v0', entry_point='gym_maze.envs:SmallMaze19', timestep_limit=1000000)
register(id='small-maze-20-v0', entry_point='gym_maze.envs:SmallMaze20', timestep_limit=1000000)
register(id='small-maze-21-v0', entry_point='gym_maze.envs:SmallMaze21', timestep_limit=1000000)
register(id='small-maze-22-v0', entry_point='gym_maze.envs:SmallMaze22', timestep_limit=1000000)
register(id='small-maze-23-v0', entry_point='gym_maze.envs:SmallMaze23', timestep_limit=1000000)
register(id='small-maze-24-v0', entry_point='gym_maze.envs:SmallMaze24', timestep_limit=1000000)
register(id='small-maze-25-v0', entry_point='gym_maze.envs:SmallMaze25', timestep_limit=1000000)
register(id='small-maze-26-v0', entry_point='gym_maze.envs:SmallMaze26', timestep_limit=1000000)
register(id='small-maze-27-v0', entry_point='gym_maze.envs:SmallMaze27', timestep_limit=1000000)
register(id='small-maze-28-v0', entry_point='gym_maze.envs:SmallMaze28', timestep_limit=1000000)
register(id='small-maze-29-v0', entry_point='gym_maze.envs:SmallMaze29', timestep_limit=1000000)
register(id='small-maze-30-v0', entry_point='gym_maze.envs:SmallMaze30', timestep_limit=1000000)
register(id='small-maze-31-v0', entry_point='gym_maze.envs:SmallMaze31', timestep_limit=1000000)
register(id='small-maze-32-v0', entry_point='gym_maze.envs:SmallMaze32', timestep_limit=1000000)
register(id='small-maze-33-v0', entry_point='gym_maze.envs:SmallMaze33', timestep_limit=1000000)
register(id='small-maze-34-v0', entry_point='gym_maze.envs:SmallMaze34', timestep_limit=1000000)
register(id='small-maze-35-v0', entry_point='gym_maze.envs:SmallMaze35', timestep_limit=1000000)
register(id='small-maze-36-v0', entry_point='gym_maze.envs:SmallMaze36', timestep_limit=1000000)
register(id='small-maze-37-v0', entry_point='gym_maze.envs:SmallMaze37', timestep_limit=1000000)
register(id='small-maze-38-v0', entry_point='gym_maze.envs:SmallMaze38', timestep_limit=1000000)
register(id='small-maze-39-v0', entry_point='gym_maze.envs:SmallMaze39', timestep_limit=1000000)
register(id='small-maze-40-v0', entry_point='gym_maze.envs:SmallMaze40', timestep_limit=1000000)
register(id='small-maze-41-v0', entry_point='gym_maze.envs:SmallMaze41', timestep_limit=1000000)
register(id='small-maze-42-v0', entry_point='gym_maze.envs:SmallMaze42', timestep_limit=1000000)
register(id='small-maze-43-v0', entry_point='gym_maze.envs:SmallMaze43', timestep_limit=1000000)
register(id='small-maze-44-v0', entry_point='gym_maze.envs:SmallMaze44', timestep_limit=1000000)
register(id='small-maze-45-v0', entry_point='gym_maze.envs:SmallMaze45', timestep_limit=1000000)
register(id='small-maze-46-v0', entry_point='gym_maze.envs:SmallMaze46', timestep_limit=1000000)
register(id='small-maze-47-v0', entry_point='gym_maze.envs:SmallMaze47', timestep_limit=1000000)
register(id='small-maze-48-v0', entry_point='gym_maze.envs:SmallMaze48', timestep_limit=1000000)
register(id='small-maze-49-v0', entry_point='gym_maze.envs:SmallMaze49', timestep_limit=1000000)
register(id='small-maze-50-v0', entry_point='gym_maze.envs:SmallMaze50', timestep_limit=1000000)
register(id='small-maze-51-v0', entry_point='gym_maze.envs:SmallMaze51', timestep_limit=1000000)
register(id='small-maze-52-v0', entry_point='gym_maze.envs:SmallMaze52', timestep_limit=1000000)
register(id='small-maze-53-v0', entry_point='gym_maze.envs:SmallMaze53', timestep_limit=1000000)
register(id='small-maze-54-v0', entry_point='gym_maze.envs:SmallMaze54', timestep_limit=1000000)
register(id='small-maze-55-v0', entry_point='gym_maze.envs:SmallMaze55', timestep_limit=1000000)
register(id='small-maze-56-v0', entry_point='gym_maze.envs:SmallMaze56', timestep_limit=1000000)
register(id='small-maze-57-v0', entry_point='gym_maze.envs:SmallMaze57', timestep_limit=1000000)
register(id='small-maze-58-v0', entry_point='gym_maze.envs:SmallMaze58', timestep_limit=1000000)
register(id='small-maze-59-v0', entry_point='gym_maze.envs:SmallMaze59', timestep_limit=1000000)
register(id='small-maze-60-v0', entry_point='gym_maze.envs:SmallMaze60', timestep_limit=1000000)
register(id='small-maze-61-v0', entry_point='gym_maze.envs:SmallMaze61', timestep_limit=1000000)
register(id='small-maze-62-v0', entry_point='gym_maze.envs:SmallMaze62', timestep_limit=1000000)
register(id='small-maze-63-v0', entry_point='gym_maze.envs:SmallMaze63', timestep_limit=1000000)
register(id='small-maze-64-v0', entry_point='gym_maze.envs:SmallMaze64', timestep_limit=1000000)
register(id='small-maze-65-v0', entry_point='gym_maze.envs:SmallMaze65', timestep_limit=1000000)
register(id='small-maze-66-v0', entry_point='gym_maze.envs:SmallMaze66', timestep_limit=1000000)
register(id='small-maze-67-v0', entry_point='gym_maze.envs:SmallMaze67', timestep_limit=1000000)
register(id='small-maze-68-v0', entry_point='gym_maze.envs:SmallMaze68', timestep_limit=1000000)
register(id='small-maze-69-v0', entry_point='gym_maze.envs:SmallMaze69', timestep_limit=1000000)
register(id='small-maze-70-v0', entry_point='gym_maze.envs:SmallMaze70', timestep_limit=1000000)
register(id='small-maze-71-v0', entry_point='gym_maze.envs:SmallMaze71', timestep_limit=1000000)
register(id='small-maze-72-v0', entry_point='gym_maze.envs:SmallMaze72', timestep_limit=1000000)
register(id='small-maze-73-v0', entry_point='gym_maze.envs:SmallMaze73', timestep_limit=1000000)
register(id='small-maze-74-v0', entry_point='gym_maze.envs:SmallMaze74', timestep_limit=1000000)
register(id='small-maze-75-v0', entry_point='gym_maze.envs:SmallMaze75', timestep_limit=1000000)
register(id='small-maze-76-v0', entry_point='gym_maze.envs:SmallMaze76', timestep_limit=1000000)
register(id='small-maze-77-v0', entry_point='gym_maze.envs:SmallMaze77', timestep_limit=1000000)
register(id='small-maze-78-v0', entry_point='gym_maze.envs:SmallMaze78', timestep_limit=1000000)
register(id='small-maze-79-v0', entry_point='gym_maze.envs:SmallMaze79', timestep_limit=1000000)
register(id='small-maze-80-v0', entry_point='gym_maze.envs:SmallMaze80', timestep_limit=1000000)
register(id='small-maze-81-v0', entry_point='gym_maze.envs:SmallMaze81', timestep_limit=1000000)
register(id='small-maze-82-v0', entry_point='gym_maze.envs:SmallMaze82', timestep_limit=1000000)
register(id='small-maze-83-v0', entry_point='gym_maze.envs:SmallMaze83', timestep_limit=1000000)
register(id='small-maze-84-v0', entry_point='gym_maze.envs:SmallMaze84', timestep_limit=1000000)
register(id='small-maze-85-v0', entry_point='gym_maze.envs:SmallMaze85', timestep_limit=1000000)
register(id='small-maze-86-v0', entry_point='gym_maze.envs:SmallMaze86', timestep_limit=1000000)
register(id='small-maze-87-v0', entry_point='gym_maze.envs:SmallMaze87', timestep_limit=1000000)
register(id='small-maze-88-v0', entry_point='gym_maze.envs:SmallMaze88', timestep_limit=1000000)
register(id='small-maze-89-v0', entry_point='gym_maze.envs:SmallMaze89', timestep_limit=1000000)
register(id='small-maze-90-v0', entry_point='gym_maze.envs:SmallMaze90', timestep_limit=1000000)
register(id='small-maze-91-v0', entry_point='gym_maze.envs:SmallMaze91', timestep_limit=1000000)
register(id='small-maze-92-v0', entry_point='gym_maze.envs:SmallMaze92', timestep_limit=1000000)
register(id='small-maze-93-v0', entry_point='gym_maze.envs:SmallMaze93', timestep_limit=1000000)
register(id='small-maze-94-v0', entry_point='gym_maze.envs:SmallMaze94', timestep_limit=1000000)
register(id='small-maze-95-v0', entry_point='gym_maze.envs:SmallMaze95', timestep_limit=1000000)
register(id='small-maze-96-v0', entry_point='gym_maze.envs:SmallMaze96', timestep_limit=1000000)
register(id='small-maze-97-v0', entry_point='gym_maze.envs:SmallMaze97', timestep_limit=1000000)
register(id='small-maze-98-v0', entry_point='gym_maze.envs:SmallMaze98', timestep_limit=1000000)
register(id='small-maze-99-v0', entry_point='gym_maze.envs:SmallMaze99', timestep_limit=1000000)

register(id='medium-maze-0-v0', entry_point='gym_maze.envs:MediumMaze0', timestep_limit=1000000)
register(id='medium-maze-1-v0', entry_point='gym_maze.envs:MediumMaze1', timestep_limit=1000000)
register(id='medium-maze-2-v0', entry_point='gym_maze.envs:MediumMaze2', timestep_limit=1000000)
register(id='medium-maze-3-v0', entry_point='gym_maze.envs:MediumMaze3', timestep_limit=1000000)
register(id='medium-maze-4-v0', entry_point='gym_maze.envs:MediumMaze4', timestep_limit=1000000)
register(id='medium-maze-5-v0', entry_point='gym_maze.envs:MediumMaze5', timestep_limit=1000000)
register(id='medium-maze-6-v0', entry_point='gym_maze.envs:MediumMaze6', timestep_limit=1000000)
register(id='medium-maze-7-v0', entry_point='gym_maze.envs:MediumMaze7', timestep_limit=1000000)
register(id='medium-maze-8-v0', entry_point='gym_maze.envs:MediumMaze8', timestep_limit=1000000)
register(id='medium-maze-9-v0', entry_point='gym_maze.envs:MediumMaze9', timestep_limit=1000000)
register(id='medium-maze-10-v0', entry_point='gym_maze.envs:MediumMaze10', timestep_limit=1000000)
register(id='medium-maze-11-v0', entry_point='gym_maze.envs:MediumMaze11', timestep_limit=1000000)
register(id='medium-maze-12-v0', entry_point='gym_maze.envs:MediumMaze12', timestep_limit=1000000)
register(id='medium-maze-13-v0', entry_point='gym_maze.envs:MediumMaze13', timestep_limit=1000000)
register(id='medium-maze-14-v0', entry_point='gym_maze.envs:MediumMaze14', timestep_limit=1000000)
register(id='medium-maze-15-v0', entry_point='gym_maze.envs:MediumMaze15', timestep_limit=1000000)
register(id='medium-maze-16-v0', entry_point='gym_maze.envs:MediumMaze16', timestep_limit=1000000)
register(id='medium-maze-17-v0', entry_point='gym_maze.envs:MediumMaze17', timestep_limit=1000000)
register(id='medium-maze-18-v0', entry_point='gym_maze.envs:MediumMaze18', timestep_limit=1000000)
register(id='medium-maze-19-v0', entry_point='gym_maze.envs:MediumMaze19', timestep_limit=1000000)
register(id='medium-maze-20-v0', entry_point='gym_maze.envs:MediumMaze20', timestep_limit=1000000)
register(id='medium-maze-21-v0', entry_point='gym_maze.envs:MediumMaze21', timestep_limit=1000000)
register(id='medium-maze-22-v0', entry_point='gym_maze.envs:MediumMaze22', timestep_limit=1000000)
register(id='medium-maze-23-v0', entry_point='gym_maze.envs:MediumMaze23', timestep_limit=1000000)
register(id='medium-maze-24-v0', entry_point='gym_maze.envs:MediumMaze24', timestep_limit=1000000)
register(id='medium-maze-25-v0', entry_point='gym_maze.envs:MediumMaze25', timestep_limit=1000000)
register(id='medium-maze-26-v0', entry_point='gym_maze.envs:MediumMaze26', timestep_limit=1000000)
register(id='medium-maze-27-v0', entry_point='gym_maze.envs:MediumMaze27', timestep_limit=1000000)
register(id='medium-maze-28-v0', entry_point='gym_maze.envs:MediumMaze28', timestep_limit=1000000)
register(id='medium-maze-29-v0', entry_point='gym_maze.envs:MediumMaze29', timestep_limit=1000000)
register(id='medium-maze-30-v0', entry_point='gym_maze.envs:MediumMaze30', timestep_limit=1000000)
register(id='medium-maze-31-v0', entry_point='gym_maze.envs:MediumMaze31', timestep_limit=1000000)
register(id='medium-maze-32-v0', entry_point='gym_maze.envs:MediumMaze32', timestep_limit=1000000)
register(id='medium-maze-33-v0', entry_point='gym_maze.envs:MediumMaze33', timestep_limit=1000000)
register(id='medium-maze-34-v0', entry_point='gym_maze.envs:MediumMaze34', timestep_limit=1000000)
register(id='medium-maze-35-v0', entry_point='gym_maze.envs:MediumMaze35', timestep_limit=1000000)
register(id='medium-maze-36-v0', entry_point='gym_maze.envs:MediumMaze36', timestep_limit=1000000)
register(id='medium-maze-37-v0', entry_point='gym_maze.envs:MediumMaze37', timestep_limit=1000000)
register(id='medium-maze-38-v0', entry_point='gym_maze.envs:MediumMaze38', timestep_limit=1000000)
register(id='medium-maze-39-v0', entry_point='gym_maze.envs:MediumMaze39', timestep_limit=1000000)
register(id='medium-maze-40-v0', entry_point='gym_maze.envs:MediumMaze40', timestep_limit=1000000)
register(id='medium-maze-41-v0', entry_point='gym_maze.envs:MediumMaze41', timestep_limit=1000000)
register(id='medium-maze-42-v0', entry_point='gym_maze.envs:MediumMaze42', timestep_limit=1000000)
register(id='medium-maze-43-v0', entry_point='gym_maze.envs:MediumMaze43', timestep_limit=1000000)
register(id='medium-maze-44-v0', entry_point='gym_maze.envs:MediumMaze44', timestep_limit=1000000)
register(id='medium-maze-45-v0', entry_point='gym_maze.envs:MediumMaze45', timestep_limit=1000000)
register(id='medium-maze-46-v0', entry_point='gym_maze.envs:MediumMaze46', timestep_limit=1000000)
register(id='medium-maze-47-v0', entry_point='gym_maze.envs:MediumMaze47', timestep_limit=1000000)
register(id='medium-maze-48-v0', entry_point='gym_maze.envs:MediumMaze48', timestep_limit=1000000)
register(id='medium-maze-49-v0', entry_point='gym_maze.envs:MediumMaze49', timestep_limit=1000000)
register(id='medium-maze-50-v0', entry_point='gym_maze.envs:MediumMaze50', timestep_limit=1000000)
register(id='medium-maze-51-v0', entry_point='gym_maze.envs:MediumMaze51', timestep_limit=1000000)
register(id='medium-maze-52-v0', entry_point='gym_maze.envs:MediumMaze52', timestep_limit=1000000)
register(id='medium-maze-53-v0', entry_point='gym_maze.envs:MediumMaze53', timestep_limit=1000000)
register(id='medium-maze-54-v0', entry_point='gym_maze.envs:MediumMaze54', timestep_limit=1000000)
register(id='medium-maze-55-v0', entry_point='gym_maze.envs:MediumMaze55', timestep_limit=1000000)
register(id='medium-maze-56-v0', entry_point='gym_maze.envs:MediumMaze56', timestep_limit=1000000)
register(id='medium-maze-57-v0', entry_point='gym_maze.envs:MediumMaze57', timestep_limit=1000000)
register(id='medium-maze-58-v0', entry_point='gym_maze.envs:MediumMaze58', timestep_limit=1000000)
register(id='medium-maze-59-v0', entry_point='gym_maze.envs:MediumMaze59', timestep_limit=1000000)
register(id='medium-maze-60-v0', entry_point='gym_maze.envs:MediumMaze60', timestep_limit=1000000)
register(id='medium-maze-61-v0', entry_point='gym_maze.envs:MediumMaze61', timestep_limit=1000000)
register(id='medium-maze-62-v0', entry_point='gym_maze.envs:MediumMaze62', timestep_limit=1000000)
register(id='medium-maze-63-v0', entry_point='gym_maze.envs:MediumMaze63', timestep_limit=1000000)
register(id='medium-maze-64-v0', entry_point='gym_maze.envs:MediumMaze64', timestep_limit=1000000)
register(id='medium-maze-65-v0', entry_point='gym_maze.envs:MediumMaze65', timestep_limit=1000000)
register(id='medium-maze-66-v0', entry_point='gym_maze.envs:MediumMaze66', timestep_limit=1000000)
register(id='medium-maze-67-v0', entry_point='gym_maze.envs:MediumMaze67', timestep_limit=1000000)
register(id='medium-maze-68-v0', entry_point='gym_maze.envs:MediumMaze68', timestep_limit=1000000)
register(id='medium-maze-69-v0', entry_point='gym_maze.envs:MediumMaze69', timestep_limit=1000000)
register(id='medium-maze-70-v0', entry_point='gym_maze.envs:MediumMaze70', timestep_limit=1000000)
register(id='medium-maze-71-v0', entry_point='gym_maze.envs:MediumMaze71', timestep_limit=1000000)
register(id='medium-maze-72-v0', entry_point='gym_maze.envs:MediumMaze72', timestep_limit=1000000)
register(id='medium-maze-73-v0', entry_point='gym_maze.envs:MediumMaze73', timestep_limit=1000000)
register(id='medium-maze-74-v0', entry_point='gym_maze.envs:MediumMaze74', timestep_limit=1000000)
register(id='medium-maze-75-v0', entry_point='gym_maze.envs:MediumMaze75', timestep_limit=1000000)
register(id='medium-maze-76-v0', entry_point='gym_maze.envs:MediumMaze76', timestep_limit=1000000)
register(id='medium-maze-77-v0', entry_point='gym_maze.envs:MediumMaze77', timestep_limit=1000000)
register(id='medium-maze-78-v0', entry_point='gym_maze.envs:MediumMaze78', timestep_limit=1000000)
register(id='medium-maze-79-v0', entry_point='gym_maze.envs:MediumMaze79', timestep_limit=1000000)
register(id='medium-maze-80-v0', entry_point='gym_maze.envs:MediumMaze80', timestep_limit=1000000)
register(id='medium-maze-81-v0', entry_point='gym_maze.envs:MediumMaze81', timestep_limit=1000000)
register(id='medium-maze-82-v0', entry_point='gym_maze.envs:MediumMaze82', timestep_limit=1000000)
register(id='medium-maze-83-v0', entry_point='gym_maze.envs:MediumMaze83', timestep_limit=1000000)
register(id='medium-maze-84-v0', entry_point='gym_maze.envs:MediumMaze84', timestep_limit=1000000)
register(id='medium-maze-85-v0', entry_point='gym_maze.envs:MediumMaze85', timestep_limit=1000000)
register(id='medium-maze-86-v0', entry_point='gym_maze.envs:MediumMaze86', timestep_limit=1000000)
register(id='medium-maze-87-v0', entry_point='gym_maze.envs:MediumMaze87', timestep_limit=1000000)
register(id='medium-maze-88-v0', entry_point='gym_maze.envs:MediumMaze88', timestep_limit=1000000)
register(id='medium-maze-89-v0', entry_point='gym_maze.envs:MediumMaze89', timestep_limit=1000000)
register(id='medium-maze-90-v0', entry_point='gym_maze.envs:MediumMaze90', timestep_limit=1000000)
register(id='medium-maze-91-v0', entry_point='gym_maze.envs:MediumMaze91', timestep_limit=1000000)
register(id='medium-maze-92-v0', entry_point='gym_maze.envs:MediumMaze92', timestep_limit=1000000)
register(id='medium-maze-93-v0', entry_point='gym_maze.envs:MediumMaze93', timestep_limit=1000000)
register(id='medium-maze-94-v0', entry_point='gym_maze.envs:MediumMaze94', timestep_limit=1000000)
register(id='medium-maze-95-v0', entry_point='gym_maze.envs:MediumMaze95', timestep_limit=1000000)
register(id='medium-maze-96-v0', entry_point='gym_maze.envs:MediumMaze96', timestep_limit=1000000)
register(id='medium-maze-97-v0', entry_point='gym_maze.envs:MediumMaze97', timestep_limit=1000000)
register(id='medium-maze-98-v0', entry_point='gym_maze.envs:MediumMaze98', timestep_limit=1000000)
register(id='medium-maze-99-v0', entry_point='gym_maze.envs:MediumMaze99', timestep_limit=1000000)
register(id='big-maze-0-v0', entry_point='gym_maze.envs:BigMaze0', timestep_limit=1000000)
register(id='big-maze-1-v0', entry_point='gym_maze.envs:BigMaze1', timestep_limit=1000000)
register(id='big-maze-2-v0', entry_point='gym_maze.envs:BigMaze2', timestep_limit=1000000)
register(id='big-maze-3-v0', entry_point='gym_maze.envs:BigMaze3', timestep_limit=1000000)
register(id='big-maze-4-v0', entry_point='gym_maze.envs:BigMaze4', timestep_limit=1000000)
register(id='big-maze-5-v0', entry_point='gym_maze.envs:BigMaze5', timestep_limit=1000000)
register(id='big-maze-6-v0', entry_point='gym_maze.envs:BigMaze6', timestep_limit=1000000)
register(id='big-maze-7-v0', entry_point='gym_maze.envs:BigMaze7', timestep_limit=1000000)
register(id='big-maze-8-v0', entry_point='gym_maze.envs:BigMaze8', timestep_limit=1000000)
register(id='big-maze-9-v0', entry_point='gym_maze.envs:BigMaze9', timestep_limit=1000000)
register(id='very-big-maze-0-v0', entry_point='gym_maze.envs:VeryBigMaze0', timestep_limit=1000000)
register(id='very-big-maze-1-v0', entry_point='gym_maze.envs:VeryBigMaze1', timestep_limit=1000000)
register(id='very-big-maze-2-v0', entry_point='gym_maze.envs:VeryBigMaze2', timestep_limit=1000000)
register(id='very-big-maze-3-v0', entry_point='gym_maze.envs:VeryBigMaze3', timestep_limit=1000000)
register(id='very-big-maze-4-v0', entry_point='gym_maze.envs:VeryBigMaze4', timestep_limit=1000000)
register(id='very-big-maze-5-v0', entry_point='gym_maze.envs:VeryBigMaze5', timestep_limit=1000000)
register(id='very-big-maze-6-v0', entry_point='gym_maze.envs:VeryBigMaze6', timestep_limit=1000000)
register(id='very-big-maze-7-v0', entry_point='gym_maze.envs:VeryBigMaze7', timestep_limit=1000000)
register(id='very-big-maze-8-v0', entry_point='gym_maze.envs:VeryBigMaze8', timestep_limit=1000000)
register(id='very-big-maze-9-v0', entry_point='gym_maze.envs:VeryBigMaze9', timestep_limit=1000000)