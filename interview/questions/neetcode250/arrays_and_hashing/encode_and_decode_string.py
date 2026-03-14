def encode(strings: list[str]) -> str:
    result = []
    for s in strings:
        result.append(f"{len(s)}#{s}")

    return "".join(result)


def decode(s: str) -> list[str]:
    result = []
    i = 0
    while i < len(s):
        j = i
        while j < len(s):
            if s[j] == "#":
                break

            j += 1


        count = int(s[i:j])
        word = []
        i = j + 1

        while count > 0:
            word.append(s[i])
            i += 1
            count -= 1

        result.append("".join(word))

    return result


def main():
    strings = ["lint", "code", "love", "you", "this is a long piece of text"]
    result = encode(strings)
    val = "4#lint4#code4#love3#you28#this is a long piece of text"
    print("passed:", result == val, "expected", val, "got", result)

    result = decode(result)
    val = strings
    print("passed:", result == val, "expected", val, "got", result)


if __name__ == "__main__":
    main()
