#!/usr/bin/env python3
# pretend we have a population of 100 people, and each person has a height.  The heights are normally distributed with mean MEAN_ACTUAL = 67 inches.  But WE THINK that the mean is m_guess = 63.  Then we draw a sample X of 10 people from the population.  Finally, we use the sample X to calculate the posterior distribution of people's heights.

import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from scipy import stats

# GLOBALS
MEAN_ACTUAL = 67
STD_DEV_ACTUAL = 4
# p(T)
MEAN_GUESS = 63
STD_DEV_GUESS = 4
# other
NUM_SAMPLES = 10

# p(T | X) = p(X | T) * p(T) / p(X)

# plot setup
plt.xlabel('mean')
plt.ylabel('probability density')
x_ = np.arange(30, 90, 0.2)


# prior distribution:
# p(T)
def p_T(x):
	return sp.stats.norm.pdf(x, loc=MEAN_GUESS, scale=STD_DEV_GUESS)
y_ = [p_T(x) for x in x_]
plt.plot(x_, y_, 'r')

# actual distribution:
def p_true(x):
	return sp.stats.norm.pdf(x, loc=MEAN_ACTUAL, scale=STD_DEV_ACTUAL)
y_ = [p_true(x) for x in x_]
plt.plot(x_, y_, 'g')

# likelihood:
# p(X | T) = prod_j p(x_j | T)

# take some samples from the actual distribution
samples = np.random.normal(loc=MEAN_ACTUAL, scale=STD_DEV_ACTUAL, size=NUM_SAMPLES)
mean_samples = np.mean(samples)
std_dev_samples = np.std(samples)

# p(X)
# is just a constant when we consider the mean T to be the variable.

# p(T | X)
# must be normal, since likelihood and prior distribution are normal.  Therefore, we need only find the mean and standard deviation.
variance_new = 1 / (1/STD_DEV_GUESS**2 + NUM_SAMPLES * 1/std_dev_samples**2)
std_dev_new = np.sqrt(variance_new)
mean_new = variance_new * (MEAN_GUESS/STD_DEV_GUESS**2 + NUM_SAMPLES * mean_samples/std_dev_samples**2)
def p_T_X(x):
	return sp.stats.norm.pdf(x, loc=mean_new, scale=std_dev_new)
y_ = [p_T_X(x) for x in x_]
plt.plot(x_, y_, 'b')

# output
print('new mean = {}'.format(mean_new))
print('new std dev = {}'.format(std_dev_new))
plt.show()

