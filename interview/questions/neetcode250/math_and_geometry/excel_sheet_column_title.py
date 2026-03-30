def excel_column(n: int) -> str:
    result = []
    while n > 0:
        offset = (n - 1) % 26
        result.append(chr(ord("A") + offset))
        n = (n - 1) // 26

    return "".join(result[::-1])


def main():
    n = 1
    result = excel_column(n)
    val = "A"
    print("passed:", result == val, "expected", val, "got", result)

    n = 28
    result = excel_column(n)
    val = "AB"
    print("passed:", result == val, "expected", val, "got", result)

    n = 701
    result = excel_column(n)
    val = "ZY"
    print("passed:", result == val, "expected", val, "got", result)

    n = 5000
    result = excel_column(n)
    val = "GJH"
    print("passed:", result == val, "expected", val, "got", result)


if __name__ == "__main__":
    main()
