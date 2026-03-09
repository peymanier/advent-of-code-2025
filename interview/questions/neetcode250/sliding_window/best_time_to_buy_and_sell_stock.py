def find_max_profit(stocks: list[int]) -> int:
    if len(stocks) < 2:
        return 0

    left = 0
    right = 1

    result = 0
    while right < len(stocks):
        profit = stocks[right] - stocks[left]
        result = max(result, profit)

        if stocks[right] < stocks[left]:
            left = right

        right += 1

    return result


def main():
    stocks = [7, 4, 13, 3, 1, 6, 3, 12, 4, 10]
    result = find_max_profit(stocks)
    print(result)


if __name__ == "__main__":
    main()
