"""
This script demonstrates some functions for prime numbers.
"""
import datetime
import random


def is_prime(n):
    """
    Checks if a given number is prime.

    Parameters:
        n (int): The number to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


# Write unit tests for is_prime() function
assert (is_prime(2))
assert (is_prime(3))
assert (not (is_prime(4)))
assert (is_prime(5))


def find_prime(input_num):
    prime_list = []
    for number in range(2, input_num + 1):
        if is_prime(number):
            prime_list.append(number)
    return prime_list


print(find_prime(100))

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
assert (primes == find_prime(100))

# Write 10 random numbers less than 100 amd check if they are prime
for k in range(10):
    num = random.randint(k, 100)
    print(f"{num} is prime: {is_prime(num)}")

assert (not (is_prime(12)))
assert (is_prime(11))
assert (not (is_prime(22)))
assert (not (is_prime(21)))
assert (not (is_prime(32)))
assert (is_prime(31))
assert (not (is_prime(42)))
assert (is_prime(41))
assert (not (is_prime(52)))
assert (not (is_prime(51)))


# Write python function to calculate prime factors of a number
def get_prime_factors(n):
    """
    This code defines a function get_prime_factors that takes an integer n as input. It finds
    all the prime factors of n and returns them as a list
    :param n:
    :return:
    """
    prime_factors = []
    for j in range(2, n + 1):
        if n % j == 0:
            prime_factors.append(j)
    return prime_factors


print(get_prime_factors(51))

print("Starting prime check for large number...")
start_time = datetime.datetime.now()
print(f"337190719854678689 is prime: {is_prime(337190719854678689)}")
end_time = datetime.datetime.now()
time_in_seconds = (end_time - start_time).total_seconds()
print("Time taken to check if 337190719854678689 is prime: " + str(time_in_seconds) + " seconds")
