#!/bin/env python3

import numpy as np

import matplotlib.colors
import matplotlib.pyplot as plt

data = np.load('data.npy')
x_list = np.array(list(map(list, zip(*data))))

dist_list = ['uniform','exponential', 'lognormal','normal 1','normal 2','normal 3']
colors_list = ['green','blue','yellow','cyan','magenta','pink']

fig,ax = plt.subplots(nrows=2, ncols=3,figsize=(12,7))
plt_ind_list = np.arange(6)+231

for dist, x, plt_ind, colors in zip(dist_list, x_list, plt_ind_list, colors_list):
    print(f'-------- {dist} --------')
    print(f'mean: {np.mean(x)}')
    print(f'standard deviation: {np.std(x)}')

    plt.subplot(plt_ind)
    plt.hist(x,bins=50,color=colors)
    plt.title(dist)

print('======= correlations between normal 1, 2, and 3 ========')
print(np.corrcoef(x_list[3:]))

fig.subplots_adjust(hspace=0.4,wspace=.3) 
plt.suptitle('Sampling from Various Distributions',fontsize=20)
plt.show()
