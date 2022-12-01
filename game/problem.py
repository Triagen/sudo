# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 22:40:51 2022

@author: Triagen
"""
from ..util import raiseNotDefined

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Get the start state of the problem.

        Returns
        -------
        The start state of the problem.

        """
        raiseNotDefined()

    def isGoalState(self, state)->bool:
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
        raiseNotDefined()

    def getSuccessors(self, state)->list:
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
        raiseNotDefined()

    def getCostOfActions(self, actions)->int:
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
        raiseNotDefined()