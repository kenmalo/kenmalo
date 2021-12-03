# %%
import numpy as np
import matplotlib.pyplot as plt
# %%
num = 20
# two dimentional data array
data = np.random.rand(4, num)
print(data)
# %%
plt.scatter(data[0], data[1], c= data[2], s = data[3]*1000, aplha=0.3, cmap='viridis')
plt.colorbar() # show color scale
# %%
