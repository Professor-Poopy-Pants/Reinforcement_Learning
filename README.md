# Reinforcement_Learning

## AIM: 
#### Kuiper Escape using RL

## REQUIREMENTS:
- `import gym`  
- `import gym_kuiper_escape`
- `import random as rnd`
- `import numpy as np`
- `import matplotlib.pyplot as plt`
- `import math`
  
## DESCRIPTION:
This repository provides a comprehensive overview of various tasks and insights obtained from studying Reinforcement Learning (RL). It features in-depth descriptions of the environments utilized, visual representations of the outcomes from implementing different algorithms, and a summary of the challenges faced throughout the process.

[frozenlake]("frozenlake.md")

[minigrid]("")

## IMAGES 
<img src="https://user-images.githubusercontent.com/20359930/146223615-de23593f-02df-4ef1-b356-87153208d6f1.png" alt="image" height="300" width="300">

## State Space

The State Space is encompasses "virtual" lidar system. It sends off virtual
beams of light in all directions to gather an array of points describing
the distance and characteristics of nearby objects. The size of the lidar array and resulting observation/state space is configurable when the environment is initialized

The observation data (for each beam in the lidar array):
 * Distance (i.e. radial distance from player to terminating point of lidar beam)
 * Collision detection
   * 0 if terminated at edge of screen, or at max radius distance
   * 1 if collided with a rock
Note: The yellow dots (1 collide state) represent contact with a rock, the green dots (0 collide state) represent contact with wall or open space.

## Action Space
The user has the following discrete actions:
 * 0: Don't move
 * 1: Up
 * 2: Right
 * 3: Down
 * 4: Left
 * 5: Up/Right Diagonal
 * 6: Right/Down Diagonal
 * 7: Down/Left Diagonal
 * 8: Left/Up Diagonal

## Reward Function

## About Algorithm

Q-Learning is a popular model-free reinforcement learning algorithm used to learn the value of actions taken in given states of an environment. It operates by learning a Q-value (quality value) function, which estimates the expected utility (or future reward) of taking a particular action in a specific state and following a certain policy thereafter. The core concept is to find an optimal action-selection policy that maximizes the total reward over time.

Q-Value is updated using the formula:

![image](https://github.com/user-attachments/assets/ec49d511-712e-4ebd-b43c-508d02d522a9)





