def coin_change(coins: list[int], amount: int) -> int:
    result = float("inf")

    def change(amt, count):
        if amt < 0:
            return

        if amt == 0:
            nonlocal result
            result = min(result, count)
            return

        for coin in coins:
            change(amt - coin, count + 1)

        return

    change(amount, 0)
    return result if result != float("inf") else -1


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
