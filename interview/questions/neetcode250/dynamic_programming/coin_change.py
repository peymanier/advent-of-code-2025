import functools


def cache_coin_change(func):
    cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        amount, current_count = args

        if amount in cache:
            return current_count + cache[amount]

        result = func(*args, **kwargs)

        cache[amount] = result - current_count
        return result

    return wrapper


def coin_change(coins: list[int], amount: int) -> int:
    @cache_coin_change
    def change(amt, count):
        if amt < 0:
            return float("inf")

        if amt == 0:
            return count

        candidates = []
        for coin in coins:
            candidates.append(change(amt - coin, count + 1))

        return min(candidates)

    return change(amount, 0)


def main():
    coins = [1, 2, 5]
    amount = 11
    result = coin_change(coins, amount)
    val = 3
    print("passed:", result == val, "expected", val, "got", result)

    coins = [2]
    amount = 3
    result = coin_change(coins, amount)
    val = -1
    print("passed:", result == val, "expected", val, "got", result)


if __name__ == "__main__":
    main()
