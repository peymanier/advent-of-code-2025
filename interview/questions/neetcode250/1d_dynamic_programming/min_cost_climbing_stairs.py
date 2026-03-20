import sys
import time
from functools import cache


def cache_climb(func):
    cache = {}

    def wrapper(*args, **kwargs):
        step, current_cost = args
        if step in cache:
            return current_cost + cache[step]

        result = func(*args, **kwargs)

        cache[step] = result - current_cost
        return result

    return wrapper


def min_cost_climbing_stairs_builtin_cache(costs: list[int]) -> int:
    @cache
    def climb(step: int, cost: int):
        if step > len(costs):
            return float("inf")

        if step == len(costs):
            return cost

        return min(
            climb(step + 1, cost + costs[step]), climb(step + 2, cost + costs[step])
        )

    return min(climb(0, 0), climb(1, 0))


def min_cost_climbing_stairs_personal_tailored_cache(costs: list[int]) -> int:
    @cache_climb
    def climb(step: int, cost: int):
        if step > len(costs):
            return float("inf")

        if step == len(costs):
            return cost

        return min(
            climb(step + 1, cost + costs[step]), climb(step + 2, cost + costs[step])
        )

    return min(climb(0, 0), climb(1, 0))


def main():
    costs = [10, 15, 20]
    result = min_cost_climbing_stairs_builtin_cache(costs)
    val = 15
    print("passed:", result == val, "expected", val, "got", result)

    costs = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    result = min_cost_climbing_stairs_builtin_cache(costs)
    val = 6
    print("passed:", result == val, "expected", val, "got", result)

    print("current recursion limit", sys.getrecursionlimit())
    sys.setrecursionlimit(5000)
    print("new recursion limit", sys.getrecursionlimit())

    costs = [1, 100, 1, 1, 100, 100, 100, 1, 100, 1] * 100
    start = time.perf_counter()
    result = min_cost_climbing_stairs_builtin_cache(costs)
    end = time.perf_counter()
    print("duration:", (end - start))
    val = 10500
    print("passed:", result == val, "expected", val, "got", result)

    costs = [1, 100, 1, 1, 100, 100, 100, 1, 100, 1] * 100
    start = time.perf_counter()
    result = min_cost_climbing_stairs_personal_tailored_cache(costs)
    end = time.perf_counter()
    print("duration:", (end - start))
    val = 10500
    print("passed:", result == val, "expected", val, "got", result)


if __name__ == "__main__":
    main()
