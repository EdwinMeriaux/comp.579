import gym
import numpy as np

env = gym.make('FrozenLake-v1', desc=["SFFF", "FHFH", "FFFH", "HFFG"], map_name="4x4", is_slippery=False)
state = env.reset()
env.render()
action = 0
obs, reward, terminated, truncated, info = env.step(action)
print(env.step(action))
action = 2
obs, reward, terminated, truncated, info = env.step(action)
print(env.step(action))
action = 2
obs, reward, terminated, truncated, info = env.step(action)
print(env.step(action))


action = 1
obs, reward, terminated, truncated, info = env.step(action)
print(env.step(action))
action = 1
obs, reward, terminated, truncated, info = env.step(action)
print(env.step(action))
print(env.action_space)