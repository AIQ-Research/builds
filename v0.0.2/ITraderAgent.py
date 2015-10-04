from abc import ABCMeta, abstractmethod

class ITraderAgent:
    __metaclass__ = ABCMeta

    @abstractmethod
    def start_episode(self, observation): pass

    @abstractmethod
    def step(self, reward, observation): pass

    @abstractmethod
    def end_episode(self, reward, terminal=True): pass