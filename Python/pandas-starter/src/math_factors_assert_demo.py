"""
This script demonstrates how to write unit tests for a function in Python
"""


# Write a function to calculate prime factors of a number
def get_factors(input_num):
    prime_factors = [1]
    for j in range(2, input_num + 1):
        if input_num % j == 0:
            prime_factors.append(j)
    return prime_factors


print(get_factors(2))
print(get_factors(3))
print(get_factors(4))
print(get_factors(10))

# Write unit tests for get_prime_factors()
assert (get_factors(2) == [1, 2])
assert (get_factors(3) == [1, 3])
assert (get_factors(4) == [1, 2, 4])
