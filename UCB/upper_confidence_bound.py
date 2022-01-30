# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 14:12:27 2022

@author: kkakh
"""

# UCB reinforcement learning
# import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# importing dataset
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

# implimenting UCB
# Step 1
import math
N = 10000
d = 10
ads_selected = []
numbers_of_selections = [0]*d
Sums_of_rewards = [0]*d
total_reward = 0

# step 2
for n in range(0, N):
    ad = 0
    max_upper_bound = 0
    for i in range(0, d):
        if numbers_of_selections[i] > 0 :
            average_reward = Sums_of_rewards[i] / numbers_of_selections [i]
            delta_i = math.sqrt((3 / 2)* (math.log(n + 1)/ numbers_of_selections[i]))
            upper_bound = average_reward + delta_i
        else:
            upper_bound = 1e400
        if upper_bound > max_upper_bound:
            max_upper_bound = upper_bound
            ad = i
    ads_selected.append(ad)
    numbers_of_selections[ad] += 1
    reward = dataset.values[n][ad]
    Sums_of_rewards[ad] += reward
    total_reward += reward


# Visualising the result
plt.hist(ads_selected)
plt.title("histogram of ads selection")
plt.xlabel("Ads")
plt.ylabel("No of times ads selected")
plt.show()