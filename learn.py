import numpy as np
data = np.loadtxt("input", dtype=int)
convolved_data = np.convolve(data, np.ones(3), "valid")

print(sum(data[:-1] < data[1:]))
print(sum(convolved_data[:-1] < convolved_data[1:]))
