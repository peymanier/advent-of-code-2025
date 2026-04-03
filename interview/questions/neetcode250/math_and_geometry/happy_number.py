# def is_happy_number(num: int) -> bool:
#     digits = list(str(num))
#     visited = set()
#     while True:
#         digits_squared = 0
#         for _ in range(len(digits)):
#             curr = digits.pop()
#             digits_squared += int(curr) ** 2
#
#         if digits_squared == 1:
#             return True
#
#         if digits_squared in visited:
#             return False
#
#         visited.add(digits_squared)
#
#         for digit in list(str(digits_squared)):
#             digits.append(digit)
#


def get_digits_of_num(num: int) -> list[int]:
    digits = []
    while num > 0:
        digits.append(num % 10)
        num //= 10

    return digits


def is_happy_number(num: int) -> bool:
    digits = get_digits_of_num(num)
    visited = set()
    while True:
        curr = 0
        for _ in range(len(digits)):
            curr += digits.pop() ** 2

        if curr == 1:
            return True

        if curr in visited:
            return False

        visited.add(curr)

        for digit in get_digits_of_num(curr):
            digits.append(digit)


def main():
    num = 19
    result = is_happy_number(num)
    val = True
    print("passed:", result == val, "expected", val, "got", result)

    num = 2
    result = is_happy_number(num)
    val = False
    print("passed:", result == val, "expected", val, "got", result)


if __name__ == "__main__":
    main()
