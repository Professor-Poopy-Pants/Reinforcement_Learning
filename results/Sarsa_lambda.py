import gym
import numpy as np
import random as rnd
import matplotlib.pyplot as plt
import gym_minigrid

Q={}
env = gym.make('MiniGrid-Empty-6x6-v0')
num_episodes = np.arange(0, 500)
alpha = 0.6
epsilon = 1.0
lamda = 0.5
epsilon_min = 0.01
epsilon_decay = 0.95
gamma = 0.9
count = []
rt = []
policy=[]

def epsilon_greedy_policy(state, Q, epsilon):
    if np.random.rand() < epsilon:
        return np.random.randint(0,3)
    else:
        return np.argmax(Q[state])

for i in range(len(num_episodes)):
    env.reset()
    total_reward = 0
    episode = []
    done = False
    steps = 0
    E={}
    state = (tuple(env.agent_pos), env.agent_dir)
    if state not in Q:
        Q[state]=np.zeros(3)
    if state not in E:
        E[state] = np.zeros(env.action_space.n)






    action = epsilon_greedy_policy(state, Q, epsilon)
    policy.append(action)
    while not done:
        next_obs_space, reward, done, truncated, info = env.step(action)
        next_state = (tuple(env.agent_pos), env.agent_dir)

        if next_state not in Q:
            Q[next_state] = np.zeros(env.action_space.n)
        if next_state not in E:
            E[next_state] = np.zeros(env.action_space.n)

        E[state][action] += 1
        next_action = epsilon_greedy_policy(next_state, Q, epsilon)
        delta = reward + gamma * Q[next_state][next_action] - Q[state][action]
        for s, actions in Q.items():
            for a in range(0,3):
                if s not in E:
                     E[s]=np.zeros(3)
                Q[s][a] += alpha * delta * E[s][a]
                E[s][a] *= gamma * lamda

        state = next_state
        action = next_action
        total_reward += reward
        steps += 1

        if steps == 70:
            break

    count.append(steps)
    rt.append(total_reward)

    if epsilon > epsilon_min:
        epsilon *= epsilon_decay

count = np.array(count)

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
