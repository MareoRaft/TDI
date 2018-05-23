
## What is a t-test?

A t-test is any hypothesis test in which the test statistic follows a Student's t-distribution.


The t-test is for normally distributed populations.  Consider we are in a situation where we know a population is normally distributed, but we don't know what the mean u is or what the st dev sigma is.  Then a t-test is appropriate.

For example, our population could be men in Bolivia.  The value we are measuring could be height.  The t-test would be appropriate to our example because human heights are normally distributed.


## So what is t?

The $t$ in a t-test is a measure of ERROR!  In particular, assuming that our predicted mean u is correct, it measures how bad our sample mean X is.


$\displaystyle t=\left({\bar {X}}-\mu \right)\left/\left({\frac {\sigma }{\sqrt {n}}}\right)\right$


u is the predicted mean.  X is the sampled mean, s is the sampled standard deviation, and n is the number of data points sampled.

This is designed so that an accurate u will lead to a small value of t!  Observe that if u is close to X, t gets smaller.  Assuming u is accurate, we expect X to get closer to u as we sample more and more data points.  Therefore, we multiply by sqrt(n) to counterbalance this.  In order to have a "good fit", we need u and X to be *so close* that they beat the growth of sqrt(n)!

For example, this [website](http://www.averageheight.co/average-male-height-by-country) says that the mean height of men in Bolivia is u=5'3" (or 64 inches), our predicted mean.  Now, we all take a flight down to Bolivia where we choose n men at random and record their heights.  The mean X of these heights is our sampled mean, and the standard deviation s of these heights is our sampled standard deviation.


see "One-sample t-test" under "Calculations" in wiki


## And what is p?

How do we know when our error t is small enough to conclude that our predicted u was correct?  By convention, we choose a specific 'cut-off' where we conclude our u was correct.  That is where `p` comes into play...

p-value means probability value.  Assuming that u is the correct mean, p is the probability of obtaining an error of t or worse.

If `p` is below 5%, this is bad news.  It means that if u was correct, there was less than a 5% chance of picking people with these heights.  In this situation, we conclude that our predicted mean was wrong.


## How do I calculate p?

Knowing n and t is enough information to calculate p.  We first calculate the number of degrees of freedom, which is simply n-1.  Then using the degrees of freedom and t, we can look up p in a [table](http://www.sjsu.edu/faculty/gerstman/StatPrimer/t-table.pdf).

Note that the left column "df" is the degrees of freedom, and the values in the table are t-values.

In our example, we had n-1 = 5-1 = 4 degrees of freedom.  So we look at row 4 in the table.  We also had a t-value of 3.7.  We have to take the worst-case scenario and round our error (t-value) UP to the next t-value we see in the row, which is 3.747.  Finally, we observe that the corresponding p-value is 0.01, or 1%.

This is less than the 5% cut-off, so unfortunately we must conclude that our predicted mean u=63 inches was WRONG.



## How are t and p related?

Recall that t measures error, and p measures the probability of obtaining such error (or worse) assuming u is correct.

Then t = 0 must give a probability of p = 100%.

As t increases, p must decrease.


## How do t-tests relate to precision recall?

Precision:

Of those classified as Will return, what proportion actually did?
True positive / (True positive + False positive)
Recall:

Recall: Of those that in fact Returned, what proportion were classified that way?
True positive / (True positive + False negative)


## Bayes' Rule

Let's say that

A

is some event that could occur (or not occur), and B is some other event.  Then

P(A)

is the probability that A occurs, and similarly P(B) is the probability that B occurs.  Now

P(A and B)

is the probability that both A and B occur.

P(A | B)

is the probability that A occurs if we already know that B occurs.  In other words, the probability of "A given B".  Bayes rule is an equation involving these concepts, which we will soon derive.  One way to calculate the probability that A and B both occur is to take the probability that A occurs, and now that we've chosen A to occur, multiply by the probability that B occurs given A is already occuring:

P(A and B) = P(A) P(B | A)

Switching the roles of B and A, we also have

P(A and B) = P(B) P(A | B).

Finally, we can set these equal to each other

P(A) P(B | A) = P(B) P(A | B)

and if we'd like, solve for P(A | B):

P(A | B) = P(A) P(B | A) / P(B).

This final equation is known as Bayes' Rule.


## What is Posterior sampling?

Firstly, what is the 'posterior distribution'?

Let T represent some information about our population, say, the mean height.

We have an initial *predicted* distribution p(T), and then we draw some sample data X from our population.  The idea of 'posterior' is to get better preditions about our population *after* (hence, 'post') having seen some sample data X from it.  We use Bayes formula:

P(T | X) = P(T) P(X | T) / P(X)

which is not only true for probabilities, but for probability density functions / distributions:

p(T | X) = p(T) p(X | T) / p(X)

Here, p(T | X) represents is the 'posterior distribution', which is the new best guess of the distribution of our population, thanks to the information X.  As you can see p(T | X) takes into account the original predicted distribution p(T) as well as information about X.










Resources Used in the making of this tutorial
-----------------------------------------------
https://en.wikipedia.org/wiki/Student%27s_t-test
https://en.wikipedia.org/wiki/Bayes%27_theorem
http://www.sjsu.edu/faculty/gerstman/StatPrimer/t-table.pdf
https://en.wikipedia.org/wiki/Student%27s_t-distribution
https://en.wikipedia.org/wiki/P-value
http://www.averageheight.co/average-male-height-by-country
https://www.youtube.com/watch?v=EHqU9LE9tg8
