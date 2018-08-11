#STEP 3: DIFFUSION

import numpy              			   
from matplotlib import pyplot as plt 

#declaring variables
#--------------------------------------
nx = 41                 #number of grid points
dx = 2 / (nx - 1)       #distance between adjacent pairs of gridpoints
nt = 20                 #the number of timesteps we want to calculate
nu = 0.3                #value of viscosity
sigma = .2              #parameter
dt = sigma * dx**2 /nu  #defining dt using sigma
print(dt)

#assigning initial conditons using a hat function
#--------------------------------------
u = numpy.ones(nx)                   #array with nx elements all equal to 1
u[int(.5 / dx):int(1 / dx + 1)] = 2  #setting u = 2 between 0.5 and 1

#calculation
#-------------------------------------
un = numpy.ones(nx)       #initializes an array
for n in range(nt):       #loops for values of n from 0 to number of timesteps
    un = u.copy()         #copies the values of u into the array
    for i in range(1, nx - 1):
        u[i] = un[i] + nu * dt / dx**2 * (un[i+1] - 2 * un[i] + un[i-1])
    plt.plot(numpy.linspace(0, 2, nx), u);
plt.show();