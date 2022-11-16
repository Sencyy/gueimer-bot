# pergunta.py
import random

def pergunta(seed):
    random.seed(seed, 2)
    rndnum = random.randrange(0, 2)
    if rndnum == 0:
        resposta = "sim"
    if rndnum == 1:
        resposta = "não"
    return(resposta)
