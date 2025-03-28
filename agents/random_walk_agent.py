import numpy as np
from agents.agent import Agent

class RandomWalkAgent(Agent):
    def decide_next_move(self):
        current_pos = self.env.agent_pos
        neighbors = self.env.get_traversable_neighbors(current_pos)
        if not neighbors:
            return None
        return neighbors[np.random.choice(len(neighbors))]