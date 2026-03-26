def merge_strings_alternately(word1: str, word2: str):
    i = 0
    j = 0
    result = []
    while i < len(word1) and j < len(word2):
        result.append(word1[i])
        i += 1
        result.append(word2[j])
        j += 1

    while i < len(word1):
        result.append(word1[i])
        i += 1

    while j < len(word2):
        result.append(word2[j])
        j += 1

    return "".join(result)


def main():
    word1 = "abc"
    word2 = "pqr"
    val = "apbqcr"
    result = merge_strings_alternately(word1, word2)
    print("passed:", result == val, "expected", val, "got", result)

    word1 = "abcxyz"
    word2 = "pqr"
    val = "apbqcrxyz"
    result = merge_strings_alternately(word1, word2)
    print("passed:", result == val, "expected", val, "got", result)


if __name__ == "__main__":
    main()
