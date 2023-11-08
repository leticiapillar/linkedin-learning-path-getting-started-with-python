# 04 Statistics Module
import statistics
import math

agesData = [10,13,14,12,11,10,11,10,15]
print("ages data:", agesData)
print("sorted   :", sorted(agesData))

# Statistics definition
print("Statistics Definition")
# Mean: average
print("Mean  :", statistics.mean(agesData))
# Median: midpoint
print("Median:", statistics.median(agesData))
# Mode: most frequent value
print("Mode  :", statistics.mode(agesData))


# Advanced Statistics Definition
print("Advanced Statistics Definition")

# Variance: the averege of the squared differences from the mean
print("Variance               :", statistics.variance(agesData))
# Standard deviation: the square root of the variance
print("Standard deviation     :", statistics.stdev(agesData))
# Square root of Variance
print("Square root of Variance:", math.sqrt(statistics.variance(agesData)))
