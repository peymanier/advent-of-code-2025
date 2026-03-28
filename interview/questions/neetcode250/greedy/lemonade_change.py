def lemonade_change(bills: list[int]) -> bool:
    five_count = 0
    ten_count = 0
    for bill in bills:
        change = bill - 5
        if change == 0:
            five_count += 1

        elif change == 5:
            if five_count < 1:
                return False

            five_count -= 1
            ten_count += 1

        elif change == 15:
            if ten_count >= 1 and five_count >= 1:
                ten_count -= 1
                five_count -= 1
            elif five_count >= 3:
                five_count -= 3
            else:
                return False

    return True


def main():
    bills = [5, 5, 5, 10, 20]
    result = lemonade_change(bills)
    val = True
    print("passed:", result == val, "expected", val, "got", result)

    bills = [5, 5, 10, 10, 20]
    result = lemonade_change(bills)
    val = False
    print("passed:", result == val, "expected", val, "got", result)


if __name__ == "__main__":
    main()
