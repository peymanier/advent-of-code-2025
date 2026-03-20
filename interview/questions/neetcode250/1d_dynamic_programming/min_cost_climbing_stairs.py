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


def min_cost_climbing_stairs(costs: list[int]) -> int:
    # from functools import cache
    #
    # @cache
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
    result = min_cost_climbing_stairs(costs)
    val = 15
    print("passed:", result == val, "expected", val, "got", result)

    costs = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    result = min_cost_climbing_stairs(costs)
    val = 6
    print("passed:", result == val, "expected", val, "got", result)

    costs = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1] * 45
    result = min_cost_climbing_stairs(costs)
    val = 270
    print("passed:", result == val, "expected", val, "got", result)


if __name__ == "__main__":
    main()
