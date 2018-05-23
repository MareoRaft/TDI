#!/usr/bin/env python3
# pretend we have a population of 100 people, and each person has a height.  The heights are normally distributed with mean MEAN_ACTUAL = 67 inches.  But WE THINK that the mean is m_guess = 63.  Then we draw a sample X of 10 people from the population.  Finally, we use the sample X to calculate the posterior distribution of people's heights.

import numpy as np
import scipy as sp

# GLOBALS
MEAN_ACTUAL = 67
STD_DEV_ACTUAL = 4
# p(T)
MEAN_GUESS = 63
STD_DEV_GUESS = 4
# other
NUM_PEOPLE = 100
NUM_SAMPLES = 10

# actual distribution
samples = np.random.normal(loc=MEAN_ACTUAL, scale=STD_DEV_ACTUAL, size=NUM_SAMPLES)

# p(T | X) = p(X | T) * p(T) / p(X)


# p(X)
mean_sample = np.mean(samples)
std_dev_sample = np.std(samples)

# p(X | T) = prod_j p(x_j | T)

# p(T | X) must be normal, since likelihood and prior distribution are normal.  Therefore, we need only find the mean and standard deviation.
# new mean is weighted average of old means
new_mean = (MEAN_GUESS * (NUM_PEOPLE - NUM_SAMPLES) + mean_sample * NUM_SAMPLES) / NUM_PEOPLE
# new variance is the weighted average of the variances
new_variance = (STD_DEV_GUESS**2 * (NUM_PEOPLE - NUM_SAMPLES) + std_dev_sample**2 * NUM_SAMPLES) / NUM_PEOPLE
new_std_dev = np.sqrt(new_variance)
print('new_mean = {}'.format(new_mean))
print('new_std_dev = {}'.format(new_std_dev))

# By identifying the mean and standard deviation of p(T | X), we have successfully identified p(T | X).
p_T_X = lambda x: sp.stats.norm.pdf(x, loc=new_mean, scale=new_std_dev)
