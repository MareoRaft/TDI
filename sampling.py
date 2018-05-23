# pretend we have a population of 100 people, and each person has a height.  The heights are normally distributed with mean MEAN = 67 inches.  But WE THINK that the mean is actually m_guess = 63.  Then we draw a sample X of 10 people from the population.  Finally, we use the sample X to calculate the posterior distribution of people's heights.

import numpy as np
import scipy as sp

# GLOBALS
# p(T)
MEAN = 67
STD_DEV = 4
# other
NUM_PEOPLE = 100
NUM_SAMPLES = 10

# actual distribution
samples = np.random.normal(loc=MEAN, scale=STD_DEV, size=NUM_SAMPLES)

# p(T | X) = p(X | T) * p(T) / p(X)


# p(X)
sample_mean = np.mean(samples)
sample_std_dev = np.std(samples)

# p(X | T) = prod_j p(x_j | T)

# p(T | X) must be normal, since likelihood and prior distribution are normal.  Therefore, we need only find the mean and standard deviation.
# new mean is weighted average of old means
new_mean = (MEAN * (NUM_PEOPLE - NUM_SAMPLES) + sample_mean * NUM_SAMPLES) / NUM_PEOPLE
# new variance is the weighted average of the variances
new_variance = (STD_DEV**2 * (NUM_PEOPLE - NUM_SAMPLES) + sample_std_dev**2 * NUM_SAMPLES) / NUM_PEOPLE
new_std_dev = np.sqrt(new_variance)

# By identifying the mean and standard deviation of p(T | X), we have successfully identified p(T | X).
p_T_X = lambda x: sp.stats.norm.pdf(x, loc=new_mean, scale=new_std_dev)
