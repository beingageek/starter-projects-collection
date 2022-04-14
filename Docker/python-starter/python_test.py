import numpy as np

# Create list of numbers in a multi-dimensional array
a = np.arange(15).reshape(3,5)

# Print array
print(a)

# Get values from array and verify 
assert 3 == len(a)
assert "[0 1 2 3 4]" == str(a[0])
assert 12 == a[2][2]