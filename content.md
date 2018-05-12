









A t-test is any hypothesis test in which the test statistic follows a Student's t-distribution.


The t-test is for normally distributed populations.  Consider we are in a situation where we know a population is normally distributed, but we don't know what the mean u is or what the st dev sigma is.

Create an example here.  population is ppl from a specific nation.  and ppl for anOTHER nation.  Measured value is 1 dimensional: height.  We want to know if they have the same height as each other, or something.  Then while we teach it, we keep returning to our example.

or it could be TWO populations and we want to see if their mean and sd are the same.


t is a measure of ERROR!


{\displaystyle t={\frac {Z}{s}}={\left({\bar {X}}-\mu \right)\left/\left({\frac {\sigma }{\sqrt {n}}}\right)\right.}}


u is the predicted mean and sigma is the predicted standard deviation.  X is the sampled mean and n is the number of data points sampled.

This is designed so that an accurate u will lead to a small value of t!  Observe that if u is close to X, t gets smaller.  Assuming u is accurate, we expect X to get closer to u as we sample more and more data points.  Therefore, we multiply by sqrt(n) to counterbalance this.  In order to have a "good fit", we need u and X to be *so close* that they beat the growth of sqrt(n)!


see "One-sample t-test" under "Calculations" in wiki

How do we know when t is small enough to conclude that our predicted u was correct?



Resources Used
-------------------
https://en.wikipedia.org/wiki/Student%27s_t-test
