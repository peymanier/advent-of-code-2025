def is_valid_palindrome(s: str) -> bool:
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            l = left
            l += 1
            r = right
            skip_left_valid = True
            while l < r:
                if s[l] != s[r]:
                    skip_left_valid = False
                    break
                l += 1
                r -= 1

            l = left
            r = right
            r -= 1
            skip_right_valid = True
            while l < r:
                if s[l] != s[r]:
                    skip_right_valid = False
                    break
                l += 1
                r -= 1

            return skip_left_valid or skip_right_valid

        left += 1
        right -= 1

    return True


def is_valid_palindrome_alt(s: str) -> bool:
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            skip_left = s[left + 1 : right + 1]
            skip_right = s[left:right]
            return skip_left == skip_left[::-1] or skip_right == skip_right[::-1]

        left += 1
        right -= 1

    return True


def main():
    s = "aba"
    result = is_valid_palindrome_alt(s)
    print("expected", True, "got", result)

    s = "abca"
    result = is_valid_palindrome_alt(s)
    print("expected", True, "got", result)

    s = "abc"
    result = is_valid_palindrome_alt(s)
    print("expected", False, "got", result)

    s = "abcdefggfedcxba"
    result = is_valid_palindrome_alt(s)
    print("expected", True, "got", result)


if __name__ == "__main__":
    main()
