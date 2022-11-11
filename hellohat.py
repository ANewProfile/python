import matplotlib.pyplot as plt
import numpy as np
# import random
# num = random.randint(0, 5)
rng = np.random.RandomState(0)
x = rng.randn(100)
y = rng.randn(100)


fig, ax = plt.subplots()
plt.scatter(x,y)
plt.show()