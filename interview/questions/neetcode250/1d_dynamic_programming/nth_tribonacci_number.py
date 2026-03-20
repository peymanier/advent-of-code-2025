from functools import cache

# @cache
# def nth_tribonacci_number(n: int) -> int:
#     if n <= 0:
#         return 0
#
#     if n in (1, 2):
#         return 1
#
#     return (
#         nth_tribonacci_number(n - 1)
#         + nth_tribonacci_number(n - 2)
#         + nth_tribonacci_number(n - 3)
#     )


# def nth_tribonacci_number(n: int) -> int:
#     if n <= 0:
#         return 0
#
#     if n in (1, 2):
#         return 1
#
#     dp = [0 for _ in range(n + 1)]
#     dp[1] = 1
#     dp[2] = 1
#
#     for i in range(3, n + 1):
#         dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
#
#     return dp[n]


# def nth_tribonacci_number(n: int) -> int:
#     if n <= 0:
#         return 0
#
#     if n in (1, 2):
#         return 1
#
#     dp = [0, 1, 1]
#     for i in range(n - 2):
#         total = dp[0] + dp[1] + dp[2]
#         dp[0] = dp[1]
#         dp[1] = dp[2]
#         dp[2] = total
#
#     return dp[-1]


def nth_tribonacci_number(n: int) -> int:
    if n <= 0:
        return 0

    if n in (1, 2):
        return 1

    dp = [0, 1, 1]
    for i in range(n - 2):
        dp[0], dp[1], dp[2] = dp[1], dp[2], sum(dp)

    return dp[-1]


def main():
    n = 3
    result = nth_tribonacci_number(n)
    val = 2
    print("passed:", result == val, "expected", val, "got", result)

    n = 4
    result = nth_tribonacci_number(n)
    val = 4
    print("passed:", result == val, "expected", val, "got", result)

    n = 25
    result = nth_tribonacci_number(n)
    val = 1389537
    print("passed:", result == val, "expected", val, "got", result)


if __name__ == "__main__":
    main()
