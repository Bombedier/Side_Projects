import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import pylab
import time

def pi_calc_inst(iterations, speed=20, interact=False, plot=True):
    '''
    Derives pi using Monte Carlo over a unit square
    Higher the iterations, the more accurately pi can be calculated
    '''
    x = np.random.rand(iterations)
    y = np.random.rand(iterations)

    if plot == True:
        xc = np.sin(np.arange(0, 2*np.pi, 0.01))/2
        yc = np.cos(np.arange(0, 2*np.pi, 0.01))/2
        plt.rc('text', usetex=True)
        fig = plt.scatter(x, y)
        plt.xlabel(r'x random numbers, $~N[0,1)$')
        plt.ylabel(r'y random numbers, $~N[0,1)$')
        plt.axis('square')
        plt.xlim(0,1)
        plt.ylim(0,1)
        plt.plot(xc+0.5, yc+0.5, '-r')
        plt.show()
    
    count = 0
    for i in range(iterations):
        if (x[i]-0.5)**2 + (y[i]-0.5)**2 < 0.25:
            count += 1

    area = count/iterations
    calc_pi = area/0.25
    print(calc_pi)

  # if interact == True:
   #     xr=[]
    #    yr=[]
     #   anim = animation.FuncAnimation(fig, update_plot, frames=iterations, interval=speed)
    
def update_plot(iterations, x, y, graph):
    xr.append(np.random.rand(1))
    yr.append(np.random.rand(1))


pi_calc_inst(1000000, plot=True)