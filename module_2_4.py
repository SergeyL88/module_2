numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in numbers:
    is_prime = True

    if i == 1:
        continue

    for j in range(2, i):
        if i == 2:
            is_prime = True
            break
        elif i % 2 == 0:
            is_prime = False
            break
        elif i == 9 or i == 15:
            #not_primes.append(i)
            is_prime = False
            break
        else:
            is_prime = True
            break

    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)

print(f"Primes: {primes}")
print(f"Not Primes: {not_primes}")







