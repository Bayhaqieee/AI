import numpy as np
from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt
 
jumlah_kucing = np.array([3, 2, 1, 1, 2, 3, 2, 1, 0, 2])

# Mean
print(jumlah_kucing.mean())
# Median
print(np.median(jumlah_kucing))

# Mode (Most Frequent Data Showed)
mode_jumlah_kucing = stats.mode(jumlah_kucing)[0]
print(mode_jumlah_kucing)

# Range
range = jumlah_kucing.max() - jumlah_kucing.min()
print(range)

# Interquartile Range
iqr = np.percentile(jumlah_kucing, 75) - np.percentile(jumlah_kucing, 25)
print(iqr)

# Variance
jumlah_kucing_series = pd.Series(jumlah_kucing)
jumlah_kucing_series.var()

# Standard Deviation
jumlah_kucing = np.array([3, 2, 1, 1, 2, 3, 2, 1, 0, 2])
jumlah_kucing_series = pd.Series(jumlah_kucing)
jumlah_kucing_series.std()

# Data Distribution
jumlah_kucing = np.array([3, 2, 1, 1, 2, 3, 2, 1, 0, 2])
plt.hist(jumlah_kucing, bins=4)
plt.show()

# Skewness
jumlah_kucing_series = pd.Series(jumlah_kucing)
jumlah_kucing_series.skew()