from collections import Counter


def has_permutation(s1, s2) -> bool:
    def has_every_char():
        for char in s1:
            if char not in window:
                return False

        return True

    window_size = len(s1)
    for right in range(window_size, len(s2) + 1):
        left = right - window_size
        window = s2[left:right]
        if has_every_char():
            return True

    return False


def has_permutation_alt(s1, s2) -> bool:
    s1_counter = Counter(s1)

    window_size = len(s1)
    for right in range(window_size, len(s2) + 1):
        left = right - window_size
        window = s2[left:right]
        if Counter(window) == s1_counter:
            return True

    return False


def has_permutation_best(s1, s2) -> bool:
    if len(s1) > len(s2):
        return False

    s1_counter = Counter(s1)

    window_size = len(s1)
    window_counter = Counter(s2[:window_size])
    left = 0
    for right in range(window_size, len(s2)):
        if s1_counter == window_counter:
            return True

        window_counter[s2[right]] = window_counter.get(s2[right], 0) + 1
        window_counter[s2[left]] -= 1
        left += 1

    return s1_counter == window_counter


def main():
    s1 = "ab"
    s2 = "eidbaooo"
    result = has_permutation_alt(s1, s2)
    print(result)
    result = has_permutation_best(s1, s2)
    print(result)

    print("-" * 10)

    s1 = "ab"
    s2 = "eidboaoo"
    result = has_permutation_alt(s1, s2)
    print(result)
    result = has_permutation_best(s1, s2)
    print(result)

    print("-" * 10)

    s1 = "abc"
    s2 = "baxyzabc"
    result = has_permutation_alt(s1, s2)
    print(result)
    result = has_permutation_best(s1, s2)
    print(result)


if __name__ == "__main__":
    main()
