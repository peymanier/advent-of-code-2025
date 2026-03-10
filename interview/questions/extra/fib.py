import functools


@functools.cache
def fib_recursive(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iter(n):
    prev = 0
    curr = 1
    for _ in range(n - 1):
        prev, curr = curr, curr + prev

    return curr


def main():
    result = fib_recursive(100)
    print(result)

    result = fib_iter(100)
    print(result)


if __name__ == "__main__":
    main()
