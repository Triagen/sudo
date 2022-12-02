# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 22:06:50 2022

@author: Triagen
"""

from . import util


class Agent:
    """
    An agent can take actions to solve the problem.
    """

    def __init__(self):
        pass

    def reigster_initial_state(self, state):
        """
        Register agent's initial state.

        """
        util.raise_not_defined()

    def get_action(self, state):
        """
        Next action the agent will take, according to the state.
        """
        util.raise_not_defined()
