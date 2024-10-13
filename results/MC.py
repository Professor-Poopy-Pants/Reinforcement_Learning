import gym
import numpy as np
import random as rnd
import matplotlib.pyplot as plt


import gym_minigrid
Q={}
env = gym.make('MiniGrid-Empty-6x6-v0')
num_episodes =np.array(range(0,50))
alpha = 0.6
epsilon = 1.0
policy=[]
gamma=0.9
count=[]
rt=[]

def epsilon_greedy_policy(state, Q, epsilon):

    if np.random.rand() < epsilon:
        return np.random.randint(0,3)  
    else:
        return np.argmax(Q[state])
       

def updated_Q(episode):
    return_value=0

    t= len(episode)-1
    while t>=0:
       state, r, a, done, next_obs_space=episode[t]
       return_value = (gamma*return_value) + r
       if state in Q:
          Q[state][a] += alpha * (return_value - Q[state][a]) #updates the Q-Value
       t=t-1
    rt.append(return_value)




for i in range(len(num_episodes)):
    env.reset()
    episode = []
    done = False
    steps = 0
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
        episode.append((state, reward, action, done,next_obs_space))
        steps += 1
        if steps == 70:
            count.append(70)
            break
        if done:
            print(f"Episode finished at step {steps}")
            count.append(steps)
            state=next_state

    if(epsilon>0.01):
      epsilon=epsilon*0.90

    updated_Q(episode)
    print(Q)
count=np.array(count)

plt.subplot(2,1,1)
plt.plot(num_episodes, count)
plt.xlabel('Episode')
plt.ylabel('Steps')
plt.title('Steps / Episode')

plt.show()
plt.subplot(2,1,2)
plt.plot(num_episodes,rt)
plt.xlabel('Episode')
plt.ylabel('return')
plt.title('Return / Episode')

plt.show()

