from abc import ABC, abstractmethod


class Equation(ABC):
    @abstractmethod
    def solve(self):
        pass
    @abstractmethod    
    def analyze(self):
        pass
        
class LinearEquation(Equation):
    def solve(self):
        pass
    def analyze(self):
        pass


