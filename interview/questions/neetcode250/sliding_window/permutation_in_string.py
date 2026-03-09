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


# O(26n)
def has_permutation_second_alt(s1, s2) -> bool:
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


# Best O(26) + O(n)
def has_permutation_third_alt(s1, s2) -> bool:
    if len(s1) > len(s2):
        return False

    s1_count = [0] * 26
    s2_count = [0] * 26
    for i in range(len(s1)):
        s1_count[ord(s1[i]) - ord("a")] += 1
        s2_count[ord(s2[i]) - ord("a")] += 1

    matches = 0
    for i in range(26):
        if s1_count[i] == s2_count[i]:
            matches += 1

    left = 0
    for right in range(len(s1), len(s2)):
        if matches == 26:
            return True

        index = ord(s2[right]) - ord("a")
        s2_count[index] += 1
        if s2_count[index] == s1_count[index]:
            matches += 1
        elif s2_count[index] - 1 == s1_count[index]:
            matches -= 1

        index = ord(s2[left]) - ord("a")
        s2_count[index] -= 1
        if s2_count[index] == s1_count[index]:
            matches += 1
        elif s2_count[index] + 1 == s1_count[index]:
            matches -= 1

        left += 1

    return matches == 26


def main():
    s1 = "ab"
    s2 = "eidbaooo"
    result = has_permutation_alt(s1, s2)
    print(result)
    result = has_permutation_second_alt(s1, s2)
    print(result)
    result = has_permutation_third_alt(s1, s2)
    print(result)

    print("-" * 10)

    s1 = "ab"
    s2 = "eidboaoo"
    result = has_permutation_alt(s1, s2)
    print(result)
    result = has_permutation_second_alt(s1, s2)
    print(result)
    result = has_permutation_third_alt(s1, s2)
    print(result)

    print("-" * 10)

    s1 = "abc"
    s2 = "baxyzabc"
    result = has_permutation_alt(s1, s2)
    print(result)
    result = has_permutation_second_alt(s1, s2)
    print(result)
    result = has_permutation_third_alt(s1, s2)
    print(result)


if __name__ == "__main__":
    main()
