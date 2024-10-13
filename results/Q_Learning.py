import gym
import numpy as np
import random as rnd
import matplotlib.pyplot as plt


import gym_minigrid

Q={}
env = gym.make('MiniGrid-Empty-6x6-v0')
num_episodes =np.array(range(0,500))
alpha = 0.6
epsilon = 1.0
epsilon_min=0.01
epsilon_decay=0.995
policy=[]
gamma=0.9
count=[]
rt=[]

def epsilon_greedy_policy(state, Q, epsilon):

    if np.random.rand() < epsilon:
        return np.random.randint(0,3)  # Random action
    else:
        return np.argmax(Q[state])
        






for i in range(len(num_episodes)):

    env.reset()
    episode = []
    done = False
    steps = 0
    total_reward=0
    while not done:
        state = (tuple(env.agent_pos), env.agent_dir)
        while state not in Q:
            Q[state]=np.zeros(3)
        action = epsilon_greedy_policy(state, Q, epsilon)
        policy.append(action)

        next_obs_space, reward, done, truncated, info = env.step(action)
        next_state=(tuple(env.agent_pos),env.agent_dir)
        while next_state not in Q:
            Q[next_state]=np.zeros(3)
        best_next_action = np.argmax(Q[next_state])
        Q[state][action] += alpha * (reward + gamma * Q[next_state][best_next_action] - Q[state][action])

        state = next_state
        steps += 1
        total_reward += reward

        if steps == 70:

            break
        if done:
            print(f"Episode finished at step {steps}")

            state=next_state
            break

    count.append(steps)
    rt.append(total_reward)
    if epsilon > epsilon_min:
        epsilon *= epsilon_decay


    print(Q)

count=np.array(count)

fig, axs = plt.subplots(2, 1, figsize=(15, 10))

# Plot Steps per Episode
axs[0].plot(num_episodes, count)
axs[0].set_xlabel('Episode')
axs[0].set_ylabel('Steps')
axs[0].set_title('Steps per Episode')

# Plot Return per Episode
axs[1].plot(num_episodes, rt)
axs[1].set_xlabel('Episode')
axs[1].set_ylabel('Return')
axs[1].set_title('Return per Episode')

plt.tight_layout()
plt.show()
