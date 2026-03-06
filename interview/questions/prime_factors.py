import math


def prime_factors(n):
    factors = []

    while n % 2 == 0:
        factors.append(2)
        n = n // 2

    for i in range(3, int(math.sqrt(n))):
        while n % i == 0:
            n = n // i
            factors.append(i)

    if n > 2:
        factors.append(n)

    return factors


def main():
    result = prime_factors(300)
    print(result)


if __name__ == "__main__":
    main()
