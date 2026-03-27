def container_with_most_water(height: list[int]) -> int:
    left = 0
    right = len(height) - 1
    result = 0
    while left < right:
        h = min(height[left], height[right])
        l = right - left
        result = max(result, h * l)

        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1

    return result


def main():
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    result = container_with_most_water(height)
    val = 49
    print("passed:", result == val, "expected", val, "got", result)


if __name__ == "__main__":
    main()
