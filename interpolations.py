import matplotlib.pyplot as plt
import numpy as np
#get_ipython().run_line_magic('matplotlib', 'notebook') #commented out since it's not necessary when running the .py as module 

methods = [None, 'none', 'nearest', 'bilinear', 'bicubic', 'spline16',
           'spline36', 'hanning', 'hamming', 'hermite', 'kaiser', 'quadric',
           'catrom', 'gaussian', 'bessel', 'mitchell', 'sinc', 'lanczos']

# Fixing random state for reproducibility
np.random.seed(19680801)

grid = np.random.rand(6, 6) #inreased the sample image size slightly

fig, axs = plt.subplots(nrows=3, ncols=6, figsize=(9, 6),
                        subplot_kw={'xticks': [], 'yticks': []})

for ax, interp_method in zip(axs.flat, methods):
    ax.imshow(grid, interpolation=interp_method, cmap='terrain') #tried out a different color map
    ax.set_title(str(interp_method))

plt.tight_layout()
plt.show()




