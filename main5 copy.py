import numpy as np
import matplotlib.pyplot as plt
import math
from numpy import matlib as mb
import time

def mormal(mat):
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            if mat[i, j]<0.05:
                mat[i, j]=0
    return mat

def my_laplacian(In):
    Out = -1.0 * In + 0.20*(np.roll(In,1,axis=1)+np.roll(In,-1,axis=1)+np.roll(In,1,axis=0)+np.roll(In,-1,axis=0) ) + \
          0.05*(np.roll(np.roll(In,1,axis=0),1,axis=1)+np.roll(np.roll(In,-1,axis=0),1,axis=1)+np.roll(np.roll(In,1,axis=0),-1,axis=1)+np.roll(np.roll(In,-1,axis=0),-1,axis=1))
    return Out

tau_1 = 0.2
tau_2 = 0.1
d_activate = 0.7
d_deactivate = 0.5
dt = 0.25
width = 128
stoptime = 10000.0
k = 0.05

#mat_activate = np.random.random(size=(width, width))
#mat_deactivate = np.random.random(size=(width, width))
mat_activate = np.zeros((width, width))
mat_deactivate = np.zeros((width, width))
for i in range(width):
    for j in range(width):
        if math.hypot(i-width/2, j-width/2)<5:
            mat_activate[i, j] = 1
t=0

mat_a_old = mat_activate
mat_d_old = mat_deactivate

plt.ion()
fig, ax = plt.subplots(1, 2)

while t<stoptime:
    mat_a_new = mat_a_old + (d_activate*my_laplacian(mat_a_old)-mat_d_old)*dt/tau_1
    mat_d_new = mat_d_old + (d_deactivate*my_laplacian(mat_d_old)+mat_a_old-k*mat_d_old)*dt/tau_2
    
    mat_a_new = mormal(mat_a_new)
    
    mat_a_old = mat_a_new
    mat_d_old = mat_d_new
    t += dt
    print(t)
    ax[0].cla()
    ax[0].matshow(mat_a_old)
    ax[1].cla()
    ax[1].matshow(mat_d_old)
    #plt.pause(0.01)
    fig.canvas.draw()
    fig.canvas.flush_events()
    plt.pause(0.01)
