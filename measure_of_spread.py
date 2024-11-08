#calculting the measure of spread of the data
# subtract mean form each data point and square the result

import numpy as np
dists = msleep['sleep_total'] - np.mean(msleep['sleep_total'])

print(dists)


#square each distance
sq_dists = dists**2

# sum square distances
sum_sq_dists = np.sum(sq_dists)
print(sum_sq_dists)


#divide by the number of data points - 1
variance = sum_sq_dists/len(msleep['sleep_total'] - 1)
print(variance)





