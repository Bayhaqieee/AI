import numpy as np
from scipy import stats
 
jumlah_kucing = np.array([3, 2, 1, 1, 2, 3, 2, 1, 0, 2])

# Mean
print(jumlah_kucing.mean())
# Median
print(np.median(jumlah_kucing))

# Mode (Most Frequent Data Showed)
mode_jumlah_kucing = stats.mode(jumlah_kucing)[0]
print(mode_jumlah_kucing)