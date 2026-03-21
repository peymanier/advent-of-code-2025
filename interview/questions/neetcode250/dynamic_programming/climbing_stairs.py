from functools import cache

# def climbing_stairs(n: int) -> int:
#     possible = []
#
#     def climb(steps: list[int], steps_sum: int):
#         if steps_sum > n:
#             return 0
#
#         if steps_sum == n:
#             possible.append(steps)
#             return 1
#
#         return climb([*steps, 1], steps_sum + 1) + climb([*steps, 2], steps_sum + 2)
#
#     result = climb([], 0)
#     print(possible)
#     return result


# def climbing_stairs(n: int) -> int:
#     @cache
#     def climb(steps: int):
#         if steps > n:
#             return 0
#
#         if steps == n:
#             return 1
#
#         return climb(steps + 1) + climb(steps + 2)
#
#     return climb(0)


@cache
def climbing_stairs(n: int) -> int:
    if n < 0:
        return 0

    if n == 0:
        return 1

    return climbing_stairs(n - 1) + climbing_stairs(n - 2)


def main():
    n = 2
    result = climbing_stairs(n)
    val = 2
    print("passed:", result == val, "expected", val, "got", result)

    n = 3
    result = climbing_stairs(n)
    val = 3
    print("passed:", result == val, "expected", val, "got", result)

    n = 5
    result = climbing_stairs(n)
    val = 8
    print("passed:", result == val, "expected", val, "got", result)

    n = 100
    result = climbing_stairs(n)
    val = 573147844013817084101
    print("passed:", result == val, "expected", val, "got", result)


if __name__ == "__main__":
    main()
