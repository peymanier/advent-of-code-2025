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


def main():
    candidate = "The quick brown fox jumps over the lazy dog."
    print(is_pangram(candidate))


if __name__ == "__main__":
    main()
