import matplotlib.pyplot as plt
import numpy as np
rng = np.random.RandomState(1)
x = rng.randn(100)
y = rng.randn(100)
colors = rng.randn(100)
sizes = 1000 * rng.randn(100)

# alpha = 0.3
#cmap = color map = viridis
plt.scatter(x,y,c=colors,s=sizes, alpha=0.3, cmap='viridis')
#show color scale using plt.colorbar()
# plt.colorbar()