class TimeMap:
    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int):
        if key not in self.store:
            self.store[key] = []

        self.store[key].append((timestamp, value))
        return

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        vals = self.store[key]

        left = 0
        right = len(vals) - 1

        result = ""
        while left <= right:
            mid = (left + right) // 2
            if vals[mid][0] == timestamp:
                result = vals[mid][1]
                break

            if timestamp > vals[mid][0]:
                result = vals[mid][1]
                left = mid + 1
            else:
                right = mid - 1

        return result


def main():
    time_map = TimeMap()
    got = time_map.set("foo", "bar", 1)
    expected = None
    print("passed:", expected == got, "expected", expected, "got", got)

    got = time_map.get("foo", 1)
    expected = "bar"
    print("passed:", expected == got, "expected", expected, "got", got)

    got = time_map.get("foo", 3)
    expected = "bar"
    print("passed:", expected == got, "expected", expected, "got", got)

    got = time_map.set("foo", "bar2", 4)
    expected = None
    print("passed:", expected == got, "expected", expected, "got", got)

    got = time_map.get("foo", 4)
    expected = "bar2"
    print("passed:", expected == got, "expected", expected, "got", got)

    got = time_map.get("foo", 5)
    expected = "bar2"
    print("passed:", expected == got, "expected", expected, "got", got)


if __name__ == "__main__":
    main()
