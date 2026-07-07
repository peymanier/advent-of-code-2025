def is_pangram(s: str) -> bool:
    if len(s) < 26:
        return False

    alphabets = [False for _ in range(26)]
    for char in s:
        if not char.isalpha():
            continue

        pos = ord(char.lower()) - ord("a")
        alphabets[pos] = True

    return all(alphabets)


def is_pangram2(s: str) -> bool:
    if len(s) < 26:
        return False

    bits = 0
    for char in s:
        if not char.isalpha():
            continue

        pos = ord(char.lower()) - ord("a")
        bits |= 1 << pos

    target = (1 << 26) - 1
    return bits == target


def main():
    candidate = "The quick brown fox jumps over the lazy dog."
    print(is_pangram(candidate))
    print(is_pangram2(candidate))


if __name__ == "__main__":
    main()
