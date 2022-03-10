import numpy as np

__author__ = "Oumar Diallo"
__version__ = "CS3270"
__pylint__ = "v2.12.2"

ALPHA = 0.1
GAMMA = 0.9
EPSILON = 0.1


'''
ask user for input
'''
episodes = input("Enter number of episodes: ")



def main(episodes):
    number_of_episodes = int(episodes)
    print(q_table)

if __name__ == '__main__':
    np.random.seed(0)
    main(episodes)
