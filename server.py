import numpy as np
import gym
from pyrpc import Server

po = gym.make('PongDeterministic-v0')
server = Server(po)
server.run()
