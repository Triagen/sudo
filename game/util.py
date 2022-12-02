# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 22:10:27 2022

@author: Triagen
"""
import sys
import inspect


def raise_not_defined():
    """
    Whenever a class has methods to defined by subClass, use this method for
    method not defined exception.

    Returns
    -------
    None.

    """
    file_name = inspect.stack()[1][1]
    line = inspect.stack()[1][2]
    method = inspect.stack()[1][3]

    print("*** Method not implemented: %s at line %s of %s" %
          (method, line, file_name))
    sys.exit(1)
