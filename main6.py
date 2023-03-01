import numpy as np
import matplotlib.pyplot as plt
import math

N = 400 #neroun sheet num
mat_map = np.zeros((N, N))
mat_speed = np.zeros((N, N))

unit_speed = 0.1

pos_x = np.zeros(40000)
pos_y = np.zeros(40000)
for i in range(19999):
    pos_x[i+1] = pos_x[i] + 10 #np.random.random()*N*0.001
    pos_y[i+1] = pos_y[i] + 10 #np.random.random()*N*0.001
    
#map test

def filter(x, y):
    global N
    a = 1
    beta = 3/(169)
    gamma = 1.05*beta
    for i in range(x-30, x+30):
        for j in range(y-30, y+30):
            r = np.hypot(x-i, y-j)
            mat_map[int(i%N-1), int(j%N-1)] += a*math.exp(-gamma*abs(r)*abs(r)) - math.exp(-beta*abs(r)*abs(r))
x = y = 200
plt.ion()
fig, ax = plt.subplots(1, 1)

for i in range(15000):
    length = 60
    theta = np.random.rand()*2*np.pi
    x += int(length*np.cos(theta))
    y += int(length*np.sin(theta))
    filter(x, y)
    
    ax.cla()
    ax.matshow(mat_map)
    fig.canvas.draw()
    fig.canvas.flush_events()
    plt.pause(0.01)
            
    