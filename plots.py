# import all necessary modules here
import numpy as np
import math
import matplotlib.pyplot as plt

# Variables for generating inputs and targets
numSamples = 8 # number of sample points
numDim = 1 # input dimensions

# Generate Inputs and Targets here
X = [i-5 for i in range(10)] ## Inputs
Y_true = [i**2 for i in X] # Targets

plt.plot(X,Y_true)
plt.xlabel("Inputs")
plt.ylabel("Targets")
plt.title('Ground Truth')
plt.show()
