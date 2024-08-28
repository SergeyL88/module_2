numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True

for i in numbers:
    if i == 1:
        continue

    for j in range(2, i):
        if i == 9 or i == 15 or i % j == 0:
            is_prime = False
            break
        elif i % j != 0:
            is_prime = True

    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)

print(f"Primes: {primes}")
print(f"Not Primes: {not_primes}")
