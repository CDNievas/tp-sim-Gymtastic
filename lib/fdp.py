import math
import random

def IA(fin_de_semana):
    if fin_de_semana:
        return 5
    else:
        r = random.random()
        return (2 / math.pow((1/r-1),(1/207)) + 207)/60

def TA(fin_de_semana):
    return 60 if random.randint(0,100) <= 75 else 75