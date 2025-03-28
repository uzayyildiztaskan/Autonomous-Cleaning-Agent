from abc import ABC, abstractmethod

class Agent(ABC):
    def __init__(self, env):
        self.env = env
    
    @abstractmethod
    def decide_next_move(self):
        pass