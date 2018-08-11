#STEP 2: NONLINEAR CONVECTION

#importing libraries
#--------------------------------------
import numpy                      		#loads numpy
from matplotlib import pyplot as plt  #loads matplotlib

#declaring variables
#--------------------------------------
nx = 41          #number of grid points
dx = 2 / (nx-1)  #distance between adjacent pairs of gridpoints
nt = 25          #number of timesteps we want
dt = .025        #amount of time each timestep covers
c = 1            #assumes wavespeed of c=1

#defining array u
#-------------------------------------
u = numpy.ones(nx)                    #array with nx elements all equal to 1
u[int(.5 / dx):int(1 / dx + 1)] = 2   #setting u=2 between 0.5 and 1 
print(u)                                
plt.plot(numpy.linspace(0, 2, nx), u);

#calculation
#-------------------------------------
un = numpy.ones(nx)        #initializes an array
for n in range(nt):        #loops for values of n from 0 to number of timesteps
    un = u.copy()          #copies the values of u into the array
    for i in range(1, nx): #replaced constant c with un[i]
            u[i] = un[i] - un[i] * dt / dx * (un[i] - un[i-1])   
    plt.plot(numpy.linspace(0, 2, nx), u);
print(u)
plt.show()