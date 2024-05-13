import random
prob = random.random()
print(prob) # prints the probability between zero and one randomly
probint = random.randint(1,6)# returns the value between 1 and 6
print(probint) # prints any value between 1 and 6 including both numbers


import numpy as np
Ran_matrix = np.random.randint(1,6,(10,10))
print(Ran_matrix) # prints 10*10 matrics with value between 1 and 6, both inclusive