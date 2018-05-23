
## What is a $t$-test?

A $t$-test is any hypothesis test in which the test statistic follows a Student's $t$-distribution.

The $t$-test is for normally distributed populations.  Consider we are in a situation where we know a population is normally distributed, but we don't know what the mean $\mu$ is.  Then a $t$-test is appropriate.

For example, our population could be men in Bolivia.  The value we are measuring could be height.  The $t$-test would be appropriate to our example because human heights are normally distributed.


## So what is $t$?

The $t$ in a $t$-test is a measure of ERROR!  In particular, assuming that our predicted mean $\mu$ is correct, it measures how bad our sample mean $X$ is.

$\displaystyle t=\frac{(X-\mu)}{\frac{s}{\sqrt{n}}}$

$\mu$ is the predicted mean.  $X$ is the sampled mean, $s$ is the sampled standard deviation, and $n$ is the number of data points sampled.

This is designed so that an accurate $\mu$ will lead to a small value of $t$!  Observe that if $\mu$ is close to $X$, $t$ gets smaller.  Assuming $\mu$ is accurate, we expect $X$ to get closer to $\mu$ as we sample more and more data points.  Therefore, we multiply by $\sqrt{n}$ to counterbalance this.  In order to have a "good fit," we need $\mu$ and $X$ to be *so close* that they beat the growth of $\sqrt{n}$!

For example, this [website](http://www.averageheight.co/average-male-height-by-country) says that the mean height of men in Bolivia is $\mu$=5'3" (or 64 inches), our predicted mean.  Now, we all take a flight down to Bolivia where we choose $n$ men at random and record their heights.  The mean $X$ of these heights is our sampled mean, and the standard deviation $s$ of these heights is our sampled standard deviation.




## And what is $p$?

How do we know when our error $t$ is small enough to conclude that our predicted $\mu$ was correct?  By convention, we choose a specific 'cut-off' where we conclude our $\mu$ was correct.  That is where $p$ comes into play...

"$p$-value" means "probability value".  Assuming that $\mu$ is the correct mean, $p$ is the probability of obtaining an error of $t$ or worse.

If $p$ is below $5\%$, this is bad news.  It means that if $\mu$ was correct, there was less than a $5\%$ chance of picking people with these heights.  In this situation, we conclude that our predicted mean was wrong.


## How do I calculate $p$?

Knowing $n$ and $t$ is enough information to calculate $p$.  We first calculate the number of degrees of freedom, which is simply $n-1$.  Then using the degrees of freedom and $t$, we can look up $p$ in a [table](http://www.sjsu.edu/faculty/gerstman/StatPrimer/t-table.pdf).

Note that the left column "df" is the degrees of freedom, and the values in the table are $t$-values.

In our example, we had $n-1 = 5-1 = 4$ degrees of freedom.  So we look at row $4$ in the table.  We also had a $t$-value of $3.7$.  We have to take the worst-case scenario and round our error ($t$-value) UP to the next $t$-value we see in the row, which is $3.747$.  Finally, we observe that the corresponding $p$-value is $0.01$, or $1\%$.

This is less than the $5\%$ cut-off, so unfortunately we must conclude that our predicted mean $\mu=63$ inches was WRONG.



## How are $t$ and $p$ related?

Recall that $t$ measures error, and $p$ measures the probability of obtaining such error (or worse) assuming $\mu$ is correct.

Then $t = 0$ must give a probability of $p = 100\%$.

As $t$ increases, $p$ must decrease.


## What is precision and recall?

Let's say our population is a bunch of frogs.  There is a certain probability that a randomly chosen frog will display the y gene, which is correlated to another gene.

*Precision*


Of those classified as Will return, what proportion actually did?
True positive / (True positive + False positive)

Recall: Of those that in fact Returned, what proportion were classified that way?
True positive / (True positive + False negative)


## Bayes' Rule

Let's say that

$\displaystyle A$

is some event that could occur (or not occur), and $B$ is some other event.  Then

$\displaystyle p(A)$

is the probability that $A$ occurs, and similarly $p(B)$ is the probability that $B$ occurs.  Now

$\displaystyle p(A , B)$

is the probability that both $A$ and $B$ occur.

$\displaystyle p(A \mid B)$

is the probability that $A$ occurs if we already know that $B$ occurs.  In other words, the probability of "$A$ given $B$".  Bayes rule is an equation involving these concepts, which we will soon derive.  One way to calculate the probability that $A$ and $B$ both occur is to take the probability that $A$ occurs, and now that we've chosen $A$ to occur, multiply by the probability that $B$ occurs given $A$ is already occuring:

$\displaystyle p(A , B) = p(A) \cdot p(B \mid A)$

Switching the roles of $B$ and $A$, we also have

$\displaystyle p(A , B) = p(B) \cdot p(A \mid B).$

Finally, we can set these equal to each other

$\displaystyle p(A) \cdot p(B \mid A) = p(B) \cdot p(A \mid B)$

and if we'd like, solve for $p(A \mid B)$:

$\displaystyle p(A \mid B) = \frac{p(A) \cdot p(B \mid A)}{p(B)}.$

This final equation is known as Bayes' Rule.


## What is Posterior sampling?

Firstly, what is the 'posterior distribution'?

Let $t$ represent some information about our population, say, the mean height.

We have an initial *predicted* distribution $p(t)$, and then we draw some sample data $X$ from our population.  The idea of 'posterior' is to get better preditions about our population *after* (hence, 'post') having seen some sample data $X$ from it.  We use Bayes formula:

$\displaystyle p(t \mid X) = \frac{p(t) \cdot p(X \mid t)}{p(X)}$

which is not only true for probabilities, but for probability density functions / distributions:

$\displaystyle p(t \mid X) = \frac{p(t) \cdot p(X \mid t)}{p(X)}$

Here, $p(t \mid X)$ represents is the 'posterior distribution', which is the new best guess of the distribution of our population, thanks to the information $X$.  As you can see $p(t \mid X)$ takes into account the original predicted distribution $p(t)$ as well as information about $X$.










Resources Used in the making of this tutorial
-----------------------------------------------
https://en.wikipedia.org/wiki/Student%27s_t-test
https://en.wikipedia.org/wiki/Bayes%27_theorem
http://www.sjsu.edu/faculty/gerstman/StatPrimer/t-table.pdf
https://en.wikipedia.org/wiki/Student%27s_t-distribution
https://en.wikipedia.org/wiki/p-value
http://www.averageheight.co/average-male-height-by-country
https://www.youtube.com/watch?v=EHqU9LE9tg8
