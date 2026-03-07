# Two Pointers
# use two pointers to avoid nested loops, find halfway point or detect cycles in linked lists
# usually works on pre-sorted data.
# usually one of the pointers moves based on a condition
def is_palindrome(s: str) -> bool:
    s = "".join([ch.lower() for ch in s if ch.isalnum()])
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False

        left += 1
        right -= 1

    return True


def is_palindrome2(s: str) -> bool:
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1

        while l < r and not s[r].isalnum():
            r -= 1

        if s[l].lower() != s[r].lower():
            return False

        l += 1
        r -= 1

    return True


def main():
    s = "A man, a plan, a canal: Panama"
    # s = "race a car"
    # result = is_palindrome(s)
    result = is_palindrome2(s)
    print(result)


if __name__ == "__main__":
    main()
