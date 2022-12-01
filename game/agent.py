# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 22:06:50 2022

@author: Triagen
"""

from ..util import raiseNotDefined

class Agent:
    """
    An agent can take actions to solve the problem.
    """
    def __init__(self):
        pass
    
    def registerInitialState(self, state):
        """
        Register agent's initial state.

        """
        pass

    def getAction(self, state):
        """
        Next action the agent will take, according to the state.
        """
        raiseNotDefined()