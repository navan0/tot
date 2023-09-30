
**Sample Space:**
- Definition: The sample space (Ω) is the set of all possible outcomes of a random experiment.
- Example: For a coin flip, Ω = {Heads, Tails}. For a six-sided die roll, Ω = {1, 2, 3, 4, 5, 6}.
- Importance: It defines all potential outcomes in a probabilistic context.

**Events:**
- Definition: Events are subsets of the sample space, representing specific outcomes or sets of outcomes.
- Example: In a die roll, "rolling an even number" corresponds to the event {2, 4, 6}.
- Importance: Events allow us to specify what we want to analyze or predict in probability.

**Outcomes:**
- Definition: Outcomes are individual results of an experiment, belonging to the sample space.
- Example: When flipping a coin, "Heads" or "Tails" in one flip is an outcome.
- Importance: Outcomes form the building blocks of the sample space and probability calculations.

**Probability Notation:**
- P(A): Probability of event A.
  - Example: P(Heads) is the probability of getting heads in a coin flip.

- P(A | B): Conditional probability of A given B.
  - Example: P(Heads | Tails) is the probability of heads in a coin flip given the previous flip was tails.

- P(A and B): Joint probability of both A and B occurring.
  - Example: P(Heads and Tails) is the probability of getting both heads and tails in consecutive coin flips.

- P(A or B): Probability of either A or B occurring (inclusive OR).
  - Example: P(Heads or Tails) is the probability of getting either heads or tails in a single coin flip.

- P(not A): Probability of the complement of A (A not occurring).
  - Example: P(not Heads) is the probability of not getting heads in a coin flip.

**Real-Life Example (Weather Forecasting):**
- In weather forecasting, the sample space includes weather conditions (sunny, rainy, cloudy).
- Events could be "rain tomorrow."
- Conditional probability might be the probability of rain given today's cloudy skies.


# Probability Distribution Functions

Introduction:
- Probability Distribution Functions (PDFs) are fundamental concepts in probability theory and statistics.
- They describe how probabilities are distributed over different values in a random variable.
- PDFs are used to model and analyze various real-world phenomena.

1. **Discrete Probability Distribution**:
   - Focuses on discrete random variables, which take on distinct, separate values.
   - Example: The probability distribution of rolling a fair six-sided die.
   - Probability Mass Function (PMF) describes the distribution.

2. **Continuous Probability Distribution**:
   - Deals with continuous random variables, which can take any value within a range.
   - Example: The distribution of heights in a population.
   - Probability Density Function (PDF) is used for continuous distributions.

3. **Probability Mass Function (PMF)**:
   - Represents the probability distribution of a discrete random variable.
   - Sum of all probabilities equals 1.
   - Often visualized using bar graphs or tables.

4. **Probability Density Function (PDF)**:
   - Represents the probability distribution of a continuous random variable.
   - The area under the curve over a specific interval represents the probability.
   - PDFs integrate to 1 over the entire range.

5. **Mean (Expected Value)**:
   - Represents the center or average value of a probability distribution.
   - For discrete random variables: ∑(x * P(x))
   - For continuous random variables: ∫(x * f(x)) dx

6. **Variance and Standard Deviation**:
   - Variance measures the spread or dispersion of the distribution.
   - Standard Deviation is the square root of the variance.
   - Smaller variance means data points are closer to the mean.

7. **Common Probability Distributions**:
   - **Binomial Distribution**: Models the number of successes in a fixed number of Bernoulli trials.
   - **Poisson Distribution**: Models the number of events occurring in a fixed interval of time or space.
   - **Normal Distribution**: A symmetric, bell-shaped distribution often found in nature.
   - **Exponential Distribution**: Models the time between events in a Poisson process.

8. **Central Limit Theorem**:
   - States that the sampling distribution of the sample means approaches a normal distribution as the sample size increases.
   - Essential for inferential statistics.

9. **Useful Properties**:
   - PDFs are non-negative.
   - The total area under a PDF or PMF is 1.
   - The mean and standard deviation provide valuable information about the distribution.
