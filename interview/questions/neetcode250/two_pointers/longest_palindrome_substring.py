def longest_palindrome_substring(s: str) -> str:
    i = 0
    result = ""
    while i < len(s):
        directions = [(0, 1), (-1, 1)]
        for dir in directions:
            dl, dr = dir
            left = i + dl
            right = i + dr

            while 0 <= left <= right < len(s):
                if s[left] != s[right]:
                    break

                if (right - left + 1) > len(result):
                    result = s[left : right + 1]

                left -= 1
                right += 1

        i += 1

    return result


def main():
    s = "babad"
    result = longest_palindrome_substring(s)
    val = "bab"
    print("passed:", result == val, "expected", val, "got", result)

    s = "cbbd"
    result = longest_palindrome_substring(s)
    val = "bb"
    print("passed:", result == val, "expected", val, "got", result)


if __name__ == "__main__":
    main()
