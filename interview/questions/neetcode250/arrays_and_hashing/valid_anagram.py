# from collections import Counter
# def is_valid_anagram(s: str, t: str) -> bool:
#     return Counter(s) == Counter(t)


def is_valid_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count_s = {}
    count_t = {}
    for i in range(len(s)):
        count_s[s[i]] = count_s.get(s[i], 0) + 1
        count_t[t[i]] = count_t.get(t[i], 0) + 1

    for c in count_s:
        if count_s[c] != count_t.get(c):
            return False

    return True


def is_valid_anagram_alt(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


def main():
    s = "anagram"
    t = "maranag"
    result = is_valid_anagram(s, t)
    print("expected", True, "got", result)

    s = "anagram"
    t = "maranag"
    result = is_valid_anagram_alt(s, t)
    print("expected", True, "got", result)

    s = "car"
    t = "rat"
    result = is_valid_anagram(s, t)
    print("expected", False, "got", result)

    s = "car"
    t = "rat"
    result = is_valid_anagram_alt(s, t)
    print("expected", False, "got", result)


if __name__ == "__main__":
    main()
