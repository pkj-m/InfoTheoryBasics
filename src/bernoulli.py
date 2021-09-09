import random

'''
Returns the result of n iid Bernoulli trials
with probability of success = p
'''
def bernoulliIID(n, p = 0.5):
    return [int(random.uniform(0, 1) < p) for _ in range(n)]
