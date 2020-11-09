"""
=============
Figimage Demo (courtesy of Matplotlib.org, modified by KWE)
=============

This illustrates placing images directly in the figure, with no Axes objects.

"""
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


fig = plt.figure()
Z = np.arange(5000).reshape((50, 100))
Z[:, 20:] = 3

im1 = fig.figimage(Z, xo=50, yo=0, origin='lower')
im2 = fig.figimage(Z, xo=100, yo=100, alpha=.8, origin='lower')
im2 = fig.figimage(Z, xo=250, yo=250, alpha=2.3, origin='lower')

plt.show()

