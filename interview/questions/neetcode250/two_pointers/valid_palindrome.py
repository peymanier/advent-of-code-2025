def is_alpha_num(char) -> bool:
    return (
        (ord("A") <= ord(char) <= ord("Z"))
        or (ord("a") <= ord(char) <= ord("z"))
        or (ord("0") <= ord(char) <= ord("9"))
    )


def is_valid_palindrome(s: str) -> bool:
    left = 0
    right = len(s) - 1
    while left <= right:
        # while left <= right and not s[left].isalnum():
        while left <= right and not is_alpha_num(s[left]):
            left += 1

        # while left <= right and not s[right].isalnum():
        while left <= right and not is_alpha_num(s[right]):
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left, right = left + 1, right - 1

    return True


def main():
    s = "A man, a plan, a canal: Panama"
    result = is_valid_palindrome(s)
    print("expected", True, "got", result)

    s = "race a car"
    result = is_valid_palindrome(s)
    print("expected", False, "got", result)


if __name__ == "__main__":
    main()
