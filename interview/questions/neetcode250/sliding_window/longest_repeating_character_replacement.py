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


def find_longest_repeating_replacement_alt(s: str, k: int) -> int:
    if len(s) < 2:
        return 1

    result = 0
    left = 0
    right = 0
    while right < len(s):
        window_frequency = defaultdict(int)
        # keep track of most_frequent_count to avoid the max function
        most_frequent_count = 0
        right = left
        while right < len(s):
            count = window_frequency.get(s[right], 0)
            if count + 1 >= most_frequent_count:
                most_frequent_count = count + 1

            window_frequency[s[right]] += 1

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
    result = find_longest_repeating_replacement_alt(s, k)
    print(result)

    print("-" * 10)

    s = "ABAB"
    k = 2
    result = find_longest_repeating_replacement(s, k)
    print(result)
    result = find_longest_repeating_replacement_alt(s, k)
    print(result)

    print("-" * 10)

    s = "ABABBA"
    k = 2
    result = find_longest_repeating_replacement(s, k)
    print(result)
    result = find_longest_repeating_replacement_alt(s, k)
    print(result)


if __name__ == "__main__":
    main()
