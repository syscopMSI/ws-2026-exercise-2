"""
This is the template for coding tasks in exercise sheet 2.

Everywhere you see "YOUR CODE", it means a playground for you :P

WARNING: do not rename variables as this will break the tests.
=============================================================================================================================

Through this exercise, you will deal with some parameter estimation problem, and get the feel of modelling.

There is one NumPy function that can ease your process of calculation with linear model:
    <https://numpy.org/doc/stable/reference/generated/numpy.sum.html>

There are also two other functions used in the template to deal with the 3rd-order polynomial:
    <https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html>
    <https://numpy.org/doc/stable/reference/generated/numpy.polyval.html>

Have fun!
"""
## PREPARATIONS

import matplotlib.pyplot as plt
import numpy as np

# the figure for plotting everything
plt.figure(1)
plt.xlim([0,100])
plt.ylim([0,50])
plt.xlabel(r"Temperature - $ T(k)$")
plt.ylabel(r"Length of steel bar - $L(k)$")

# to be used only in plotting a line
T_line = np.linspace(0, 100)


## (a)
# YOUR CODE: Plot the ∆T (k), L(k) relation using ’x’ markers.
# "None" is just to pass the syntax check. Replace them with your code. Don't need to stick to a single line.
# (The same holds for all the following cases)

# datapoints from measurement
T = np.array(None)
L = None

# (a) Plot the data
plt.plot(None)




# (b) YOUR CODE: Calculate the experimental values of theta_1 and A:
# WARNING: do not rename variables this will break the tests!

# calculate the values
theta_1_opt = None
theta_2_opt = None

# for plotting:
L_1d = theta_1_opt * T_line + theta_2_opt
plt.plot(T_line, L_1d, "g")


# (c) YOUR CODE: Fit third order polynomial to data
# WARNING: do not rename variables this will break the tests!

# finde the poly coefficinets using polyfit
poly_coeffs = np.polyfit(None)

# evaluate the polynomial with over the interval
L_3d = np.polyval(None)

# plot the fit
plt.plot(None)


# (d) YOUR CODE: Validate fits with additional measurement
T_val = None
L_val = None

plt.plot(T_val, L_val, "x")


plt.legend(["original dataset","first order fit","third order fit","validation datapoint"])

# show all plots
# ===============
# If you don't see any plots but also no errors, it is very likely because a non-interactive backend is chosen by default.
# One possible solution you can try is to manually select another backend via "matplotlib.use()" function at the beginning.
# Here gives more details: <https://matplotlib.org/stable/users/explain/backends.html>
plt.show()
