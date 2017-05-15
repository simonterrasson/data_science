from collections import Counter
from matplotlib import pyplot as plt
import random
import math
from vectors import sum_of_squares
from numpy import dot
import pprint

# ---------------------------------------------------------------------------------------------------------
# STUDY CASE BASIS
# ---------------------------------------------------------------------------------------------------------

num_friends = []
cnt_minutes = []

for i in range(200):
    new_val = random.randrange(1,100,1)
    new_mnts = new_val * 0.5
    new_val *= (random.randrange(0,100,1) / 100)
    num_friends.append(int(new_val))
    cnt_minutes.append(int(new_mnts))

num_points = len(num_friends)
max_val = max(num_friends)
min_val = min(num_friends)
sorted_values = sorted(num_friends)
smallest_value = sorted_values[0]
largest_value = sorted_values[-1]

# pp = pprint.PrettyPrinter(width=200)
print(num_friends)
print(cnt_minutes)

print("Count Num Friends : " + str(num_points) + " / " + str(max_val) + " / " + str(min_val))
print("Sorted Values : " + str(smallest_value) + " / " + str(largest_value))

# ---------------------------------------------------------------------------------------------------------
# CENTRAL TENDENCIES
# ---------------------------------------------------------------------------------------------------------

def mean(vector_friends) :
    return sum(vector_friends) / len(vector_friends)

print("Friends count mean : " + str(mean(num_friends)))

def median(v):
    v = sorted(v)
    cnt_vals = len(v)

    if (cnt_vals == 0):
        return -1
    if (cnt_vals == 1):
        return v[0]

    if (cnt_vals % 2 == 1):
        idx = math.floor(cnt_vals/2)
        return v[idx]
    else:
        idx = math.floor(cnt_vals/2)
        idxP = math.floor(cnt_vals/2) + 1
        return (v[idx] + v[idxP])/2

print("Friends median : " + str(median(num_friends)))

def quantile(x,p):
    p_index = int(p*len(x))
    return sorted(x)[p_index]

print("First decile : " + str(quantile(num_friends,.1)))
print("First quartile : " + str(quantile(num_friends,.25)))
print("Last quartile : " + str(quantile(num_friends,.75)))
print("Last decile : " + str(quantile(num_friends,.9)))

# ---------------------------------------------------------------------------------------------------------
# DISPERSION
# ---------------------------------------------------------------------------------------------------------

def data_range(v):
    return max(v)-min(v)

print("Data Range : " + str(data_range(num_friends)))

def de_mean(v):
    v_mean = mean(v)
    return [v_i - v_mean for v_i in v]

def variance(v):
    n = len(v)
    deviations = de_mean(v)
    return sum_of_squares(deviations)/(n-1)

def standard_deviation(x):
    return math.sqrt(variance(x))

def interquartile_range(x):
    return quantile(x,.75) - quantile(x,.25)

print("Variance : " + str(variance(num_friends)))
print("Standard Deviation : " + str(standard_deviation(num_friends)))
print("Interquartile Range : " + str(interquartile_range(num_friends)))

# ---------------------------------------------------------------------------------------------------------
# CORRELATION
# ---------------------------------------------------------------------------------------------------------

def covariance(x,y):
    n = len(x)
    return dot(de_mean(x),de_mean(y)) / (n-1)

print("Covariance Value : " + str(covariance(num_friends,cnt_minutes)))

def correlation(x,y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x,y) / stdev_x / stdev_y
    else:
        return 0

print("Correlation Value : " + str(correlation(num_friends,cnt_minutes)))

# ---------------------------------------------------------------------------------------------------------
# GRAPH PART
# ---------------------------------------------------------------------------------------------------------

friend_counts = Counter(num_friends)
xs = range(101) # largest value is 100
ys = [friend_counts[x] for x in xs] # height is just # of friends
plt.bar(xs, ys)
plt.axis([0, 101, 0, 25])
plt.title("Histogram of Friend Counts")
plt.xlabel("# of friends")
plt.ylabel("# of people")
plt.show()
