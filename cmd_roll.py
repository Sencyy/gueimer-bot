# cmd_roll.py
import random

def roll():
    random.seed(None, 2)
    return(random.randrange(1, 101))