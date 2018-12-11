import numpy as np
from scipy import stats
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

height = [172,
174,
176,
172,
172,
173,
176,
172,
177,
174,
176,
175,
176,
169,
175,
174,
174,
174,
175,
173,
171,
171,
175,
175,
173,
175,
175]

print(height)

print(np.average(height))
print(np.median(height))
print(stats.mode(height))
plt.hist(height,5)
plt.show()

weight = [
    184,
180,
181,
184,
182,
181,
182,
182,
183,
182,
181,
182,
182,
180,
183,
181,
184,
183,
182,
182,
183,
182,
183,
181,
180,
181,
183
]

print(weight)

print(np.std(weight))

plt.hist(weight,5)
plt.show()

print(0.1*0.9*0.1)