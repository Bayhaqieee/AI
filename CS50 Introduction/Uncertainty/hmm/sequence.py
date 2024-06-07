from model import model

# Observed data
observations = [
    "umbrella",
    "no umbrella",
    "no umbrella",
    "umbrella",
    "no umbrella",
    "umbrella",
    "umbrella",
    "no umbrella",
    "no umbrella",
    "umbrella",
    "umbrella",
    "no umbrella",
    "no umbrella"
]

# Predict underlying states
predictions = model.predict(observations)
for prediction in predictions:
    print(model.states[prediction].name)
