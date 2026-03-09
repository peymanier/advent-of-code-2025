from collections import defaultdict


def find_longest_repeating_replacement(s: str, k: int) -> int:
    if len(s) < 2:
        return 1

    result = 0
    left = 0
    right = 0
    while right < len(s):
        window_frequency = defaultdict(int)
        right = left
        while right < len(s):
            window_frequency[s[right]] += 1
            most_frequent_count = max(window_frequency.values())

            if (right - left + 1) - most_frequent_count > k:
                break

            result = max(result, (right - left + 1))

            right += 1

        left += 1

    return result


def main():
    s = "AABABBA"
    k = 1
    result = find_longest_repeating_replacement(s, k)
    print(result)

    s = "ABAB"
    k = 2
    result = find_longest_repeating_replacement(s, k)
    print(result)

    s = "ABABBA"
    k = 2
    result = find_longest_repeating_replacement(s, k)
    print(result)


if __name__ == "__main__":
    main()
