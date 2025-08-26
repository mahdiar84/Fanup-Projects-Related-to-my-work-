import numpy as np

a = "machine learning is fun"

b = np.array(a.split())
c = np.sort(b)
result = " ".join(c)

print(result)