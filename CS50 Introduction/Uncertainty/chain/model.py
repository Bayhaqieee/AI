from pomegranate import *

# Define starting probabilities
start = DiscreteDistribution({
    "sun": 0.6,
    "rain": 0.4
})

# Define transition model
transitions = ConditionalProbabilityTable([
    ["sun", "sun", 0.6],
    ["sun", "rain", 0.5],
    ["rain", "sun", 0.4],
    ["rain", "rain", 0.8]
], [start])

# Create Markov chain
model = MarkovChain([start, transitions])

# Sample 50 states from chain
print(model.sample(50))
