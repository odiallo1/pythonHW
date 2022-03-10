"""
Script for homework 1
"""
import itertools
__author__ = "Oumar Diallo"
__pylint__ = "v2.12.2"
__version__ = "CS3270"

def main():
    """
    Displays all possible states for the Fox-Goose-Grain problem
    Args: none
    Returns
    """
    combinations = tuple(itertools.product(range(2), repeat= 4))
    states = list(combinations)
    print(states)
main()
