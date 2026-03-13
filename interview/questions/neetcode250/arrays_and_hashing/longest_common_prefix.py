# def are_all_the_same(chars: list[str]) -> bool:
#     first_ch = chars[0]
#     for ch in chars:
#         if first_ch != ch:
#             return False
#
#     return True
#
#
# def longest_common_prefix(strings: list[str]) -> str:
#     result = []
#     for zipped in zip(*[list(s) for s in strings]):
#         if not are_all_the_same(zipped):
#             break
#
#         result.append(zipped[0])
#
#     return "".join(result)


def longest_common_prefix(strings: list[str]) -> str | None:
    if len(strings) < 2:
        return None

    result = []
    first_string = strings[0]
    for i in range(len(first_string)):
        for string in strings[1:]:
            if i == len(string) or first_string[i] != string[i]:
                return "".join(result)

        result.append(first_string[i])

    return "".join(result)


def main():
    strings = ["flower", "flow", "flight"]
    result = longest_common_prefix(strings)
    val = "fl"
    print("passed:", result == val, "expected", val, "got", result)

    strings = ["dog", "racecar", "car"]
    result = longest_common_prefix(strings)
    val = ""
    print("passed:", result == val, "expected", val, "got", result)

    strings = ["flower", "flow"]
    result = longest_common_prefix(strings)
    val = "flow"
    print("passed:", result == val, "expected", val, "got", result)


if __name__ == "__main__":
    main()
