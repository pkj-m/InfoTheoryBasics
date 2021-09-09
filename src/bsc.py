import numpy as np
import random

'''
Simulates transmission of a binary string through 
a binary symetric channel with error probability 
of flipping equal to p
'''
def bsc(inp, p = 0.5):
    n = len(inp)
    noise = [int(random.uniform(0, 1) < p) for _ in range(n)]
    return [(x + y) % 2 for x, y in zip(inp, noise)]
    


def test_bsc():
    print("Enter size of input: ")
    n = int(input())

    x = []
    for i in range(n):
        c = int(input())
        x.append(c)

    print("\nEnter BSC error probability: ")
    p = float(input())

    print("Sending the input through BSC with prob = ", p)

    out = BSC(x, p)

    print("Input: ", x)
    print("Output: ", out)