from collections import defaultdict


def find_longest_substr_without_repetition(s: str) -> int:
    left = 0
    result = 0
    window = set()
    for right in range(len(s)):
        if s[right] in window:
            while left < right and s[right] in window:
                window.remove(s[left])
                left += 1

        window.add(s[right])

        result = max(result, len(window))

    return result


def find_longest_substr_without_repetition2(s: str) -> int:
    left = 0
    result = 0
    counter = defaultdict(int)
    for right in range(len(s)):
        counter[s[right]] += 1

        if counter[s[right]] > 1:
            while counter[s[right]] > 1:
                counter[s[left]] -= 1
                left += 1

        result = max(result, right - left + 1)

    return result


def main():
    s = "abcdbea"
    # result = find_longest_substr_without_repetition(s)
    result = find_longest_substr_without_repetition2(s)
    print(result)

    s = "abccabcabcc"
    # result = find_longest_substr_without_repetition(s)
    result = find_longest_substr_without_repetition2(s)
    print(result)

    s = "aaaabaaa"
    # result = find_longest_substr_without_repetition(s)
    result = find_longest_substr_without_repetition2(s)
    print(result)


if __name__ == "__main__":
    main()
