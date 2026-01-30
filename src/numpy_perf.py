import numpy as np
import time

nums = list(range(1000000))
start = time.time()
[ x * 2 for x in nums ]
print("Python List: ", time.time() - start)

arr = np.arange(1000000)
start = time.time()
arr * 2
print("NumPy array: ", time.time() - start)

