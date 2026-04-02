# def greatest_common_divisor(str1: str, str2: str) -> str:
#     if len(str1) <= len(str2):
#         shorter = str1
#         bigger = str2
#     else:
#         shorter = str2
#         bigger = str1
#
#     result = 0
#     result_len = 0
#     for i in range(1, len(shorter) + 1):
#         substr = shorter[:i]
#         if len(shorter) % i != 0 or len(bigger) % i != 0:
#             continue
#
#         x = len(shorter) // i
#         y = len(bigger) // i
#         if substr * x == shorter and substr * y == bigger:
#             if i > result_len:
#                 result = substr
#                 result_len = i
#
#     return result


def greatest_common_divisor(str1: str, str2: str) -> str:
    if len(str1) <= len(str2):
        shorter = str1
        bigger = str2
    else:
        shorter = str2
        bigger = str1

    # Greedy
    for i in range(len(shorter), 0, -1):
        substr = shorter[:i]
        if len(shorter) % i != 0 or len(bigger) % i != 0:
            continue

        x = len(shorter) // i
        y = len(bigger) // i
        if substr * x == shorter and substr * y == bigger:
            return substr

    return ""


def main():
    str1 = "ABCABC"
    str2 = "ABC"
    result = greatest_common_divisor(str1, str2)
    val = "ABC"
    print("passed:", result == val, "expected", val, "got", result)

    str1 = "ABABAB"
    str2 = "ABAB"
    result = greatest_common_divisor(str1, str2)
    val = "AB"
    print("passed:", result == val, "expected", val, "got", result)


if __name__ == "__main__":
    main()
