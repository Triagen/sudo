# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 22:40:51 2022

@author: Triagen
"""
from . import util


class Problem:
    """
    A problem has a startState, successors of any particular state,
    a goalState and costs of any actions.
    """

    def get_start_state(self):
        """
        Get the start state of the problem.

        Returns
        -------
        The start state of the problem.

        """
        util.raise_not_defined()

    def is_goal_state(self, state) -> bool:
        """
        Returns True if and only if the state is a valid goal state.

        Parameters
        ----------
        state : TYPE
            A particular state.

        Returns
        -------
        bool
            Whether the state is a valid goal state or not.

        """
        util.raise_not_defined()

    def get_successors(self, state) -> list:
        """
        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.

        Parameters
        ----------
        state : TYPE
            A particular state.

        Returns
        -------
        list
            A list of successor to the current state.

        """
        util.raise_not_defined()

    def get_cost_of_actions(self, actions) -> int:
        """
        This method returns the total cost of a particular sequence of actions.

        Parameters
        ----------
        actions : TYPE
            A list of actions to take.

        Returns
        -------
        int
            The total cost of actions.

        """
        util.raise_not_defined()
