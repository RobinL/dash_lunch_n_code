# Euler Problem 3

def find_factors (num):
    factors = []
    for i in range(1, round(num**0.5), 1):
        if num % i == 0:
            factors.append(i)
            factors.append(round(num/i))
    return factors

factors = find_factors(600851475143)

non_prime_factors = []

for num in factors:
    for div in range(2, num, 1):
        if num % div == 0:
            non_prime_factors.append(num)
            break

largest_prime_factor = max([x for x in factors if x not in non_prime_factors])
print(largest_prime_factor)