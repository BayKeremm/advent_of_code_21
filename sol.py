import numpy as np

depths = np.loadtxt('input', dtype=int)
convolved_depths = np.convolve(depths, np.ones(3), 'valid')
answer = lambda x: sum(x[:-1] < x[1:])
print(answer(depths), answer(convolved_depths))
