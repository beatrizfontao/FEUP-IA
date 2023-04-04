from Game import *

# random vs random
for i in range(5):
    game((5,5))

# random vs ai easy
for i in range(5):
    game((5,PlayerMode.AI_EASY))

# random vs ai medium
for i in range(5):
    game((5,PlayerMode.AI_MEDIUM))

# random vs ai hard
for i in range(5):
    game((5,PlayerMode.AI_HARD))

# ai easy vs ai easy
game((PlayerMode.AI_EASY,PlayerMode.AI_EASY))

# ai medium vs ai medium
game((PlayerMode.AI_MEDIUM,PlayerMode.AI_MEDIUM))

# ai hard vs ai hard
game((PlayerMode.AI_HARD,PlayerMode.AI_HARD))

# mix evaluation functions and depths

# ai easy vs ai medium
game((PlayerMode.AI_EASY,PlayerMode.AI_MEDIUM))
game((PlayerMode.AI_MEDIUM,PlayerMode.AI_EASY))

# ai medium vs ai hard
game((PlayerMode.AI_MEDIUM,PlayerMode.AI_HARD))
game((PlayerMode.AI_HARD,PlayerMode.AI_MEDIUM))

# ai easy vs ai hard
game((PlayerMode.AI_EASY,PlayerMode.AI_HARD))
game((PlayerMode.AI_HARD,PlayerMode.AI_EASY))
