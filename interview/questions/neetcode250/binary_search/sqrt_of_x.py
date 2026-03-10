def sqrt(x: int) -> int:
    if x <= 0:
        return 0

    left = 1
    right = x
    result = 0
    while left <= right:
        mid = (left + right) // 2
        squared = mid**2
        if squared == x:
            return mid

        if squared > x:
            right = mid - 1
        else:
            result = mid
            left = mid + 1

    return result


def main():
    x = 4
    result = sqrt(x)
    print("expected", 2, end=" ")
    print("got", result)

    x = 8
    result = sqrt(x)
    print("expected", 2, end=" ")
    print("got", result)


if __name__ == "__main__":
    main()
