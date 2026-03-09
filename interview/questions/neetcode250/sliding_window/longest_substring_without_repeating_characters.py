def find_longest_substr(string: str) -> int:
    window = set()
    result = 0

    left = 0
    for right in range(len(string)):
        while string[right] in window:
            window.remove(string[left])
            left += 1

        window.add(string[right])
        result = max(result, right - left + 1)

    return result


def main():
    string = "abcabcbb"
    result = find_longest_substr(string)
    print(result)


if __name__ == "__main__":
    main()
