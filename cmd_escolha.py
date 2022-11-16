# cmd_escolha.py
import random

def escolha(esc1, esc2):
    random.seed(None, 2)
    escnum = random.randrange(0, 2)
    if escnum == 0:
        escres = esc1
    
    if escnum == 1:
        escres = esc2

    return(escres)